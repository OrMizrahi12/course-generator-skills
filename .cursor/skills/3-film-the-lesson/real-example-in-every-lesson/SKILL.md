---
name: real-example-in-every-lesson
description: >-
  Judges whether a lesson's example is the optimal one for teaching this material
  — clear, interesting, relatable, unmistakably making the feature's point, and
  matching the pedagogical context and the course's own instructions — then holds
  the film to 0% to 100% on camera with the result visible in the last frames.
  Use when preparing or reviewing the take for a course lesson, before the
  recorder starts and again after the take. Runs from the ready brief left by
  /research-the-current-lesson. Refuses smoke tests, tours, and takes that hide
  how the lesson object was created.
icon: shield
color: purple
metadata:
  stage: 3-film-the-lesson
  consumes: courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md
  produces: courses/<course-slug>/lessons/<NN>-<lesson-slug>/take-plan.md
  runs_with: human-screen-recordings, record-until-the-result-is-visible
---

# Real example in every lesson

Stage 3 of 4, and the gate the other two filming skills run behind. Two things
are decided here, in this order:

1. **Is this the optimal example for teaching this material?** Not merely valid —
   optimal. Teaching is the product, and the example is the entire vehicle.
2. **Is the film 0% to 100%?** Creation, path, and result, with nothing that
   matters happening off camera.

Either one failing means the recorder does not start, or the take is deleted.

## The example is the teaching

A lesson is a silent film. There is no narration to rescue a confusing example,
no voice to explain why the viewer should care, and no second chance to make the
feature's point. Whatever the example carries, the viewer gets; whatever it
fails to carry is simply lost.

So the example is not a stage prop chosen for convenience. It is judged against
five criteria, all of them, before anything is recorded:

- **Clear** — a viewer follows it with no explanation. Nothing in it needs
  knowledge the course has not already taught.
- **Interesting** — the viewer wants to see how it ends.
- **Relatable** — a person recognizes the situation as one of their own.
- **It carries the message** — what the feature makes possible is unmissable in
  the outcome, not inferable from it.
- **It fits this course** — the audience, the level, the lessons already shipped,
  and the instructions the user gave for this specific course.

The tests for each, their failure signatures, and worked pass/fail pairs are in
[references/example-rubric.md](references/example-rubric.md). Read it before you
judge, and record a verdict per criterion — an unrecorded judgment is a judgment
that gets reversed under time pressure.

Where the course's own instructions live, and what outranks what when they
conflict, is in
[references/pedagogical-context.md](references/pedagogical-context.md).

## Chooser and judge are different jobs

`/research-the-current-lesson` chooses the example, because it holds the mastery
of the material. This skill judges the choice and can refuse it.

Do not re-open the research here, and do not run a second shallow search to find
a replacement. If the example fails the rubric, say which criterion it failed and
send it back to stage 2 with that finding. Coming back with a better example is
that stage's job.

## Workflow

Copy this checklist into your reply and keep it current:

```
Lesson <N> take:
- [ ] 1. Ready brief read, preconditions met
- [ ] 2. Example judged against all five criteria, verdict recorded
- [ ] 3. Take plan written, every created object mapped to a step
- [ ] 4. Validator clean on the take plan
- [ ] 5. Filmed with /human-screen-recordings and /record-until-the-result-is-visible
- [ ] 6. Both gates checked against the MP4 itself
```

### 1. Preconditions

- `courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md` exists with
  `status: ready`.
- `courses/<course-slug>/pedagogy.md` exists, or you are about to write it from
  the user's instructions — see
  [references/pedagogical-context.md](references/pedagogical-context.md).

No brief, no filming. A take shot from your own memory of the research is a take
nobody can check.

### 2. Judge the example

Score all five criteria from
[references/example-rubric.md](references/example-rubric.md) against the brief's
`## The human example`, and write the verdict into the take plan.

**Gate:** every criterion passes, or the example goes back to stage 2. A single
failure is enough — an example that is real and finishable but confusing teaches
nothing, and one that is clear but trivial teaches nothing worth knowing.

### 3. Write the take plan

Copy [assets/take-plan-template.md](assets/take-plan-template.md) to
`courses/<course-slug>/lessons/<NN>-<lesson-slug>/take-plan.md` and write the
exact steps the viewer will see, in order.

Every object in the brief's `## Must be created on camera` gets a step number
before it is used. A plan that starts at the last verb — type the command, hold
the row, ask the agent to use the thing — is an automatic fail.

What may be off camera, what may not, and the invalid-take list are in
[references/on-camera-path.md](references/on-camera-path.md).

### 4. Validate

From the workspace root:

```bash
python3 .cursor/skills/3-film-the-lesson/real-example-in-every-lesson/scripts/validate_take_plan.py \
  courses/<course-slug>/lessons/<NN>-<lesson-slug>/take-plan.md
```

It cross-checks the plan against the ready brief and the course's pedagogy file,
so a plan that drops a creation step or was judged against nothing fails before
the recorder starts.

**Gate:** validator clean, then set `status: approved`.

### 5. Film

Run `/human-screen-recordings` for how the input must look and
`/record-until-the-result-is-visible` for when the recorder may stop. They are
not optional companions; all three run on the same take.

### 6. The two gates, checked against the MP4

1. **Path on camera, 0% to 100%** — every step a new user needs, including how
   the lesson object came to exist.
2. **Result in the actual last frames** — the finished output of that path, read
   from the file, not from the live screen.

Last-frame proof is necessary and not sufficient. Result without process is the
same class of failure as a tour, which is process without result. Either gate
failing means the take is deleted and reshot from the reset in the brief.

## Do not

- Film without a `ready` brief, or judge the example against nothing
- Re-choose the example here instead of sending the finding back to stage 2
- Accept a smoke test: `echo`, hello files, a dummy server, "reply with only this"
- Rename a lesson "Run X" or "Use X" as permission to hide how X came to exist
- Create the lesson object off camera, with a shell, a pre-written file, an API,
  or an earlier unfilmed click
- Ship a take whose last frames still say Waiting, Working, or Synthesizing
- Use a live screenshot, a log line, or your own done flag as proof
- Keep a take because reshooting is expensive

## Done when

The take plan is `approved`, the MP4 shows creation, path, and result with
nothing critical off camera, the last frames hold the finished result, and the
example still reads — to a stranger watching only the film — as work a person
would want to do.

On any conflict between this skill and the repo-root `COURSE_AGENT.md`, that
document wins.
