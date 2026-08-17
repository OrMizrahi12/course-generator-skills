---
name: Human screen recordings
description: >-
  Use this when a screen recording or live demo must look like a real person
  using the computer, not automation. Every recorded window must fill the entire
  screen. Covers ballistic mouse motion, bursty human typing, and how to record
  it.
---
# Human screen recordings

Use this protocol whenever the output is a video (or a live demo) of using a computer and it must look authentic: a person moving a mouse and typing, not a script.

Smoothness alone is not enough. A perfectly smooth path along the top of the screen still looks fake. The goal is **intent**: rest somewhere a person would rest, go to a target in a fast stroke plus a small correction, type in bursts with pauses at words, then stop.

## Hard rules

Never:

- Record a window that does not fill the entire screen. Every window in the take must be maximized / full-bleed across the display. A floating, tiled, half-screen, or picture-in-picture window is a failed take. Delete it.
- Teleport the cursor, or click at `(x, y)` without traveling there.
- Paste text, or send a whole word/string in one input event.
- Slide along the screen edge (top/bottom/left/right bezel). That is the most common fake look.
- Use a fixed delay between keys (`sleep(0.1)` every character) or a flat `random.uniform` on every key.
- Wander the mouse in a random box while waiting.
- Start recording while the cursor is parked on the bezel (`y ≈ 0` or `x ≈ 0`).

Always:

- **Before ffmpeg starts**, make every window that will appear in the take fill the screen (maximize or fullscreen). Confirm it from a still frame. If a second window opens mid-take, maximize it before it is the subject of the shot.
- Drive a **high-frequency pointer stream** (hundreds of updates per second, 1px steps, flush every event) so a 60fps recording never shows a jump.
- Type **one key at a time** with real key-down and key-up (dwell), not an instant press.
- Park the pointer in a normal rest spot **before** the recorder starts.

## Before you record

1. Note screen size. Keep a ~18px margin from every edge unless the target itself is near the edge.
2. Maximize the subject window so it covers the full display. Do not start the recorder on a restored/small window, a split layout, or a browser that leaves desktop chrome visible around it.
3. Read the current pointer. If it is on the bezel, lift it inward first (do not crawl the edge). Then move to a rest point a person would actually leave the mouse: mid-desktop, slightly off-center, not a corner. Example rest: around 55–60% width, 50% height.
4. Start the recorder only after the pointer is at rest **and** the window fills the screen.
5. Record 60fps, include the hardware cursor (`-draw_mouse 1` on X11). No narration unless asked.

## Mouse: ballistic then correct

Pointing is two phases, not one pretty curve.

**Duration (Fitts):**

```
T = 0.085 + 0.125 * log2(distance / target_width + 1)
clamp T to [0.22, 1.15] seconds
```

Large buttons are reached faster. Tiny targets take longer and get more correction.

**Phase 1 — ballistic (about 78% of T):**
Cover 92–97% of the distance in one stroke. Velocity peak **before** the midpoint (time-warp the ease: `u ** 0.72`, then a smoothstep). Slight arc from a perpendicular bulge of 4–9% of distance. Do **not** hug the bezel; clamp the path into the inner rectangle.

**Phase 2 — correction:**
About 70% of the time, and when distance > 80px, overshoot the target by 6–14px, then settle back (two short strokes, ~90–200ms each). Otherwise one short settle onto the target.

**After arriving:** wait 140–320ms (look at the target), then click. Hold the button 50–90ms, then release.

**While waiting for an app:** leave the mouse still, or one tiny settle of a few pixels. No sightseeing.

**Long jumps (> ~400px):** still one ballistic + one/two corrections (1–3 speed peaks total). Do not inject per-pixel noise; that looks like vibration, not a hand.

## Typing: bursts, not a metronome

After focusing a field, wait 280–550ms before the first key (compose the sentence).

Each key:

- **Dwell** (keydown → keyup): 45–90ms.
- **Flight / IKI** (after keyup until next keydown): draw from a **lognormal**, not a uniform. Use `lognormvariate(log(0.082), 0.38)`, then shape it:
  - Same-hand bigram (QWERTY left `qwertasdfgzxcvb` vs right `yuiophjklnm`): ×1.16.
  - Alternating hands: ×0.90.
  - Common English bigrams (`th he in er an re on at en ed to it is or te al es`): ×0.80.
  - Start of a word: add 80–200ms.
  - After `. ! ?`: add 200–420ms.
  - After `,`: add 70–160ms.
  - Clamp to 35–550ms.

**Bursts:** type 4–7 words fluently, then pause 320–750ms (think), then another burst. Reset the burst length each time so there is no repeating pattern.

Capitals: hold Shift, tap the letter, release Shift. Never paste.

Do not sprinkle fake typos unless asked. One optional backspace on a long prompt is enough; a lot of typos looks staged.

## Recorder

X11 example:

```
ffmpeg -y -f x11grab -draw_mouse 1 -video_size WIDTHxHEIGHT -framerate 60 -i $DISPLAY \
  -c:v libx264 -preset veryfast -crf 16 -pix_fmt yuv420p -an out.mp4
```

Stop with SIGINT so the MP4 is finalized. Check duration, 60fps, and a few frames: the recorded window must fill the screen; start must not be on the bezel; keys must appear one by one; the cursor path must not ride an edge. If the first frames show a small or tiled window, delete the take.

## Platform notes

The **protocol** is the same everywhere. Only the injector changes:

- **Linux/X11:** `XTestFakeMotionEvent` at 1px + flush; `XTestFakeKeyEvent` for keys. Relative XTest is unreliable on some servers; a dense absolute stream is fine if each step is 1px.
- **macOS / Windows:** the same timing and path math, using that OS’s pointer/key event API. Do not use accessibility “set cursor to x,y” once per click.

Pixel-click desktop agents (click-at-coordinates) will look fake. If that is the only tool, do not use it for the recording. Generate the path and play it as a stream.

## Linux X11 reference (drop-in)

A complete `HumanInput` class: `park()` before record, `move_to(x, y, target_w=)`, `click()`, `type_text(s)`. Keep this logic; change `DISPLAY` / screen size to match the machine.

Typical session: maximize the window to fill the screen → `h = HumanInput(width, height)` → `h.park()` → start ffmpeg → `h.move_to(...)` / `h.click()` / `h.type_text(...)` → SIGINT ffmpeg → `h.close()`.

## Done when

A person watching the MP4 should not see a window that fails to fill the screen, edge-crawling, teleporting, pasted text, or a metronome cadence. Consecutive 60fps frames show the cursor mid-path, and letters appear one at a time with faster runs inside words and slower gaps between them.
