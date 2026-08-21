#!/usr/bin/env python3
"""Validate a take plan written by the real-example-in-every-lesson skill.

Usage:
    python3 scripts/validate_take_plan.py courses/<course-slug>/lessons/<NN>-<lesson-slug>/take-plan.md

Cross-checks the plan against the ready brief beside it and the course's pedagogy
file, so a plan that drops a creation step, or that judged the example against
nothing, fails before the recorder starts.

Exit codes:
    0  no errors (warnings may be present)
    1  errors found, do not start the recorder
    2  the file could not be read
"""

from __future__ import annotations

import argparse
import os
import re
import sys

REQUIRED_KEYS = ("course", "lesson", "lesson_slug", "status")
REQUIRED_SECTIONS = (
    "Example verdict",
    "Created on camera",
    "Steps",
    "Result held on screen",
    "Reset if the take misses",
)
VERDICT_FIELDS = (
    "Clear",
    "Interesting",
    "Relatable",
    "Carries the message",
    "Fits this course",
)

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_RE = re.compile(r"^-\s+([A-Z][A-Za-z -]*?):\s*(.*)$")
STEP_RE = re.compile(r"^(\d+)\.\s+(\S.*)$")
STEP_REF_RE = re.compile(r"step\s+(\d+)", re.I)
BACKTICK_RE = re.compile(r"`([^`\n]+)`")
PLACEHOLDER_RE = re.compile(r"<[^<>]{1,300}>", re.S)

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

MIN_EVIDENCE_WORDS = 6  # A verdict line is evidence about this example, not a restatement.
MIN_STEPS = 3  # Creation, path, result. Fewer than three is not a lesson.
MIN_PEDAGOGY_WORDS = 40  # Enough to judge criterion 5 against.
STOPWORDS = {
    "about", "after", "again", "along", "because", "before", "being", "between",
    "could", "every", "first", "itself", "lesson", "other", "should", "steps",
    "their", "there", "these", "thing", "those", "under", "until", "viewer",
    "which", "while", "would", "created", "creates", "camera",
}


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


def protected_ranges(text: str) -> list[tuple[int, int]]:
    """Character ranges inside fenced blocks or inline code, where <angle> is a signature."""
    ranges = [(match.start(), match.end()) for match in re.finditer(r"```.*?```", text, re.S)]
    ranges += [(match.start(), match.end()) for match in re.finditer(r"`[^`\n]*`", text)]
    return ranges


def inside(ranges: list[tuple[int, int]], position: int) -> bool:
    return any(start <= position < end for start, end in ranges)


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


def section_body(lines: list[str], span: tuple[int, int]) -> str:
    return " ".join(text.strip() for _, text in section_lines(lines, span)).strip()


def bullet_entries(lines: list[str], span: tuple[int, int]) -> list[tuple[int, str]]:
    entries: list[tuple[int, str]] = []
    for number, text in section_lines(lines, span):
        stripped = text.strip()
        if stripped.startswith("- "):
            entries.append((number, stripped[2:]))
        elif entries and text.startswith("  ") and stripped:
            first_line, value = entries[-1]
            entries[-1] = (first_line, f"{value} {stripped}")
    return entries


def read_reference(path: str) -> tuple[dict[str, str], list[str]] | None:
    """Read a sibling artifact — the brief or the pedagogy file — without validating it."""
    try:
        with open(path, encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    except OSError:
        return None
    data: dict[str, str] = {}
    if lines and lines[0].strip() == "---":
        for raw in lines[1:]:
            if raw.strip() == "---":
                break
            if ":" in raw:
                key, value = raw.split(":", 1)
                data[key.strip()] = value.strip().strip("\"'")
    return data, lines


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
    if status and status not in ("draft", "approved"):
        report.error(None, f"status must be 'draft' or 'approved': got {status!r}")


def check_placeholders(text: str, lines: list[str], report: Report) -> None:
    commented: set[int] = set()
    for number, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if stripped.startswith("<!--") or stripped.endswith("-->"):
            report.error(number, "template comment left in the take plan; delete it")
            commented.add(number)

    protected = protected_ranges(text)
    for match in PLACEHOLDER_RE.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        if line in commented or inside(protected, match.start()):
            continue
        report.error(line, f"unfilled placeholder {' '.join(match.group(0).split())!r}")


def check_verdict(lines: list[str], sections: dict, report: Report) -> None:
    if "Example verdict" not in sections:
        return
    span = sections["Example verdict"]
    fields: dict[str, tuple[int, str]] = {}
    for number, entry in bullet_entries(lines, span):
        match = FIELD_RE.match(f"- {entry}")
        if match:
            fields[match.group(1).strip()] = (number, match.group(2).strip())

    for name in VERDICT_FIELDS:
        if name not in fields:
            report.error(span[0], f"the example verdict is missing '{name}:'")
            continue
        number, value = fields[name]
        if len(value.split()) < MIN_EVIDENCE_WORDS:
            report.error(
                number,
                f"'{name}:' restates the criterion instead of evidencing it for this example",
            )

    if "Verdict" not in fields:
        report.error(span[0], "the example verdict is missing 'Verdict:'")
    else:
        number, value = fields["Verdict"]
        if value.strip().lower() != "film":
            report.error(
                number,
                f"verdict is {value!r}; an example that did not pass the rubric is not filmed, "
                "it goes back to /research-the-current-lesson",
            )

    body = section_body(lines, span).lower()
    for pattern in SMOKE_TEST_MARKERS:
        if re.search(pattern, body):
            report.error(
                span[0],
                f"the example reads as a smoke test (matched {pattern!r}); "
                "it cannot carry a lesson",
            )


def check_steps(lines: list[str], sections: dict, report: Report) -> list[int]:
    if "Steps" not in sections:
        return []
    numbers: list[int] = []
    for number, text in section_lines(lines, sections["Steps"]):
        match = STEP_RE.match(text.strip())
        if match:
            numbers.append(int(match.group(1)))
    if not numbers:
        report.error(sections["Steps"][0], "the plan has no numbered steps")
        return []
    if len(numbers) < MIN_STEPS:
        report.error(
            sections["Steps"][0],
            f"{len(numbers)} step(s) cannot hold creation, path and result",
        )
    for position, value in enumerate(numbers, start=1):
        if value != position:
            report.error(
                sections["Steps"][0],
                f"steps must run 1..N with no gaps; expected {position}, got {value}",
            )
            break
    return numbers


def check_created_on_camera(
    lines: list[str],
    sections: dict,
    steps: list[int],
    lesson: str,
    brief_section: str,
    report: Report,
) -> None:
    if "Created on camera" not in sections:
        return
    span = sections["Created on camera"]
    entries = bullet_entries(lines, span)
    if not entries:
        report.error(span[0], "no object is listed as created on camera")

    current = int(lesson) if lesson.isdigit() else 0
    creation_steps: list[int] = []
    for number, entry in entries:
        lowered = entry.lower()
        matched = next((p for p in OFF_CAMERA_MARKERS if re.search(p, lowered)), None)
        earlier = [int(value) for value in re.findall(r"lesson\s+(\d+)", lowered)
                   if int(value) < current]
        if matched and not earlier:
            report.error(
                number,
                f"this entry says the object is not created on camera (matched {matched!r}); "
                "either film its creation, or name the earlier lesson that already filmed it",
            )
        if matched and earlier:
            continue

        reference = STEP_REF_RE.search(entry)
        if not reference:
            report.error(number, "entry has no 'step N' reference into the plan's steps")
            continue
        target = int(reference.group(1))
        if steps and target not in steps:
            report.error(number, f"step {target} does not exist in the plan")
            continue
        creation_steps.append(target)
        if brief_section and not shares_token(entry, brief_section):
            report.error(
                number,
                "this object does not appear in the brief's 'Must be created on camera'",
            )

    if creation_steps and steps and min(creation_steps) == max(steps):
        report.error(
            span[0],
            "the only creation step is the last step; a plan that starts at the payoff "
            "hides how the object came to exist",
        )

    for identifier in sorted(backticked(brief_section) - backticked(" ".join(lines))):
        report.warn(
            span[0],
            f"the brief names `{identifier}` as created on camera and the plan never mentions it",
        )


def backticked(text: str) -> set[str]:
    return {value.strip().lower() for value in BACKTICK_RE.findall(text) if value.strip()}


def shares_token(entry: str, reference: str) -> bool:
    """True when the plan entry names something the brief's section also names."""
    if backticked(entry) & backticked(reference):
        return True
    words = {
        word
        for word in re.findall(r"[A-Za-z][A-Za-z0-9_.-]{4,}", entry.lower())
        if word not in STOPWORDS
    }
    return any(word in reference.lower() for word in words)


def check_tail_sections(lines: list[str], sections: dict, report: Report) -> None:
    if "Result held on screen" in sections:
        span = sections["Result held on screen"]
        body = section_body(lines, span)
        if len(body.split()) < MIN_EVIDENCE_WORDS:
            report.error(span[0], "say what the last frames show; this is the lesson's proof")
        elif not re.search(r"\d", body):
            report.warn(span[0], "no hold duration given; a result the viewer cannot read is lost")

    if "Reset if the take misses" in sections:
        span = sections["Reset if the take misses"]
        if len(section_body(lines, span).split()) < MIN_EVIDENCE_WORDS:
            report.error(
                span[0],
                "copy the reset from the brief; improvising it after a missed take is how "
                "half-created state reaches a shipped lesson",
            )


def check_title(lines: list[str], body_start: int, lesson: str, title: str, report: Report) -> None:
    if not title:
        return
    expected = f"Take plan — Lesson {lesson} — {title}"
    for offset in range(body_start, len(lines)):
        if lines[offset].startswith("# "):
            heading = lines[offset][2:].strip()
            if heading != expected:
                report.error(offset + 1, f"H1 should read {expected!r}, got {heading!r}")
            return
    report.error(None, "body has no H1 take-plan heading")


def check_context(data: dict[str, str], path: str, report: Report) -> tuple[str, str]:
    """Confirm the ready brief and the pedagogy file, and return what they establish."""
    absolute = os.path.abspath(path)
    lesson_dir = os.path.dirname(absolute)
    lessons_dir = os.path.dirname(lesson_dir)
    course_dir = os.path.dirname(lessons_dir)

    if os.path.basename(lessons_dir) != "lessons":
        report.warn(
            None,
            "take plan is not at courses/<course-slug>/lessons/<NN>-<lesson-slug>/take-plan.md, "
            "so the brief and pedagogy cross-checks are skipped",
        )
        return "", ""

    number = data.get("lesson", "")
    slug = data.get("lesson_slug", "")
    if number.isdigit() and slug:
        expected = f"{int(number):02d}-{slug}"
        if os.path.basename(lesson_dir) != expected:
            report.error(
                None,
                f"directory {os.path.basename(lesson_dir)!r} does not match the plan; "
                f"expected {expected!r}",
            )

    pedagogy = read_reference(os.path.join(course_dir, "pedagogy.md"))
    if pedagogy is None:
        report.error(
            None,
            f"no {os.path.join(os.path.basename(course_dir), 'pedagogy.md')}; criterion 5 "
            "was judged against nothing",
        )
    elif len(" ".join(pedagogy[1]).split()) < MIN_PEDAGOGY_WORDS:
        report.error(None, "pedagogy.md is too thin to judge an example against")

    brief = read_reference(os.path.join(lesson_dir, "brief.md"))
    if brief is None:
        report.error(None, "no brief.md beside this plan; stage 2 has to run first")
        return "", ""

    brief_data, brief_lines = brief
    if brief_data.get("status") != "ready":
        report.error(
            None,
            f"the brief's status is {brief_data.get('status', 'missing')!r}; filming starts "
            "from a ready brief and from nothing else",
        )

    brief_sections = collect_sections(brief_lines, 0)
    created = (
        section_body(brief_lines, brief_sections["Must be created on camera"])
        if "Must be created on camera" in brief_sections
        else ""
    )
    return created, brief_data.get("title", "")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="path to courses/<slug>/lessons/<NN>-<slug>/take-plan.md")
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

    sections = collect_sections(lines, body_start)
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            report.error(None, f"missing required section '## {name}'")

    brief_section, brief_title = check_context(frontmatter, args.path, report)
    check_title(lines, body_start, frontmatter.get("lesson", ""), brief_title, report)
    check_verdict(lines, sections, report)
    steps = check_steps(lines, sections, report)
    check_created_on_camera(
        lines, sections, steps, frontmatter.get("lesson", ""), brief_section, report
    )
    check_tail_sections(lines, sections, report)

    for message in report.errors:
        print(message)
    for message in report.warnings:
        print(message)

    if report.errors:
        print(
            f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s) "
            "— do not start the recorder"
        )
        return 1

    print(
        f"OK {args.path}: lesson {frontmatter.get('lesson')}, {len(steps)} step(s), "
        f"status {frontmatter.get('status', 'unknown')}, {len(report.warnings)} warning(s)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
