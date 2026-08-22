# Lesson 56 — Use the sticky bit on a shared directory

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 57 here.

## Feature

The sticky bit (`t`) on a world-writable directory means you can only delete files you own. `/tmp` is the live example: `drwxrwxrwt` mode 1777.

## What it is / is not

- It is: `ls -ld /tmp` showing `t`, `touch` your own scratch, `sudo -u sam touch` Sam’s scratch, `rm` your own succeeds, `rm -f` Sam’s fails with `Operation not permitted`, then `ls -l` still lists Sam’s file.
- It is not: chmod letters/numbers on rent-log. It is not chown (next). It is not `echo`. It is not turning sticky off on /tmp.

## Live sources (fetched this pass)

- `man chmod` RESTRICTED DELETION FLAG OR STICKY BIT: for directories, unprivileged users cannot remove or rename a file unless they own the file or the directory; commonly found on `/tmp`.
- Live `/tmp`: `drwxrwxrwt` `1777` root root.
- Live: `sudo -n -u sam touch /tmp/sam-rent-scratch.txt` → `-rw-rw-r-- 1 sam sam` (sam’s umask is `0002`). GNU `rm` without `-f` first asks `remove write-protected regular empty file?` and never shows sticky. `rm -f` skips the prompt and prints `Operation not permitted`. Probe files deleted so creation stays on camera.

## Live operation on this host (2026-08-22)

- Last command: `ls -l /tmp/sam-rent-scratch.txt` holding `-rw-rw-r-- 1 sam sam` after `rm -f` failed.
- If leftover scratches exist, `rm` ubuntu’s and `sudo rm` sam’s off-camera so both `touch` lines are on camera.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Sam left a rent scratch in the shared `/tmp` tray. ubuntu must not be able to throw Sam’s paper away even though everyone can write there. Sticky `t` is required.

Candidates considered: (1) `ls -ld /tmp` only — no proof. (2) chmod +t on a toy dir in /tmp — hides the real `/tmp`. (3) two real people, two files in `/tmp`, prove ubuntu cannot delete Sam’s. Picked (3).

## Done on screen

Fullscreen terminal. `rm -f /tmp/sam-rent-scratch.txt` prints `Operation not permitted`. `ls -l /tmp/sam-rent-scratch.txt` still shows owner `sam`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. Leave `/tmp/sam-rent-scratch.txt` after the take. ubuntu’s scratch is deleted on camera.

## Viewer must see created on camera

Opening Terminal Emulator, `ls -ld /tmp` with `t`, both `touch` lines, successful `rm` of ubuntu’s file, failed `rm -f` of Sam’s, last `ls -l`.
