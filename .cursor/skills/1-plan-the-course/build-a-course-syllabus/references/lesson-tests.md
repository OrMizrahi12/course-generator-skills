# The five lesson tests

Read this while drafting the spine. Load it at step 4 of [SKILL.md](../SKILL.md).

Apply all five tests to each line as you write it. A line that fails one gets
rewritten, split, or dropped now — a bad spine line cannot be fixed by the
camera.

## Contents

- Test 1: Competence
- Test 2: Necessity
- Test 3: Filmable in one take
- Test 4: Visible result
- Test 5: Order
- Sizing: split and merge
- Banned lesson shapes and their rewrites

## Test 1: Competence

Name what the viewer can **do** after the lesson that they could not do before.
A verb they perform, not a state of mind.

The `Can do after` line may not start with understand, know, learn, be familiar
with, be aware of, appreciate, or grasp. Those describe an audience feeling, and
no camera can film them.

| Fails | Passes |
|---|---|
| Understand how skills work | Write a skill and see the agent invoke it |
| Know what a rule is for | Scope a rule to one folder and watch it apply there |
| Learn about branching | Recover a commit from a branch they deleted by mistake |

## Test 2: Necessity

There must be a real job where this feature is required. If you can delete the
feature and the job still gets done the same way, the lesson has no reason to
exist and stage 2 will be forced into a smoke test.

Ask: what breaks for this person without the feature? If the answer is
"nothing", either the lesson is a settings tour, or the job is wrong.

## Test 3: Filmable in one take

One continuous silent recording must be able to show creation, path, and result:
0% to 100%, nothing off camera.

That bounds a lesson:

- One thing gets created, not three unrelated ones.
- Every prerequisite is either already taught earlier in the course or trivially
  visible in the same take.
- The work fits a take a viewer will actually sit through — roughly two to six
  minutes of screen for a silent lesson.

If the line needs two creations that do not depend on each other, it is two
lessons. If it needs a fifteen-minute wait in the middle, either the wait is the
subject or the example is wrong.

## Test 4: Visible result

The lesson has an end state a stranger can see on the last frames: a file that
exists, a reply that finished, a page that loaded, a check that turned green.

There is no narration in these courses. Anything the viewer cannot see, the
viewer does not get. A lesson whose payoff is an internal state change — "the
setting is now on" with nothing observable following it — is not a lesson.

## Test 5: Order

Everything a lesson depends on is either taught in an earlier lesson or is
outside the course and listed as assumed knowledge.

Record it on the line: `Depends on: none` or `Depends on: Lesson 2`. A dependency
on a later lesson is an error the validator rejects, and it is the defect most
likely to survive a casual read of the spine.

## Sizing: split and merge

- **Split** when the line contains two independent creations, two features that
  do not need each other, or a path so long it cannot finish in one take.
- **Merge** when two lines teach the same gesture on different objects, or when
  one line only exists as setup for the next and produces no visible result of
  its own.
- Honor the count the user asked for. If the material genuinely does not fit,
  say so and propose the number you would use, with what each extra lesson buys.
- Do not pad to reach a round number. Six lessons that each teach something are
  better than ten where four are tours.

## Banned lesson shapes and their rewrites

These are the shapes that survive review and then fail at film time.

| Banned shape | Why it fails | Rewrite |
|---|---|---|
| Overview of the Agents Window | Nothing is created, nothing finishes | Run one real task in the Agents Window and read its result |
| Tour of the settings panel | No competence, no visible result | Scope a rule with `paths` and prove it fires on one folder only |
| Introduction to skills | A topic, not a job | Write a skill that opens a PR from the current branch |
| Tips and tricks | No spine, no dependency, no end state | Pick the one trick with a real job and film that job |
| Everything you can do with MCP | Unfilmable in one take | Connect one MCP server and use it to answer a real question |
| Getting started | Usually a tour wearing a verb | Name the first real thing the viewer produces, and film that |
| Understanding merge conflicts | Feeling, not doing | Resolve a real conflict in a repo that already has one |

The pattern behind all of them: a lesson is a **job someone does**, named as the
thing they end up with. If the title could be a chapter in a manual, rewrite it
until it is something a person finished.
