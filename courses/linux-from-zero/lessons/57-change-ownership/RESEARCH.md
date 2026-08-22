# Lesson 57 — Change ownership

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 58 here.

## Feature

`chown` and `chgrp` change who owns a file. Locks belong to someone. Prove it with `ls -l` after handing Sam the September due note.

## What it is / is not

- It is: `sudo chown sam sep-due-note.txt` then `sudo chgrp sam sep-due-note.txt`, `ls -l` → `sam sam`. GNU chown/chgrp 9.4.
- It is not: sticky bit. It is not a generic sudo lesson (next). It is not `echo`. Do not type `sam:sam` (colon is not in HumanInput; GNU also warns that `.` should be `:`).

## Live sources (fetched this pass)

- `man chown` NAME: change file owner and group. Owner-only leaves group unchanged.
- Live: `sudo -n chown sam` → owner sam, group still ubuntu. `sudo -n chgrp sam` → `sam sam`. Reset with `chown ubuntu` then `chgrp ubuntu` so the take starts ubuntu ubuntu.

## Live operation on this host (2026-08-22)

- Start: `ls -l sep-due-note.txt` is `-rw-r--r-- 1 ubuntu ubuntu 0 Aug 22 02:52`.
- Last command: `ls -l sep-due-note.txt` holding `1 sam sam`.
- If leftover take left sam as owner, reset off-camera with `sudo chown ubuntu` and `sudo chgrp ubuntu`.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Sam needs to own the empty September due paper so later they can write it as themselves. `chown`/`chgrp` are required; a folder named sam is not ownership.

Candidates considered: (1) chown /tmp/foo — smoke test. (2) chown rent-log — would also change due-call hard link. (3) chown+chgrp on sep-due-note.txt. Picked (3).

## Done on screen

Fullscreen terminal. `ls -l sep-due-note.txt` shows owner `sam` and group `sam`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave sep-due-note.txt owned by sam:sam after the take. Do not rewrite rent-log.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, the ubuntu ubuntu `ls -l`, `sudo chown sam`, `sudo chgrp sam`, last `ls -l` with sam sam.
