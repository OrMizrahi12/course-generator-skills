# The example rubric

Read this at step 2 of [SKILL.md](../SKILL.md), before you judge anything.

Five criteria. All five have to pass. The example was chosen in stage 2 by someone
who had just mastered the material — which is exactly the position from which an
example can be technically perfect and pedagogically poor, because everything
looks obvious once you understand it.

## Contents

- How to score
- 1. Clear
- 2. Interesting
- 3. Relatable
- 4. It carries the message
- 5. It fits this course
- Worked pairs
- When to send it back

## How to score

For each criterion, write one sentence of evidence into the take plan's
`## Example verdict`. Evidence means something about this example, not a
restatement of the criterion.

- Not evidence: "Clear: yes, the example is easy to follow."
- Evidence: "Clear: the only unfamiliar thing on screen is the command being
  taught; the project, the file, and the error were all established in lesson 1."

A criterion you cannot evidence is a criterion that fails. Judge as the viewer,
not as the person who did the research.

## 1. Clear

**Test:** watch the example in your head with the sound off and nothing explained.
Can a viewer follow every step and know, at the end, what happened?

Silence is the constraint that makes this hard. Anything the picture does not
carry is lost, so the example must not depend on knowledge the course has not
taught, on off-screen context, or on the viewer inferring intent from a command
they have never seen.

**Failure signatures:** more than one new thing happening at once; a step whose
purpose only makes sense after the next three steps; names on screen
(`x`, `tmp2`, `thing-final`) that carry no meaning; an outcome the viewer has to
be told about because they cannot see it.

## 2. Interesting

**Test:** would a viewer want to see how this ends, before knowing it is a lesson?

Interest here is not entertainment. It comes from a real stake: something is
broken, something is blocked, something is about to be lost, or something tedious
is about to become fast. A lesson with no stake is a demonstration, and viewers
stop watching demonstrations.

**Failure signatures:** nothing is at risk; the outcome is a confirmation message;
the work would not have been done if nobody were filming; the interesting part
happens off screen and only its result is shown.

## 3. Relatable

**Test:** name the person who has had this exact problem. If the answer is "a
learner in this course", it fails.

The viewer has to see themselves in the situation. That means the setup is
ordinary — the interruption, the review, the mistake, the deadline — rather than
exotic, and the inputs look like things people actually have rather than things
made for a lesson.

**Failure signatures:** a scenario that requires an unusual setup to make sense;
a job invented to give the feature something to do; inputs that are round,
clean, and fictional where real ones are messy.

## 4. It carries the message

**Test:** delete the feature from the example. Does something visibly break or
become worse on screen? And can a stranger, watching only the film, say what the
feature made possible?

This is the criterion that separates an example that teaches from one that merely
uses. The feature has to be the reason the outcome happens, and the outcome has to
show it. If the viewer needs the title of the lesson to know what they just
watched, the example is not carrying the message.

**Failure signatures:** the feature is one interchangeable step among many; the
same outcome is reachable without it and nothing in the film says otherwise; the
payoff is a state change nobody can see; the film would look identical if a
different feature had been used.

## 5. It fits this course

**Test:** read the course's pedagogical context and the user's instructions, then
ask whether this example belongs to this course rather than to a generic one.

Check the audience and level from the syllabus, the lessons already shipped, and
anything the user asked for explicitly. Precedence and where those instructions
live are in [pedagogical-context.md](pedagogical-context.md).

**Failure signatures:** an example above the level the syllabus promised, or below
it; one that depends on a feature a later lesson teaches; one that ignores an
explicit instruction from the user; one that would fit any course about anything.

## Worked pairs

| Feature | Fails, and why | Passes |
|---|---|---|
| A second checkout of a repository | Create one, list it, remove it — clear but no stake and no message | A colleague's branch has to be reviewed and run while a half-written refactor stays untouched; switching branches instead visibly breaks her tests |
| A reusable command | A command that prints a confirmation — no stake, no message | A command that opens the pull request with the changelog entry already filled in, on a branch that is actually ready |
| Scoping a rule to files | A rule saying "be helpful" — unclear and unmeasurable | A rule that stops an agent from editing generated files, filmed on the folder where it kept doing exactly that |
| Connecting a data source | A server that stores one note — no relatable job | Answering a question the team asks weekly, which nobody could answer without the connection |

The pattern in the passing column: someone wanted the outcome before the course
existed, and the film shows the feature being the reason they got it.

## When to send it back

Say which criterion failed, in one sentence, with the evidence you could not
write. Then hand it back to `/research-the-current-lesson`.

Do not repair the example yourself. Choosing an example requires the material
mastery that stage 2 has and this stage does not, and an example patched at film
time is how a course ends up with a lesson that works on camera and teaches
nothing.

Sending it back is cheap. A shot lesson that had to be rebuilt afterwards is not.
