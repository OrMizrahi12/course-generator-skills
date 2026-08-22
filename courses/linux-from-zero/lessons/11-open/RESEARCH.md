# Lesson 11 research brief

- **Lesson:** 11 — See why Linux is open
- **After:** After the four freedoms picture: open a real GPL text shipped with a GNU tool on this disk
- **Audience:** Zero computer background; picture-first. Act II.

## Feature

FSF / GNU: **free software is liberty, not price** — four essential freedoms (0 run, 1 study/change, 2 redistribute copies, 3 distribute modified copies). Open is a rule about copies, not a vibe. This lesson shows those four, then opens the GPL that Debian/Ubuntu actually ships at `/usr/share/common-licenses/GPL-3` (the same license `ls --version` pointed at).

It is **not** “Linux vs Windows vendors” (lesson 12), not compiling from source (lesson 80).

## Human job

A person heard “Linux is free/open.” They will think that means no invoice. They need the four-freedoms picture, then the GPL file on **this** disk, because that file is the rule that shipped with GNU coreutils — not a poster, not a website.

If you only show a logo, open stays a vibe. If you paste license text, the viewer never sees where it lives.

## Done on screen

1. HyperFrames: Stallman; a photocopier (copies); Heckert GNU head; four numbered freedoms.
2. Terminal 19pt: `ls /usr/share/common-licenses` lists `GPL-3`; `head -n 20 /usr/share/common-licenses/GPL-3` shows GNU GPL Version 3 and “freedom, not price.” Last frames hold that preamble.

## Sources used

- FSF / GNU, *What is free software?* — four essential freedoms; free as in speech, not beer
- FSF four-freedoms handout — Run / Study / Share / Change
- This host: `/usr/share/common-licenses/GPL-3` (35,149 bytes); `GPL` symlink → `GPL-3`; coreutils copyright points at the same license
- gnu.org HTML still 403; definition from FSF/GNU archive cited above
- Wikimedia: Stallman at LibrePlanet 2019; File:Photocopier.jpg; Heckert GNU white

## Must be created on camera

Both commands typed. Do not paste GPL text.

## Terminal font

1.75× default (JetBrains Mono 19).
