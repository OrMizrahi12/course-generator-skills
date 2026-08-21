---
name: build-a-course-syllabus
description: >-
  Plans a new course and writes the syllabus artifact that every later stage of
  production reads: promise, audience, explicit out-of-scope, and an ordered
  spine of lessons that are each filmable 0% to 100% around one real human
  example. Use when the user asks for a new course, a syllabus, a curriculum, a
  lesson list, a lesson plan, or "what should the lessons be", and before any
  lesson is researched or recorded. Asks intake questions first, then researches
  live sources, then hands the user a draft to accept. Does not write shot
  lists, click paths, prompts, or narration.
icon: book-open
color: blue
metadata:
  stage: 1-plan-the-course
  produces: courses/<course-slug>/syllabus.md
  next: research-the-current-lesson
---

# Build a course syllabus

Stage 1 of 4. Decide what the course teaches and in what order, then write it to
one artifact that every later stage reads. Nothing here is shot-level.

Terms, used the same way in every stage:

- **syllabus** — the artifact: `courses/<course-slug>/syllabus.md`
- **spine** — its ordered list of lessons
- **lesson** — one silent MP4 plus its states JSON, filmed 0% to 100%

## The failure this skill exists to stop

Asked for a course, a model can emit a plausible lesson list from training
memory in ten seconds: no intake, no live sources, a third of the lessons named
"Overview of X", and a spine whose lesson 3 needs a feature lesson 7 teaches.
Each of those defects surfaces later, at film time, after real takes have been
shot and thrown away — and no amount of camera work rescues a lesson line that
was never filmable.

Questions first. Live research second. Draft third. Acceptance fourth. A
syllabus produced faster than that is the bug, not the win.

## Workflow

Copy this checklist into your reply and keep it current:

```
Syllabus progress:
- [ ] 1. Intake answered by the user, or defaults stated and confirmed
- [ ] 2. Live research done, every source recorded with its URL
- [ ] 3. Capability probe: every planned lesson is producible in this environment
- [ ] 4. Spine drafted, every lesson passes the five lesson tests
- [ ] 5. Validator clean on courses/<course-slug>/syllabus.md
- [ ] 6. User accepted the spine, status flipped to accepted
```

### 1. Intake

Ask before you research. Ask only what the user alone can know, in the language
they are writing in; the artifact itself is English.

Cover: the subject, the size, the audience and their prior knowledge, the level
to reach, the delivery character, and what is explicitly out of scope. Six
questions is the ceiling. Skip anything the conversation already answered.

The full question set, the defaults you may adopt when the user waves you off,
and the answers you may never invent are in
[references/intake.md](references/intake.md). Read it before you ask.

**Gate:** do not open a browser until subject, audience, size, and scope are
settled — either answered by the user or stated by you as explicit defaults the
user can correct.

### 2. Research live

Research the product as it is now, not as your training data remembers it.
Feature names, menu locations, and defaults drift, and a syllabus built from
memory plans lessons for a UI that no longer exists.

Read [references/research.md](references/research.md) before your first search.
It sets the source order, what counts as a source, and the ledger format.

**Gate:** a feature you cannot confirm in a live source does not go on the
spine. Record every source URL and what it established.

### 3. Probe what this environment can actually produce

A lesson you cannot film here is a promise you cannot keep. Before a feature
earns a line on the spine, confirm the tool exists in this environment, that any
account, tier, or connector it needs is available, and that its result appears
on screen where a camera can see it.

The probe procedure is in
[references/research.md](references/research.md#capability-probe). Record what it
found in the artifact's `## Capability probe` section — a gate that leaves no
trace is a gate the next stage has to run again.

**Gate:** anything blocked gets resolved, replaced, or told to the user before
acceptance. Never plan a lesson you already know cannot be filmed.

### 4. Draft the spine

Copy [assets/syllabus-template.md](assets/syllabus-template.md) to
`courses/<course-slug>/syllabus.md` and fill it in. Derive the slug from the
course title in kebab-case.

Every lesson must pass all five tests — competence, necessity, filmable, visible
result, and order. The tests, the sizing rules for splitting and merging, and
worked pass/fail examples are in
[references/lesson-tests.md](references/lesson-tests.md). Apply them to each
line as you write it, not once at the end.

**Gate:** a lesson that fails a test gets rewritten, split, or dropped here.
Never carried "we will fix it when we film it".

### 5. Validate

From the workspace root:

```bash
python3 .cursor/skills/1-plan-the-course/build-a-course-syllabus/scripts/validate_syllabus.py \
  courses/<course-slug>/syllabus.md
```

Fix every reported error and run it again until it exits clean. Warnings are
judgment calls: fix them or be able to say why you kept them.

**Gate:** never show the user a draft the validator rejects.

### 6. Acceptance

Present the spine in the chat language and ask for edits explicitly. The first
draft is a proposal, not a decision. Expect to cut, merge, and reorder.

How to present it, the three reactions you will get and their repairs, and how
to re-enter an accepted syllabus later are in
[references/review-and-revise.md](references/review-and-revise.md).

**Gate:** set `status: accepted` only after the user accepts. No lesson is
researched, filmed, or numbered on disk while the status is `draft`.

## Scope boundary

This skill writes direction, not production. It does not write click paths, shot
lists, prompts, coordinates, narration, or the human example for any lesson —
those are chosen fresh, one lesson at a time, in stage 2.

The syllabus only has to make that possible: each line names one teachable
feature and one shape of real work, so the stage 2 research has something
specific to lock onto.

## Handoff

When `status: accepted`, hand off to `/research-the-current-lesson`
(`.cursor/skills/2-research-the-lesson/research-the-current-lesson/SKILL.md`) for
lesson 1, and to that same skill again, from scratch, for every lesson after it. Pass the lesson
line and its sources; do not pass your own guesses about the shot.

## Do not

- Emit a lesson list before intake, or from training memory instead of live sources
- Invent a lesson count, an audience, or a must-include the user did not give
- Start from "list every button in the product"
- Write a lesson that is a tour, an overview, or a settings walk-through
- Plan a lesson whose result never becomes visible on screen
- Order a lesson before the lesson it depends on
- Reduce scope silently — the artifact has an out-of-scope section for exactly this
- Flip `status` to `accepted` on your own authority
- Start filming, or pick a human example, while the status is `draft`

## Done when

`courses/<course-slug>/syllabus.md` exists, the validator exits clean, every
lesson traces to a live source and to a capability that exists here, the
out-of-scope section says what the course will not cover, and the user has
accepted the spine.

On any conflict between this skill and the repo-root `COURSE_AGENT.md`, that
document wins.
