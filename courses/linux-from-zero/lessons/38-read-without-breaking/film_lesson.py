#!/usr/bin/env python3
"""Film lesson 38: cat, head, tail, then install less and page the rent log."""
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
VIZ = ROOT / "viz/renders/lesson-38-viz.mp4"
OUT = ROOT / "lesson-38.mp4"
W, H = 1920, 1080
WORK = Path("/home/ubuntu/linux-workshop")
NOTE = WORK / "rent-log.txt"
LESS = Path("/usr/bin/less")

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


def wait_apt_idle(timeout: float = 180.0) -> None:
    time.sleep(2.0)
    t0 = time.time()
    while time.time() - t0 < timeout:
        proc = subprocess.run(["pgrep", "-x", "apt-get"], capture_output=True)
        if proc.returncode != 0:
            time.sleep(1.2)
            return
        time.sleep(0.4)
    raise SystemExit("apt-get still running")


def wait_less_installed(timeout: float = 180.0) -> None:
    t0 = time.time()
    while time.time() - t0 < timeout:
        if LESS.is_file() and os.access(LESS, os.X_OK):
            time.sleep(1.4)
            return
        time.sleep(0.4)
    raise SystemExit("less did not appear after apt-get install")


def main() -> None:
    if not VIZ.is_file():
        raise SystemExit(f"missing viz mp4: {VIZ}")
    if not WORK.is_dir():
        raise SystemExit("linux-workshop missing; lesson 35 must exist")
    if not NOTE.is_file():
        raise SystemExit("rent-log.txt missing; lesson 36 must exist")
    if LESS.exists():
        raise SystemExit("less already installed; reset before filming")

    pkill_exact("mpv")
    pkill_exact("xfce4-terminal")
    pkill_exact("Thunar")
    pkill_exact("nano")
    time.sleep(0.4)
    run(["xset", "s", "off"])
    run(["xset", "-dpms"])

    h = HumanInput(W, H, DISPLAY)
    h.park(1680, 920)
    time.sleep(0.3)

    log = open("/tmp/lesson38-ffmpeg.log", "w")
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

    h.move_to(700, 400, target_w=90)
    time.sleep(0.15)
    h.right_click()
    time.sleep(0.4)
    h.move_to(740, 448, target_w=36)
    time.sleep(0.2)
    h.click()
    time.sleep(0.85)
    fill_screen(wait_win(["xfce4-terminal"], timeout=3.0, by="class"))
    time.sleep(0.25)
    h.move_to(960, 540, target_w=220)
    h.click()
    time.sleep(0.45)
    h.type_line("pwd")
    time.sleep(1.4)
    h.type_line("cd ~/linux-workshop")
    time.sleep(1.4)
    h.type_line("ls")
    time.sleep(1.6)
    h.type_line("cat rent-log.txt")
    time.sleep(2.2)
    h.type_line("head -n 2 rent-log.txt")
    time.sleep(1.8)
    h.type_line("tail -n 1 rent-log.txt")
    time.sleep(1.8)
    h.type_line("less rent-log.txt")
    time.sleep(2.0)
    h.type_line("sudo apt-get update")
    wait_apt_idle()
    h.type_line("sudo apt-get install -y less")
    wait_less_installed()
    time.sleep(1.8)
    h.type_line("less --version")
    time.sleep(2.2)
    h.type_line("less rent-log.txt")
    time.sleep(3.5)
    h.type_text("q")
    time.sleep(1.6)
    h.type_line("tail -n 1 rent-log.txt")
    time.sleep(6.0)

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
