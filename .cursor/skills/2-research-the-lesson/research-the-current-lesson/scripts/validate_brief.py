#!/usr/bin/env python3
"""Validate a lesson brief written by the research-the-current-lesson skill.

Usage:
    python3 scripts/validate_brief.py courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md

Also cross-checks the brief against the accepted syllabus two directories up, so a
brief that has drifted from the spine fails here rather than at film time.

Exit codes:
    0  no errors (warnings may be present)
    1  errors found, the brief is not ready to film from
    2  the file could not be read
"""

from __future__ import annotations

import argparse
import os
import re
import sys

REQUIRED_KEYS = ("course", "lesson", "lesson_slug", "title", "status")

REQUIRED_FIELDS = {
    "The feature": ("Is", "Is not", "Called now", "Mechanism"),
    "Mastery notes": (
        "Limits and defaults",
        "First-timer mistakes",
        "Failure on screen",
        "Cost of the shortcut",
    ),
    "Live operation": ("Entry", "Steps observed", "Done on screen", "Waits and interruptions"),
    "Reset": ("Method", "Verified"),
    "Best practice": (
        "Path we teach",
        "Why this path",
        "Order traps",
        "Shortcut refused",
        "Viewer verification",
    ),
    "The human example": (
        "Job",
        "Because",
        "Feature required because",
        "Not a smoke test because",
    ),
}
PROSE_SECTIONS = ("Dead paths", "Must be created on camera", "Constrains later lessons")
REQUIRED_SECTIONS = tuple(REQUIRED_FIELDS) + PROSE_SECTIONS + ("Sources",)

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_RE = re.compile(r"^-\s+([A-Z][A-Za-z -]*?):\s*(.*)$")
URL_RE = re.compile(r"https?://[^\s<>,;)\]]+")
REAL_URL_RE = re.compile(r"^https?://[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,}(?:/|$)")
PLACEHOLDER_RE = re.compile(r"<[^<>]{1,300}>", re.S)
SYLLABUS_LESSON_RE = re.compile(r"^###\s+Lesson\s+(\d+)\s*(?:—|–|-)\s*(\S.*?)\s*$")

# An example that only proves the machinery is wired up is not an example.
SMOKE_TEST_MARKERS = (
    r"\becho\b",
    r"\bhello[-_ ]?(a|b|world)\b",
    r"\bhello\.\w+\b",
    r"\btest\.txt\b",
    r"\bfoo\b\s*/\s*\bbar\b",
    r"\bfoo\.\w+\b",
    r"\bfoobar\b",
    r"\bdummy\b",
    r"reply with only",
    r"\blorem\b",
)

# Phrases that mean the object was not, in fact, created on camera.
OFF_CAMERA_MARKERS = (
    r"already exist",
    r"already create",
    r"already there",
    r"pre-?creat",
    r"pre-?exist",
    r"created earlier",
    r"creat\w*\s+off[- ]camera",
    r"off[- ]camera\s+creat",
)

MIN_FIELD_WORDS = 4  # Enough to be an answer rather than a label.
MIN_PROSE_WORDS = 6  # Same, for the free-form sections.
MIN_DESCRIPTION_WORDS = 3  # A source entry has to say what it established.
MIN_SOURCES = 2  # One source is a summary, not research.


class Report:
    def __init__(self, path: str) -> None:
        self.path = path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, line: int | None, message: str) -> None:
        self.errors.append(self._format("ERROR", line, message))

    def warn(self, line: int | None, message: str) -> None:
        self.warnings.append(self._format("WARN ", line, message))

    def _format(self, level: str, line: int | None, message: str) -> str:
        where = f"{self.path}:{line}" if line else self.path
        return f"{level} {where}: {message}"


def normalize_url(url: str) -> str:
    return url.strip().strip("<>").rstrip(".,;)").rstrip("/")


def is_real_url(url: str) -> bool:
    """True for a URL that was actually fetched, false for 'https://...' shaped stubs."""
    return bool(REAL_URL_RE.match(url)) and "..." not in url


def ledger_key(url: str) -> str:
    """Compare sources without letting http vs https look like two different pages."""
    return re.sub(r"^https?://", "", normalize_url(url)).lower()


def protected_ranges(text: str) -> list[tuple[int, int]]:
    """Character ranges inside fenced blocks or inline code, where <angle> is a signature."""
    ranges = [(match.start(), match.end()) for match in re.finditer(r"```.*?```", text, re.S)]
    ranges += [(match.start(), match.end()) for match in re.finditer(r"`[^`\n]*`", text)]
    return ranges


def inside(ranges: list[tuple[int, int]], position: int) -> bool:
    return any(start <= position < end for start, end in ranges)


def bullet_entries(lines: list[str], span: tuple[int, int]) -> list[tuple[int, str]]:
    """Bullets in a section, each joined with the lines its value wraps onto."""
    entries: list[tuple[int, str]] = []
    for number, text in section_lines(lines, span):
        stripped = text.strip()
        if stripped.startswith("- "):
            entries.append((number, stripped[2:]))
        elif entries and text.startswith("  ") and stripped:
            first_line, value = entries[-1]
            entries[-1] = (first_line, f"{value} {stripped}")
    return entries


def parse_frontmatter(lines: list[str], report: Report) -> tuple[dict[str, str], int]:
    if not lines or lines[0].strip() != "---":
        report.error(1, "file must open with a YAML frontmatter block delimited by ---")
        return {}, 0
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end = index
            break
    else:
        report.error(1, "frontmatter block is never closed with ---")
        return {}, 0

    data: dict[str, str] = {}
    for offset in range(1, end):
        raw = lines[offset]
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            report.error(offset + 1, f"frontmatter line is not 'key: value': {raw.strip()!r}")
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data, end + 1


def check_frontmatter(data: dict[str, str], report: Report) -> None:
    for key in REQUIRED_KEYS:
        if not data.get(key):
            report.error(None, f"frontmatter is missing a value for '{key}'")

    for key in ("course", "lesson_slug"):
        value = data.get(key, "")
        if value and not SLUG_RE.match(value):
            report.error(None, f"{key} must be kebab-case lowercase: got {value!r}")

    if data.get("lesson") and not data["lesson"].isdigit():
        report.error(None, f"lesson must be a positive integer: got {data['lesson']!r}")

    status = data.get("status", "")
    if status and status not in ("draft", "ready"):
        report.error(None, f"status must be 'draft' or 'ready': got {status!r}")


def check_location(data: dict[str, str], path: str, report: Report) -> str | None:
    """Confirm the canonical path, and return the course directory when it is found."""
    absolute = os.path.abspath(path)
    lesson_dir = os.path.dirname(absolute)
    lessons_dir = os.path.dirname(lesson_dir)
    course_dir = os.path.dirname(lessons_dir)

    if os.path.basename(absolute) != "brief.md" or os.path.basename(lessons_dir) != "lessons":
        report.warn(
            None,
            "brief is not at courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md, "
            "so the syllabus cross-check is skipped",
        )
        return None

    number = data.get("lesson", "")
    slug = data.get("lesson_slug", "")
    if number.isdigit() and slug:
        expected = f"{int(number):02d}-{slug}"
        if os.path.basename(lesson_dir) != expected:
            report.error(
                None,
                f"directory {os.path.basename(lesson_dir)!r} does not match the brief; "
                f"expected {expected!r}",
            )
    course = data.get("course", "")
    if course and os.path.basename(course_dir) != course:
        report.error(
            None,
            f"course directory {os.path.basename(course_dir)!r} does not match "
            f"frontmatter course {course!r}",
        )
    return course_dir


def check_against_syllabus(
    data: dict[str, str], course_dir: str, ledger: set[str], report: Report
) -> None:
    syllabus_path = os.path.join(course_dir, "syllabus.md")
    if not os.path.isfile(syllabus_path):
        report.error(
            None,
            f"no syllabus at {os.path.relpath(syllabus_path)}; stage 1 has to run first",
        )
        return

    try:
        with open(syllabus_path, encoding="utf-8") as handle:
            syllabus = handle.read()
    except OSError as problem:
        report.error(None, f"cannot read the syllabus: {problem.strerror}")
        return

    status = re.search(r"^status:\s*(\S+)\s*$", syllabus, re.M)
    if not status or status.group(1) != "accepted":
        found = status.group(1) if status else "missing"
        report.error(
            None,
            f"the syllabus status is {found!r}; a lesson is not researched until the "
            "user has accepted the spine",
        )

    number = data.get("lesson", "")
    if not number.isdigit():
        return

    titles = {
        int(match.group(1)): match.group(2)
        for match in (SYLLABUS_LESSON_RE.match(line) for line in syllabus.splitlines())
        if match
    }
    if int(number) not in titles:
        report.error(None, f"the syllabus has no Lesson {number}")
        return

    expected_title = titles[int(number)]
    if data.get("title", "") != expected_title:
        report.error(
            None,
            f"title {data.get('title', '')!r} does not match the syllabus line "
            f"{expected_title!r}",
        )

    lesson_block = syllabus.split(f"### Lesson {int(number)} ", 1)[-1].split("\n### ", 1)[0]
    for raw_url in syllabus_lesson_sources(lesson_block):
        url = normalize_url(raw_url)
        if is_real_url(url) and ledger_key(url) not in ledger:
            report.warn(
                None,
                f"{raw_url} is a source the syllabus already found for this lesson "
                "and it is not in this brief's ledger",
            )


def syllabus_lesson_sources(lesson_block: str) -> list[str]:
    """Collect the lesson's Sources field, including values continued on later lines."""
    collected: list[str] = []
    inside = False
    for raw in lesson_block.splitlines():
        if re.match(r"^-\s*Sources:", raw):
            inside = True
            collected.extend(URL_RE.findall(raw))
        elif inside and raw.startswith("  ") and raw.strip():
            collected.extend(URL_RE.findall(raw))
        elif raw.strip().startswith("- ") or not raw.strip():
            inside = False
    return collected


def check_placeholders(text: str, lines: list[str], report: Report) -> None:
    commented: set[int] = set()
    for number, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if stripped.startswith("<!--") or stripped.endswith("-->"):
            report.error(number, "template comment left in the brief; delete it")
            commented.add(number)

    protected = protected_ranges(text)
    for match in PLACEHOLDER_RE.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        if line in commented or inside(protected, match.start()):
            continue
        found = match.group(0)
        if any(is_real_url(normalize_url(url)) for url in URL_RE.findall(found)):
            continue
        report.error(line, f"unfilled placeholder {' '.join(found.split())!r}")


def collect_sections(lines: list[str], body_start: int) -> dict[str, tuple[int, int]]:
    marks: list[tuple[str, int]] = []
    for offset in range(body_start, len(lines)):
        if lines[offset].startswith("## "):
            marks.append((lines[offset][3:].strip(), offset + 1))
    sections: dict[str, tuple[int, int]] = {}
    for position, (title, start) in enumerate(marks):
        end = marks[position + 1][1] - 1 if position + 1 < len(marks) else len(lines)
        sections[title] = (start, end)
    return sections


def section_lines(lines: list[str], span: tuple[int, int]) -> list[tuple[int, str]]:
    start, end = span
    return [(number, lines[number - 1]) for number in range(start + 1, end + 1)]


def parse_fields(lines: list[str], span: tuple[int, int]) -> dict[str, tuple[int, str]]:
    fields: dict[str, tuple[int, str]] = {}
    last: str | None = None
    for number, raw in section_lines(lines, span):
        match = FIELD_RE.match(raw)
        if match:
            last = match.group(1).strip()
            fields[last] = (number, match.group(2).strip())
        elif raw.startswith("  ") and raw.strip() and last:
            line_number, value = fields[last]
            fields[last] = (line_number, f"{value} {raw.strip()}")
        elif not raw.strip():
            last = None
    return fields


def check_title(lines: list[str], body_start: int, data: dict[str, str], report: Report) -> None:
    expected = f"Lesson {data.get('lesson', '')} — {data.get('title', '')}"
    for offset in range(body_start, len(lines)):
        if lines[offset].startswith("# "):
            heading = lines[offset][2:].strip()
            if heading != expected:
                report.error(offset + 1, f"H1 should read {expected!r}, got {heading!r}")
            return
    report.error(None, "body has no H1 lesson heading")


def check_fields(lines: list[str], sections: dict, report: Report) -> dict[str, str]:
    values: dict[str, str] = {}
    for section, required in REQUIRED_FIELDS.items():
        if section not in sections:
            continue
        fields = parse_fields(lines, sections[section])
        for name in required:
            if name not in fields:
                report.error(sections[section][0], f"'{section}' is missing the '{name}:' field")
                continue
            line_number, value = fields[name]
            if len(value.split()) < MIN_FIELD_WORDS:
                report.error(line_number, f"'{name}:' needs a real answer, not a label")
            values[f"{section}/{name}"] = value
        for name, (line_number, _value) in fields.items():
            if name not in required:
                report.warn(line_number, f"unrecognized field {name!r} in '{section}'")
    return values


def check_prose_sections(lines: list[str], sections: dict, report: Report) -> dict[str, str]:
    collected: dict[str, str] = {}
    for name in PROSE_SECTIONS:
        if name not in sections:
            continue
        body = " ".join(text.strip() for _, text in section_lines(lines, sections[name])).strip()
        collected[name] = body
        if len(body.split()) < MIN_PROSE_WORDS:
            report.error(
                sections[name][0],
                f"'{name}' needs an actual answer; leaving it blank hides the finding",
            )
    return collected


def check_example(values: dict[str, str], sections: dict, report: Report) -> None:
    example = " ".join(
        value for key, value in values.items() if key.startswith("The human example/")
    ).lower()
    if not example or "The human example" not in sections:
        return
    for pattern in SMOKE_TEST_MARKERS:
        if re.search(pattern, example):
            report.error(
                sections["The human example"][0],
                f"the example reads as a smoke test (matched {pattern!r}); "
                "pick work a person would do anyway",
            )


def check_created_on_camera(
    prose: dict[str, str], sections: dict, lesson: str, report: Report
) -> None:
    body = prose.get("Must be created on camera", "")
    if not body or "Must be created on camera" not in sections:
        return

    current = int(lesson) if lesson.isdigit() else 0
    for sentence in re.split(r"(?<=[.!?])\s+", body):
        lowered = sentence.lower()
        matched = next((p for p in OFF_CAMERA_MARKERS if re.search(p, lowered)), None)
        if not matched:
            continue
        # Pointing at a lesson that already filmed the creation is the one legitimate
        # way for something to pre-exist, so the sentence has to name that lesson.
        earlier = [
            int(number)
            for number in re.findall(r"lesson\s+(\d+)", lowered)
            if int(number) < current
        ]
        if earlier:
            continue
        report.error(
            sections["Must be created on camera"][0],
            f"this section says the object is not created on camera (matched {matched!r}); "
            "either film its creation, or name the earlier lesson that already filmed it",
        )


def check_ledger(lines: list[str], sections: dict, report: Report) -> set[str]:
    ledger: set[str] = set()
    if "Sources" not in sections:
        return ledger
    for number, text in bullet_entries(lines, sections["Sources"]):
        urls = URL_RE.findall(text)
        if not urls:
            report.error(number, "source entry has no URL")
            continue
        for raw_url in urls:
            if not is_real_url(normalize_url(raw_url)):
                report.error(number, f"{raw_url} is not a real URL you fetched")
        ledger.update(
            ledger_key(url) for url in urls if is_real_url(normalize_url(url))
        )
        tail = text.split(urls[-1], 1)[-1]
        if len(re.sub(r"^[\s—–\-:>]+", "", tail).split()) < MIN_DESCRIPTION_WORDS:
            report.error(number, "source entry must say what it established")
    if len(ledger) < MIN_SOURCES:
        report.error(
            sections["Sources"][0],
            f"{len(ledger)} source(s) is not mastery of the material; at least "
            f"{MIN_SOURCES} live sources are required",
        )
    return ledger


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="path to courses/<slug>/lessons/<NN>-<slug>/brief.md")
    args = parser.parse_args()

    try:
        with open(args.path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as problem:
        print(f"cannot read {args.path}: {problem.strerror}", file=sys.stderr)
        return 2

    lines = text.splitlines()
    report = Report(args.path)
    if not lines:
        print(f"ERROR {args.path}: file is empty", file=sys.stderr)
        return 1

    frontmatter, body_start = parse_frontmatter(lines, report)
    check_frontmatter(frontmatter, report)
    check_placeholders(text, lines, report)
    check_title(lines, body_start, frontmatter, report)

    sections = collect_sections(lines, body_start)
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            report.error(None, f"missing required section '## {name}'")

    values = check_fields(lines, sections, report)
    prose = check_prose_sections(lines, sections, report)
    check_example(values, sections, report)
    check_created_on_camera(prose, sections, frontmatter.get("lesson", ""), report)
    ledger = check_ledger(lines, sections, report)

    course_dir = check_location(frontmatter, args.path, report)
    if course_dir:
        check_against_syllabus(frontmatter, course_dir, ledger, report)

    for message in report.errors:
        print(message)
    for message in report.warnings:
        print(message)

    if report.errors:
        print(
            f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s) "
            "— not ready to film from"
        )
        return 1

    print(
        f"OK {args.path}: lesson {frontmatter.get('lesson')}, {len(ledger)} source(s), "
        f"status {frontmatter.get('status', 'unknown')}, {len(report.warnings)} warning(s)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
