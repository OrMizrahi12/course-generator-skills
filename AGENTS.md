# Course Generator

Record any course as silent screen lessons. Each lesson is an MP4 plus a states JSON array.

Chat with the user in Hebrew. Skills, instructions, course production, on-screen prompts, and JSON are English.

Use every skill below. Do not skip one because the lesson "seems simple". Do not invent a parallel process.

## Skill order (required)

1. **New course** — [Build a course syllabus](.cursor/skills/1-plan-the-course/build-a-course-syllabus/SKILL.md). Intake first, then live research, then a high-level spine, written to `courses/<course-slug>/syllabus.md` and accepted by the user. Do not write per-lesson shot lists here.
2. **Before each lesson** — [Research the current lesson](.cursor/skills/research-the-current-lesson/SKILL.md). Lock onto that lesson only. Master the live material, then pick the human example.
3. **Film** — all three, together:
   - [Human screen recordings](.cursor/skills/human-screen-recordings/SKILL.md)
   - [Real example in every lesson](.cursor/skills/real-example-in-every-lesson/SKILL.md)
   - [Record until the result is visible](.cursor/skills/record-until-the-result-is-visible/SKILL.md)
4. **After the MP4 is locked** — [Extract lesson states](.cursor/skills/extract-lesson-states/SKILL.md). Timed on-screen states from the frames only.
5. COURSE_AGENT.md it the GOD

## Hard rules

- The MP4 is the only source of truth for states.
- No narration in the video or in the JSON.
- Every lesson is filmed 0% to 100%: creation, path, and result. Never omit even 1% of the path, including as off-camera setup.
- Examples are never smoke tests.
