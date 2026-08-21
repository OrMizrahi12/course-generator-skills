# Establishing best practice

Read this at step 4 of [SKILL.md](../SKILL.md).

A path that works is not automatically the path to teach. This step decides which
path the lesson shows, on evidence, and records the one it refuses so a later
stage cannot quietly optimize it back in.

## Contents

- Three candidate paths
- Choosing between them
- Name the shortcut you refuse
- The verification the viewer performs
- Deprecated paths
- Order traps

## Three candidate paths

For the feature this lesson teaches, find all three. They are frequently
different, and the difference is the whole content of this step.

1. **The recommended path.** What the current official material tells you to do.
2. **The shortest path that works.** The fewest steps that reach the result,
   usually skipping creation, configuration, or verification.
3. **The path practitioners actually use.** What people who do this daily do —
   found in issue threads, write-ups, and answers to real problems, not in the
   marketing page.

Each needs a live source. If you cannot find the third one, say so; do not invent
a practitioner consensus that you have not seen.

## Choosing between them

Teach the path that satisfies all three of these, and prefer the practitioner path
when they conflict:

- **It reveals how the thing is made.** The viewer sees the object come into
  existence, not a finished object being used.
- **It generalizes.** The viewer could apply it to their own case, not only to the
  exact case on screen.
- **It survives being wrong.** If the viewer mistypes or the environment differs,
  the path they learned gives them something to check rather than a dead end.

A path chosen because it is easier to film is the wrong reason, and it is the
reason that shows up most often when the take is hard.

## Name the shortcut you refuse

Write down, in the brief, the shortcut you are not showing and what it costs. For
example: the wizard that generates the file, when the lesson is about what is in
the file; or the pre-built template, when the lesson is about building it.

This matters because the shortcut is genuinely attractive under time pressure. A
refusal with a stated reason survives; an unstated preference gets reversed by
whoever is holding the recorder at two in the morning.

## The verification the viewer performs

Establish the check a practitioner runs afterwards to know it worked: the command
they run, the panel they open, the file they look at.

This becomes the visible end of the lesson, so it has to be something the camera
can see. "It is now configured" is not a verification. "The setting appears in the
list, and the run picks it up" is.

## Deprecated paths

Check explicitly whether any step you are about to teach has been replaced. The
changelog is the source, not the docs page, which often keeps working examples of
the old way for months.

Teaching a dead path is worse than teaching nothing: the viewer follows it, it
fails, and they cannot tell whether they made the mistake or the course did.

Write every dead path you found into the brief, with its replacement. If you
looked and found none, write that, and where you looked.

## Order traps

Some sequences only work one way round: create before connect, save before run,
select before apply. If the order matters, establish why, so the lesson teaches
the order rather than accidentally demonstrating it.

An order trap discovered during a take is a deleted take. Discovered here, it is
one line in the brief.
