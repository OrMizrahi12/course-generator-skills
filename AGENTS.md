# Course Generator

Record any course as silent screen lessons. Each lesson is an MP4 plus a timed states array.

Chat with the user in Hebrew. Skills, instructions, course production, on-screen text, and artifacts are English.

## Precedence

`COURSE_AGENT.md` is the constitution, and it is always in force — read it before the first decision, not after the work. It governs judgment; the skills govern procedure. On any conflict between a skill and that document, it wins.

What it decides, so you know when you need it: what may be shown to a learner and what may not, how far to degrade when the real thing is unavailable and how to disclose it, what counts as evidence that you are done.

## The pipeline

| Stage | Skill | Reads | Writes | The next stage opens when |
|---|---|---|---|---|
| **1. Plan the course** — once per course | `/build-a-course-syllabus` | the user | `courses/<slug>/syllabus.md` | the user has accepted the spine and `status: accepted` |
| **2. Research the lesson** — once per lesson | `/research-the-current-lesson` | the accepted syllabus | `.../lessons/<NN>-<slug>/brief.md` | the validator is clean and `status: ready` |
| **3. Film the lesson** — once per lesson | `/real-example-in-every-lesson` first, then `/human-screen-recordings` and `/record-until-the-result-is-visible` on the same take | the ready brief | `.../take-plan.md`, then `.../lesson.mp4` | the example passed the rubric, the plan is `approved` and rehearsed, and the MP4's own frames show the state before the action, the whole path, and the finished result |
| **4. Extract the states** — once per lesson | `/extract-lesson-states` | the locked MP4 | `.../states.json` | the array covers the film with no gaps and the validator is clean |

**Rehearsed** means the plan was walked end to end off camera, in the environment you will film in, and the state it created was reset. The MP4 is **locked** once that stage-3 gate passes, and the locked take is the one that ships. A re-shoot means it was never locked: the old take and any states extracted from it go together. `states.json` is the handoff out of this repository — the narration is written from it, elsewhere, by something that never sees the video.

Use every skill. Do not skip one because the lesson "seems simple", and do not invent a parallel process.

Each lesson runs stages 2 to 4 from scratch — last lesson's research is not this lesson's research.

## Weight: what is absolute, and what is yours

**Absolute.** Not negotiable by time pressure, by convenience, or by a user's impatience:

- The MP4 is the only source of truth for states. Not the input log, not a live screenshot, not your memory of the take.
- No narration, in the video or in the JSON.
- Every lesson is filmed 0% to 100% — creation, path, result. Never omit even 1% of the path, including as off-camera setup.
- Examples are never smoke tests.
- No lesson research on a `draft` syllabus. No filming without a `ready` brief. No recorder before an `approved` take plan.
- The status fields follow the user's decision, never your own. They say yes and you write it down; you never supply the yes.
- The subject, the audience, what must be covered, and how many lessons there are belong to the user. Ask; do not invent them.
- A completion claim without checked evidence is not a claim.

**Yours,** and you state the decision out loud so the user can reverse it: lesson order and titles, which live sources to trust, the shape of the example, how the take is paced, how the states name their regions.

The test runs one way only: **every rule with a validator behind it is absolute.** The list above is not limited to those, and anything on neither list is judgment you have to be able to defend.

## Validators

One per artifact, run from the workspace root at the gate that artifact opens. Fix what they report rather than explaining it away.

```bash
python3 .cursor/skills/1-plan-the-course/build-a-course-syllabus/scripts/validate_syllabus.py courses/<slug>/syllabus.md
python3 .cursor/skills/2-research-the-lesson/research-the-current-lesson/scripts/validate_brief.py <lesson-dir>/brief.md
python3 .cursor/skills/3-film-the-lesson/real-example-in-every-lesson/scripts/validate_take_plan.py <lesson-dir>/take-plan.md
python3 .cursor/skills/3-film-the-lesson/record-until-the-result-is-visible/scripts/verify_take.py <lesson-dir>/lesson.mp4
python3 .cursor/skills/4-extract-states/extract-lesson-states/scripts/validate_states.py <lesson-dir>/states.json
```

The input tooling has its own check, which needs no display and no recorder. Run it before the first take on a machine, and after any change to it:

```bash
python3 .cursor/skills/3-film-the-lesson/human-screen-recordings/scripts/human_input.py --selftest
```

## Stop and ask when

The subject is a product category rather than a course. A feature cannot be produced in this environment. Research contradicts a line the user already accepted. The example fails the rubric. Anything requires an account, a payment, or terms accepted.

Park the blocked item with the blocker named in the artifact that decides that work — the lesson's brief once it has one, the syllabus while the lesson is still only a line on the spine — and carry on with everything that does not depend on it.

## Where the skills live

Stage folders are organizational: a skill's identity is the folder holding its `SKILL.md`, so each is invoked as `/its-own-name`.

- [1-plan-the-course/build-a-course-syllabus](.cursor/skills/1-plan-the-course/build-a-course-syllabus/SKILL.md)
- [2-research-the-lesson/research-the-current-lesson](.cursor/skills/2-research-the-lesson/research-the-current-lesson/SKILL.md)
- [3-film-the-lesson/real-example-in-every-lesson](.cursor/skills/3-film-the-lesson/real-example-in-every-lesson/SKILL.md)
- [3-film-the-lesson/human-screen-recordings](.cursor/skills/3-film-the-lesson/human-screen-recordings/SKILL.md)
- [3-film-the-lesson/record-until-the-result-is-visible](.cursor/skills/3-film-the-lesson/record-until-the-result-is-visible/SKILL.md)
- [4-extract-states/extract-lesson-states](.cursor/skills/4-extract-states/extract-lesson-states/SKILL.md)
