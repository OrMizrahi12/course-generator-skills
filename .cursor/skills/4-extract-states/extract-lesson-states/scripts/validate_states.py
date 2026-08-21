#!/usr/bin/env python3
"""Validate a lesson states array against what narration syncing needs.

Usage:
    python3 validate_states.py courses/<slug>/lessons/<NN>-<slug>/states.json
                               [--video PATH] [--extract-frames DIR]

Checks the array covers the whole video with no gap and no overlap, that the
timestamps are exact and ordered, that no narration has crept into the file, and
that no object is too short to speak over. With --extract-frames it writes the
start and end frame of every object, so the frame checks in SKILL.md are done by
reading images rather than by remembering the take.

Exit codes:
    0  no errors (warnings may be present)
    1  errors found, the array is not shippable
    2  the file could not be read
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

ALLOWED_KEYS = {"start", "end", "on_screen", "changed"}

# Narration is the other model's job. These are the field names it arrives under.
FORBIDDEN_KEYS = {
    "say", "must_cover", "narration", "narrate", "voiceover", "vo", "script",
    "caption", "subtitle", "line", "lines", "suggested", "suggestion", "tone",
    "emphasis", "advice", "teaching", "takeaway", "note_to_narrator", "speak",
}

# 'changed' states a fact about the picture. These openings state a teaching line.
NARRATION_PHRASES = (
    r"\bnotice\b", r"\bnote that\b", r"\bobserve\b", r"\bremember\b",
    r"\byou (can|will|should|now)\b", r"\bwe (can|will|now|have)\b",
    r"\blet'?s\b", r"\bas you can see\b", r"\bthis shows\b", r"\bthis means\b",
    r"\bhere we\b", r"\bnext,? we\b",
)

EPSILON = 0.002  # seconds of slack for a boundary, below one frame at 60fps
FIRST_START_MAX = 0.5  # the array has to start where the film starts
LAST_END_SLACK = 0.35  # how far the last state may fall short of the file's end
MIN_NARRATABLE = 0.30  # a state shorter than this cannot carry a spoken line
MAX_UNBROKEN = 25.0  # a state longer than this is usually two states


class Report:
    def __init__(self, path: str) -> None:
        self.path = path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, message: str) -> None:
        self.errors.append(f"ERROR {self.path}{where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f"WARN  {self.path}{where}: {message}")


def find_forbidden(node, trail: str = "") -> list[tuple[str, str]]:
    """Narration fields hide at any depth, so look at every key in the tree."""
    found: list[tuple[str, str]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if str(key).strip().lower() in FORBIDDEN_KEYS:
                found.append((f"{trail}.{key}", str(key)))
            found.extend(find_forbidden(value, f"{trail}.{key}"))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            found.extend(find_forbidden(value, f"{trail}[{index}]"))
    return found


def has_content(node) -> bool:
    if isinstance(node, str):
        return bool(node.strip())
    if isinstance(node, dict):
        return any(has_content(value) for value in node.values())
    if isinstance(node, list):
        return any(has_content(value) for value in node)
    return node is not None


def three_decimals(value: float) -> bool:
    return round(float(value), 3) == float(value)


def video_duration(path: str) -> float | None:
    if not shutil.which("ffprobe") or not os.path.isfile(path):
        return None
    done = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True,
    )
    try:
        return float(done.stdout.strip())
    except ValueError:
        return None


def extract_frames(video: str, states: list[dict], out_dir: str) -> int:
    os.makedirs(out_dir, exist_ok=True)
    written = 0
    for index, state in enumerate(states, start=1):
        for label, when in (("start", state["start"]),
                            ("end", max(state["start"], state["end"] - 0.05))):
            target = os.path.join(out_dir, f"{index:03d}-{label}.png")
            done = subprocess.run(
                ["ffmpeg", "-v", "error", "-y", "-ss", f"{float(when):.3f}",
                 "-i", video, "-frames:v", "1", target],
                capture_output=True, text=True,
            )
            if done.returncode == 0 and os.path.exists(target):
                written += 1
    return written


def check_object(index: int, state, report: Report) -> bool:
    where = f"[{index}]"
    if not isinstance(state, dict):
        report.error(where, "each state must be a JSON object")
        return False

    keys = set(state)
    for missing in sorted(ALLOWED_KEYS - keys):
        report.error(where, f"missing '{missing}'")
    for extra in sorted(keys - ALLOWED_KEYS):
        report.error(where, f"unexpected field {extra!r}; the shape is "
                            f"{', '.join(sorted(ALLOWED_KEYS))}")

    ok = True
    for field in ("start", "end"):
        value = state.get(field)
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            report.error(where, f"'{field}' must be a number of seconds")
            ok = False
        elif not three_decimals(value):
            report.error(where, f"'{field}' is {value}; timestamps carry three decimals")
    if ok and float(state["start"]) >= float(state["end"]):
        report.error(where, f"start {state['start']} is not before end {state['end']}")
        ok = False

    if not isinstance(state.get("on_screen"), dict):
        report.error(where, "'on_screen' must be an object of structured facts")
    elif not has_content(state["on_screen"]):
        report.error(where, "'on_screen' is empty; nothing can be narrated over nothing")

    changed = state.get("changed")
    if not isinstance(changed, str) or not changed.strip():
        report.error(where, "'changed' must say what became true on screen")
    else:
        lowered = changed.lower()
        for pattern in NARRATION_PHRASES:
            if re.search(pattern, lowered):
                report.error(
                    where,
                    f"'changed' reads as narration (matched {pattern!r}); state the fact "
                    "about the picture and let the other model decide what to say",
                )
                break
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="the states array")
    parser.add_argument("--video", default=None,
                        help="the lesson MP4 (default: lesson.mp4 beside the array)")
    parser.add_argument("--extract-frames", default=None,
                        help="write the start and end frame of every state here")
    args = parser.parse_args()

    try:
        with open(args.path, encoding="utf-8") as handle:
            data = json.load(handle)
    except OSError as problem:
        print(f"cannot read {args.path}: {problem.strerror}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as problem:
        print(f"{args.path} is not valid JSON: {problem}", file=sys.stderr)
        return 2

    report = Report(args.path)
    if not isinstance(data, list) or not data:
        print(f"ERROR {args.path}: the whole video is one non-empty JSON array",
              file=sys.stderr)
        return 1

    for path, key in find_forbidden(data):
        report.error(path, f"narration field {key!r}; this file describes the picture only")

    timed: list[tuple[int, dict]] = []
    for index, state in enumerate(data):
        if check_object(index, state, report):
            timed.append((index, state))

    for (left_index, left), (right_index, right) in zip(timed, timed[1:]):
        gap = float(right["start"]) - float(left["end"])
        if gap > EPSILON:
            report.error(
                f"[{right_index}]",
                f"{gap:.3f}s gap after state {left_index}; the narration would have "
                "nothing to sit on there",
            )
        elif gap < -EPSILON:
            report.error(
                f"[{right_index}]",
                f"overlaps state {left_index} by {-gap:.3f}s; two lines would compete "
                "for the same second",
            )

    for index, state in timed:
        span = float(state["end"]) - float(state["start"])
        if span < MIN_NARRATABLE:
            report.warn(f"[{index}]", f"{span:.3f}s is too short to speak over; if the "
                                      "picture did not materially change, merge it")
        elif span > MAX_UNBROKEN:
            report.warn(f"[{index}]", f"{span:.1f}s without a change is usually two "
                                      "states; check the frames in the middle")

    for (left_index, left), (_right_index, right) in zip(timed, timed[1:]):
        if left.get("changed") and left.get("changed") == right.get("changed"):
            report.warn(f"[{left_index}]", "the next state reports the same change, which "
                                           "means one of them did not happen")

    if timed and float(timed[0][1]["start"]) > FIRST_START_MAX:
        report.error("[0]", f"the array starts at {timed[0][1]['start']}s; the film starts "
                            "at 0 and the states have to cover it")

    video = args.video or os.path.join(os.path.dirname(os.path.abspath(args.path)),
                                       "lesson.mp4")
    duration = video_duration(video)
    if duration is None:
        report.warn("", f"no readable video at {video}, so coverage of "
                        "the end of the film was not checked")
    elif timed:
        last_end = float(timed[-1][1]["end"])
        if last_end > duration + EPSILON:
            report.error(f"[{timed[-1][0]}]",
                         f"ends at {last_end}s but the video is {duration:.3f}s long")
        elif duration - last_end > LAST_END_SLACK:
            report.error(f"[{timed[-1][0]}]",
                         f"the states stop at {last_end}s and the video runs to "
                         f"{duration:.3f}s; {duration - last_end:.2f}s has no state")

    if args.extract_frames and duration is not None:
        written = extract_frames(video, [state for _index, state in timed],
                                 args.extract_frames)
        print(f"wrote {written} frame(s) to {args.extract_frames}")

    for message in report.errors:
        print(message)
    for message in report.warnings:
        print(message)

    if report.errors:
        print(f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s) "
              "— not shippable")
        return 1

    covered = sum(float(state["end"]) - float(state["start"]) for _index, state in timed)
    print(f"OK {args.path}: {len(timed)} state(s), {covered:.2f}s covered"
          + (f" of a {duration:.2f}s video" if duration else "")
          + f", {len(report.warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
