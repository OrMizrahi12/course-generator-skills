# Lesson 72 — Rewrite a file with sed

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 73 here.

## Feature

GNU sed 4.9 `s/Sep/Oct/` prints a rewritten stream of `rent-log.txt`. The file on disk still says Sep. The substitution is the stream, not nano.

## What it is / is not

- It is: one `s///` on the rent due line. Last `sed 's/Sep/Oct/' rent-log.txt` holds `Next due 21 Oct.` while a prior `cat` still showed Sep.
- It is not: `echo`. It is not `sed -i` on the workshop notes (that would break the matching draft). It is not awk (next lesson) or nano (lesson 74). Do not rewrite `rent-log.txt`.

## Live sources (fetched this pass)

- `sed --version`: GNU sed 4.9 `/usr/bin/sed`. No local man page. gnu.org sed manual 403 this pass. man7.org sed(1): “sed - stream editor for filtering and transforming text.” `s/regexp/replacement/` replaces the matched portion.
- Live: `sed 's/Sep/Oct/' rent-log.txt` prints `Next due 21 Oct.` Third line. `cat rent-log.txt` still `Next due 21 Sep.` `sed -n 's/Sep/Oct/p'` prints only the changed line.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- `rent-log.txt` already exists from lesson 36. Feature is rewriting the due month on the stream.

## Human job

Change Sep to Oct on the due line without touching the saved note.

Candidates considered: (1) `sed -i` on rent-log — destroys the original. (2) sed on passwd — needs a colon. (3) cat the note, sed Sep→Oct, last the Oct stream with Sep still above. Picked (3). Without sed the due month cannot change.

## Done on screen

Fullscreen terminal at `linux-workshop $`. Last `sed 's/Sep/Oct/' rent-log.txt` holding `Next due 21 Oct.`

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not `sed -i`. Do not rewrite `rent-log.txt` or `sep-due-draft.txt`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `cat rent-log.txt`, last `sed 's/Sep/Oct/' rent-log.txt`.
