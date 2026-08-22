# Lesson 50 — See who you are

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 51 here.

## Feature

`whoami` prints the effective user name. `id` prints uid, gid, and groups. `getent passwd ubuntu` prints this account’s `/etc/passwd` line: name, uid, gid, GECOS, home, shell.

## What it is / is not

- It is: open a terminal, `whoami` → `ubuntu`, `id` → `uid=1000(ubuntu)`, then `getent passwd ubuntu` → `ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash`.
- It is not: `echo`. It is not creating a user (next lessons). It is not listing `/etc/group` as the last proof (that is lesson 51). It is not `whoami` as the last command (lesson 4 already ended on `whoami`).

## Live sources (fetched this pass)

- `whoami(1)` GNU coreutils 9.4 on this host: “Print the user name associated with the current effective user ID. Same as id -un.”
- `id(1)` GNU coreutils 9.4: “Print user and group information… Without any OPTION, print some useful set of identified information.”
- `getent` Ubuntu GLIBC 2.39. Live line: `ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash`.
- `/etc/passwd` on this host is ASCII text, mode `-rw-r--r--`, root:root. `passwd(5)` man page is not installed here; the live file is the source.

## Live operation on this host (2026-08-22)

- Account is `ubuntu`, uid 1000, home `/home/ubuntu`, shell `/bin/bash`.
- Do not type a colon. Use `getent passwd ubuntu`, not `grep ubuntu: /etc/passwd`.
- Last command: `getent passwd ubuntu` with the full seven-field line visible.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person about to lock workshop files and later add another account needs to prove this login is `ubuntu` with home `/home/ubuntu` and shell `/bin/bash`. `whoami` is not enough; the passwd line is required.

Candidates considered: (1) `echo ubuntu` — smoke test. (2) `whoami` only — already lesson 4’s last frame. (3) `whoami`, `id`, then `getent passwd ubuntu`. Picked (3).

## Done on screen

Fullscreen terminal. `getent passwd ubuntu` prints `ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log, due-call, papers, or receipts.

## Viewer must see created on camera

Opening Terminal Emulator, `whoami`, `id`, `getent passwd ubuntu`.
