# Lesson 33 — List what is here

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 34 here.

## Feature

List the home directory three ways: names only, long view, then all including hidden names that start with a dot. See before you move.

## What it is / is not

- It is: GNU coreutils `ls` 9.4. Default listing hides names that start with `.`. `-l` is the long format (mode, owner, size, time). `-a` / `--all` does not ignore entries starting with `.`.
- It is not: `cd`. It is not creating a hidden file (lesson 39). It is not `echo`. It is not starting `~/linux-workshop`.

## Live sources (fetched this pass)

- Ubuntu Noble `ls(1)` — coreutils 9.4-3ubuntu6.2. `-a` do not ignore entries starting with `.`. `-l` long listing. https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html
- This host: `ls --version` → GNU coreutils 9.4.

## Live operation on this host (2026-08-21)

- `ls ~` prints two names: `go` and `rent-receipts`.
- `ls -l ~` adds mode, owner, size, date for those two directories.
- `ls -la ~` adds `.`, `..`, `.bashrc`, `.profile`, `.bash_history`, and the rest. About 25 names. Fits one 1920×1080 JetBrains Mono 19 screen.
- Do not `cd`. List `~` from `/workspace`.
- Do not create extra files. `rent-receipts` and `go` already exist.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person found the house last lesson. Before walking in, they need to see what is actually there: the rent folder, and the hidden shell config sitting next to it. Names-only misses `.bashrc`. Long view plus `-a` is required.

Candidates considered: (1) `ls` of `/workspace` — the course repo, not the house. (2) `ls -A` without `.` and `..` — extra flag. (3) `ls ~`, `ls -l ~`, `ls -la ~` held on the full house including `.bashrc` and `rent-receipts`. Picked (3).

## Done on screen

Fullscreen terminal. Names, then long view of two directories, then `ls -la ~` holding `.bashrc` and `rent-receipts` in the same listing.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35.

## Viewer must see created on camera

Opening Terminal Emulator and the three `ls` commands. Do not seed extra files. Do not `cd` off-camera.
