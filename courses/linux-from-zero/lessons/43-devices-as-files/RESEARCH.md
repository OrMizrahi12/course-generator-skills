# Lesson 43 — See devices as files

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 44 here.

## Feature

Hardware and kernel gadgets appear as files under `/dev`. `file` names the kind: character special vs block special. You find a real node and say what kind it is.

## What it is / is not

- It is: listing `/dev` on this Ubuntu, then `ls -l` and `file` of `/dev/null` (character special 1/3) and `/dev/vda` (block special 254/0), this machine’s disk.
- It is not: `echo`. It is not `/proc` or `/sys` (lesson 42). It is not teaching the full `ls -l` first-character map (next lesson). It is not writing the disk, not `cat /dev/vda`, not redirecting into `/dev/null` (this typer has no `>`).

## Live sources (fetched this pass)

- `intro(4)` on this host (man-pages 6.7): “Section 4 of the manual describes special files (devices).” Files: `/dev/*` — device files. https://man7.org/linux/man-pages/man4/intro.4.html
- `null(4)` on this host: `/dev/null` and `/dev/zero` are data sinks. Reads from null return EOF. Typically `mknod -m 666 /dev/null c 1 3`.
- FHS 3.0 `/dev`: the location of device files. https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s05.html
- This host (2026-08-22): `/dev` is a directory (devtmpfs). `file /dev/null` → `character special (1/3)`. `file /dev/vda` → `block special (254/0)`. `ls -l` first character `c` vs `b`. 135 names in `/dev`. Do not write `/dev/vda`.

## Live operation on this host (2026-08-22)

- Workshop files stay. Do not create, move, or delete them. Do not write device nodes.
- Menu-launched xfce4-terminal cwd is `/workspace`.
- `ls -ld /dev` then `file /dev` (directory).
- `ls -l /dev/null` then `file /dev/null`.
- `ls -l /dev/vda`.
- Last command: `file /dev/null /dev/vda` prints character special (1/3) and block special (254/0).
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person needs to know the bit-bucket and this machine’s disk are files they can name, not magic boxes. Without `/dev` they would think hardware lives outside the tree.

Candidates considered: (1) `echo /dev/null` — smoke test, forbidden. (2) `cat /dev/vda` — binary, wrong, dangerous. (3) `ls /dev` of all 135 names then `file` on `/dev/null` and `/dev/vda`. Picked (3) with a short `/dev` listing via `ls -ld` plus the two named nodes, because an unfiltered 135-line dump hides the kinds.

## Done on screen

Fullscreen terminal. `file /dev/null /dev/vda` shows `character special (1/3)` and `block special (254/0)`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the three papers and the hidden note. Nothing new is written.

## Viewer must see created on camera

Opening Terminal Emulator, `ls -ld /dev`, `file /dev`, `ls -l` of `/dev/null` and `/dev/vda`, `file /dev/null`, and `file /dev/null /dev/vda`.
