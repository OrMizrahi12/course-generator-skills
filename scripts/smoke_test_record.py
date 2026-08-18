#!/usr/bin/env python3
"""Record a minimal terminal smoke-test MP4."""

from __future__ import annotations

import os
import signal
import subprocess
import sys
import time
from pathlib import Path

from human_input import HumanInput

WIDTH = 1920
HEIGHT = 1200
OUTPUT = Path("/opt/cursor/artifacts/smoke-test-terminal.mp4")
TERMINAL_TITLE = "Smoke Test Terminal"


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    env.setdefault("DISPLAY", ":1")
    return subprocess.run(cmd, env=env, check=True, **kwargs)


def start_terminal() -> subprocess.Popen:
    env = os.environ.copy()
    env.setdefault("DISPLAY", ":1")
    proc = subprocess.Popen(
        [
            "xfce4-terminal",
            "--maximize",
            "--hide-menubar",
            "--hide-toolbar",
            f"--title={TERMINAL_TITLE}",
            "--working-directory=/workspace",
        ],
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    time.sleep(1.5)
    return proc


def focus_terminal() -> None:
    out = subprocess.check_output(
        ["xdotool", "search", "--name", TERMINAL_TITLE],
        env={**os.environ, "DISPLAY": ":1"},
        text=True,
    ).strip()
    if not out:
        raise RuntimeError("Terminal window not found")
    win_id = out.splitlines()[-1]
    run(["xdotool", "windowactivate", "--sync", win_id])
    run(["xdotool", "windowfocus", win_id])
    run(["xdotool", "windowsize", win_id, str(WIDTH), str(HEIGHT)])
    run(["xdotool", "windowmove", win_id, "0", "0"])
    time.sleep(0.5)


def start_ffmpeg() -> subprocess.Popen:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()
    return subprocess.Popen(
        [
            "ffmpeg",
            "-y",
            "-f",
            "x11grab",
            "-draw_mouse",
            "1",
            "-video_size",
            f"{WIDTH}x{HEIGHT}",
            "-framerate",
            "60",
            "-i",
            os.environ.get("DISPLAY", ":1"),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "16",
            "-pix_fmt",
            "yuv420p",
            "-an",
            str(OUTPUT),
        ],
        env={**os.environ, "DISPLAY": ":1"},
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )


def stop_ffmpeg(proc: subprocess.Popen) -> None:
    if proc.poll() is None:
        proc.send_signal(signal.SIGINT)
        try:
            proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=5)


def verify_mp4() -> None:
    probe = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height,r_frame_rate,duration",
            "-of",
            "default=noprint_wrappers=1",
            str(OUTPUT),
        ],
        text=True,
    )
    print(probe)

    frame_path = Path("/tmp/smoke_last.png")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-sseof",
            "-3",
            "-i",
            str(OUTPUT),
            "-frames:v",
            "1",
            str(frame_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"Last frame saved to {frame_path}")


def main() -> int:
    os.environ.setdefault("DISPLAY", ":1")
    terminal_proc = start_terminal()
    focus_terminal()

    hi = HumanInput(WIDTH, HEIGHT)
    hi.park()

    ff = start_ffmpeg()
    time.sleep(0.8)

    try:
        hi.move_to(WIDTH // 2, HEIGHT // 2, target_w=120)
        hi.click()
        time.sleep(0.4)

        commands = [
            "pwd",
            "ls -la /workspace",
            'echo pipeline-ok',
            "date",
        ]
        for cmd in commands:
            hi.type_text(cmd)
            hi.press_enter()
            time.sleep(1.2)

        time.sleep(4.0)
    finally:
        stop_ffmpeg(ff)
        hi.close()
        if terminal_proc.poll() is None:
            terminal_proc.terminate()
            try:
                terminal_proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                terminal_proc.kill()

    if not OUTPUT.exists() or OUTPUT.stat().st_size < 1000:
        print("ERROR: MP4 missing or too small", file=sys.stderr)
        return 1

    verify_mp4()
    print(f"Smoke test MP4: {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
