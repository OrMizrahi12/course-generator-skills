# Course Generator

Record any course as silent screen lessons. Each lesson is an MP4 plus a timed states array, and every stage leaves an artifact on disk that the next stage reads.

Chat with the user in Hebrew. Skills, instructions, course production, on-screen text, and artifacts are English.

## Precedence

`COURSE_AGENT.md` is the constitution, and it is always in force — read it before the first decision, not after the work. It governs judgment; the skills govern procedure. On any conflict between a skill and that document, it wins.

## The pipeline

| Stage | Skill | Reads | Writes | The next stage opens when |
|---|---|---|---|---|
| **1. Plan the course** — once per course | `/build-a-course-syllabus` | the user | `courses/<slug>/syllabus.md` | the user has accepted the spine and `status: accepted` |
| **2. Research the lesson** — once per lesson | `/research-the-current-lesson` | the accepted syllabus | `.../lessons/<NN>-<slug>/brief.md` | the validator is clean and `status: ready` |
| **3. Film the lesson** — once per lesson | `/real-example-in-every-lesson` first, then `/human-screen-recordings` and `/record-until-the-result-is-visible` on the same take | the ready brief | `.../take-plan.md`, then `.../lesson.mp4` | the example passed the rubric, the plan is `approved` and rehearsed, and the MP4's own frames show the state before the action, the whole path, and the finished result |
| **4. Extract the states** — once per lesson | `/extract-lesson-states` | the locked MP4 | `.../states.json` | the array covers the film with no gaps and the validator is clean |

Use every skill. Do not skip one because the lesson "seems simple", and do not invent a parallel process. "Every skill" spans the course rather than a single reply: each skill is the gate for its own stage, and you do not open the next stage until the current gate passes.

Stage 1 runs once. Stages 2 to 4 repeat per lesson, in order, from scratch every time — last lesson's research is not this lesson's research.

## Weight: what is absolute, and what is yours

**Absolute.** Not negotiable by time pressure, by convenience, or by a user's impatience:

- The MP4 is the only source of truth for states. Not the input log, not a live screenshot, not your memory of the take.
- No narration, in the video or in the JSON.
- Every lesson is filmed 0% to 100% — creation, path, result. Never omit even 1% of the path, including as off-camera setup.
- Examples are never smoke tests.
- No lesson research on a `draft` syllabus. No filming without a `ready` brief. No recorder before an `approved` take plan.
- The status fields are the user's decision to make, never yours to flip.
- A completion claim without checked evidence is not a claim.

**Yours,** and you state the decision out loud so the user can reverse it: lesson order and titles, which live sources to trust, the shape of the example, how the take is paced, how the states name their regions.

How to tell them apart: **a rule with a validator behind it is absolute; everything else is judgment you have to be able to defend.**

## Validators

Run from the workspace root, and fix what they report rather than explaining it away.

```bash
python3 .cursor/skills/1-plan-the-course/build-a-course-syllabus/scripts/validate_syllabus.py courses/<slug>/syllabus.md
python3 .cursor/skills/2-research-the-lesson/research-the-current-lesson/scripts/validate_brief.py <lesson-dir>/brief.md
python3 .cursor/skills/3-film-the-lesson/real-example-in-every-lesson/scripts/validate_take_plan.py <lesson-dir>/take-plan.md
python3 .cursor/skills/3-film-the-lesson/record-until-the-result-is-visible/scripts/verify_take.py <lesson-dir>/lesson.mp4
python3 .cursor/skills/4-extract-states/extract-lesson-states/scripts/validate_states.py <lesson-dir>/states.json
python3 .cursor/skills/3-film-the-lesson/human-screen-recordings/scripts/human_input.py --selftest
```

## Stop and ask when

The subject is a product category rather than a course. A feature cannot be produced in this environment. Research contradicts a line the user already accepted. The example fails the rubric. Anything requires an account, a payment, or terms accepted.

Park the blocked item with the blocker named in the artifact that decides that work, carry on with everything that does not depend on it, and never walk through a blocker instead of around it.

## Where the skills live

Each stage folder under `.cursor/skills/` holds the skills for that stage. The folder is organizational: a skill's identity is the folder that holds its `SKILL.md`, so every skill is still invoked as `/its-own-name`.

- [1-plan-the-course/build-a-course-syllabus](.cursor/skills/1-plan-the-course/build-a-course-syllabus/SKILL.md)
- [2-research-the-lesson/research-the-current-lesson](.cursor/skills/2-research-the-lesson/research-the-current-lesson/SKILL.md)
- [3-film-the-lesson/real-example-in-every-lesson](.cursor/skills/3-film-the-lesson/real-example-in-every-lesson/SKILL.md)
- [3-film-the-lesson/human-screen-recordings](.cursor/skills/3-film-the-lesson/human-screen-recordings/SKILL.md)
- [3-film-the-lesson/record-until-the-result-is-visible](.cursor/skills/3-film-the-lesson/record-until-the-result-is-visible/SKILL.md)
- [4-extract-states/extract-lesson-states](.cursor/skills/4-extract-states/extract-lesson-states/SKILL.md)
