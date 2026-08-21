#!/usr/bin/env python3
"""Validate a syllabus artifact written by the build-a-course-syllabus skill.

Usage:
    python3 scripts/validate_syllabus.py courses/<course-slug>/syllabus.md

Exit codes:
    0  no errors (warnings may be present)
    1  errors found, the syllabus is not ready to show the user
    2  the file could not be read
"""

from __future__ import annotations

import argparse
import os
import re
import sys

REQUIRED_KEYS = ("course", "slug", "status", "level", "delivery", "lessons_planned")
REQUIRED_SECTIONS = ("Promise", "Audience and level", "Out of scope", "Spine", "Sources")
REQUIRED_LESSON_FIELDS = (
    "Can do after",
    "Feature taught",
    "Why here",
    "Example shape",
    "Result on screen",
    "Depends on",
    "Sources",
)

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LESSON_HEADING_RE = re.compile(r"^###\s+Lesson\s+(\d+)\s*(?:—|–|-)\s*(\S.*?)\s*$")
FIELD_RE = re.compile(r"^-\s+([A-Z][A-Za-z ]*?):\s*(.*)$")
URL_RE = re.compile(r"https?://[^\s<>,;)\]]+")
REAL_URL_RE = re.compile(r"^https?://[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,}(?:/|$)")
PLACEHOLDER_RE = re.compile(r"<[^<>]{1,300}>", re.S)

# A lesson promises something the viewer does. These openings promise a feeling,
# and no camera can film a feeling.
BANNED_COMPETENCE_OPENERS = (
    "understand",
    "understands",
    "know",
    "knows",
    "knowing",
    "learn",
    "learns",
    "grasp",
    "appreciate",
    "realize",
    "be familiar",
    "be aware",
    "get to know",
    "see how",
    "have a sense",
)

# Titles that describe a chapter of a manual instead of a job someone finished.
BANNED_TITLE_PATTERNS = (
    (r"\boverview\b", "an overview is a tour: nothing is created and nothing finishes"),
    (r"\btour\b", "a tour has no competence and no visible result"),
    (r"\bintro(duction)? to\b", "that names a topic, not a job"),
    (r"\btips and tricks\b", "no spine, no dependency, no end state"),
    (r"\beverything you can do\b", "cannot be filmed 0% to 100% in one take"),
    (r"\bwalk-?through of\b", "a walk-through of a surface is a tour"),
)

SOFT_TITLE_PATTERNS = (
    (r"\bunderstanding\b", "usually a feeling, not a job"),
    (r"\bexplained\b", "explaining is narration, and these lessons are silent"),
    (r"\bbasics of\b", "vague scope; name the thing the viewer produces"),
    (r"\bgetting started\b", "often a tour wearing a verb"),
    (r"\bdeep dive\b", "vague scope; name the thing the viewer produces"),
)

MAX_PROMISE_WORDS = 35  # One sentence to the viewer. Longer means it is a paragraph.
MIN_DESCRIPTION_WORDS = 3  # A source entry has to say what it established.


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


def parse_frontmatter(lines: list[str], report: Report) -> tuple[dict[str, str], int]:
    """Return the frontmatter mapping and the line number where the body starts."""
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


def check_frontmatter(data: dict[str, str], path: str, report: Report) -> None:
    for key in REQUIRED_KEYS:
        if not data.get(key):
            report.error(None, f"frontmatter is missing a value for '{key}'")

    slug = data.get("slug", "")
    if slug and not SLUG_RE.match(slug):
        report.error(None, f"slug must be kebab-case lowercase: got {slug!r}")

    status = data.get("status", "")
    if status and status not in ("draft", "accepted"):
        report.error(None, f"status must be 'draft' or 'accepted': got {status!r}")

    planned = data.get("lessons_planned", "")
    if planned and not planned.isdigit():
        report.error(None, f"lessons_planned must be a positive integer: got {planned!r}")
    elif planned.isdigit() and int(planned) == 0:
        report.error(None, "lessons_planned must be at least 1")

    parent = os.path.basename(os.path.dirname(os.path.abspath(path)))
    grandparent = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(path))))
    if grandparent == "courses":
        if slug and parent != slug:
            report.error(
                None,
                f"directory name {parent!r} does not match slug {slug!r}; "
                "the artifact belongs at courses/<slug>/syllabus.md",
            )
    else:
        report.warn(None, "artifact is not at courses/<course-slug>/syllabus.md")


def check_placeholders(text: str, lines: list[str], report: Report) -> None:
    commented: set[int] = set()
    for number, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if stripped.startswith("<!--") or stripped.endswith("-->"):
            report.error(number, "template comment left in the artifact; delete it")
            commented.add(number)

    for match in PLACEHOLDER_RE.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        if line in commented:
            continue
        found = match.group(0)
        if any(is_real_url(normalize_url(url)) for url in URL_RE.findall(found)):
            continue
        shown = " ".join(found.split())
        report.error(line, f"unfilled placeholder {shown!r}")


def collect_sections(lines: list[str], body_start: int) -> dict[str, tuple[int, int]]:
    """Map '## Section' titles to their (start_line, end_line), 1-based inclusive."""
    marks: list[tuple[str, int]] = []
    for offset in range(body_start, len(lines)):
        if lines[offset].startswith("## "):
            marks.append((lines[offset][3:].strip(), offset + 1))
    sections: dict[str, tuple[int, int]] = {}
    for position, (title, start) in enumerate(marks):
        end = marks[position + 1][1] - 1 if position + 1 < len(marks) else len(lines)
        sections[title] = (start, end)
    return sections


def section_text(lines: list[str], span: tuple[int, int]) -> list[tuple[int, str]]:
    start, end = span
    return [(number, lines[number - 1]) for number in range(start + 1, end + 1)]


def check_title(lines: list[str], body_start: int, course: str, report: Report) -> None:
    for offset in range(body_start, len(lines)):
        if lines[offset].startswith("# "):
            heading = lines[offset][2:].strip()
            if course and heading != course:
                report.error(
                    offset + 1,
                    f"H1 {heading!r} does not match frontmatter course {course!r}",
                )
            return
    report.error(None, "body has no H1 course title")


def check_promise(lines: list[str], sections: dict, report: Report) -> None:
    if "Promise" not in sections:
        return
    words = " ".join(text for _, text in section_text(lines, sections["Promise"])).split()
    if not words:
        report.error(sections["Promise"][0], "Promise section is empty")
    elif len(words) > MAX_PROMISE_WORDS:
        report.warn(
            sections["Promise"][0],
            f"promise is {len(words)} words; one sentence to the viewer is the target",
        )


def check_out_of_scope(lines: list[str], sections: dict, report: Report) -> None:
    if "Out of scope" not in sections:
        return
    bullets = [
        (number, text)
        for number, text in section_text(lines, sections["Out of scope"])
        if text.strip().startswith("- ")
    ]
    if not bullets:
        report.error(
            sections["Out of scope"][0],
            "Out of scope is empty; an unstated boundary is a defect, not a courtesy",
        )
    for number, text in bullets:
        if len(text.strip("- ").split()) < MIN_DESCRIPTION_WORDS:
            report.error(number, "out-of-scope entry is too short to mean anything")


def normalize_url(url: str) -> str:
    return url.strip().strip("<>").rstrip(".,;)").rstrip("/")


def is_real_url(url: str) -> bool:
    """True for a URL that was actually fetched, false for 'https://...' shaped stubs."""
    return bool(REAL_URL_RE.match(url)) and "..." not in url


def check_ledger(lines: list[str], sections: dict, report: Report) -> set[str]:
    ledger: set[str] = set()
    if "Sources" not in sections:
        return ledger
    start = sections["Sources"][0]
    entries = [
        (number, text)
        for number, text in section_text(lines, sections["Sources"])
        if text.strip().startswith("- ")
    ]
    if not entries:
        report.error(start, "Sources ledger is empty; every spine traces to live sources")
    for number, text in entries:
        urls = URL_RE.findall(text)
        if not urls:
            report.error(number, "source entry has no URL")
            continue
        for url in urls:
            if not is_real_url(normalize_url(url)):
                report.error(number, f"{url} is not a real URL you fetched")
        ledger.update(normalize_url(url) for url in urls if is_real_url(normalize_url(url)))
        tail = text.split(urls[-1], 1)[-1]
        if len(re.sub(r"^[\s—–\-:>]+", "", tail).split()) < MIN_DESCRIPTION_WORDS:
            report.error(number, "source entry must say what it established")
    return ledger


def parse_lessons(lines: list[str], sections: dict, report: Report) -> list[dict]:
    if "Spine" not in sections:
        return []
    start, end = sections["Spine"]
    lessons: list[dict] = []
    current: dict | None = None
    last_field: str | None = None

    for number in range(start + 1, end + 1):
        raw = lines[number - 1]
        if raw.startswith("### "):
            match = LESSON_HEADING_RE.match(raw)
            if not match:
                report.error(number, "lesson heading must read '### Lesson N — Title'")
                current = None
                continue
            current = {
                "number": int(match.group(1)),
                "title": match.group(2),
                "line": number,
                "fields": {},
                "field_lines": {},
            }
            lessons.append(current)
            last_field = None
            continue
        if current is None:
            continue
        field = FIELD_RE.match(raw)
        if field:
            name = field.group(1).strip()
            current["fields"][name] = field.group(2).strip()
            current["field_lines"][name] = number
            last_field = name
        elif raw.startswith("  ") and raw.strip() and last_field:
            current["fields"][last_field] += " " + raw.strip()
        elif not raw.strip():
            last_field = None
    return lessons


def check_lessons(lessons: list[dict], planned: str, ledger: set[str], report: Report) -> None:
    if not lessons:
        report.error(None, "spine has no lessons")
        return

    if planned.isdigit() and int(planned) != len(lessons):
        report.error(
            None,
            f"lessons_planned is {planned} but the spine has {len(lessons)} lessons",
        )

    for position, lesson in enumerate(lessons, start=1):
        if lesson["number"] != position:
            report.error(
                lesson["line"],
                f"lesson numbering must run 1..N with no gaps; expected Lesson {position}",
            )

    seen: dict[str, int] = {}
    for lesson in lessons:
        key = lesson["title"].lower()
        if key in seen:
            report.error(lesson["line"], f"duplicate lesson title, first seen on line {seen[key]}")
        seen[key] = lesson["line"]

    for lesson in lessons:
        check_one_lesson(lesson, ledger, report)


def check_one_lesson(lesson: dict, ledger: set[str], report: Report) -> None:
    line = lesson["line"]
    title_lower = lesson["title"].lower()

    for pattern, why in BANNED_TITLE_PATTERNS:
        if re.search(pattern, title_lower):
            report.error(line, f"banned lesson shape in title ({why})")
    for pattern, why in SOFT_TITLE_PATTERNS:
        if re.search(pattern, title_lower):
            report.warn(line, f"weak lesson title ({why})")

    for name in REQUIRED_LESSON_FIELDS:
        if name not in lesson["fields"]:
            report.error(line, f"lesson is missing the '{name}:' field")
        elif not lesson["fields"][name]:
            report.error(lesson["field_lines"][name], f"'{name}:' has no value")

    for name in lesson["fields"]:
        if name not in REQUIRED_LESSON_FIELDS:
            report.warn(lesson["field_lines"][name], f"unrecognized lesson field {name!r}")

    competence = lesson["fields"].get("Can do after", "").lower().lstrip("*_ ")
    if competence:
        for opener in BANNED_COMPETENCE_OPENERS:
            if competence.startswith(opener):
                report.error(
                    lesson["field_lines"]["Can do after"],
                    f"'Can do after' starts with {opener!r}; name a verb the viewer performs",
                )
                break

    depends = lesson["fields"].get("Depends on", "")
    if depends:
        referenced = [int(value) for value in re.findall(r"[Ll]esson\s+(\d+)", depends)]
        if depends.strip().lower() == "none":
            pass
        elif not referenced:
            report.error(
                lesson["field_lines"]["Depends on"],
                "'Depends on' must be 'none' or one or more 'Lesson N' references",
            )
        else:
            for target in referenced:
                if target >= lesson["number"]:
                    report.error(
                        lesson["field_lines"]["Depends on"],
                        f"Lesson {lesson['number']} depends on Lesson {target}, "
                        "which is not taught yet",
                    )

    sources = lesson["fields"].get("Sources", "")
    if sources:
        found = URL_RE.findall(sources)
        if not found:
            report.error(
                lesson["field_lines"]["Sources"],
                "lesson has no source URL; a feature with no live source is not on the spine",
            )
        for raw_url in found:
            url = normalize_url(raw_url)
            if not is_real_url(url):
                report.error(
                    lesson["field_lines"]["Sources"],
                    f"{raw_url} is not a real URL you fetched",
                )
            elif url not in ledger:
                report.error(
                    lesson["field_lines"]["Sources"],
                    f"{raw_url} is not in the ## Sources ledger",
                )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="path to courses/<course-slug>/syllabus.md")
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
    check_frontmatter(frontmatter, args.path, report)
    check_placeholders(text, lines, report)
    check_title(lines, body_start, frontmatter.get("course", ""), report)

    sections = collect_sections(lines, body_start)
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            report.error(None, f"missing required section '## {name}'")

    check_promise(lines, sections, report)
    check_out_of_scope(lines, sections, report)
    ledger = check_ledger(lines, sections, report)
    lessons = parse_lessons(lines, sections, report)
    check_lessons(lessons, frontmatter.get("lessons_planned", ""), ledger, report)

    for message in report.errors:
        print(message)
    for message in report.warnings:
        print(message)

    error_count = len(report.errors)
    warning_count = len(report.warnings)
    if error_count:
        print(f"\n{error_count} error(s), {warning_count} warning(s) — not ready to show")
        return 1

    status = frontmatter.get("status", "unknown")
    print(
        f"OK {args.path}: {len(lessons)} lesson(s), {len(ledger)} source(s), "
        f"status {status}, {warning_count} warning(s)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
