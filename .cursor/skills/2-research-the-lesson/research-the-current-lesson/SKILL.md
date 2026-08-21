---
name: research-the-current-lesson
description: >-
  Makes you competent to teach one specific lesson before it is filmed: masters
  the current material to teaching depth, operates the feature live in this
  environment, establishes the path a practitioner would actually use, then
  chooses the real human example and writes the lesson brief the filming stages
  read. Use before recording, scripting, or delivering any single course lesson,
  once the syllabus is accepted — and again, from scratch, for every lesson after
  it. Does not re-plan the syllabus, research other lessons, write shot lists, or
  start a recorder.
icon: beaker
color: cyan
metadata:
  stage: 2-research-the-lesson
  consumes: courses/<course-slug>/syllabus.md
  produces: courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md
  next: real-example-in-every-lesson
---

# Research the current lesson

Stage 2 of 4. Deep and narrow: one lesson, now. Stage 1 decided what the course
teaches. This stage makes you able to teach **this** lesson at the level of
someone who uses the thing daily, and writes that competence down as the brief
every filming stage reads.

Mastery is the deliverable, not a reading list. A summary of the docs is what a
model produces in two minutes and it is exactly what produces a lesson that
collapses the first time the UI does something unexpected.

## The failure this skill exists to stop

Three things happen when this stage is rushed, and all three are only visible
after the takes are wasted:

- **Shallow material.** The path is memorized, the mechanism is not, so the
  lesson teaches a gesture rather than a skill and cannot survive a deviation.
- **The example chosen first.** The feature gets bolted onto a job that never
  needed it, and the lesson becomes a demonstration of nothing.
- **Drift into the rest of the course.** Attention leaks to lesson N+1, and this
  lesson gets the leftovers.

## Preconditions

Before anything else, confirm all three. Any failure stops the stage.

1. `courses/<course-slug>/syllabus.md` exists and its `status` is `accepted`.
2. You were told which lesson number to work on, or it is the first lesson with
   no brief yet.
3. No brief for this lesson exists yet, or you were asked to redo it.

Never research a lesson off a draft syllabus. A spine the user has not accepted
is still a proposal, and researching it is work done against a moving target.

If the user says they accepted the spine but the artifact still says `draft`, the
acceptance was never recorded. Hand back to `/build-a-course-syllabus` to record
it, then resume here. Do not flip the status yourself, and do not proceed on the
strength of a chat message.

## Workflow

Copy this checklist into your reply and keep it current:

```
Lesson <N> research:
- [ ] 1. Scope locked to lesson <N> from the accepted syllabus
- [ ] 2. Material mastered — every question on the mastery bar answered
- [ ] 3. Operated live in this environment, reset method verified
- [ ] 4. Best practice established, the shortcut named and refused
- [ ] 5. Human example chosen after the research, necessity test passed
- [ ] 6. Brief written and the validator is clean
```

### 1. Lock the scope

Read the lesson's line in the accepted syllabus and copy out only: the number,
the exact title, what the viewer can do after, the feature taught, the example
shape, the result on screen, the dependencies, and the sources already found.

Do not reopen lesson count, order, or titles. Do not research the next lesson
"while you are here". If the next lesson keeps pulling at you, that is the drift
this stage exists to stop.

### 2. Master the material

Not "read the docs". Reach the point where you could answer a practitioner's
questions without looking anything up again.

Work the questions in
[references/mastery-bar.md](references/mastery-bar.md) — mechanism, limits,
defaults, first-timer mistakes, failure modes, the adjacent thing it gets
confused with, and the teach-back test. Every answer needs a live source.

**Gate:** you can state what the feature is in one sentence, what it is not in
one sentence, and what breaks without it — and you hedged on none of them.

### 3. Operate it live, off camera

Do it yourself before you describe it. Walk the whole path in this environment,
watch what the screen actually does, and find out where the docs and the product
disagree.

[references/operate-it-live.md](references/operate-it-live.md) covers what to
record while walking it, and how to find and verify the reset method.

**Gate:** the reset works. Research and probing are off camera, but the object
the lesson must show being created is not pre-created — if your probe made it,
undo it and confirm it is gone.

### 4. Establish best practice

A path that works is not the path to teach. Find the one a practitioner would
use, and be able to say why the shortcut is worse.

[references/best-practice.md](references/best-practice.md) has the procedure:
gather the candidate paths, choose on evidence, name the shortcut you refuse, and
name the check the viewer performs to know it worked.

**Gate:** the path you will teach reveals how the thing is made. A path that
hides creation is rejected here, not at film time.

### 5. Choose the human example

Only now. Choosing the example first and researching to justify it is the classic
version of this failure.

[references/choose-the-example.md](references/choose-the-example.md) has the
candidate procedure, the necessity and finishability tests, and the smoke-test
blacklist.

**Gate:** delete the feature and the job must break. If the job survives, the
example is dead — pick another.

### 6. Write the brief and validate it

Copy [assets/lesson-brief-template.md](assets/lesson-brief-template.md) to
`courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md`, two digits for the
number, then:

From the workspace root:

```bash
python3 .cursor/skills/2-research-the-lesson/research-the-current-lesson/scripts/validate_brief.py \
  courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md
```

It also cross-checks the brief against the accepted syllabus, so a brief that has
quietly drifted from the spine fails here rather than at film time.

**Gate:** validator clean, then set `status: ready`. Filming starts from a `ready`
brief and from nothing else.

## When the research contradicts the syllabus

Two different cases, and they get different treatment.

**This lesson's line is wrong.** The feature was renamed, it now needs an account
the course does not have, or the line cannot be filmed 0% to 100% after all. Do
not quietly rewrite the lesson and do not proceed with a line you know is broken.
Stop, say plainly what the research established and which line it breaks, and
hand it back to `/build-a-course-syllabus` with the user. The syllabus returns to
`draft`, gets fixed, and gets accepted again before this stage resumes.

**This lesson constrains a later line.** What you build or refuse here can decide
whether a later lesson is filmable at all — the state this lesson creates is the
state that lesson inherits. That is a finding, not permission to research the
later lesson. Record it in the brief's `## Constrains later lessons` section, tell
the user in one line, and leave the later line alone unless they change it.

**The syllabus's prose is wrong, but no lesson line depends on it.** Descriptions
of the project or of production order can go stale without breaking the spine. Do
not reopen acceptance over prose. State the correction in the brief, which governs
the film, and tell the user in one line.

All three are cheap now and expensive after the first take.

## Scope boundary

This stage produces knowledge and one decision: what will be filmed and why. It
does not produce the film.

No click scripts, no coordinates, no prompts, no timeline, no recorder. Those
belong to the filming stages, which read the brief you write here.

## Handoff

With `status: ready`, hand off to `/real-example-in-every-lesson`
(`.cursor/skills/3-film-the-lesson/real-example-in-every-lesson/SKILL.md`) for the
0% to 100% path and its ship gates, then to the recording skills. Pass the brief; do not pass
guesses that are not in it.

Then, for the next lesson, start this skill again from step 1. Last lesson's
research is not this lesson's research, and reusing it is how a course ends up
teaching a dead path in lesson 5.

## Do not

- Research off a `draft` syllabus, or flip that status yourself
- Reopen the syllabus: count, order, or titles
- Research more than one lesson in a pass
- Pick the example first and research afterwards to justify it
- Accept a smoke test: `echo`, hello files, a dummy server, "reply with only this"
- Create the lesson object off camera, or leave a probe's leftovers in place
- Teach a path you found in training memory instead of in the live product
- Write the click script, open ffmpeg, or start a recorder here
- Set `status: ready` while the validator still reports an error

## Done when

`courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md` exists with
`status: ready`, the validator is clean, every claim in it traces to a live
source, the reset method has been verified by doing it, and the example is work a
person would do even if nobody were filming.

On any conflict between this skill and the repo-root `COURSE_AGENT.md`, that
document wins.
