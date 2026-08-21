# Review, acceptance, and revision

Read this at step 6 of [SKILL.md](../SKILL.md), and again whenever an accepted
syllabus has to change.

## Contents

- How to present the draft
- The three reactions and their repairs
- What acceptance means
- Re-entering an accepted syllabus
- When you disagree with the user's call

## How to present the draft

In the chat, in the user's language:

- The promise, in one sentence.
- The audience and level, in one line.
- The spine as a numbered list: title, and what the viewer can do after.
- What is out of scope, said plainly rather than buried.
- Anything you decided for them, marked as a decision they can reverse.
- Anything the capability probe flagged, before they accept rather than after.

Then ask for edits directly: what to cut, what to add, what order is wrong. Do
not ask "does this look good?" — that question gets a yes and a course nobody
wanted.

Keep the full artifact on disk. The chat shows the spine; the file holds the
sources, the dependencies, and the per-lesson fields.

## The three reactions and their repairs

**"Too many lessons."** Do not delete from the end. Merge the lines that teach
the same gesture, then drop the line with the weakest necessity, and say which
one you dropped and why.

**"You missed X."** Place X where its dependencies allow, not at the end. Then
re-run Test 5 on every line after it — inserting a lesson is the most common way
a forward dependency appears.

**"Lesson 4 should come first."** Check what lesson 4 depends on. If moving it
breaks a dependency, say which one and offer the reorder that works. If nothing
breaks, move it and renumber.

After any of the three, re-run the validator before you show the revision.

## What acceptance means

Acceptance is the user saying yes to the spine, in the chat, after seeing it.
Not your own judgment that it is good, and not silence.

Only then:

- Set `status: accepted` in the artifact.
- Re-run the validator one last time.
- Hand lesson 1 to `/research-the-current-lesson`.

While the status is `draft`: no lesson research, no example chosen, no recorder,
no numbered lesson directories on disk.

## Re-entering an accepted syllabus

Courses change mid-production. When they do, the artifact leads and the footage
follows — never the other way around.

1. Set `status` back to `draft`.
2. Make the change: edit, insert, drop, or reorder.
3. Re-run Test 5 on every line at or after the change.
4. Re-run the validator.
5. Get acceptance again.
6. Note any already-filmed lesson the change invalidates, and say so plainly. A
   lesson whose spine line no longer exists is not shipped as if it does.

Renumbering after lessons are filmed is expensive. Prefer inserting at the end
of a dependency chain, and say when the cheaper option is worse for the viewer.

## When you disagree with the user's call

Say it once, with the reason and the concrete consequence — "lesson 2 would need
the connector from lesson 5, so it cannot be filmed 0% to 100% in that position"
— then follow their decision and record it in the artifact.

Do not relitigate across turns, and do not quietly implement your own version.
An explicit user instruction outranks this skill; an unstated preference of yours
outranks nothing.
