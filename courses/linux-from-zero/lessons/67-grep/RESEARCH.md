# Lesson 67 — Search inside files

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 68 here.

## Feature

`grep` prints the lines that contain a fixed phrase. Search the rent log for `paid`, then the hidden landlord note for `Sep`.

## What it is / is not

- It is: GNU grep 3.11 on papers this person wrote. Last `grep Sep .landlord.txt` holding `Call the landlord on 21 Sep before six.`
- It is not: `echo`. It is not a regular expression (next lesson). Do not invent a new file off-camera.

## Live sources (fetched this pass)

- GNU grep 3.11 `/usr/bin/grep`. Probe: `grep paid rent-log.txt` prints `21 Aug rent is paid.` exit 0. `grep Sep .landlord.txt` prints the 21 Sep call line. `grep nosuch rent-log.txt` prints nothing, exit 1.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Both papers already exist from lessons 36 and 39. The feature is the search, not creating the notes.

## Human job

Find the paid line in the rent log, then find the September call in the hidden landlord note. Without grep, they would reread the whole paper.

Candidates considered: (1) `grep hello` — smoke test. (2) grep only rent-log — misses the hidden note they already made. (3) paid then Sep. Picked (3).

## Done on screen

Fullscreen terminal. Last grep holds the landlord September line.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log or `.landlord.txt`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `cat rent-log.txt`, `grep paid rent-log.txt`, `cat .landlord.txt`, last `grep Sep .landlord.txt`.
