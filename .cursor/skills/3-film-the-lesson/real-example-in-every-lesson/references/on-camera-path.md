# The on-camera path

Read this at step 3 of [SKILL.md](../SKILL.md), while writing the take plan.

The rule is one sentence: every step a new user needs is in the film, including
how the lesson object came to exist. Everything below is that sentence applied to
the places it gets bent.

## Contents

- The feature is not the last verb
- Setup versus the lesson object
- Writing the steps
- Invalid takes
- When the take misses

## The feature is not the last verb

A lesson teaches a feature, not the final gesture in its title.

- "Custom command" means where commands live, creating one, what goes in it,
  saving it, and then running it. Not only the run.
- "Pin" means the pinning gesture and the item appearing under Pinned. Not a hold
  on an already-pinned row.
- "Connect a data source" means creating or connecting it in the interface, then
  using it for something.

A lesson renamed "Run X" or "Use X" is not permission to hide how X came to
exist. If a viewer would ask "wait, where did that come from?", the take is dead.

## Setup versus the lesson object

**May be off camera:** launching the application, opening the window, a signed-in
session, an installed tool, a machine that exists. Things the lesson makes no
claim about.

**May not be off camera:** the object the lesson exists to show being created —
the command, the skill, the rule, the automation, the connection, the branch, the
file, the state the lesson asserts. Not with a shell, not with a pre-written file,
not with an API call, not with an earlier unfilmed click.

The one exception is a prior **shipped** lesson in this same course that filmed
the creation. Name that lesson when you rely on it. The first lesson of a course
has no prior lesson, so it builds whatever it claims, and that is correct rather
than a problem to design away.

If the object already exists when you sit down to film, use the reset from the
brief and confirm it is gone before the recorder starts.

## Writing the steps

- One numbered step per thing the viewer must see happen, in the order it happens.
- Every object in the brief's `## Must be created on camera` gets a step number,
  and that number comes before the step that uses it.
- The plan ends with the result on screen and a hold long enough to read it.
- Mid-flow interruptions the brief recorded — approvals, confirmations, sign-ins —
  are steps, not surprises.
- Include the reset, copied from the brief, so a missed take is recoverable
  without improvising.

A plan whose first step is the payoff is an automatic fail, and it is the most
common shape a rushed plan takes.

## Invalid takes

Delete these. Do not send them, do not explain them.

- Opening a panel, typing a command, or hovering something with no finished output
- A hold on a pre-completed state — already created, already saved, already
  connected — where the viewer never sees how it was done
- The lesson object created off camera, with only its use or its result filmed
- Any required step skipped as "setup" or "we already did that"
- A smoke-test example: `echo`, hello files, a dummy server, "reply with only this"
- An example that never passed the rubric
- Last frames that still say Waiting, Working, Synthesizing, or show a spinner
- A live screenshot, a log line, or a self-set done flag used as proof

## When the take misses

Wrong click, a menu closed, a ceiling hit, an unexpected dialog: delete the take,
run the reset from the brief, confirm the state is back to before the object
existed, and record the whole path again from 0%.

Do not finish the missing step off camera and ship a result-only clip. Do not
splice. Do not keep a take because reshooting is expensive — that cost is paid
once, and a broken lesson is paid for by every viewer.

A genuine failure that happens on camera is different, and often worth keeping:
if the thing fails the way it really fails and the film shows the fix, that is
teaching. What is forbidden is a film that hides the failure and presents a path
nobody walked.
