---
name: record-until-the-result-is-visible
description: >-
  Holds a screen recording to the whole arc of an action: the starting state
  visible before it begins, the entire path visible while it happens, and the
  complete finished result visible at the end, held long enough to read. Use
  whenever a recording contains an action that produces output — an agent reply,
  a build, a page load, a search, an install, a dialog — and when deciding
  whether a take can be shipped. Verifies all three against frames extracted from
  the MP4 itself, never from the live desktop.
icon: shield
color: red
metadata:
  stage: 3-film-the-lesson
  consumes: courses/<course-slug>/lessons/<NN>-<lesson-slug>/take-plan.md
  produces: courses/<course-slug>/lessons/<NN>-<lesson-slug>/lesson.mp4
  runs_with: real-example-in-every-lesson, human-screen-recordings
---

# Record until the result is visible

Every action in a lesson has three parts, and a viewer needs all three to learn
anything from it:

1. **Before** — the state the action starts from, on screen, before it begins.
2. **Path** — the whole action happening, continuously, with nothing cut out.
3. **Result** — the complete finished output, held long enough to read.

Miss the first and the result proves nothing, because the viewer cannot tell what
changed. Miss the second and they cannot reproduce it, because the transition
happened somewhere they could not see. Miss the third and they never learn what
the action was for.

This is a contract, not a preference. A take that fails any of the three is a
failed take. Delete it. Do not send it.

## The failure this exists to stop

The recorder is not the live desktop. The recorder is the MP4 file.

If you watch the live screen, or a screenshot tool, or a log line, and decide "the
answer is there", you can still ship a video whose last frames say
`Waiting for subagent` / `Working` / `Synthesizing`. That has already happened.
The live desktop and the encoded file are not interchangeable proof.

The same mistake has a quieter version at the other end: starting the recorder
after the interesting state was already set up, so the film opens on a screen the
viewer has no way to account for.

## Hard rules

Never:

- Start the recorder after the starting state exists. The viewer has to see the
  empty file, the missing entry, the failing test — whatever the action changes.
- Cut, splice, or jump between two states of the same action. The transition is
  the lesson.
- Speed up a section in a way that hides a step a learner must perform.
- Stop ffmpeg (or any recorder) on a fixed `sleep` after sending a prompt.
- Stop because "it should be done by now".
- Stop because a live screenshot, a chat log, or a description looks done.
- Stop because you wrote yourself a `/tmp/done` flag from that live still.
- Deliver a video you have not opened. The MP4 is the only source of truth.
- Call a take good if the last 2 seconds still show waiting, working,
  synthesizing, a spinner, or a partial stream.
- Wander the mouse to other UI to "fill time" while the result is not yet on
  screen.

Always:

1. Start the recorder **before** the starting state is disturbed, and hold on it
   long enough to be read — a second or two, longer if it is dense.
2. Keep recording through the whole action. Approvals, permission prompts and 2FA
   are part of the path: complete them on camera and keep going.
3. Wait until the **full output** is painted: the complete reply, the loaded page,
   the finished build.
4. Hold 3–5 seconds on that result, longer when it has several lines to read. Do
   not cut on the first token.
5. **Then** extract frames from the MP4 itself and read them.
6. Only after that check may you send the file.

## What "done" means

| Action | Done only when the last MP4 frames show |
|---|---|
| Agent / chat prompt | The complete answer text. No `Waiting`, `Working`, `Synthesizing`, `Waiting for subagent`, no primary Stop-as-busy state. |
| Navigate to a URL | Destination content painted, not a blank tab or spinner. |
| Search | Results list visible. |
| Build / install | Success, or a finished error, not a running log. |
| Click Allow | Not done. Allow is a mid-step. Keep waiting for the output Allow was blocking. |

Partial text at the bottom of a stream is not done. The viewer must be able to
read the result the lesson promised — all four bullets, not the last sentence.

## How to wait

Do not guess a duration. Poll the **recorded display** until the done condition is
true, with a high ceiling: minutes, not fifteen seconds.

- Grab frames from the same display ffmpeg is recording, or read the output file
  once it has flushed a recent frame.
- Detect done from those pixels: a known idle state, the follow-up box back, no
  working bar.
- If an approval appears, complete it with the same human-input protocol, then
  keep polling.
- If the ceiling hits and the result is still not visible, fail the take, delete
  the file, and do not deliver.

A live screenshot tool is allowed only as a hint that an approval is waiting. It
is never permission to stop, and never proof to send.

## Verify from the file

From the workspace root, once the recorder has exited:

```bash
python3 .cursor/skills/3-film-the-lesson/record-until-the-result-is-visible/scripts/verify_take.py \
  courses/<course-slug>/lessons/<NN>-<lesson-slug>/lesson.mp4 --action-at <seconds>
```

It pulls the frames the three gates need, proves from the pixels that the ending
is settled rather than still moving, and refuses the mechanical failures: a take
with no motion, a result that never stops changing, a hold that is too short.

Then **read the frames it wrote**. The script cannot tell whether the answer on
screen is the answer the lesson promised; that judgment is yours, and
[references/verify-from-frames.md](references/verify-from-frames.md) says what
disqualifies each of the three.

The manual version of the last check, when all you need is one frame:

```bash
ffmpeg -y -sseof -3 -i lesson.mp4 -frames:v 1 /tmp/last.png
```

Read `/tmp/last.png`. Can a stranger see the finished output in this frame? If
no, delete the MP4 and the states JSON. Reshoot. Do not explain the file away.

## Done when

A person watching the MP4, and only the MP4, sees: the starting state → the
action → the wait → the full result on screen → a hold long enough to read it →
end. The last frames are the result, not the wait, and the first frames are the
world before the action, not after it.

On any conflict between this skill and the repo-root `COURSE_AGENT.md`, that
document wins.
