#!/usr/bin/env python3
"""Film lesson 25: open Thunar from the desktop, create rent-receipts, close, reopen."""
from __future__ import annotations

import os
import signal
import subprocess
import time
from pathlib import Path

DISPLAY = os.environ.get("DISPLAY", ":1")
os.environ["DISPLAY"] = DISPLAY
os.environ.setdefault("XDG_RUNTIME_DIR", f"/tmp/runtime-{os.environ.get('USER', 'ubuntu')}")
Path(os.environ["XDG_RUNTIME_DIR"]).mkdir(mode=0o700, exist_ok=True)
ROOT = Path(__file__).resolve().parent
HOME = Path(os.environ.get("HOME", "/home/ubuntu"))
FOLDER = HOME / "rent-receipts"
VIZ = ROOT / "viz/renders/lesson-25-viz.mp4"
OUT = ROOT / "lesson-25.mp4"
W, H = 1920, 1080

from human_input import HumanInput  # noqa: E402

ENV = {**os.environ, "DISPLAY": DISPLAY}


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, env=ENV, **kw)


def pkill_exact(name: str) -> None:
    proc = subprocess.run(["pgrep", "-x", name], capture_output=True, text=True)
    for pid in proc.stdout.split():
        try:
            os.kill(int(pid), signal.SIGTERM)
        except ProcessLookupError:
            pass


def wait_win(patterns: list[str], timeout: float = 3.0, by: str = "class") -> str | None:
    flag = "--class" if by == "class" else "--name"
    t0 = time.time()
    while time.time() - t0 < timeout:
        for pat in patterns:
            r = run(["xdotool", "search", flag, pat], capture_output=True, text=True)
            ids = [x for x in r.stdout.split() if x]
            if ids:
                return ids[-1]
        time.sleep(0.08)
    return None


def fill_screen(wid: str | None) -> None:
    if not wid:
        return
    run(["wmctrl", "-i", "-r", wid, "-b", "add,fullscreen"])
    run(["wmctrl", "-i", "-r", wid, "-e", "0,0,0,1920,1080"])
    run(["xdotool", "windowmove", "--sync", wid, "0", "0"])
    run(["xdotool", "windowsize", "--sync", wid, str(W), str(H)])
    run(["xdotool", "windowactivate", "--sync", wid])


def open_file_manager(h: HumanInput) -> str | None:
    h.move_to(700, 400, target_w=90)
    time.sleep(0.15)
    h.right_click()
    time.sleep(0.4)
    h.move_to(740, 476, target_w=36)
    time.sleep(0.2)
    h.click()
    time.sleep(0.9)
    wid = wait_win(["Thunar"], timeout=4.0, by="class")
    fill_screen(wid)
    time.sleep(0.35)
    return wid


def main() -> None:
    if not VIZ.is_file():
        raise SystemExit(f"missing viz mp4: {VIZ}")
    if FOLDER.exists():
        FOLDER.rmdir()

    pkill_exact("mpv")
    pkill_exact("xfce4-terminal")
    pkill_exact("Thunar")
    pkill_exact("thunar")
    time.sleep(0.4)
    run(["xset", "s", "off"])
    run(["xset", "-dpms"])

    h = HumanInput(W, H, DISPLAY)
    h.park(1680, 920)
    time.sleep(0.3)

    log = open("/tmp/lesson25-ffmpeg.log", "w")
    rec = subprocess.Popen(
        [
            "ffmpeg", "-y", "-f", "x11grab", "-draw_mouse", "1",
            "-video_size", f"{W}x{H}", "-framerate", "60", "-i", DISPLAY,
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
            "-pix_fmt", "yuv420p", "-an", str(OUT),
        ],
        stdout=log, stderr=log,
    )
    time.sleep(0.5)

    mpv = subprocess.Popen(
        [
            "mpv", "--fullscreen", "--no-osc", "--osd-level=0", "--really-quiet",
            "--no-audio", "--keep-open=no", "--no-border", "--cursor-autohide=always",
            "--geometry=1920x1080", str(VIZ),
        ],
        env=ENV,
    )
    time.sleep(0.45)
    fill_screen(wait_win(["mpv"], timeout=2.0, by="class"))
    mpv.wait()
    time.sleep(0.3)

    open_file_manager(h)

    # Go to home (Thunar last-dir may be /workspace)
    h.move_to(900, 420, target_w=160)
    h.click()
    time.sleep(0.2)
    h.alt_home()
    time.sleep(0.7)

    # Create Folder... (Shift+Ctrl+N — same item as File → Create Folder...)
    h.shift_ctrl_n()
    time.sleep(0.6)

    h.type_text("rent-receipts")
    time.sleep(0.25)
    h.press_return()
    time.sleep(1.6)

    h.move_to(720, 240, target_w=80)
    time.sleep(2.8)

    h.ctrl_key("q")
    time.sleep(0.9)

    open_file_manager(h)
    h.move_to(900, 420, target_w=160)
    h.click()
    time.sleep(0.2)
    h.alt_home()
    time.sleep(0.7)
    h.move_to(720, 240, target_w=90)
    time.sleep(5.2)

    rec.send_signal(signal.SIGINT)
    try:
        rec.wait(timeout=20)
    except subprocess.TimeoutExpired:
        rec.send_signal(signal.SIGTERM)
        rec.wait(timeout=8)
    log.close()
    h.close()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
