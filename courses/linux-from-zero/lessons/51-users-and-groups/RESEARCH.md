# Lesson 51 — See users and groups

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 52 here.

## Feature

`/etc/group` lists groups. `groups` and `id -nG` print the names this account belongs to. `grep ubuntu /etc/group` shows the live lines that name this account, including `sudo`.

## What it is / is not

- It is: `groups`, `id -nG`, `getent group sudo`, then `grep ubuntu /etc/group` so `sudo:x:27:ubuntu` is visible with the other memberships.
- It is not: `echo`. It is not creating a user (lesson 52). It is not `getent passwd` as the last command (lesson 50). It is not chmod.

## Live sources (fetched this pass)

- `group(5)` on this host: `/etc/group` is one entry per line, `group_name:password:GID:user_list`.
- `groups(1)` GNU coreutils 9.4. Live: `ubuntu adm dialout cdrom floppy sudo audio dip video plugdev`.
- `id -nG` prints the same names. `getent group sudo` is `sudo:x:27:ubuntu`.
- `/etc/group` is ASCII text, 594 bytes. `grep ubuntu /etc/group` lists ten lines including `sudo:x:27:ubuntu` and `ubuntu:x:1000:`.

## Live operation on this host (2026-08-22)

- Do not type a colon. `grep ubuntu /etc/group` is colon-free.
- Last command: `grep ubuntu /etc/group` with `sudo:x:27:ubuntu` visible.
- Do not add or delete users. Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

A person about to do an admin job needs to prove this login is in `sudo` by reading the group file, not by guessing from memory. `grep ubuntu /etc/group` is required.

Candidates considered: (1) `echo sudo` — smoke test. (2) `id` only — already shown in lesson 50. (3) `groups`, `id -nG`, `getent group sudo`, `grep ubuntu /etc/group`. Picked (3).

## Done on screen

Fullscreen terminal. `grep ubuntu /etc/group` includes `sudo:x:27:ubuntu`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite workshop files.

## Viewer must see created on camera

Opening Terminal Emulator, `groups`, `id -nG`, `getent group sudo`, `grep ubuntu /etc/group`.
