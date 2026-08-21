# Course Generator skills

Cursor skills for recording any course as silent screen lessons.

Skills live under `.cursor/skills/`, grouped into the production stage they belong to. The stage folder is organizational; a skill's identity is the folder that holds its `SKILL.md`, so `build-a-course-syllabus` is still `/build-a-course-syllabus`. Clone this repo, or copy `.cursor/skills/` into `~/.cursor/skills/`.

## Skills

- `1-plan-the-course/build-a-course-syllabus` — intake, live research, and the accepted spine, written to `courses/<course-slug>/syllabus.md`
- `2-research-the-lesson/research-the-current-lesson` — master one lesson to teaching depth, operate it live, then write `courses/<course-slug>/lessons/<NN>-<lesson-slug>/brief.md`
- `3-film-the-lesson/real-example-in-every-lesson` — judge the example against the course's pedagogical bar, then hold the film to 0% to 100% with the result in the last frames
- `3-film-the-lesson/human-screen-recordings` — ballistic mouse, burst typing and clicked scrolling, with a working injector for Linux X11 and Windows
- `3-film-the-lesson/record-until-the-result-is-visible` — the whole arc on camera: the state before the action, the path, and the finished result in the MP4's own last frames
- `extract-lesson-states` — timed on-screen states from the locked MP4, no narration
