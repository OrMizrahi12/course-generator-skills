---
name: Extract lesson states
description: >-
  Use after a lesson MP4 is locked. Extract a timed JSON array of on-screen
  states from the video frames only. No narration, no suggested lines. Verify
  every object against start and end frames. The MP4 is the only source of
  truth.
---
# Extract lesson states

After a lesson MP4 is locked, the video is a connected sequence of **states**. This skill turns that video into one JSON array: one object per state, timed, objective, detailed. Another model will write narration from this. You do not tell it what to say.

The model will want to reuse the mouse-action log, invent what it meant to film, or add `say` / `must_cover` fields. That is the bug.

## When this runs

After the MP4 exists and has passed the recording gates (0–100% on camera, last-frame result). Not during recording. Not from a live screenshot.

Output sits next to the video, e.g. `lesson-19-states.json`.

## Source of truth

The MP4 frames are the only source of truth.

Not the HumanInput log. Not the old action timeline. Not a live desktop shot. Not memory of the take. If the log says click and the frame has no menu, the frame wins and that claim is deleted.

## What a state is

A state is what is true on screen for a stretch of time. A new object starts only when something material on screen changes (menu opens, text appears, selection moves, spinner starts or dies, a chat moves to Pinned).

Timestamps are exact (seconds, three decimals — we record 60fps). If one state holds for eight seconds, that is one object, not eight copies. A tick every second with no change is noise.

## Array shape

The whole video is one array. No narration fields. No `say`, `must_cover`, `kind: action` as a speech instruction, no suggested wording.

```json
[
  {
    "start": 2.252,
    "end": 3.363,
    "on_screen": {
      "window": "Agents Window",
      "sidebar": {},
      "menu": {},
      "main": {},
      "cursor": ""
    },
    "changed": "What became true on screen versus the previous state, as a fact."
  }
]
```

`on_screen` is structured fact: visible strings copied exactly, which panel is open, what is selected or highlighted, menu open or not and its items, spinner or not, pin icon filled or not, cursor target if visible. Fill the regions that exist in that frame. Do not invent widgets that are not there.

`changed` is the event that opened this state, stated as a fact about the picture, not as a teaching line.

## How to extract

1. Read duration from the MP4 (`ffprobe`).
2. Walk the video by extracting frames (not by trusting the action log). Use the action log only as a hint for where to look.
3. When the picture changes, close the previous object and open a new one. Set `start` / `end` from the frame times.
4. For each object, extract a frame at `start` and a frame at `end`.
5. Write `on_screen` from those frames. Copy on-screen text as written.

## How to verify (required before shipping the JSON)

For every object:

- The start frame shows this state.
- The end frame still shows this state.
- A frame just before `start` still shows the previous state.
- A frame just after `end` already shows the next state (or the video ended).

If a frame is unclear, extract another nearby frame. Do not guess. If you cannot see a string, omit it or mark that it was unreadable. Never fill from memory.

If any object fails this check, fix or delete it. Do not ship the array.

## Do not

- Tell the other model what to say
- Write voiceover, captions, or pedagogical "what to cover"
- Use live screenshots or the recorder script as proof
- Emit one object per mouse twitch that did not change the picture
- Emit one object per clock second when the state did not change
- Start this skill before the MP4 is locked
