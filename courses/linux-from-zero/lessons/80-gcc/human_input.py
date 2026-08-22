#!/usr/bin/env python3
"""Human-like X11 pointer + keyboard. See human-screen-recordings skill."""
from __future__ import annotations

import math
import os
import random
import time

from Xlib import XK, X, display
from Xlib.ext import xtest

LEFT = set("qwertasdfgzxcvb")
RIGHT = set("yuiophjklnm")
COMMON = set("th he in er an re on at en ed to it is or te al es".split())

NAMED = {
    " ": "space",
    "\n": "Return",
    "\t": "Tab",
    "-": "minus",
    "_": "underscore",
    ".": "period",
    "/": "slash",
    "\\": "backslash",
    "|": "bar",
    "=": "equal",
    "'": "apostrophe",
    "*": "asterisk",
    "&": "ampersand",
    "%": "percent",
    "$": "dollar",
    "~": "asciitilde",
    '"': "quotedbl",
    ";": "semicolon",
    ",": "comma",
    "`": "grave",
    "[": "bracketleft",
    "]": "bracketright",
    ">": "greater",
    "^": "asciicircum",
    "{": "braceleft",
    "}": "braceright",
    "#": "numbersign",
    "(": "parenleft",
    ")": "parenright",
    "<": "comma",
}


class HumanInput:
    def __init__(self, width: int, height: int, dpy: str | None = None):
        self.width = width
        self.height = height
        self.margin = 18
        self.d = display.Display(dpy or os.environ.get("DISPLAY", ":1"))
        self.shift = self.d.keysym_to_keycode(XK.XK_Shift_L)
        self.ctrl = self.d.keysym_to_keycode(XK.XK_Control_L)
        self.alt = self.d.keysym_to_keycode(XK.XK_Alt_L)
        self.home = self.d.keysym_to_keycode(XK.XK_Home)
        self.nkey = self.d.keysym_to_keycode(XK.XK_n)
        self.sync_pointer()

    def sync_pointer(self) -> None:
        ptr = self.d.screen().root.query_pointer()
        self.x, self.y = int(ptr.root_x), int(ptr.root_y)

    def _flush_move(self, x: int, y: int) -> None:
        x = max(self.margin, min(self.width - self.margin - 1, int(round(x))))
        y = max(self.margin, min(self.height - self.margin - 1, int(round(y))))
        xtest.fake_input(self.d, X.MotionNotify, x=x, y=y)
        self.d.flush()
        self.x, self.y = x, y

    def park(self, x: int | None = None, y: int | None = None) -> None:
        self.sync_pointer()
        if self.x < self.margin + 4 or self.y < self.margin + 4:
            self._flush_move(int(self.width * 0.40), int(self.height * 0.45))
            time.sleep(0.12)
        self.move_to(
            x if x is not None else int(self.width * 0.57),
            y if y is not None else int(self.height * 0.50),
            target_w=80,
        )
        time.sleep(0.25)

    def move_to(self, x: int, y: int, target_w: int = 48) -> None:
        x0, y0 = self.x, self.y
        dx, dy = x - x0, y - y0
        dist = math.hypot(dx, dy) or 1
        T = 0.085 + 0.125 * math.log2(dist / max(target_w, 1) + 1)
        T = max(0.22, min(1.15, T))
        n = max(int(T * 240), 40)
        bulge = dist * random.uniform(0.04, 0.09)
        px, py = -dy / dist * bulge, dx / dist * bulge
        ballistic = int(n * 0.78)
        for i in range(ballistic):
            u = (i + 1) / ballistic
            u = u**0.72
            u = u * u * (3 - 2 * u)
            cover = random.uniform(0.92, 0.97)
            xx = x0 + dx * u * cover + px * math.sin(math.pi * u)
            yy = y0 + dy * u * cover + py * math.sin(math.pi * u)
            self._flush_move(xx, yy)
            time.sleep(T * 0.78 / ballistic)
        if dist > 80 and random.random() < 0.7:
            ox = x + random.choice((-1, 1)) * random.randint(6, 14)
            oy = y + random.choice((-1, 1)) * random.randint(6, 14)
            steps = max(int(0.12 * 240), 12)
            for i in range(steps):
                u = (i + 1) / steps
                self._flush_move(ox + (x - ox) * u * 0.15, oy + (y - oy) * u * 0.15)
                time.sleep(0.12 / steps)
            steps = max(int(0.16 * 240), 14)
            sx, sy = self.x, self.y
            for i in range(steps):
                u = (i + 1) / steps
                self._flush_move(sx + (x - sx) * u, sy + (y - sy) * u)
                time.sleep(0.16 / steps)
        else:
            steps = max(int(0.12 * 240), 12)
            sx, sy = self.x, self.y
            for i in range(steps):
                u = (i + 1) / steps
                self._flush_move(sx + (x - sx) * u, sy + (y - sy) * u)
                time.sleep(0.12 / steps)
        self._flush_move(x, y)

    def click(self) -> None:
        time.sleep(random.uniform(0.14, 0.32))
        xtest.fake_input(self.d, X.ButtonPress, 1)
        self.d.flush()
        time.sleep(random.uniform(0.05, 0.09))
        xtest.fake_input(self.d, X.ButtonRelease, 1)
        self.d.flush()

    def right_click(self) -> None:
        time.sleep(random.uniform(0.16, 0.34))
        xtest.fake_input(self.d, X.ButtonPress, 3)
        self.d.flush()
        time.sleep(random.uniform(0.05, 0.09))
        xtest.fake_input(self.d, X.ButtonRelease, 3)
        self.d.flush()

    def _keycode(self, ch: str) -> tuple[int, bool]:
        shift = False
        if ch in NAMED:
            ks = XK.string_to_keysym(NAMED[ch])
            shift = ch in '_|*$~"&%>^{}#()<'
        elif ch.isupper():
            ks = XK.string_to_keysym(ch.lower())
            shift = True
        elif ch.isalnum():
            ks = XK.string_to_keysym(ch)
        else:
            ks = XK.string_to_keysym(ch) or ord(ch)
        code = self.d.keysym_to_keycode(ks)
        if not code:
            raise RuntimeError(f"no keycode for {ch!r} keysym={ks}")
        return code, shift

    def tap(self, ch: str) -> None:
        code, need_shift = self._keycode(ch)
        if need_shift:
            xtest.fake_input(self.d, X.KeyPress, self.shift)
            self.d.flush()
        xtest.fake_input(self.d, X.KeyPress, code)
        self.d.flush()
        time.sleep(random.uniform(0.045, 0.090))
        xtest.fake_input(self.d, X.KeyRelease, code)
        self.d.flush()
        if need_shift:
            xtest.fake_input(self.d, X.KeyRelease, self.shift)
            self.d.flush()

    def press_return(self) -> None:
        time.sleep(random.uniform(0.12, 0.22))
        self.tap("\n")

    def press_up(self) -> None:
        time.sleep(random.uniform(0.22, 0.40))
        code = self.d.keysym_to_keycode(XK.XK_Up)
        xtest.fake_input(self.d, X.KeyPress, code)
        self.d.flush()
        time.sleep(random.uniform(0.050, 0.090))
        xtest.fake_input(self.d, X.KeyRelease, code)
        self.d.flush()
        time.sleep(random.uniform(0.18, 0.32))

    def press_down(self) -> None:
        time.sleep(random.uniform(0.22, 0.40))
        code = self.d.keysym_to_keycode(XK.XK_Down)
        xtest.fake_input(self.d, X.KeyPress, code)
        self.d.flush()
        time.sleep(random.uniform(0.050, 0.090))
        xtest.fake_input(self.d, X.KeyRelease, code)
        self.d.flush()
        time.sleep(random.uniform(0.18, 0.32))

    def press_end(self) -> None:
        time.sleep(random.uniform(0.18, 0.32))
        code = self.d.keysym_to_keycode(XK.XK_End)
        xtest.fake_input(self.d, X.KeyPress, code)
        self.d.flush()
        time.sleep(random.uniform(0.050, 0.090))
        xtest.fake_input(self.d, X.KeyRelease, code)
        self.d.flush()
        time.sleep(random.uniform(0.12, 0.22))

    def press_backspace(self) -> None:
        time.sleep(random.uniform(0.08, 0.16))
        code = self.d.keysym_to_keycode(XK.XK_BackSpace)
        xtest.fake_input(self.d, X.KeyPress, code)
        self.d.flush()
        time.sleep(random.uniform(0.045, 0.080))
        xtest.fake_input(self.d, X.KeyRelease, code)
        self.d.flush()

    def press_tab(self) -> None:
        time.sleep(random.uniform(0.22, 0.40))
        self.tap("\t")
        time.sleep(random.uniform(0.18, 0.28))

    def ctrl_key(self, ch: str) -> None:
        time.sleep(random.uniform(0.18, 0.32))
        xtest.fake_input(self.d, X.KeyPress, self.ctrl)
        self.d.flush()
        time.sleep(random.uniform(0.04, 0.07))
        self.tap(ch)
        xtest.fake_input(self.d, X.KeyRelease, self.ctrl)
        self.d.flush()
        time.sleep(random.uniform(0.12, 0.22))

    def alt_home(self) -> None:
        time.sleep(random.uniform(0.18, 0.32))
        xtest.fake_input(self.d, X.KeyPress, self.alt)
        self.d.flush()
        time.sleep(random.uniform(0.04, 0.07))
        xtest.fake_input(self.d, X.KeyPress, self.home)
        self.d.flush()
        time.sleep(random.uniform(0.05, 0.09))
        xtest.fake_input(self.d, X.KeyRelease, self.home)
        self.d.flush()
        xtest.fake_input(self.d, X.KeyRelease, self.alt)
        self.d.flush()
        time.sleep(random.uniform(0.12, 0.22))

    def shift_ctrl_n(self) -> None:
        time.sleep(random.uniform(0.18, 0.32))
        xtest.fake_input(self.d, X.KeyPress, self.shift)
        self.d.flush()
        xtest.fake_input(self.d, X.KeyPress, self.ctrl)
        self.d.flush()
        time.sleep(random.uniform(0.04, 0.07))
        xtest.fake_input(self.d, X.KeyPress, self.nkey)
        self.d.flush()
        time.sleep(random.uniform(0.05, 0.09))
        xtest.fake_input(self.d, X.KeyRelease, self.nkey)
        self.d.flush()
        xtest.fake_input(self.d, X.KeyRelease, self.ctrl)
        self.d.flush()
        xtest.fake_input(self.d, X.KeyRelease, self.shift)
        self.d.flush()
        time.sleep(random.uniform(0.12, 0.22))

    def type_text(self, s: str) -> None:
        time.sleep(random.uniform(0.28, 0.55))
        burst = random.randint(4, 7)
        words = 0
        prev = ""
        for ch in s:
            self.tap(ch)
            iki = random.lognormvariate(math.log(0.082), 0.38)
            a, b = prev.lower(), ch.lower()
            if a in LEFT and b in LEFT:
                iki *= 1.16
            elif a in RIGHT and b in RIGHT:
                iki *= 1.16
            elif a.isalpha() and b.isalpha():
                iki *= 0.90
            if (prev + ch).lower() in COMMON:
                iki *= 0.80
            if ch == " ":
                words += 1
                iki += random.uniform(0.08, 0.20)
                if words >= burst:
                    time.sleep(random.uniform(0.32, 0.75))
                    words = 0
                    burst = random.randint(4, 7)
            if ch in ".!?":
                iki += random.uniform(0.20, 0.42)
            if ch == ",":
                iki += random.uniform(0.07, 0.16)
            time.sleep(max(0.035, min(0.55, iki)))
            prev = ch

    def type_line(self, s: str) -> None:
        self.type_text(s)
        self.press_return()

    def close(self) -> None:
        self.d.close()
