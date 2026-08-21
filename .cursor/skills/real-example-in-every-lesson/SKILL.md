---
name: Real example in every lesson
description: >-
  Use when recording a course lesson. Film the feature from 0% to 100% on
  camera. Run [Research the current
  lesson](sand-workflow:research-the-current-lesson) first. Examples are never
  smoke tests. A viewer must be able to reproduce the feature from the MP4
  alone.
---
# Real example in every lesson

Every course lesson is one complete film: 0% to 100%. Creation, path, and result. Never omit even 1% of the path.

The example in that film is never a smoke test. It is the most human, useful, deep job that still fits this exact feature and can finish on camera.

The model will naturally want to skip setup, film only the last verb, and pick `echo` / `hello.txt` / a dummy server. Those instincts are the bug. Treat them as forbidden, not as efficiency.

## Before this skill

Run [Research the current lesson](sand-workflow:research-the-current-lesson) first. That skill owns learning the material, live operation, and choosing the human example for **this** lesson only.

Do not run a second shallow search here. If that brief does not exist yet, stop and do it. If the example was chosen from habit, send it back.

## Human example (foundation)

This is a premise, not a style preference. It does not get dropped to save time, to make last-frame proof easier, or because a tiny prompt is simpler to verify.

A valid example is work a real person would do even if they were not watching a course. The feature must be necessary for that work, not stuck on as a sticker.

If you can delete the feature and the task stays the same, the example is dead.

Smoke tests are invalid: `echo` a lesson name, write `hello-a` / `hello-b`, a command that only says "Course command ran", an MCP that stores a fake note and does nothing else, "reply with only this string".

## Viewer test (must pass before shipping)

A person who has never used the feature can reproduce it from the MP4 alone: where to click, what to type, how the thing is created, and what the finished result looks like.

If that person would ask "wait, where did this command / rule / skill / pin / server come from?", the take is dead. Delete it.

If that person would ask "why would anyone do this?", the example is dead. Delete it.

## Two gates, both required

1. **Path on camera (0% to 100%)** — every UI step a new user needs, including how the lesson object is created.
2. **Result in the actual MP4 last frames** — the finished output of that path, not a spinner.

Last-frame proof is necessary but not sufficient. Result without process is the same class of failure as a UI tour (process without result). Either gate failing means delete the take.

## Feature vs last verb

The feature is the thing the lesson teaches, not the last verb in the title.

- "Custom command" means: where commands live, New, what to write, save, then run. Not only `/course-hello`.
- "Pin" means the pin gesture and the chat appearing under Pinned. Not a hold of an already-pinned row.
- "MCP" / "skill" / "rule" / "automation" means create or connect in the UI, then use.

Do not rename a lesson "Run X" or "Use X" as permission to hide how X came to exist.

## Setup vs the lesson object

Off-camera is allowed only for things that are not the feature: launch Cursor, open Agents Window, New Chat, dismiss a leftover menu.

Off-camera is forbidden for the object of the lesson. Do not create it with Shell, a pre-written file, an API, or an earlier unfilmed click. If the command / skill / rule / automation / pin / MCP is already there before ffmpeg starts, and no prior shipped lesson taught creating it on camera, reset the UI and film creation.

Research can happen off-camera. Creating the lesson object cannot.

## Before ffmpeg (preflight)

You already have the lesson brief from [Research the current lesson](sand-workflow:research-the-current-lesson). Then write the on-camera path: the exact UI steps the viewer must see, in order.

- If any step is "I already wrote this file" or "this already exists", reject the plan. Do not start the recorder.
- If the example is a smoke test or was chosen without that research, reject the plan.
- The timeline must include those create/path steps as first-class actions.
- A timeline that starts at the last verb (type `/course-hello`, hold Pinned, ask the agent to use a tool) is an automatic fail.
- If the lesson uses a terminal: the on-camera path includes setting (or confirming) a **1.75× default** terminal font before typing commands. Small default text is an automatic fail.

## Invalid takes (delete them)

- Opening a panel, typing a slash, or hovering a chip with no finished output
- A hold of a pre-completed state (already pinned, already saved, already created) where the viewer never sees how it was done
- Creating the lesson object off-camera, then filming only use or only the result
- Skipping any required step, even a small one, as "setup" or "we already did that"
- A smoke-test example (`echo`, hello files, dummy MCP, "reply with only this")
- An example chosen from habit instead of researching this feature
- Last frames that still say Waiting / Working / Synthesizing
- Live screenshots or self-set done flags used as proof

## What to do when the action is hard

If the on-camera path misses (wrong click, menu closed, ceiling hit): delete the take, reset the UI to the state before the feature existed, and record the full path again from 0%. Do not finish the missing step off-camera and ship a result-only clip.
