# Lesson 55 — See umask

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 56 here.

## Feature

`umask` is the shell’s file-creation mask. New files lose the bits in the mask. Prove it by printing the mask, then `touch` a real September due scratch and `ls -l`.

## What it is / is not

- It is: `umask` → `0022`, `umask -S` → `u=rwx,g=rx,o=rx`, `touch sep-due-note.txt`, `ls -l` → `-rw-r--r--` on a 0-byte new note (666 minus 022).
- It is not: `chmod 644` on an existing file (previous lesson). It is not sticky bit (next). It is not `echo`.

## Live sources (fetched this pass)

- `help umask`: bash builtin. Display or set file mode mask. `-S` prints symbolic.
- Live this host: `umask` prints `0022`. `touch` in `~/linux-workshop` created `-rw-r--r--` size 0. Deleted so `touch` stays on camera.

## Live operation on this host (2026-08-22)

- Last command: `ls -l sep-due-note.txt` holding `-rw-r--r-- 1 ubuntu ubuntu 0`.
- If leftover `sep-due-note.txt` exists, `rm` off-camera so creation is on camera.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Before writing September’s due date as a new paper, see what bits a brand-new file gets. `umask` is required; chmod on rent-log does not show the default.

Candidates considered: (1) `echo hi > /tmp/x` — smoke test, and `>` is not in HumanInput. (2) only print umask, no file. (3) `touch sep-due-note.txt` in the workshop after printing umask. Picked (3).

## Done on screen

Fullscreen terminal. `umask` prints `0022`. `ls -l sep-due-note.txt` starts with `-rw-r--r--` and size 0.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `sep-due-note.txt` after the take. Do not rewrite rent-log.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `umask`, `umask -S`, `touch sep-due-note.txt`, `ls -l sep-due-note.txt`.
