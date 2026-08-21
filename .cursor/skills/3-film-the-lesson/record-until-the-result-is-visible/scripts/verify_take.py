#!/usr/bin/env python3
"""Check a take against the three gates, using the MP4's own pixels.

Usage:
    python3 verify_take.py lesson.mp4 [--action-at SECONDS] [--hold 3] [--frames-dir DIR]

Writes the frames the three gates need — before, along the path, and at the end —
then reports what the pixels prove: that the picture moves while the action
happens, that it stops moving before the recorder does, and that the ending is
held long enough to read.

It cannot tell whether the result on screen is the result the lesson promised.
Read the frames it writes; references/verify-from-frames.md says what to look for.

Exit codes:
    0  the mechanical checks passed, now read the frames
    1  a check failed, the take is not shippable
    2  the file or ffmpeg could not be used
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

# freezedetect's noise tolerance. Low enough that a few characters appearing in a
# terminal still count as movement, which is the smallest change a lesson ever turns on.
FREEZE_NOISE = 0.00003
MIN_FREEZE = 0.5  # seconds of stillness before it counts as held
STATIC_SHARE = 0.95  # a freeze covering this much of the take means nothing happened
MIN_DURATION = 4.0  # seconds; shorter than this cannot hold an arc
PATH_CHECKPOINTS = 4


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def check(self, name: str, ok: bool, detail: str = "", on_fail: str = "") -> bool:
        note = detail if ok or not on_fail else on_fail
        print(f"  {'pass' if ok else 'FAIL'}  {name}{'  ' + note if note else ''}")
        if not ok:
            self.errors.append(name)
        return ok

    def warn(self, name: str, detail: str = "") -> None:
        print(f"  warn  {name}{'  ' + detail if detail else ''}")
        self.warnings.append(name)


def probe(path: str) -> dict:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height,avg_frame_rate:format=duration", "-of", "json", path],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "ffprobe failed")
    data = json.loads(result.stdout)
    stream = data["streams"][0]
    numerator, _, denominator = stream["avg_frame_rate"].partition("/")
    fps = float(numerator) / float(denominator or 1)
    return {
        "width": stream["width"],
        "height": stream["height"],
        "fps": fps,
        "duration": float(data["format"]["duration"]),
    }


def extract(path: str, when: float, out: str) -> bool:
    done = subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", f"{when:.3f}", "-i", path,
         "-frames:v", "1", out],
        capture_output=True, text=True,
    )
    return done.returncode == 0 and os.path.exists(out)


def freezes(path: str, noise: float, duration: float) -> list[tuple[float, float]]:
    """Stretches where the picture holds still, as (start, end) in seconds."""
    done = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", path,
         "-vf", f"freezedetect=n={noise}:d={MIN_FREEZE}", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    spans: list[tuple[float, float]] = []
    start: float | None = None
    for match in re.finditer(r"freeze_(start|end): ([0-9.]+)", done.stderr):
        kind, value = match.group(1), float(match.group(2))
        if kind == "start":
            start = value
        elif start is not None:
            spans.append((start, value))
            start = None
    if start is not None:  # a freeze that runs to the end of the file has no end line
        spans.append((start, duration))
    return spans


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="the recorded take")
    parser.add_argument("--action-at", type=float, default=None,
                        help="seconds at which the action begins, for the before frame")
    parser.add_argument("--hold", type=float, default=3.0,
                        help="seconds the finished result must be held (default 3)")
    parser.add_argument("--frames-dir", default=None,
                        help="where to write the frames (default: <take>-frames/)")
    parser.add_argument("--freeze-noise", type=float, default=FREEZE_NOISE,
                        help="stillness tolerance; raise it for a UI with a blinking caret")
    args = parser.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            print(f"{tool} is not on PATH", file=sys.stderr)
            return 2
    if not os.path.isfile(args.path):
        print(f"cannot read {args.path}", file=sys.stderr)
        return 2

    try:
        info = probe(args.path)
    except (RuntimeError, KeyError, ValueError) as problem:
        print(f"cannot probe {args.path}: {problem}", file=sys.stderr)
        return 2

    frames_dir = args.frames_dir or os.path.splitext(args.path)[0] + "-frames"
    os.makedirs(frames_dir, exist_ok=True)
    report = Report()
    duration = info["duration"]

    print(f"{args.path}: {info['width']}x{info['height']}, {info['fps']:.0f}fps, "
          f"{duration:.1f}s")

    print("\nrecording")
    report.check("the take is long enough to hold an arc", duration >= MIN_DURATION,
                 f"{duration:.1f}s")
    if info["fps"] < 30:
        report.warn("recorded below 30fps", f"{info['fps']:.0f}fps shows pointer motion as steps")

    spans = freezes(args.path, args.freeze_noise, duration)
    longest = max((end - start for start, end in spans), default=0.0)
    report.check("something actually happens on screen",
                 longest < duration * STATIC_SHARE,
                 f"the picture holds still for {longest:.1f}s of {duration:.1f}s")

    ending = [span for span in spans if span[1] >= duration - 0.35]
    settled_at = ending[0][0] if ending else duration
    tail = duration - settled_at

    print("\ngate 3: the result is finished and held")
    report.check("the picture stops changing before the recorder does", bool(ending),
                 f"settled at {settled_at:.1f}s of {duration:.1f}s",
                 on_fail="the take ends while the screen is still moving, which is a "
                         "result that was cut off mid-stream")
    report.check(f"the ending is held at least {args.hold:.0f}s",
                 tail >= args.hold, f"held {tail:.1f}s")
    if not ending:
        print("       (if this UI has a blinking caret or an animated background, "
              f"raise --freeze-noise above {args.freeze_noise})")

    print("\nframes to read")
    before_at = max(0.2, (args.action_at - 0.6) if args.action_at else 0.5)
    written: list[str] = []
    for name, when in [("01-before", before_at)] + (
        [("02-action-start", args.action_at)] if args.action_at else []
    ):
        target = os.path.join(frames_dir, f"{name}.png")
        if extract(args.path, when, target):
            written.append(f"{target}  (t={when:.1f}s)")

    path_start = args.action_at or duration * 0.1
    path_end = max(path_start, settled_at)
    for index in range(1, PATH_CHECKPOINTS + 1):
        when = path_start + (path_end - path_start) * index / (PATH_CHECKPOINTS + 1)
        target = os.path.join(frames_dir, f"1{index}-path.png")
        if extract(args.path, when, target):
            written.append(f"{target}  (t={when:.1f}s)")

    for offset in (3.0, 2.0, 1.0, 0.15):
        when = max(0.0, duration - offset)
        target = os.path.join(frames_dir, f"2{int(offset * 10):02d}-result.png")
        if extract(args.path, when, target):
            written.append(f"{target}  (t={when:.1f}s)")

    for line in written:
        print(f"  {line}")

    print()
    if report.errors:
        print(f"{len(report.errors)} check(s) failed — the take is not shippable: "
              f"{', '.join(report.errors)}")
        return 1
    print("mechanical checks passed. Now read the frames above against the three gates: "
          "the before frame states what the action will change, the path frames connect "
          "without a gap, and the result frames show the finished output.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
