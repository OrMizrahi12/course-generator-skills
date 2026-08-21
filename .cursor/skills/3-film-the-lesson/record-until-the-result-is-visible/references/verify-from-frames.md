# Verifying a take from its own frames

Read this after `scripts/verify_take.py` has written the frames, at the last step
of [SKILL.md](../SKILL.md).

The script proves the mechanical things: that the picture moves during the action,
that it stops moving at the end, that the hold is long enough. It cannot tell
whether what is on screen is what the lesson promised. That is this procedure.

## Contents

- Read frames, not memory
- Gate 1: the before frame
- Gate 2: the path frames
- Gate 3: the result frames
- Busy states, by name
- What to do with a failed take

## Read frames, not memory

Open the extracted images and describe what you see, out loud, before you judge
them. Two things go wrong when this step is skipped: you see the state you
intended to film rather than the one you filmed, and you accept a partial result
because you know what the rest of it said.

The question at every gate is the same: **what could a stranger who has never seen
this tool conclude from this frame alone?**

## Gate 1: the before frame

The first frames, before the action begins. They fail if:

- The thing the action creates is already there.
- The state the action changes is not visible at all, so the change will be
  invisible too — an empty panel where the list should be, a scrolled-away file,
  a collapsed section.
- The window does not fill the screen, or another window is in frame.
- The screen is mid-transition: a menu closing, a notification fading, a cursor
  still travelling from the last action.

A useful test: cover the rest of the video and ask what this frame claims. "There
are three worktrees" or "this file does not exist yet" is a claim the result can
be measured against. "A terminal" is not.

## Gate 2: the path frames

The frames between the action starting and the result appearing. They fail if:

- Two consecutive checkpoints show states that cannot be connected by anything
  visible — the viewer would have to guess what happened in between.
- A step happened while the camera was elsewhere: a dialog dismissed off-frame,
  a file edited in a window that is not on screen.
- An approval or confirmation was handled outside the recording.
- The action visibly restarts, which means the take contains two attempts.

The standard is reproduction, not aesthetics: a learner with the stated
prerequisites, watching only these frames, can perform the same sequence.

## Gate 3: the result frames

The last frames, and the ones a second or two before them. They fail if:

- Any busy state is on screen (see below).
- The output is still growing between the last two checkpoints — the script
  reports this as an unsettled ending, and it means the recorder stopped mid
  stream.
- The result is cut off by the viewport: the answer continues below the fold, or
  the important line has scrolled past.
- The result is visible but unreadable: too small, obscured by a tooltip, hidden
  behind the cursor.
- The hold is shorter than a viewer needs to read it. Four lines of output need
  longer than one.

## Busy states, by name

Any of these in the last frames is a failed take, regardless of what the live
screen showed:

`Waiting`, `Waiting for subagent`, `Working`, `Thinking`, `Generating`,
`Synthesizing`, `Loading`, `Running`, `Building`, `Installing`, a progress bar, a
spinner, a skeleton placeholder, a blinking caret in an empty output area, a Stop
button where a Send button belongs.

Two that are easy to miss: a partially painted page whose layout is still
shifting, and a terminal that has printed the command but not yet its output.

## What to do with a failed take

Delete the MP4, and the states JSON if one was already extracted. Then reset with
the method in the lesson brief, confirm the state is back to before the action,
and record the whole arc again from the beginning.

Do not finish the missing part off camera and splice it in. Do not ship the take
with a note explaining what the viewer should imagine. A take that needs an
explanation has already failed the only test that matters.
