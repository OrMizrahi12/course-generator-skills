# Lesson 46 — Measure disk and directory size

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 47 here.

## Feature

`df` reports space on the filesystem a path lives on. `du` estimates how much that directory tree uses. The tree drawing is not the disk.

## What it is / is not

- It is: `df -h /` on this machine, then `du -sh` of the workshop, the rent papers, and home, then one last `du -sh` of workshop and papers together.
- It is not: `echo`. It is not mounting tmpfs (next lesson). It is not filling the disk. It is not `df` of an unmounted device.

## Live sources (fetched this pass)

- `df(1)` GNU coreutils 9.4 on this host: report file system space usage; `-h` human-readable powers of 1024.
- `du(1)` GNU coreutils 9.4: estimate file space usage, recursively for directories; `-s` summarize, `-h` human-readable.
- This host (2026-08-22): `df -h /` → overlay, 252G size, 17G used, 223G avail, 7%, mounted on `/`. `du -sh ~/linux-workshop` → 16K. `du -sh ~/rent-receipts` → 4.0K. `du -sh ~` → 3.5G.

## Live operation on this host (2026-08-22)

- Workshop files stay. Do not mount, fill, or delete.
- Menu-launched xfce4-terminal cwd is `/workspace`.
- Last command: `du -sh ~/linux-workshop ~/rent-receipts` showing 16K and 4.0K.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person has a small workshop and a small papers folder. They need to know how much those trees use, and how much room the disk still has. `df` and `du` are required; `ls -l` size of one note is not the directory or the disk.

Candidates considered: (1) `echo 16K` — smoke test. (2) mount tmpfs and write — next lesson. (3) `df -h /` then `du -sh` of the two live folders. Picked (3).

## Done on screen

Fullscreen terminal. `du -sh ~/linux-workshop ~/rent-receipts` shows `16K` and `4.0K`, with `df -h /` overlay `252G` still on screen.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the notes. Nothing new is written.

## Viewer must see created on camera

Opening Terminal Emulator, `df -h /`, `du -sh` of the workshop, of the papers, of home, and of both folders together.
