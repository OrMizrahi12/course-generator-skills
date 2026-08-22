# Lesson 93 — See time and locale

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 94 here.

## Feature

`date`, then `locale | grep '^LANG='`, then `ls -l /etc/localtime`. Last `cat /etc/timezone` holds `Etc/UTC`.

## What it is / is not

- It is: this host’s clock and locale. `timedatectl` fails: System has not been booted with systemd as init system (PID 1). Do not fake it. `date` as a last command was already used in lesson 26 — last here is the timezone file.
- It is not: `echo`. It is not `dmesg` (lesson 92). It is not boot/PID 1 (lesson 94).

## Live sources (fetched this pass)

- Ubuntu Noble `date(1)`. https://manpages.ubuntu.com/manpages/noble/man1/date.1.html
- Probe: `date` → Sat Aug 22 01:34:25 PM UTC 2026. `LANG=en_US.UTF-8`. `/etc/localtime` → `/usr/share/zoneinfo/Etc/UTC`. `cat /etc/timezone` → `Etc/UTC`. `timedatectl` → Can't operate.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.

## Human job

A person needs the current time, the language, and the timezone file — without inventing systemd.

Candidates considered: (1) `timedatectl` — fails honestly, but is not the hold. (2) only `date` — already lesson 26’s last command. (3) `date`, `locale | grep '^LANG='`, `ls -l /etc/localtime`, last `cat /etc/timezone`. Picked (3).

## Done on screen

Fullscreen terminal. Last `cat /etc/timezone` holding `Etc/UTC`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `example.html`. Do not rewrite timezone.

## Viewer must see created on camera

Opening Terminal Emulator, `date`, LANG grep, `ls -l /etc/localtime`, last `cat /etc/timezone`.
