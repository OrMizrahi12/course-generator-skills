---
name: Build a course syllabus
description: >-
  Use when the user wants a new course or a syllabus. Ask a short intake first,
  then research live sources, then draft a high-level lesson spine together. Do
  not write per-lesson shot lists. Every lesson on the spine must be filmable 0%
  to 100% with a human example.
---
# Build a course syllabus

This skill builds a **syllabus**: direction, audience, and lesson order. It does not plan each lesson surgically (no click paths, no shot lists, no prompts). Those come later, one lesson at a time, under the recording skills.

The model will want to skip intake and emit a feature checklist from memory. That is the bug. Questions first, live research second, draft third.

## When this runs

The user asks for a new course, a syllabus, or "what should the lessons be". Run this skill before recording anything and before inventing lesson titles.

## 1. Intake (before research)

Ask a short set. Do not ask twenty questions. If only the user can know a thing, ask. Decide the rest.

Ask, in the user's language:

- What is the course about (product, feature area, or job)?
- How many lessons, or how long should the whole course feel?
- Who is it for, and what do they already know?
- What level should it reach (first hour, daily user, power user)?
- What is the delivery character (silent screen demo, live practice, product walkthrough)?
- What must be in, and what is out of scope?

If they already answered some of this in the conversation, do not re-ask. Fill only the gaps.

Do not start web research until the intake is enough to know audience, scope, and size.

## 2. Research (after intake, not before)

Research the **current** product and how people use it now. Do not build a syllabus from training memory or from a UI menu.

- Official current docs and changelog
- How real users talk about the job (what they are trying to get done)
- What is actually available here (connectors, UI, constraints) when that changes the spine

Keep sources. When you draft, you should be able to say where a lesson idea came from. If you cannot find a live source, say so. Do not invent a feature.

## 3. Draft the spine together

Output a syllabus, not a production plan:

- Course title and one-sentence promise to the viewer
- Audience and level, in one line
- Ordered lessons: number, title, what the viewer can do after it, why it comes after the previous one
- Explicitly out of scope

Invite the user to edit the draft. Do not treat the first list as final. Do not start recording until they accept the spine.

## Constraints from the other course skills

Every line on the spine must be a complete film later:

- 0% to 100% on camera (creation, path, result). No "overview" or "tour" lessons.
- A human example will be researched again when that lesson is recorded. The syllabus only has to make that possible: each lesson is one teachable feature or job, not a smoke test, not a pile of menus.
- If a proposed lesson cannot be filmed as one real worked example, it does not go on the spine. Split it or drop it.
- Sequence so that no lesson needs a feature the course has not taught yet, unless that feature is not part of the course.

## Do not

- Write per-lesson scripts, coordinates, or prompts here
- Invent lesson counts the user did not want
- Start from "list every button in the app"
- Record, or pick the human example for lesson N, until the syllabus is accepted and that lesson is the one being made
