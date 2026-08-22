# Lesson 48 — Make a hard link

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 49 here.

## Feature

`ln` without `-s` makes a hard link: a second name for the same inode. Two names, one file.

## What it is / is not

- It is: `cd ~/linux-workshop`, `ls -li` of `rent-log.txt` (inode 1575463, link count 1), `ln rent-log.txt due-call.txt`, then `ls -li` of both names showing the same inode and link count 2, then `cat due-call.txt` matching the rent log.
- It is not: `echo`. It is not `cp` (that made a second inode in lesson 37). It is not `ln -s` (next lesson). It is not rewriting `rent-log.txt`.

## Live sources (fetched this pass)

- `ln(1)` GNU coreutils 9.4 on this host: “Create hard links by default, symbolic links with --symbolic.” “When creating hard links, each TARGET must exist.”
- GNU coreutils info on this host: a hard link cannot cross filesystems; the inode is the file.
- This host (2026-08-22): probe `ln rent-log.txt due-call.txt` then `rm due-call.txt` so creation stays on camera. Same inode `1575463`, link count 2, `cmp` identical, `cat` shows the three rent sentences. After `rm`, link count 1 again.

## Live operation on this host (2026-08-22)

- Workshop files stay except the new name `due-call.txt` created on camera.
- Do not `ln -s`. Do not `cp`. Do not nano the rent log.
- Last command: `ls -li rent-log.txt due-call.txt` with inode `1575463` twice and link count `2`.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person wants a second name `due-call.txt` for the rent log so they can find the same paper from the 21 Sep call, without making a copy that can drift. `ln` is required; `cp` already made a different inode (`sep-due-draft.txt`).

Candidates considered: (1) `echo` two names — smoke test. (2) `ln -s` — next lesson. (3) `ln rent-log.txt due-call.txt` then prove same inode. Picked (3).

## Done on screen

Fullscreen terminal in `linux-workshop`. `ls -li rent-log.txt due-call.txt` shows inode `1575463` on both lines and link count `2`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `rent-log.txt` bytes and mtime. Leave `sep-due-draft.txt`. Create `due-call.txt` as a hard link. Do not delete it after the take.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `ls -li`, `ln rent-log.txt due-call.txt`, `ls -li` of both names, `cat due-call.txt`.
