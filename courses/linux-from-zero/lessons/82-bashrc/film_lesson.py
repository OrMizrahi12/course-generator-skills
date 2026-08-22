#!/usr/bin/env python3
"""Film lesson 82: alias due in ~/.bashrc, source, run due from home."""
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
VIZ = ROOT / "viz/renders/lesson-82-viz.mp4"
OUT = ROOT / "lesson-82.mp4"
W, H = 1920, 1080

from human_input import HumanInput  # noqa: E402

ENV = {**os.environ, "DISPLAY": DISPLAY}

ALIAS = "alias due=/home/ubuntu/linux-workshop/due"


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, env=ENV, **kw)


def kill_rent_tails() -> None:
    proc = subprocess.run(["pgrep", "-x", "tail"], capture_output=True, text=True)
    for pid_s in proc.stdout.split():
        pid = int(pid_s)
        try:
            raw = Path(f"/proc/{pid}/cmdline").read_bytes()
        except FileNotFoundError:
            continue
        cmd = raw.replace(b"\x00", b" ").decode("utf-8", "replace")
        if "rent-log" in cmd:
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                pass


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


def main() -> None:
    if not VIZ.is_file():
        raise SystemExit(f"missing viz mp4: {VIZ}")
    bashrc = Path("/home/ubuntu/.bashrc")
    if ALIAS in bashrc.read_text():
        raise SystemExit("due alias already in .bashrc — reset before filming")
    if not Path("/home/ubuntu/linux-workshop/due").is_file():
        raise SystemExit("missing workshop due binary")
    kill_rent_tails()
    pkill_exact("sha256sum")
    pkill_exact("top")

    pkill_exact("mpv")
    pkill_exact("xfce4-terminal")
    pkill_exact("Thunar")
    pkill_exact("nano")
    pkill_exact("less")
    time.sleep(0.4)
    run(["xset", "s", "off"])
    run(["xset", "-dpms"])

    h = HumanInput(W, H, DISPLAY)
    h.park(1680, 920)
    time.sleep(0.3)

    log = open("/tmp/lesson82-ffmpeg.log", "w")
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
    h.type_line("cd ~")
    time.sleep(1.2)
    h.type_line("cat .bashrc")
    time.sleep(2.0)
    h.type_line("nano .bashrc")
    time.sleep(1.5)
    fill_screen(wait_win(["xfce4-terminal"], timeout=2.0, by="class"))
    time.sleep(0.3)
    for _ in range(6):
        h.press_down()
        time.sleep(0.08)
    h.press_end()
    time.sleep(0.25)
    h.press_return()
    time.sleep(0.3)
    h.type_text(ALIAS)
    time.sleep(0.7)
    h.ctrl_key("o")
    time.sleep(0.9)
    h.press_return()
    time.sleep(1.2)
    h.ctrl_key("x")
    time.sleep(1.4)
    h.type_line("source .bashrc")
    time.sleep(1.6)
    h.type_line("type due")
    time.sleep(1.8)
    h.type_line("due")
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
