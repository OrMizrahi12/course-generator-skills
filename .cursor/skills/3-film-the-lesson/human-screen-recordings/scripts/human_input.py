#!/usr/bin/env python3
"""Human pointer, keyboard and wheel input for screen recordings.

The protocol is platform independent and lives in HumanInput: Fitts-timed moves,
one ballistic stroke plus a correction, lognormal typing in bursts, wheel scrolls
in discrete clicks. Only the injector changes per platform.

    Linux / X11   XTestFakeMotionEvent at 1px, flushed every event
    Windows       SendInput with absolute normalized coordinates, uncoalesced

Usage:
    python3 human_input.py --selftest        # protocol checks, no display needed
    python3 human_input.py --demo            # moves the real pointer, needs a display

    from human_input import HumanInput
    h = HumanInput()          # picks the injector for this platform
    h.park()                  # before the recorder starts
    h.move_to(960, 540, target_w=120)
    h.click()
    h.type_text("git worktree add ../checkout-api-reports reports")
    h.press("Return")
    h.scroll(-5)
    h.close()

Exit codes: 0 all checks passed, 1 a check failed, 2 the platform is unsupported.
"""

from __future__ import annotations

import argparse
import ctypes
import math
import platform
import random
import sys
import time

# --- protocol constants, from the skill body -------------------------------------

EDGE_MARGIN = 18  # px kept clear of every screen edge unless the target is there
FITTS_A, FITTS_B = 0.085, 0.125  # T = a + b * log2(distance / target_width + 1)
FITTS_MIN, FITTS_MAX = 0.22, 1.15  # seconds
BALLISTIC_SHARE = 0.78  # of the total move time
BALLISTIC_COVER = (0.92, 0.97)  # fraction of the distance covered in one stroke
BALLISTIC_WARP = 0.72  # u ** this, so peak velocity lands before the midpoint
ARC_BULGE = (0.04, 0.09)  # perpendicular bulge as a fraction of distance
OVERSHOOT_PROBABILITY = 0.70
OVERSHOOT_DISTANCE = 80  # px, below which a move does not overshoot
OVERSHOOT_RANGE = (6, 14)  # px past the target
SETTLE_TIME = (0.090, 0.200)  # seconds per correction stroke
LOOK_BEFORE_CLICK = (0.140, 0.320)
BUTTON_HOLD = (0.050, 0.090)
STREAM_HZ = 400  # pointer updates per second, so 60fps never shows a jump

COMPOSE_BEFORE_TYPING = (0.280, 0.550)
KEY_DWELL = (0.045, 0.090)
IKI_MEDIAN = 0.082  # lognormal median flight time between keys
IKI_SIGMA = 0.38
IKI_CLAMP = (0.035, 0.550)
SAME_HAND_FACTOR = 1.16
ALTERNATING_FACTOR = 0.90
COMMON_BIGRAM_FACTOR = 0.80
WORD_START_EXTRA = (0.080, 0.200)
SENTENCE_EXTRA = (0.200, 0.420)
COMMA_EXTRA = (0.070, 0.160)
BURST_WORDS = (4, 7)
BURST_PAUSE = (0.320, 0.750)

LEFT_HAND = set("qwertasdfgzxcvb")
RIGHT_HAND = set("yuiophjklnm")
COMMON_BIGRAMS = {
    "th", "he", "in", "er", "an", "re", "on", "at", "en", "ed", "to", "it",
    "is", "or", "te", "al", "es",
}

WHEEL_CLICKS_PER_BURST = (3, 8)
WHEEL_CLICK_GAP = (0.060, 0.160)
WHEEL_BURST_PAUSE = (0.240, 0.600)


def _uniform(bounds: tuple[float, float], rng: random.Random) -> float:
    return rng.uniform(*bounds)


def _smoothstep(u: float) -> float:
    return u * u * (3.0 - 2.0 * u)


# --- injectors --------------------------------------------------------------------


class Injector:
    """What a platform has to provide. Everything else is shared."""

    name = "none"

    def screen_size(self) -> tuple[int, int]:
        raise NotImplementedError

    def pointer_position(self) -> tuple[int, int]:
        raise NotImplementedError

    def move_absolute(self, x: int, y: int) -> None:
        raise NotImplementedError

    def button(self, pressed: bool, button: int = 1) -> None:
        raise NotImplementedError

    def key_char(self, char: str, pressed: bool) -> None:
        raise NotImplementedError

    def key_name(self, name: str, pressed: bool) -> None:
        raise NotImplementedError

    def wheel(self, clicks: int) -> None:
        raise NotImplementedError

    def close(self) -> None:
        pass


class RecordingInjector(Injector):
    """Records events instead of sending them. Used by --selftest on any platform."""

    name = "recording"

    def __init__(self, width: int = 1920, height: int = 1200) -> None:
        self.width, self.height = width, height
        self.x, self.y = width // 2, height // 2
        self.events: list[tuple[float, str, object]] = []

    def _log(self, kind: str, payload: object) -> None:
        self.events.append((time.perf_counter(), kind, payload))

    def screen_size(self) -> tuple[int, int]:
        return self.width, self.height

    def pointer_position(self) -> tuple[int, int]:
        return self.x, self.y

    def move_absolute(self, x: int, y: int) -> None:
        self.x, self.y = x, y
        self._log("move", (x, y))

    def button(self, pressed: bool, button: int = 1) -> None:
        self._log("button", (button, pressed))

    def key_char(self, char: str, pressed: bool) -> None:
        self._log("key", (char, pressed))

    def key_name(self, name: str, pressed: bool) -> None:
        self._log("key", (name, pressed))

    def wheel(self, clicks: int) -> None:
        self._log("wheel", clicks)


class X11Injector(Injector):
    """XTest on Linux. A dense absolute stream at 1px, flushed every event."""

    name = "x11"

    def __init__(self, display: str | None = None) -> None:
        self.xlib = ctypes.CDLL("libX11.so.6")
        self.xtst = ctypes.CDLL("libXtst.so.6")
        self.xlib.XOpenDisplay.restype = ctypes.c_void_p
        self.xlib.XDefaultRootWindow.restype = ctypes.c_ulong
        self.xlib.XDefaultRootWindow.argtypes = [ctypes.c_void_p]
        self.xlib.XKeysymToKeycode.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
        self.xlib.XKeysymToKeycode.restype = ctypes.c_ubyte
        self.xlib.XGetKeyboardMapping.restype = ctypes.POINTER(ctypes.c_ulong)
        self.xlib.XStringToKeysym.restype = ctypes.c_ulong
        self.xlib.XStringToKeysym.argtypes = [ctypes.c_char_p]

        name = display.encode() if display else None
        self.display = self.xlib.XOpenDisplay(name)
        if not self.display:
            raise RuntimeError(f"cannot open the X display {display or '$DISPLAY'}")
        self.screen = self.xlib.XDefaultScreen(self.display)
        self.root = self.xlib.XDefaultRootWindow(self.display)
        self._charmap = self._build_charmap()

    def _build_charmap(self) -> dict[str, tuple[int, bool]]:
        """Map every printable character to its keycode and whether shift is held."""
        low, high = ctypes.c_int(), ctypes.c_int()
        self.xlib.XDisplayKeycodes(self.display, ctypes.byref(low), ctypes.byref(high))
        count = high.value - low.value + 1
        per_code = ctypes.c_int()
        table = self.xlib.XGetKeyboardMapping(
            self.display, low.value, count, ctypes.byref(per_code)
        )
        charmap: dict[str, tuple[int, bool]] = {}
        for index in range(count):
            for level in (0, 1):  # unshifted, shifted
                if level >= per_code.value:
                    continue
                keysym = table[index * per_code.value + level]
                if 0x20 <= keysym <= 0x7E:
                    charmap.setdefault(chr(keysym), (low.value + index, level == 1))
        self.xlib.XFree(table)
        return charmap

    def screen_size(self) -> tuple[int, int]:
        return (
            int(self.xlib.XDisplayWidth(self.display, self.screen)),
            int(self.xlib.XDisplayHeight(self.display, self.screen)),
        )

    def pointer_position(self) -> tuple[int, int]:
        root_return, child_return = ctypes.c_ulong(), ctypes.c_ulong()
        root_x, root_y = ctypes.c_int(), ctypes.c_int()
        win_x, win_y = ctypes.c_int(), ctypes.c_int()
        mask = ctypes.c_uint()
        self.xlib.XQueryPointer(
            self.display, self.root,
            ctypes.byref(root_return), ctypes.byref(child_return),
            ctypes.byref(root_x), ctypes.byref(root_y),
            ctypes.byref(win_x), ctypes.byref(win_y), ctypes.byref(mask),
        )
        return root_x.value, root_y.value

    def move_absolute(self, x: int, y: int) -> None:
        self.xtst.XTestFakeMotionEvent(self.display, -1, int(x), int(y), 0)
        self.xlib.XFlush(self.display)

    def button(self, pressed: bool, button: int = 1) -> None:
        self.xtst.XTestFakeButtonEvent(self.display, button, 1 if pressed else 0, 0)
        self.xlib.XFlush(self.display)

    def _shift_keycode(self) -> int:
        return self.xlib.XKeysymToKeycode(self.display, self.xlib.XStringToKeysym(b"Shift_L"))

    def key_char(self, char: str, pressed: bool) -> None:
        entry = self._charmap.get(char)
        if entry is None:
            raise KeyError(f"no key on this layout produces {char!r}")
        keycode, needs_shift = entry
        if needs_shift and pressed:
            self.xtst.XTestFakeKeyEvent(self.display, self._shift_keycode(), 1, 0)
        self.xtst.XTestFakeKeyEvent(self.display, keycode, 1 if pressed else 0, 0)
        if needs_shift and not pressed:
            self.xtst.XTestFakeKeyEvent(self.display, self._shift_keycode(), 0, 0)
        self.xlib.XFlush(self.display)

    def key_name(self, name: str, pressed: bool) -> None:
        keysym = self.xlib.XStringToKeysym(name.encode())
        if not keysym:
            raise KeyError(f"unknown key name {name!r}")
        keycode = self.xlib.XKeysymToKeycode(self.display, keysym)
        self.xtst.XTestFakeKeyEvent(self.display, keycode, 1 if pressed else 0, 0)
        self.xlib.XFlush(self.display)

    def wheel(self, clicks: int) -> None:
        button = 4 if clicks > 0 else 5  # X11 wheel up / down
        for _ in range(abs(clicks)):
            self.button(True, button)
            self.button(False, button)

    def close(self) -> None:
        self.xlib.XCloseDisplay(self.display)


class Win32Injector(Injector):
    """SendInput on Windows.

    Three traps this handles, all of which make a recording look synthetic:
    relative motion is scaled by the pointer-speed and acceleration settings, so
    every move is absolute; WM_MOUSEMOVE is coalesced by default, which eats a
    dense stream, so MOUSEEVENTF_MOVE_NOCOALESCE is set; and an unaware process
    reads virtualized screen coordinates on a scaled display, so DPI awareness is
    set before anything is measured.
    """

    name = "win32"

    INPUT_MOUSE, INPUT_KEYBOARD = 0, 1
    MOUSEEVENTF_MOVE = 0x0001
    MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP = 0x0002, 0x0004
    MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP = 0x0008, 0x0010
    MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP = 0x0020, 0x0040
    MOUSEEVENTF_WHEEL = 0x0800
    MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000
    MOUSEEVENTF_VIRTUALDESK = 0x4000
    MOUSEEVENTF_ABSOLUTE = 0x8000
    KEYEVENTF_KEYUP, KEYEVENTF_UNICODE = 0x0002, 0x0004
    WHEEL_DELTA = 120
    SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN = 76, 77
    SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN = 78, 79
    DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = ctypes.c_void_p(-4)

    VK_NAMES = {
        "Return": 0x0D, "Enter": 0x0D, "Tab": 0x09, "Escape": 0x1B, "space": 0x20,
        "BackSpace": 0x08, "Delete": 0x2E, "Up": 0x26, "Down": 0x28,
        "Left": 0x25, "Right": 0x27, "Home": 0x24, "End": 0x23,
        "Shift_L": 0x10, "Control_L": 0x11, "Alt_L": 0x12,
    }

    def __init__(self) -> None:
        self.user32 = ctypes.WinDLL("user32", use_last_error=True)
        try:
            self.user32.SetProcessDpiAwarenessContext(
                self.DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
            )
        except AttributeError:
            self.user32.SetProcessDPIAware()  # pre-1703 fallback
        self._define_structures()
        self.origin_x = self.user32.GetSystemMetrics(self.SM_XVIRTUALSCREEN)
        self.origin_y = self.user32.GetSystemMetrics(self.SM_YVIRTUALSCREEN)
        self.width = self.user32.GetSystemMetrics(self.SM_CXVIRTUALSCREEN)
        self.height = self.user32.GetSystemMetrics(self.SM_CYVIRTUALSCREEN)

    def _define_structures(self) -> None:
        ulong_ptr = ctypes.POINTER(ctypes.c_ulong)

        class MOUSEINPUT(ctypes.Structure):
            _fields_ = [("dx", ctypes.c_long), ("dy", ctypes.c_long),
                        ("mouseData", ctypes.c_ulong), ("dwFlags", ctypes.c_ulong),
                        ("time", ctypes.c_ulong), ("dwExtraInfo", ulong_ptr)]

        class KEYBDINPUT(ctypes.Structure):
            _fields_ = [("wVk", ctypes.c_ushort), ("wScan", ctypes.c_ushort),
                        ("dwFlags", ctypes.c_ulong), ("time", ctypes.c_ulong),
                        ("dwExtraInfo", ulong_ptr)]

        class INPUT_UNION(ctypes.Union):
            _fields_ = [("mi", MOUSEINPUT), ("ki", KEYBDINPUT)]

        class INPUT(ctypes.Structure):
            _anonymous_ = ("u",)
            _fields_ = [("type", ctypes.c_ulong), ("u", INPUT_UNION)]

        self.MOUSEINPUT, self.KEYBDINPUT, self.INPUT = MOUSEINPUT, KEYBDINPUT, INPUT

    def _send(self, item) -> None:
        sent = self.user32.SendInput(1, ctypes.byref(item), ctypes.sizeof(item))
        if sent != 1:
            raise OSError(
                ctypes.get_last_error(),
                "SendInput was blocked. A process at a higher integrity level, or an "
                "elevated window in the foreground, refuses injected input (UIPI).",
            )

    def screen_size(self) -> tuple[int, int]:
        return self.width, self.height

    def pointer_position(self) -> tuple[int, int]:
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

        point = POINT()
        self.user32.GetCursorPos(ctypes.byref(point))
        return point.x - self.origin_x, point.y - self.origin_y

    def move_absolute(self, x: int, y: int) -> None:
        # Absolute coordinates are normalized to 0..65535 across the virtual desktop.
        nx = int(round((x + self.origin_x) * 65535 / max(self.width - 1, 1)))
        ny = int(round((y + self.origin_y) * 65535 / max(self.height - 1, 1)))
        flags = (self.MOUSEEVENTF_MOVE | self.MOUSEEVENTF_ABSOLUTE
                 | self.MOUSEEVENTF_VIRTUALDESK | self.MOUSEEVENTF_MOVE_NOCOALESCE)
        item = self.INPUT(type=self.INPUT_MOUSE,
                          mi=self.MOUSEINPUT(nx, ny, 0, flags, 0, None))
        self._send(item)

    def button(self, pressed: bool, button: int = 1) -> None:
        down_up = {
            1: (self.MOUSEEVENTF_LEFTDOWN, self.MOUSEEVENTF_LEFTUP),
            2: (self.MOUSEEVENTF_MIDDLEDOWN, self.MOUSEEVENTF_MIDDLEUP),
            3: (self.MOUSEEVENTF_RIGHTDOWN, self.MOUSEEVENTF_RIGHTUP),
        }[button]
        flags = down_up[0] if pressed else down_up[1]
        item = self.INPUT(type=self.INPUT_MOUSE,
                          mi=self.MOUSEINPUT(0, 0, 0, flags, 0, None))
        self._send(item)

    def key_char(self, char: str, pressed: bool) -> None:
        # Unicode injection, so the result does not depend on the active layout.
        flags = self.KEYEVENTF_UNICODE | (self.KEYEVENTF_KEYUP if not pressed else 0)
        item = self.INPUT(type=self.INPUT_KEYBOARD,
                          ki=self.KEYBDINPUT(0, ord(char), flags, 0, None))
        self._send(item)

    def key_name(self, name: str, pressed: bool) -> None:
        code = self.VK_NAMES.get(name)
        if code is None:
            raise KeyError(f"unknown key name {name!r}")
        flags = self.KEYEVENTF_KEYUP if not pressed else 0
        item = self.INPUT(type=self.INPUT_KEYBOARD,
                          ki=self.KEYBDINPUT(code, 0, flags, 0, None))
        self._send(item)

    def wheel(self, clicks: int) -> None:
        for _ in range(abs(clicks)):
            data = self.WHEEL_DELTA if clicks > 0 else -self.WHEEL_DELTA
            item = self.INPUT(
                type=self.INPUT_MOUSE,
                mi=self.MOUSEINPUT(0, 0, ctypes.c_ulong(data & 0xFFFFFFFF).value,
                                   self.MOUSEEVENTF_WHEEL, 0, None),
            )
            self._send(item)


def make_injector(display: str | None = None) -> Injector:
    system = platform.system()
    if system == "Windows":
        return Win32Injector()
    if system == "Linux":
        return X11Injector(display)
    raise RuntimeError(f"no injector for {system}; add one with the same five methods")


# --- the protocol -------------------------------------------------------------------


class HumanInput:
    """Pointing, typing and scrolling that look like a person, not a script."""

    def __init__(self, injector: Injector | None = None, seed: int | None = None,
                 display: str | None = None, sleep=time.sleep) -> None:
        self.injector = injector or make_injector(display)
        self.width, self.height = self.injector.screen_size()
        self.rng = random.Random(seed)
        self.sleep = sleep  # replaced only by the geometry checks, which need no clock

    # -- pointer ---------------------------------------------------------------

    def _clamp(self, x: float, y: float, target: tuple[int, int]) -> tuple[float, float]:
        """Keep the path out of the bezel band unless the target itself lives there."""
        low_x = min(EDGE_MARGIN, target[0])
        high_x = max(self.width - EDGE_MARGIN, target[0])
        low_y = min(EDGE_MARGIN, target[1])
        high_y = max(self.height - EDGE_MARGIN, target[1])
        return min(max(x, low_x), high_x), min(max(y, low_y), high_y)

    def _stream(self, points: list[tuple[int, int]], duration: float) -> None:
        """Play a whole-pixel path at STREAM_HZ so 60fps never catches a jump."""
        if not points:
            return
        start = time.perf_counter()
        last: tuple[int, int] | None = self.injector.pointer_position()
        for index, point in enumerate(points):
            if point != last:
                self.injector.move_absolute(*point)
                last = point
            target_time = start + duration * (index / max(len(points) - 1, 1))
            remaining = target_time - time.perf_counter()
            if remaining > 0:
                self.sleep(remaining)

    def _densify(self, path: list[tuple[float, float]]) -> list[tuple[int, int]]:
        """Walk the path in whole pixels, so no two consecutive samples exceed 1px.

        Rounding a float path is not enough: two samples a pixel apart can round two
        pixels apart, and a 60fps recording catches that as a jump.
        """
        dense: list[tuple[int, int]] = []
        last: tuple[int, int] | None = None
        for point in path:
            target = (int(round(point[0])), int(round(point[1])))
            if last is None:
                dense.append(target)
                last = target
                continue
            while last != target:
                last = (last[0] + (0 if target[0] == last[0] else (1 if target[0] > last[0] else -1)),
                        last[1] + (0 if target[1] == last[1] else (1 if target[1] > last[1] else -1)))
                dense.append(last)
        return dense

    def move_to(self, x: int, y: int, target_w: int = 24) -> None:
        start = self.injector.pointer_position()
        distance = math.hypot(x - start[0], y - start[1])
        if distance < 1:
            return

        duration = FITTS_A + FITTS_B * math.log2(distance / max(target_w, 1) + 1)
        duration = min(max(duration, FITTS_MIN), FITTS_MAX)

        cover = _uniform(BALLISTIC_COVER, self.rng)
        overshoots = distance > OVERSHOOT_DISTANCE and self.rng.random() < OVERSHOOT_PROBABILITY
        if overshoots:
            past = _uniform(OVERSHOOT_RANGE, self.rng)
            cover = (distance + past) / distance

        landing = (start[0] + (x - start[0]) * cover, start[1] + (y - start[1]) * cover)
        bulge = distance * _uniform(ARC_BULGE, self.rng) * self.rng.choice((-1.0, 1.0))
        normal = (-(y - start[1]) / distance, (x - start[0]) / distance)

        ballistic: list[tuple[float, float]] = []
        for index in range(60):
            u = index / 59
            eased = _smoothstep(u ** BALLISTIC_WARP)  # velocity peaks before the midpoint
            arc = math.sin(math.pi * u) * bulge
            point = (start[0] + (landing[0] - start[0]) * eased + normal[0] * arc,
                     start[1] + (landing[1] - start[1]) * eased + normal[1] * arc)
            ballistic.append(self._clamp(*point, target=(x, y)))
        self._stream(self._densify(ballistic), duration * BALLISTIC_SHARE)

        corrections = 2 if overshoots else 1
        origin = ballistic[-1]
        for index in range(corrections):
            fraction = (index + 1) / corrections
            step_target = (origin[0] + (x - origin[0]) * fraction,
                           origin[1] + (y - origin[1]) * fraction)
            leg = [self._clamp(origin[0] + (step_target[0] - origin[0]) * (s / 20),
                               origin[1] + (step_target[1] - origin[1]) * (s / 20),
                               target=(x, y)) for s in range(21)]
            self._stream(self._densify(leg), _uniform(SETTLE_TIME, self.rng))
            origin = step_target
        self.injector.move_absolute(x, y)

    def click(self, button: int = 1) -> None:
        self.sleep(_uniform(LOOK_BEFORE_CLICK, self.rng))  # look at the target
        self.injector.button(True, button)
        self.sleep(_uniform(BUTTON_HOLD, self.rng))
        self.injector.button(False, button)

    def park(self) -> None:
        """Leave the pointer where a person would leave it, before the recorder starts."""
        self.move_to(int(self.width * self.rng.uniform(0.55, 0.60)),
                     int(self.height * 0.50), target_w=200)

    # -- keyboard --------------------------------------------------------------

    def _flight(self, previous: str | None, char: str, word_start: bool) -> float:
        gap = self.rng.lognormvariate(math.log(IKI_MEDIAN), IKI_SIGMA)
        if previous:
            pair = (previous + char).lower()
            left = previous.lower() in LEFT_HAND, char.lower() in LEFT_HAND
            right = previous.lower() in RIGHT_HAND, char.lower() in RIGHT_HAND
            if (left[0] and left[1]) or (right[0] and right[1]):
                gap *= SAME_HAND_FACTOR
            elif (left[0] and right[1]) or (right[0] and left[1]):
                gap *= ALTERNATING_FACTOR
            if pair in COMMON_BIGRAMS:
                gap *= COMMON_BIGRAM_FACTOR
            if previous in ".!?":
                gap += _uniform(SENTENCE_EXTRA, self.rng)
            elif previous == ",":
                gap += _uniform(COMMA_EXTRA, self.rng)
        if word_start:
            gap += _uniform(WORD_START_EXTRA, self.rng)
        return min(max(gap, IKI_CLAMP[0]), IKI_CLAMP[1])

    def type_text(self, text: str) -> None:
        self.sleep(_uniform(COMPOSE_BEFORE_TYPING, self.rng))  # compose the sentence
        previous: str | None = None
        words_typed = 0
        burst_length = self.rng.randint(*BURST_WORDS)
        for index, char in enumerate(text):
            word_start = index > 0 and text[index - 1] == " " and char != " "
            if previous is not None:
                self.sleep(self._flight(previous, char, word_start))
            if word_start:
                words_typed += 1
                if words_typed >= burst_length:
                    self.sleep(_uniform(BURST_PAUSE, self.rng))  # think
                    words_typed = 0
                    burst_length = self.rng.randint(*BURST_WORDS)
            self.injector.key_char(char, True)
            self.sleep(_uniform(KEY_DWELL, self.rng))
            self.injector.key_char(char, False)
            previous = char

    def press(self, name: str) -> None:
        self.injector.key_name(name, True)
        self.sleep(_uniform(KEY_DWELL, self.rng))
        self.injector.key_name(name, False)

    # -- wheel -----------------------------------------------------------------

    def scroll(self, clicks: int) -> None:
        """Wheel in discrete clicks with human gaps. Positive is up, negative is down."""
        remaining = abs(clicks)
        direction = 1 if clicks > 0 else -1
        while remaining:
            burst = min(remaining, self.rng.randint(*WHEEL_CLICKS_PER_BURST))
            for _ in range(burst):
                self.injector.wheel(direction)
                self.sleep(_uniform(WHEEL_CLICK_GAP, self.rng))
            remaining -= burst
            if remaining:
                self.sleep(_uniform(WHEEL_BURST_PAUSE, self.rng))

    def close(self) -> None:
        self.injector.close()


# --- checks ---------------------------------------------------------------------------


def selftest() -> int:
    """Assert the protocol's own invariants. Runs on any platform, no display needed."""
    failures: list[str] = []

    def check(name: str, condition: bool, detail: str = "") -> None:
        print(f"  {'pass' if condition else 'FAIL'}  {name}{'' if condition else '  ' + detail}")
        if not condition:
            failures.append(name)

    print("pointer")
    recorder = RecordingInjector()
    human = HumanInput(injector=recorder, seed=7)
    human.injector.move_absolute(200, 900)
    human.move_to(1500, 240, target_w=40)
    moves = [payload for _, kind, payload in recorder.events if kind == "move"]
    steps = [max(abs(b[0] - a[0]), abs(b[1] - a[1])) for a, b in zip(moves, moves[1:])]
    check("every pointer step is 1px", max(steps) <= 1, f"largest step {max(steps)}px")
    check("no teleport to the target", len(moves) > 500, f"{len(moves)} updates")
    inner = [m for m in moves if EDGE_MARGIN <= m[0] <= 1920 - EDGE_MARGIN
             and EDGE_MARGIN <= m[1] <= 1200 - EDGE_MARGIN]
    check("the path never rides an edge", len(inner) == len(moves),
          f"{len(moves) - len(inner)} points in the bezel band")
    check("the move lands on the target", moves[-1] == (1500, 240), f"landed on {moves[-1]}")

    times = [stamp for stamp, kind, _ in recorder.events if kind == "move"]
    half = len(times) // 2
    early = times[half] - times[0]
    late = times[-1] - times[half]
    check("velocity peaks before the midpoint", early < late,
          f"first half {early * 1000:.0f}ms, second half {late * 1000:.0f}ms")

    overshoots = 0
    trials = 40
    for seed in range(trials):
        probe = RecordingInjector()
        pointer = HumanInput(injector=probe, seed=seed, sleep=lambda _seconds: None)
        probe.move_absolute(300, 600)
        pointer.move_to(1400, 600, target_w=30)
        path = [payload for _, kind, payload in probe.events if kind == "move"]
        if any(point[0] > 1400 for point in path):
            overshoots += 1
    rate = overshoots / trials
    check("long moves overshoot then settle, most of the time", 0.5 <= rate <= 0.9,
          f"overshoot rate {rate:.2f}")

    print("typing")
    typist_recorder = RecordingInjector()
    typist = HumanInput(injector=typist_recorder, seed=3)
    typist.type_text("git worktree add ../checkout-api-reports reports")
    keys = [(stamp, payload) for stamp, kind, payload in typist_recorder.events if kind == "key"]
    downs = [(stamp, char) for stamp, (char, pressed) in keys if pressed]
    ups = [(stamp, char) for stamp, (char, pressed) in keys if not pressed]
    check("one key-down and one key-up per character",
          len(downs) == len(ups) == 48, f"{len(downs)} down, {len(ups)} up")
    check("nothing is pasted", all(len(char) == 1 for _, char in downs))
    dwells = [up - down for (down, _), (up, _) in zip(downs, ups)]
    check("dwell stays in the documented band",
          all(0.040 <= value <= 0.100 for value in dwells),
          f"{min(dwells) * 1000:.0f}-{max(dwells) * 1000:.0f}ms")
    flights = [down - up for (up, _), (down, _) in zip(ups, downs[1:])]
    check("no two consecutive gaps are identical",
          all(abs(a - b) > 1e-6 for a, b in zip(flights, flights[1:])))
    distinct = len({round(value, 3) for value in flights})
    check("the cadence is not a metronome", distinct > len(flights) * 0.6,
          f"{distinct} distinct gaps in {len(flights)}")

    print("wheel")
    wheel_recorder = RecordingInjector()
    HumanInput(injector=wheel_recorder, seed=11).scroll(-12)
    wheel_events = [(stamp, payload) for stamp, kind, payload in wheel_recorder.events
                    if kind == "wheel"]
    check("the wheel moves in discrete clicks", len(wheel_events) == 12,
          f"{len(wheel_events)} clicks")
    gaps = [b - a for (a, _), (b, _) in zip(wheel_events, wheel_events[1:])]
    check("scrolling pauses between bursts", max(gaps) > min(gaps) * 2,
          f"gaps {min(gaps) * 1000:.0f}-{max(gaps) * 1000:.0f}ms")

    print()
    if failures:
        print(f"{len(failures)} check(s) failed: {', '.join(failures)}")
        return 1
    print("all protocol checks passed")
    return 0


def demo(display: str | None) -> int:
    """Move the real pointer and type into whatever has focus. Needs a live desktop."""
    human = HumanInput(display=display)
    width, height = human.width, human.height
    print(f"injector {human.injector.name}, screen {width}x{height}")
    human.park()
    human.move_to(int(width * 0.25), int(height * 0.35), target_w=60)
    human.click()
    human.type_text("echo real input, not a screenshot")
    human.press("Return")
    human.scroll(-4)
    human.close()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--selftest", action="store_true",
                        help="check the protocol's invariants without a display")
    parser.add_argument("--demo", action="store_true",
                        help="drive the real pointer and keyboard")
    parser.add_argument("--display", default=None, help="X display, defaults to $DISPLAY")
    args = parser.parse_args()

    if args.selftest:
        return selftest()
    if args.demo:
        try:
            return demo(args.display)
        except RuntimeError as problem:
            print(problem, file=sys.stderr)
            return 2
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
