# Lesson 92 — Read the system’s memory of what happened

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 93 here.

## Feature

List `/var/log`, read the apt history this session wrote, then `dmesg | head -n 1`. Last line holds `Linux version 6.12.94+`.

## What it is / is not

- It is: a real log file plus the kernel ring buffer. `dmesg` works here without sudo. `journalctl` has no journal files. `/var/log/syslog` is not installed.
- It is not: `echo`. It is not `/proc/cmdline` as the lesson object (lesson 94). It is not `date` (lesson 93). Do not fake systemd journals.

## Live sources (fetched this pass)

- Ubuntu Noble `dmesg(1)`. https://manpages.ubuntu.com/manpages/noble/man1/dmesg.1.html
- Probe: `dmesg | head -n 1` prints `Linux version 6.12.94+ ...`. `/var/log/apt/history.log` records `apt-get install -y iproute2` at 13:00:46. `journalctl -n 3` → No journal files were found.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.

## Human job

A person needs one kernel boot line and proof apt wrote a history row.

Candidates considered: (1) `journalctl` — empty here. (2) only `tail` apt history — misses the kernel. (3) `ls /var/log`, `tail -n 6 /var/log/apt/history.log`, last `dmesg | head -n 1`. Picked (3).

## Done on screen

Fullscreen terminal. Last `dmesg | head -n 1` holding Linux version 6.12.94+.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `example.html`. Do not rewrite logs.

## Viewer must see created on camera

Opening Terminal Emulator, `ls /var/log`, `tail` of apt history, last `dmesg | head -n 1`.
