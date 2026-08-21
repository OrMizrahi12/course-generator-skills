# The mastery bar

Read this at step 2 of [SKILL.md](../SKILL.md). It defines when you know the
material well enough to teach it.

The bar is not "I read the docs". It is: **a practitioner could interrogate you
about this feature and you would not have to look anything up.** Everything below
has to be answerable from live sources, not from training memory.

## Contents

- The nine questions
- Where the answers live
- The teach-back test
- When to stop researching
- What insufficient mastery looks like on camera

## The nine questions

Answer all nine in writing. An answer you cannot write is an answer you do not
have.

1. **What is it, in one sentence?** No marketing words, no "powerful" or
   "seamless". A sentence that would survive a practitioner reading it.
2. **What is it not?** The nearest thing it gets mistaken for, and the line
   between them. This single answer prevents most confused lessons.
3. **What is it called now, and where does it live?** The current name, the
   current location, and what it replaced. Names drift, and teaching last year's
   name teaches a dead path.
4. **What actually happens one level below the gesture?** What file, record,
   setting, or state changes when the user does this. A lesson that teaches only
   the gesture cannot survive the first deviation, because the viewer has no model
   of what they are affecting.
5. **What are the limits and defaults?** Sizes, counts, timeouts, scoping, what
   is on out of the box, what needs a paid tier or a flag. These are the facts
   that decide whether the example you are about to pick is even possible.
6. **What do first-time users get wrong?** Three specific mistakes and the
   correct move for each. Not "they forget to save" — the real ones, from where
   people report them.
7. **What does failure look like on screen?** The actual error, the silent
   no-op, the spinner that never resolves — and why it happens. A silent course
   cannot narrate its way out of a failure, so you have to know the shape of it
   before you meet it in a take.
8. **What breaks if you skip the step the shortcut skips?** There is always a
   shortcut. Knowing what it costs is what lets you refuse it in step 4 with a
   reason instead of a preference.
9. **How does a user verify it worked?** The check a practitioner performs
   afterwards. This becomes the visible end of the lesson.

## Where the answers live

In roughly this order, and no answer is complete without a URL or an observed
state in this environment:

- **Current official docs** — questions 1, 3, 5.
- **Release notes and changelog, newest first** — question 3, and the only
  reliable way to catch a rename or a replacement.
- **The live product in this environment** — questions 4, 7, 9. The screen
  outranks the docs when they disagree.
- **Issue trackers, forums, and support threads** — questions 6 and 7. This is
  where real mistakes and real failure modes are written down; docs describe the
  happy path.
- **Nothing from another model's summary.** A page you fetched or a state you
  observed. Not a search snippet, not a recollection.

## The teach-back test

Write five sentences that explain the feature to a skeptical practitioner who
does not want to be sold anything. No hedging, no "generally", no "should".

Read them back. If any sentence would make that person ask "wait, how does that
actually work?" and you would have to go look, you are not at the bar yet. Go
back to whichever of the nine questions produced the hedge.

## When to stop researching

Stop when new sources stop changing your answers.

Not when you have enough for a script — that threshold arrives long before
mastery and it feels identical from the inside. If the last two sources you read
told you nothing you had not already written down, you are done. If either of
them surprised you, keep going.

## What insufficient mastery looks like on camera

Recognize these in yourself before the recorder starts, because they are obvious
to a viewer and expensive to fix later:

- The path is followed correctly but nothing in the lesson explains what it
  produced, because you do not know (question 4).
- The example turns out to be impossible partway through, because a limit was
  never checked (question 5).
- A dialog appears that was not in the docs and the take stalls (question 7).
- The lesson ends without showing that it worked, because the verification step
  was never established (question 9).
