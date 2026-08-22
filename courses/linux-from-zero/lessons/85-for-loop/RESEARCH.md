# Lesson 85 — Loop over real files

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 86 here.

## Feature

A `for` loop walks `papers/*.txt` (three real receipt names, including a space). Each basename is appended to `receipt-loop.txt`. Last `cat receipt-loop.txt` holds the three names.

## What it is / is not

- It is: `for NAME in WORDS; do COMMANDS; done` doing useful work on three real files.
- It is not: `echo` as the whole job. It is not a function (lesson 86). Do not rewrite `snap.sh`. Do not invent dummy files.

## Live sources (fetched this pass)

- `help for`: `for NAME [in WORDS ... ] ; do COMMANDS; done`. For each element in WORDS, NAME is set to that element. Exit status is the last command executed.
- Chet Ramey bash(1) compound commands: a list may be separated by newlines in place of a semicolon.
- Live glob: `papers/*.txt` expands to `21 Aug receipt.txt`, `landlord-note.txt`, `late-notice.txt`. Quoted `"$f"` keeps the space.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- `papers` is the symlink to `/home/ubuntu/rent-receipts`. Do not create `receipt-loop.txt` off camera.

## Human job

Write a one-page list of every receipt name without typing each name twice.

Candidates considered: (1) `for i in 1 2 3; do echo $i; done` — smoke test. (2) `for f in papers/*.txt; do basename "$f" >> receipt-loop.txt; done` then cat. Picked (2). Without `for`, they would type three basenames by hand.

## Done on screen

Fullscreen terminal. `ls papers/*.txt` shows three paths. The loop runs. Last `cat receipt-loop.txt` holds `21 Aug receipt.txt`, `landlord-note.txt`, `late-notice.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `snap.sh` as the lesson-84 version with `$1`. Leave `due` / alias. Create `receipt-loop.txt` on camera.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `ls papers/*.txt`, the `for` loop, last `cat receipt-loop.txt`.
