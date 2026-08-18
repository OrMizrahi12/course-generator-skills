#!/usr/bin/env python3
"""Human-like mouse and keyboard input for X11 screen recordings."""

from __future__ import annotations

import math
import random
import time
from typing import Iterable

from Xlib import X, XK, display
from Xlib.ext import xtest

LEFT_HAND = set("qwertasdfgzxcvb")
RIGHT_HAND = set("yuiophjklnm")
FAST_BIGRAMS = {
    "th", "he", "in", "er", "an", "re", "on", "at", "en", "ed", "to", "it", "is", "or", "te", "al", "es",
}

KEYSYM = {
    " ": "space",
    "-": "minus",
    "_": "underscore",
    "/": "slash",
    ".": "period",
    '"': "quotedbl",
    "'": "apostrophe",
}


class HumanInput:
    def __init__(self, width: int, height: int, margin: int = 18) -> None:
        self.width = width
        self.height = height
        self.margin = margin
        self.dpy = display.Display()
        self.root = self.dpy.screen().root
        self._ensure_xtest()

    def _ensure_xtest(self) -> None:
        info = self.dpy.query_extension(xtest.extname)
        if not info.present:
            raise RuntimeError("XTEST extension not available")

    def _clamp(self, x: float, y: float) -> tuple[int, int]:
        lo = self.margin
        hi_x = self.width - self.margin - 1
        hi_y = self.height - self.margin - 1
        return int(max(lo, min(hi_x, x))), int(max(lo, min(hi_y, y)))

    def _pointer(self) -> tuple[int, int]:
        return self.root.query_pointer().root_x, self.root.query_pointer().root_y

    def _motion(self, x: int, y: int) -> None:
        xtest.fake_input(self.dpy, X.MotionNotify, x=x, y=y)
        self.dpy.sync()

    def _move_stream(self, points: Iterable[tuple[int, int]]) -> None:
        for x, y in points:
            self._motion(x, y)
            time.sleep(1 / 480)

    def park(self) -> None:
        x0, y0 = self._pointer()
        if y0 <= self.margin + 2 or x0 <= self.margin + 2:
            mid_x = int(self.width * 0.58)
            mid_y = int(self.height * 0.50)
            self.move_to(mid_x, mid_y, target_w=80)
        rest_x = int(self.width * 0.57 + random.uniform(-20, 20))
        rest_y = int(self.height * 0.50 + random.uniform(-15, 15))
        self.move_to(rest_x, rest_y, target_w=60)

    def move_to(self, x: int, y: int, target_w: float = 40) -> None:
        sx, sy = self._pointer()
        dx, dy = x - sx, y - sy
        dist = math.hypot(dx, dy)
        if dist < 2:
            return

        tw = max(8.0, float(target_w))
        duration = 0.085 + 0.125 * math.log2(dist / tw + 1)
        duration = max(0.22, min(1.15, duration))

        overshoot = random.random() < 0.70 and dist > 80
        ox = oy = 0
        if overshoot:
            scale = random.uniform(6, 14) / dist
            ox, oy = dx * scale, dy * scale

        tx, ty = x + ox, y + oy
        phase1 = duration * 0.78
        steps1 = max(8, int(dist * 0.9 / 1.0))
        perp_x, perp_y = -dy, dx
        plen = math.hypot(perp_x, perp_y) or 1.0
        bulge = random.uniform(0.04, 0.09) * dist

        points: list[tuple[int, int]] = []
        for i in range(1, steps1 + 1):
            u = i / steps1
            eased = u**0.72
            eased = eased * eased * (3 - 2 * eased)
            px = sx + dx * eased * 0.95
            py = sy + dy * eased * 0.95
            arc = math.sin(math.pi * eased) * bulge
            px += perp_x / plen * arc
            py += perp_y / plen * arc
            points.append(self._clamp(px, py))

        t_end = time.time() + phase1
        self._move_stream(points)
        while time.time() < t_end:
            time.sleep(0.005)

        if overshoot:
            self._move_stream([self._clamp(tx, ty)])
            time.sleep(random.uniform(0.09, 0.20))
            self._move_stream([self._clamp(x, y)])
            time.sleep(random.uniform(0.09, 0.20))
        else:
            self._move_stream([self._clamp(x, y)])

    def click(self, button: int = 1) -> None:
        time.sleep(random.uniform(0.14, 0.32))
        xtest.fake_input(self.dpy, X.ButtonPress, detail=button)
        self.dpy.sync()
        time.sleep(random.uniform(0.05, 0.09))
        xtest.fake_input(self.dpy, X.ButtonRelease, detail=button)
        self.dpy.sync()

    def _flight(self, prev: str | None, nxt: str) -> float:
        iki = random.lognormvariate(math.log(0.082), 0.38)
        if prev:
            pair = prev + nxt
            if prev in LEFT_HAND and nxt in LEFT_HAND:
                iki *= 1.16
            elif (prev in LEFT_HAND and nxt in RIGHT_HAND) or (prev in RIGHT_HAND and nxt in LEFT_HAND):
                iki *= 0.90
            if pair.lower() in FAST_BIGRAMS:
                iki *= 0.80
        if prev in ".!?":
            iki += random.uniform(0.20, 0.42)
        elif prev == ",":
            iki += random.uniform(0.07, 0.16)
        if prev in (None, " ", "\n"):
            iki += random.uniform(0.08, 0.20)
        return max(0.035, min(0.55, iki))

    def _keysym(self, name: str) -> int:
        return XK.string_to_keysym(name)

    def _keycode(self, name: str) -> int:
        return self.dpy.keysym_to_keycode(self._keysym(name))

    def _type_char(self, ch: str) -> None:
        if ch == "\n":
            key = self._keycode("Return")
            xtest.fake_input(self.dpy, X.KeyPress, detail=key)
            self.dpy.sync()
            time.sleep(random.uniform(0.045, 0.09))
            xtest.fake_input(self.dpy, X.KeyRelease, detail=key)
            self.dpy.sync()
            return

        if ch.isupper():
            shift = self._keycode("Shift_L")
            key = self._keycode(ch.lower())
            xtest.fake_input(self.dpy, X.KeyPress, detail=shift)
            self.dpy.sync()
            xtest.fake_input(self.dpy, X.KeyPress, detail=key)
            self.dpy.sync()
            time.sleep(random.uniform(0.045, 0.09))
            xtest.fake_input(self.dpy, X.KeyRelease, detail=key)
            xtest.fake_input(self.dpy, X.KeyRelease, detail=shift)
            self.dpy.sync()
            return

        keyname = KEYSYM.get(ch, ch)
        key = self._keycode(keyname)
        xtest.fake_input(self.dpy, X.KeyPress, detail=key)
        self.dpy.sync()
        time.sleep(random.uniform(0.045, 0.09))
        xtest.fake_input(self.dpy, X.KeyRelease, detail=key)
        self.dpy.sync()

    def type_text(self, text: str) -> None:
        time.sleep(random.uniform(0.28, 0.55))
        words = text.split(" ")
        burst = random.randint(4, 7)
        count = 0
        prev: str | None = None
        for wi, word in enumerate(words):
            for ci, ch in enumerate(word):
                if prev is not None:
                    time.sleep(self._flight(prev, ch))
                self._type_char(ch)
                prev = ch
            if wi < len(words) - 1:
                if prev is not None:
                    time.sleep(self._flight(prev, " "))
                self._type_char(" ")
                prev = " "
            count += 1
            if count >= burst and wi < len(words) - 1:
                time.sleep(random.uniform(0.32, 0.75))
                burst = random.randint(4, 7)
                count = 0

    def press_enter(self) -> None:
        self._type_char("\n")

    def close(self) -> None:
        self.dpy.close()
