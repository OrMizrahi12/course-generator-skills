# Pedagogical context

Read this with the rubric, at step 2 of [SKILL.md](../SKILL.md). Criterion 5 —
"it fits this course" — cannot be judged against nothing, and the thing it is
judged against has to be written down rather than remembered.

## Contents

- The course pedagogy file
- Precedence
- When the user gives instructions in chat
- When there are no instructions
- What this file is not for

## The course pedagogy file

One per course, at `courses/<course-slug>/pedagogy.md`, written from
[assets/pedagogy-template.md](../assets/pedagogy-template.md).

It holds what a good example looks like **in this course specifically**: who is
watching, what they can already do, the tone and pace, the kinds of examples that
would be wrong here, and — most importantly — the instructions the user gave for
this course, quoted rather than paraphrased.

It exists because the same feature deserves different examples in different
courses. A course for people in their first hour and a course for power users are
served by opposite examples of the same command, and nothing about the feature
itself tells you which one you are making.

## Precedence

When these disagree, the earlier one wins:

1. **An explicit instruction from the user**, in this conversation or quoted in
   the pedagogy file. If the user said "no examples that need a paid account",
   that is not advice.
2. **The pedagogy file**, for anything the user established earlier in the course.
3. **The syllabus** — its audience, level, promise, and out-of-scope list.
4. **The rubric's defaults** in [example-rubric.md](example-rubric.md).
5. **Your own taste**, which outranks nothing.

Where an instruction conflicts with the repo-root `COURSE_AGENT.md`, that document
wins, and you say so plainly rather than quietly obeying the weaker rule.

## When the user gives instructions in chat

Instructions arrive in conversation, not in files. The moment the user says
something about how examples should work in this course, write it into
`courses/<course-slug>/pedagogy.md`, quoted, before you use it.

Two reasons this matters more than it sounds. An instruction that lives only in a
chat message is lost by the next lesson, so lesson 4 quietly violates what was
agreed at lesson 2. And an instruction you paraphrase becomes an instruction you
have edited — "keep examples short" is not "no example longer than three minutes".

Confirm the file with the user the first time you write it. After that, add to it
as instructions arrive.

## When there are no instructions

Derive the context from the syllabus — audience, level, promise, the project, the
out-of-scope list — and write that into the pedagogy file as a derivation, marked
as one, so the next lesson does not re-derive it differently.

Then tell the user, in one line, what you derived. That gives them a cheap moment
to correct it, which is far cheaper than discovering the mismatch after four
lessons are shot.

## What this file is not for

Not the shot list, not the click path, not the lesson's own example — those are
per lesson and live in the brief and the take plan. Not the syllabus's job either:
it holds the promise, the audience, and the spine.

This file holds only what a good example looks like here, so that criterion 5 has
something to be judged against.
