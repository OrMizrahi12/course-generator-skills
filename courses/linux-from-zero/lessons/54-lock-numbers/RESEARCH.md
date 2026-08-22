# Lesson 54 — Lock a file with numbers

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 55 here.

## Feature

`chmod` with octal digits sets the same rwx bits as letters. 4+2+1 per class. Prove 644 on the rent note and 755 on the workshop directory.

## What it is / is not

- It is: `chmod 644 rent-log.txt` then `chmod 700 .` then `chmod 755 .`, proved with `ls -l` / `ls -ld`.
- It is not: `chmod go-rw` (previous lesson). It is not umask (next). It is not `echo`.

## Live sources (fetched this pass)

- `man chmod`: a numeric mode is one to four octal digits, bits 4 2 1.
- Live: rent-log starts `-rw-------` (600) from lesson 53. `chmod 644` → `-rw-r--r--`. Workshop dir starts `drwxr-xr-x` (755). `chmod 700 .` → `drwx------`. `chmod 755 .` restores `drwxr-xr-x`.
- Reset before filming: file 600, directory 755, so both number changes happen on camera.

## Live operation on this host (2026-08-22)

- Last command: `ls -l rent-log.txt` holding `-rw-r--r--` after the numbers, with `chmod 755 .` still on screen.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Letters shut the rent note. Reopen it with 644 so group and others can read the paid date again, then lock and reopen the workshop folder with 700 then 755. Numbers are required.

Candidates considered: (1) chmod 644 /tmp/foo — smoke test. (2) only 644, skip 755. (3) 644 on the note plus 700/755 on the real workshop. Picked (3).

## Done on screen

Fullscreen terminal. `ls -l rent-log.txt` starts with `-rw-r--r--`. `ls -ld .` after 755 starts with `drwxr-xr-x`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave rent-log at 644 and linux-workshop at 755 after the take. Do not rewrite contents.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, the 600 `ls -l`, `chmod 644`, `chmod 700 .`, `chmod 755 .`, final `ls -l rent-log.txt`.
