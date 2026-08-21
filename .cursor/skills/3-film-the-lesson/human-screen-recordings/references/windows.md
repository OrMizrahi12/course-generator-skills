# Recording on Windows

Read this before the first Windows take. The protocol in [SKILL.md](../SKILL.md) does
not change — the same Fitts timing, the same ballistic stroke and correction, the same
lognormal typing. What changes is the injector, and Windows has four traps that turn a
correct protocol into an obviously synthetic recording.

## Contents

- Four traps
- The injector
- The recorder
- Filling the screen
- Verifying a take here

## Four traps

**Relative motion is scaled by the user's settings.** `MOUSEEVENTF_MOVE` without
`MOUSEEVENTF_ABSOLUTE` is multiplied by the pointer-speed slider and the acceleration
thresholds — up to four times — so a carefully shaped 1px stream arrives as something
else entirely. Always move in absolute coordinates, normalized to 0–65535 across the
target surface.

**Mouse moves are coalesced by default.** Windows merges `WM_MOUSEMOVE` messages, which
is exactly what a dense pointer stream cannot survive: the path arrives at the
application as a few long jumps. Set `MOUSEEVENTF_MOVE_NOCOALESCE` on every motion
event.

**0–65535 maps to the primary monitor, not the desktop.** On a multi-monitor machine the
normalized coordinates land on the primary display unless you also set
`MOUSEEVENTF_VIRTUALDESK`, and the virtual desktop can start at negative coordinates when
the primary monitor is not the leftmost one. Measure with `SM_XVIRTUALSCREEN` (76),
`SM_YVIRTUALSCREEN` (77), `SM_CXVIRTUALSCREEN` (78) and `SM_CYVIRTUALSCREEN` (79), and
normalize against that rectangle.

**Injection into an elevated window is refused, silently.** `SendInput` is subject to
UIPI: a process may only inject into applications at an equal or lower integrity level,
and neither the return value nor `GetLastError` tells you that UIPI was the reason. If the
recorded application runs as administrator, the recorder must too — otherwise the pointer
moves, the keystrokes vanish, and the take looks like the app froze.

One more, smaller: an unaware process on a scaled display reads virtualized screen
coordinates, so the pointer lands in the wrong place. Set per-monitor DPI awareness
before measuring anything.

Sources for all of the above:
[SendInput](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput),
[MOUSEINPUT](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput),
[KEYBDINPUT](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-keybdinput),
[GetSystemMetrics](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemmetrics).

## The injector

`Win32Injector` in [scripts/human_input.py](../scripts/human_input.py) handles all of
them. It needs Python 3 and nothing else — `ctypes` against `user32` — so there is no
install step on a clean machine.

Typing goes through `KEYEVENTF_UNICODE`, which sends the character itself rather than a
virtual key, so the text on screen does not depend on the active keyboard layout. Named
keys (`Return`, `Tab`, `Escape`, arrows) go through virtual-key codes, because a layout
cannot change what Enter means.

Check it before the first take:

```
python scripts\human_input.py --selftest
python scripts\human_input.py --demo
```

The selftest exercises the shared protocol and needs no desktop; the demo drives the real
pointer and types into whatever has focus.

## The recorder

```
ffmpeg -y -f gdigrab -draw_mouse 1 -framerate 60 -i desktop ^
  -c:v libx264 -preset veryfast -crf 16 -pix_fmt yuv420p -an out.mp4
```

`gdigrab` draws the pointer by default; `-draw_mouse 0` turns it off, which is never what
a lesson wants. `-i title=Window Name` captures one window regardless of position, but
prefer `desktop` with the window maximized — a window-scoped capture hides the moment the
pointer arrives from outside it.

Stop the recorder with Ctrl+C in its own console so the MP4 is finalized. Killing the
process leaves an unplayable file.

## Filling the screen

Every recorded window fills the display, the same rule as everywhere. On Windows the
reliable way is the application's own full-screen key (F11 in browsers and most
terminals) rather than the maximize button, because maximize leaves the taskbar and the
title bar in frame.

Confirm from a still frame before the take, not from the live desktop.

## Verifying a take here

Same checks as X11, one Windows-specific addition: confirm that keystrokes actually
landed. A UIPI refusal produces a video in which the pointer moves correctly and nothing
is typed, which is easy to mistake for a slow application.

Extract a frame from a few seconds into the typing and read the text on screen. If the
field is empty, the recorder is running at a lower integrity level than the application.
