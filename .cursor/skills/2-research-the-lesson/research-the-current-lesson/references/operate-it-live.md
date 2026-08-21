# Operate it live, off camera

Read this at step 3 of [SKILL.md](../SKILL.md).

Do the thing before you describe the thing. Every claim about the path has to
come from having walked it in this environment, because the gap between the
documented path and the real one is exactly where takes die.

## Contents

- Walk it end to end
- What to write down
- Find and verify the reset
- What must not be pre-created
- When the product disagrees with the docs
- When the live surface is unavailable

## Walk it end to end

Once, all the way, in the environment the lesson will be filmed in. Not a partial
probe, not a read of a screenshot in the docs.

Watch what the screen does between the steps, not only at the end. The states in
between are what the viewer will be looking at for most of the lesson, and they
are what a documentation page never shows.

## What to write down

- **Entry point.** Where a person starts, exactly as it is labeled now.
- **The gesture sequence.** The real steps in the real order, including the ones
  the docs skip because they are obvious to the author.
- **The states in between.** What appears, what changes, what has to be dismissed.
- **Done on screen.** The specific thing a stranger could point at and say: that
  worked.
- **Waits.** Anything that takes long enough to matter, with roughly how long.
- **Interruptions.** Approvals, permission prompts, sign-ins, confirmations —
  anything that appears mid-flow and has to be handled without breaking the take.

That list is the raw material the filming stage turns into a path. Do not turn it
into one here.

## Find and verify the reset

The lesson has to be filmable from zero, which means the state it creates has to
be removable.

1. Find the reset: delete the file, remove the folder, revoke the connection, undo
   the commit, clear the setting.
2. **Do it, and confirm the thing is gone from the screen** — not from your
   memory of having clicked delete.
3. Write down the reset in the brief. The filming stage will need it after every
   failed take, and rediscovering it under pressure is how a half-created state
   ends up in a shipped lesson.

If nothing resets the state, say so now. A lesson that can be filmed exactly once
is a fact the whole production has to plan around, and it is much cheaper to know
before the first take.

## What must not be pre-created

Probing is off camera and allowed. Creating the object the lesson exists to show
being created is not.

If your walkthrough created that object — the command, the skill, the rule, the
connection, the branch, the file — remove it and confirm it is gone before the
recorder starts. Being able to say "it was already there" is not a defense; the
viewer needs to see it come into existence.

Everything else that is merely context — an open window, a signed-in session, an
existing repository the lesson does not claim to create — can stay.

## When the product disagrees with the docs

The screen wins. Record both: what the docs say, what the product does, and which
one the lesson will teach.

Then check the changelog before concluding the docs are simply wrong. A
disagreement is usually a rename or a replacement, and knowing which one it is
changes what the lesson says.

## When the live surface is unavailable

If the feature cannot be reached here — no account, no tier, no connector, no
network — you have hit the limit of what this stage can honestly produce.

Do not describe a path you did not walk. Do not reconstruct it from documentation
and present it as observed. Say what is blocked, what would unblock it, and stop.
The syllabus's capability probe should have caught this at stage 1; if it did not,
that is a finding to hand back with the blocker.
