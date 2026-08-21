# Where one state ends and the next begins

Read this while walking the video, at step 3 of [SKILL.md](../SKILL.md).

One rule, applied consistently: a new object starts when something **material**
changes on screen. Everything here is that rule at the boundaries where it gets
decided.

## Contents

- Material changes
- Not material
- The two failure shapes
- Continuous change
- Worked example

## Material changes

Each of these opens a new state:

- A panel, menu, dialog, or tab opens or closes.
- Text appears, finishes appearing, or is replaced.
- A list gains or loses a row, or an item moves to a different section.
- A selection or highlight moves to a different element.
- A spinner, progress bar, or busy label starts or stops.
- An icon changes what it asserts: filled instead of hollow, green instead of grey.
- The window under focus changes.

## Not material

None of these opens a new state:

- The pointer moving without arriving anywhere that changes the picture.
- A caret blinking.
- A clock or timer ticking in a status bar, unless the lesson is about it.
- Antialiasing, compression noise, or a one-frame flicker.
- A hover highlight that appears and disappears while the pointer passes over.

If you are unsure, ask what a narration writer would do differently. If the answer
is nothing, it is the same state.

## The two failure shapes

**Fragmentation.** One object per mouse twitch, or one per second. It makes the
file long, and it makes narration impossible: a line that needs four seconds of
picture now spans eleven objects, and nothing in the file says they belong
together.

**Collapse.** One object over a stretch that visibly changed twice. The narration
writer gets one description for two pictures, and whatever they write is wrong for
half of it. The tell is a `changed` string with an "and then" in it.

Between the two, prefer the boundary you can defend from two frames: extract the
frame before and the frame after, and see whether a stranger would call them the
same picture.

## Continuous change

Some stretches change every frame: text being typed, a log scrolling, a progress
bar filling, a page painting.

Treat a continuous stretch as **one state with its own start and end**, described
as the process it is — the command being typed into the prompt, the build log
scrolling, the page painting — and open the next state when it finishes. Do not
sample it into twenty objects, and do not fold it into the state before or after
it: for the narration, the process itself is usually the moment worth speaking
over.

Where it ends is where it stops changing, and that timestamp comes from frames, not
from an estimate.

## Worked example

A lesson opens on a terminal, a command is typed, it runs, and its output appears.
Four states, not fourteen:

| start | end | what is on screen | why the boundary is here |
|---|---|---|---|
| 0.000 | 2.100 | the prompt, empty, the working directory in the prompt string | the starting state, nothing has happened yet |
| 2.100 | 5.480 | the command appearing character by character after the prompt | typing is one continuous process |
| 5.480 | 6.910 | the command committed on its own line, no output yet | Enter was pressed and the picture is briefly stable |
| 6.910 | 11.400 | the full output, then the next prompt below it | the output is painted and the shell is idle again |

The pointer moved during all four and never opened a state of its own, because
nothing it did changed the picture.
