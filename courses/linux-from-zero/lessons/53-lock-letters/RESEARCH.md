# Lesson 53 — Lock a file with letters

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 54 here.

## Feature

`chmod` with letters (u/g/o and rwx) changes who can read or write a file. Prove it with `ls -l` on a workshop note.

## What it is / is not

- It is: `chmod go-rw rent-log.txt`, then `ls -l rent-log.txt` → `-rw-------`. GNU chmod 9.4 symbolic mode.
- It is not: octal `chmod 644` / `chmod 600` (next lesson). It is not `echo`. It is not locking a toy file.

## Live sources (fetched this pass)

- `man chmod` NAME: change file mode bits. Symbolic: `[ugoa...][[-+=][perms...]...]`.
- Live `chmod go-rw rent-log.txt` turns `-rw-r--r--` into `-rw-------` on inode 1575463. `due-call.txt` (hard link) follows. Reset with `chmod u=rw,g=r,o=r` so the take starts world-readable again.

## Live operation on this host (2026-08-22)

- Start: `ls -l rent-log.txt` is `-rw-r--r-- 2 ubuntu ubuntu 92 Aug 21 22:12`.
- After letters: `-rw------- 2 ubuntu ubuntu 92 Aug 21 22:12`.
- Last command: `ls -l rent-log.txt` holding `-rw-------`.
- If a leftover take left 600, reset with letters off-camera: `chmod u=rw,g=r,o=r`.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

The rent-paid note is still group-and-world readable. The landlord’s helper Sam now exists; do not leave the due date open. `chmod go-rw` is required.

Candidates considered: (1) `chmod` on /tmp/foo — smoke test. (2) `chmod +x` a script that does not exist. (3) `chmod go-rw` on the real rent-log. Picked (3).

## Done on screen

Fullscreen terminal. `ls -l rent-log.txt` starts with `-rw-------`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log contents. Leave mode `-rw-------` after the take (numeric lesson can lock it a different way later — do not research that here).

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, the 644-looking `ls -l`, `chmod go-rw rent-log.txt`, then `ls -l` with dashes in the group and other columns.
