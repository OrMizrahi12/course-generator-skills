# Course Generator skills

Cursor skills for recording any course as silent screen lessons.

Skills live under `.cursor/skills/`, grouped into the production stage they belong to. The stage folder is organizational; a skill's identity is the folder that holds its `SKILL.md`, so `build-a-course-syllabus` is still `/build-a-course-syllabus`. Clone this repo, or copy `.cursor/skills/` into `~/.cursor/skills/`.

## Skills

- `human-screen-recordings` — ballistic mouse and burst typing
- `record-until-the-result-is-visible` — do not stop until the MP4 last frames show the result
- `real-example-in-every-lesson` — 0% to 100% on camera, no smoke-test examples
- `1-plan-the-course/build-a-course-syllabus` — intake, live research, and the accepted spine, written to `courses/<course-slug>/syllabus.md`
- `2-research-the-lesson/research-the-current-lesson` — master one lesson to teaching depth, operate it live, then write `courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md`
- `extract-lesson-states` — timed on-screen states from the locked MP4, no narration
