# Lesson 83 — Write a backup script and run it

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 84 here.

## Feature

Write `snap.sh` with `#!/bin/bash`, `chmod +x`, run `./snap.sh`. Last `ls -l /home/ubuntu/workshop-bak.tar.gz` holds the archive the script made.

## What it is / is not

- It is: a real bash script archives the workshop. Last frame is the `.tar.gz` on disk, not the editor.
- It is not: `echo`. It is not arguments/`if` (next lesson). It is not typing `tar` by hand as the whole job (lesson 75). Do not rewrite `rent-log.txt`. Do not put the archive inside `linux-workshop`.

## Live sources (fetched this pass)

- man7.org execve(2): a script starts with `#!interpreter` [optional-arg].
- `/bin/bash` is GNU bash, ELF pie on this host. GNU tar 1.35. `tar -czf` creates a gzip archive.
- `chmod +x` makes the script executable. On this X keyboard, `!` is Shift+1 and `+` is Shift+equal.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Do not pre-create `snap.sh` or `workshop-bak.tar.gz`. `linux-workshop.tar.gz` from lesson 75 stays; this lesson writes a new name.

## Human job

One command that packs the whole workshop so the Oct due draft and `due` binary are in an archive without typing tar flags every time.

Candidates considered: (1) a script that only `echo`s — smoke test. (2) `tar` typed by hand — already lesson 75. (3) `snap.sh` with shebang that writes `~/workshop-bak.tar.gz`. Picked (3). Without the script the archive is not produced this way.

## Done on screen

Fullscreen terminal. Last `ls -l /home/ubuntu/workshop-bak.tar.gz` holding a regular file with size greater than zero.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Create `linux-workshop/snap.sh` on camera. Write the archive to `/home/ubuntu/workshop-bak.tar.gz` so tar does not pack a growing file inside the tree. Leave `due.c` / `due` / `.bashrc` alias.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, nano `snap.sh` with shebang and tar line, save, `chmod +x snap.sh`, `./snap.sh`, last `ls -l /home/ubuntu/workshop-bak.tar.gz`.
