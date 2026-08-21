# Research for the syllabus

Read this before your first search. Load it at step 2 of
[SKILL.md](../SKILL.md).

This is course-level research: what exists, what it is called now, and which
jobs people actually use it for. Lesson-level research — the exact click path
and the human example — belongs to stage 2 and is a different skill. Stop at the
line where a lesson brief would begin.

## Contents

- Source order
- What counts as a source
- Reading the live surface
- Capability probe
- The source ledger
- Hard rules
- When research is enough

## Source order

1. **Current official docs** for the feature area. They define the vocabulary
   the course must use.
2. **Release notes or changelog**, newest first. This is where renames,
   replacements, and deprecations live — the single most common way a
   memory-built syllabus goes stale.
3. **How practitioners describe the job.** Forum posts, issues, and write-ups
   tell you what people are trying to get done, which is what a lesson is
   actually about.
4. **The live surface in this environment** — see below.

## What counts as a source

A URL you fetched during this session, or a UI state you observed in this
environment during this session.

Not a source: your recollection of the docs, a plausible feature name, a blog
post whose date you cannot establish, or another model's summary.

## Reading the live surface

Docs lag shipping. Where the docs and the live product disagree, the live
product wins, and you note the disagreement in the ledger so the lesson does not
teach a dead path.

Check, for each candidate feature: the current name, where it lives now, what it
replaced, and whether it is default-on, flagged, or paid.

## Capability probe

Run this before a feature becomes a lesson. It answers one question: can this
lesson be produced here, all the way to a visible result?

1. **Exists here** — the tool, surface, or command is actually present in this
   environment, not just in the docs.
2. **Reachable** — any account, tier, connector, key, or network access it needs
   is available, or can be obtained. Name the blocker if not.
3. **Finishes** — the work it does can complete on camera, and its output is
   something a viewer sees on screen rather than something you assert.
4. **Resettable** — the state the lesson creates can be undone, so creation can
   be filmed from zero rather than found already done.

A feature that fails 1 or 2 is not a lesson until the blocker is resolved. A
feature that fails 3 is not a lesson at all in a silent course. A feature that
fails 4 needs the reset method noted now, before stage 2 discovers it at film
time.

Probe by looking, not by reasoning. Opening the surface and reading what is
there beats any inference from the docs. Probing is off-camera work and does not
count as filming — but do not create the object a lesson must show being
created.

## The source ledger

Every syllabus carries its sources, so stage 2 starts from evidence instead of
repeating this work:

```
- https://example.com/docs/feature — established the current name and where it lives
- https://example.com/changelog — established that it replaced the old panel
```

Each lesson also lists the sources behind that specific line. Every URL on a
lesson line must appear in the ledger; the validator enforces it.

## Hard rules

- No feature on the spine without a live source. No exceptions for features you
  are sure about.
- Never invent a feature, a menu name, or a limit. If you cannot confirm it,
  say so in the chat and leave it off.
- Do not plan around a feature you only saw announced. Shipped and reachable, or
  not on the spine.
- Keep the user's vocabulary where it is correct and the product's vocabulary
  where they differ; the artifact uses the product's current names.

## When research is enough

You can state, for every line on the spine: the feature, its current name, one
live source, the job a person does with it, and the fact that it can be produced
here. Nothing more is needed at this stage, and less is not enough.
