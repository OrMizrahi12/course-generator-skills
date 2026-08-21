# Choosing the human example

Read this at step 5 of [SKILL.md](../SKILL.md), after the material is mastered and
the path has been walked. Not before.

The example is the difference between a lesson that teaches a feature and a lesson
that demonstrates that the feature exists. It is chosen last because until you
know what the feature actually does, you cannot know what work genuinely needs it.

## Contents

- Inventory what is real here
- Generate three candidates
- The four tests
- The smoke-test blacklist
- Write it as one sentence
- Worked examples

## Inventory what is real here

Before inventing a job, list what actually exists in this environment that a job
could be about: real repositories, real files with real content, real data, real
connections, real accounts, real history.

Prefer a real artifact over a constructed one every time. A job performed on
something that already exists for its own reasons is authentic by default; a job
performed on a folder you created for the lesson has to work to look real, and
usually fails.

## Generate three candidates

Write three, not one. The first idea is almost always the feature's own
documentation example rephrased.

For each candidate: who wants it, why they want it today, and what they would do
instead if this feature did not exist.

That third question is the useful one. If the honest answer is "the same thing,
slightly slower", the candidate is weak and you now know it before filming.

## The four tests

Apply all four to each candidate, then pick the strongest survivor.

**1. Necessity.** Delete the feature. Does the job break? If the job still gets
done the same way, the example is dead. This is the test the other three depend
on.

**2. Finishability.** Can it complete on camera, 0% to 100%, in one take: the
object created, the path walked, the result visible? A job that needs a
fifteen-minute build in the middle is not finishable unless the wait is the
subject.

**3. Depth.** Would a practitioner recognize this as work, or as a course
exercise? The tell is the input: real work has messy, specific inputs, and
exercises have clean, round ones.

**4. Reproducibility.** Could a viewer do the same thing in their own
environment, changing only the specifics? An example that only works because of
something unusual here teaches nothing transferable.

## The smoke-test blacklist

These are invalid, always, regardless of how much easier they make the take:

- `echo` of anything, especially the lesson's own name
- `hello.txt`, `hello-a`, `hello-b`, `test.txt`, `foo`, `bar`
- a command whose only output is a confirmation that it ran
- a connection or server that stores a fake note and does nothing with it
- "reply with only this string"
- a file created solely so that the lesson has a file

If the example only proves the machinery is wired up, it is a smoke test wearing a
job's clothes.

## Write it as one sentence

One sentence, in the brief:

> A person wants **X** because **Y**, and this feature is required for X.

If you cannot fill in Y with something a person would actually care about, go back
to the candidates. If the sentence still reads as true after you delete the
feature, go back to test 1.

## Worked examples

| Feature | Dead example | Live example |
|---|---|---|
| A reusable command | A command that prints "it ran" | A command that opens a pull request from the current branch with the changelog entry filled in |
| Scoping a rule to files | A rule that says "be helpful" | A rule that stops the agent from touching generated files, proven on the folder where it kept doing it |
| Connecting a data source | A server that stores one note | Answering a question about real data that nobody could answer without the connection |
| A worktree, a branch, a stash | Creating one and deleting it | Carrying an urgent fix while a half-finished change stays exactly where it was |

The pattern: the live column names an outcome someone wanted before the course
existed. The dead column names the feature with a costume on.
