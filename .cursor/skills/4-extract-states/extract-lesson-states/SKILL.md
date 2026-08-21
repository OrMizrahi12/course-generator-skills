---
name: extract-lesson-states
description: >-
  Breaks a locked lesson MP4 into one timed JSON array of on-screen states, so
  narration can be written and synced to the video without watching it: one
  object per material change, exact timestamps, structured facts copied from the
  frames, and no narration of any kind. Use after a lesson recording is locked and
  has passed its filming gates, when a states file is needed for a lesson, or when
  a states file has to be verified. The MP4 frames are the only source of truth —
  not the action log, not a live screenshot, not memory of the take.
icon: book-open
color: green
metadata:
  stage: 4-extract-states
  consumes: courses/<course-slug>/lessons/<NN>-<lesson-slug>/lesson.mp4
  produces: courses/<course-slug>/lessons/<NN>-<lesson-slug>/states.json
  next: none, the lesson is finished
---

# Extract lesson states

Stage 4 of 4, and the last thing a lesson needs. Once the MP4 is locked, the video
is a connected sequence of **states**. This skill turns that video into one JSON
array: one object per state, timed, objective, detailed.

## What the array is for

Another model writes the narration from this file and syncs it to the video. That
purpose sets every requirement below:

- **The array covers the whole video.** No gaps, no overlaps. A gap is a stretch
  of film with nothing to say over it, and an overlap is two lines competing for
  the same second.
- **Timestamps are exact**, in seconds with three decimals, because they are what
  the narration is aligned against. At 60fps a frame time is `n/60`, and only every
  third frame lands on an exact three-decimal value — round to the nearest, so that
  seeking to the timestamp lands on the frame the boundary is about. `end` is
  exclusive: the next state owns the frame at that timestamp.
- **Each object is readable on its own.** The narration writer should not have to
  open the video to know what is on screen. If a state's description only makes
  sense to someone who watched the take, it is not written yet.
- **No narration, in any form.** You describe the picture; the other model decides
  what to say about it. The moment you write a suggested line, you have taken that
  decision away from the model that has the context to make it.

The model will want to reuse the mouse-action log, invent what it meant to film, or
add `say` / `must_cover` fields. That is the bug.

## When this runs

After the MP4 exists and has passed the recording gates — the path filmed 0% to
100%, the result visible in the last frames. Not during recording. Not from a live
screenshot.

The output sits beside the video, at
`courses/<course-slug>/lessons/<NN>-<lesson-slug>/states.json`.

If there is no `brief.md` and no `take-plan.md` beside the MP4, the film did not
come through the earlier stages. Extract the states anyway — a locked recording is
a legitimate input — but establish the recording gate from the film itself with
`/record-until-the-result-is-visible` first, and tell the user which upstream
artifacts are missing. A states file whose lesson has no brief is honest; one that
pretends the brief existed is not.

## Source of truth

The MP4 frames, and nothing else.

Not the input log. Not the take plan. Not a live desktop shot. Not memory of the
take. If the log says click and the frame has no menu, the frame wins and that
claim is deleted. The take plan is a hint about where to look, never a source for
what to write.

## What a state is

A state is what is true on screen for a stretch of time. A new object starts only
when something material changes: a menu opens, text appears, a selection moves, a
spinner starts or dies, a list gains a row, an item moves to a new section.

If one state holds for eight seconds, that is one object, not eight copies. A tick
every second with no change is noise, and for narration it is worse than noise: it
fragments a line that should be read over one continuous picture.

What counts as material, what does not, and the two failure shapes — one object per
mouse twitch, and one object for a stretch that visibly changed twice — are in
[references/state-boundaries.md](references/state-boundaries.md).

## Array shape

The whole video is one array. No narration fields: no `say`, no `must_cover`, no
`kind` used as a speech instruction, no suggested wording.

```json
[
  {
    "start": 2.252,
    "end": 3.363,
    "on_screen": {
      "window": "the application, as its title bar names it",
      "regions": {},
      "text": [],
      "cursor": ""
    },
    "changed": "What became true on screen versus the previous state, as a fact."
  }
]
```

`on_screen` is structured fact: visible strings copied exactly, which panel is
open, what is selected or highlighted, whether a menu is open and what its items
are, spinner or not. Use the region names that fit the application in the frames —
a terminal has a prompt and output, an editor has a sidebar and a tab, a browser
has an address bar. Fill the regions that exist in that frame and do not invent
widgets that are not there.

`cursor` is the mouse pointer: where it is, and what it is over if that matters. A
text caret is a different thing and belongs in the region that holds it, named so
that nobody can confuse the two.

`changed` is the event that opened this state, stated as a fact about the picture,
not as a teaching line.

## How to extract

1. Read the duration from the MP4 with `ffprobe`.
2. Walk the video by extracting frames, not by trusting any log. Use the take plan
   only as a hint for where to look.
3. When the picture changes, close the previous object and open a new one. Set
   `start` and `end` from the frame times.
4. For each object, extract a frame at `start` and a frame at `end`.
5. Write `on_screen` from those frames. Copy on-screen text as written.

## How to verify

For every object:

- The start frame shows this state.
- The end frame still shows this state.
- A frame just before `start` still shows the previous state.
- A frame just after `end` already shows the next state, or the video ended.

If a frame is unclear, extract another nearby frame. Do not guess. If you cannot
read a string, omit it or record that it was unreadable. Never fill from memory.

Then run the machine checks, from the workspace root:

```bash
python3 .cursor/skills/4-extract-states/extract-lesson-states/scripts/validate_states.py \
  courses/<course-slug>/lessons/<NN>-<lesson-slug>/states.json
```

It enforces what a narration writer depends on: the array covers the video from
start to end with no gap and no overlap, the timestamps are exact and ordered, no
narration field has crept in, and no object is too short to speak over. Add
`--extract-frames DIR` and it writes the start and end frame of every object, so
the check above is reading images rather than remembering them.

**Gate:** every object passes the four frame checks and the validator exits clean.
If any object fails, fix or delete it. Do not ship the array.

## Do not

- Tell the other model what to say
- Write voiceover, captions, or pedagogical "what to cover"
- Use a live screenshot or the recorder script as proof
- Emit one object per mouse twitch that did not change the picture
- Emit one object per clock second when the state did not change
- Leave a gap between two objects, or let two objects overlap
- Start this skill before the MP4 is locked

## Done when

`states.json` sits beside `lesson.mp4`, the validator exits clean, every object
has been read off its own start and end frames, and a narration writer could work
from the file alone.

On any conflict between this skill and the repo-root `COURSE_AGENT.md`, that
document wins.
