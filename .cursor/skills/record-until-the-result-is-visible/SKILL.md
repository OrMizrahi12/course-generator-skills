---
name: Record until the result is visible
description: >-
  Use when a screen recording includes an action that produces output (agent
  reply, page load, build, search). Never stop the recorder until that full
  result is visible in the actual MP4 frames.
---
# Record until the result is visible

Use this whenever the recording contains an action that produces output: an agent reply, a page load, a search, a build, a dialog, a download. The viewer must see the **finished result**, not the wait.

This is a contract, not a nice-to-have. A take that ends on a spinner is a failed take. Delete it. Do not send it.

## The failure this exists to stop

The recorder is not the live desktop. The recorder is the MP4 file.

If you watch the live screen, or a Screenshot tool still, or a log line, and decide "the answer is there", you can still ship a video whose last frames say `Waiting for subagent` / `Working` / `Synthesizing`. That has already happened. The live desktop and the encoded file are not interchangeable proof.

## Hard rules

Never:

- Stop ffmpeg (or any recorder) on a fixed `sleep` after sending a prompt.
- Stop because "it should be done by now".
- Stop because a live Screenshot / screenshot-description / chat log looks done.
- Stop because you wrote yourself a `/tmp/done` flag from that live still.
- Deliver a video you have not opened. The MP4 is the only source of truth.
- Call a take good if the last 2 seconds still show waiting, working, synthesizing, a spinner, or a partial stream.
- Wander the mouse to other UI (sidebar, IDE switcher) to "fill time" while the result is not yet on screen.

Always:

1. After the action (click, Enter, submit), keep recording.
2. If the UI asks for Allow / approval / 2FA to finish the action, complete that, then keep recording.
3. Wait until the **full output** is painted on screen: the complete reply, the loaded page, the finished build.
4. Hold 3–5 seconds on that result so a viewer can read it. Do not cut on the first token.
5. **Then** extract frames from the MP4 itself (not a live grab) at the last 1s, 2s, and 3s. Read those frames. If the result is not fully there, the take is invalid.
6. Only after that check may you send the file.

## What "done" means

| Action | Done only when the last MP4 frames show |
|---|---|
| Agent / chat prompt | The complete answer text. No `Waiting`, `Working`, `Synthesizing`, `Waiting for subagent`, no primary Stop-as-busy state. |
| Navigate to a URL | Destination content painted, not a blank tab or spinner. |
| Search | Results list visible. |
| Build / install | Success (or a finished error), not a running log. |
| Click Allow | Not done. Allow is a mid-step. Keep waiting for the output Allow was blocking. |

Partial text at the bottom of a stream is not done. The viewer must be able to read the result the lesson promised (e.g. all 4 bullets, not the last sentence).

## How to wait (technical)

Do not guess duration. Poll the **recorded display** until the done condition is true, with a high ceiling (minutes, not 15 seconds).

- Grab frames from the same `$DISPLAY` ffmpeg is recording, or read ffmpeg's output file once it has flushed a recent frame.
- Detect done from those pixels (OCR or a known "idle" UI: follow-up box, no Working bar).
- If an Allow button appears, click it with the same human-input protocol, then keep polling.
- If the ceiling hits and the result is still not visible: fail the take, delete the file, do not deliver.

A live Screenshot tool is allowed only as a hint to click Allow. It is **not** permission to stop or to send.

## Before you send

```
ffmpeg -y -sseof -3 -i lesson.mp4 -frames:v 1 /tmp/last.png
```

Read `/tmp/last.png`. Ask: can a stranger see the finished output in this frame? If no, delete the MP4 and the timeline JSON. Reshoot. Do not explain the file away.

## Done when

A person watching the MP4, and only the MP4, sees: action → wait → **full result on screen** → short hold → end. The last frames are the result, not the wait.
