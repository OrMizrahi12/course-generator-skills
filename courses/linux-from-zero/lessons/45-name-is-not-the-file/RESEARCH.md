# Lesson 45 — See that a name is not the file

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 46 here.

## Feature

`ls -i` prints the inode (index number) to the left of the name. That number is the file. The name is a label. Link count 1 on `ls -l` means one name for that inode.

## What it is / is not

- It is: `cd` into the workshop, `ls -l` the two 92-byte rent papers, `ls -i`, then `ls -li rent-log.txt sep-due-draft.txt` so two different inodes sit next to two names.
- It is not: `echo`. It is not making a hard link (later). It is not `md5sum`. It is not inodes of `/dev` or `/proc`.

## Live sources (fetched this pass)

- GNU coreutils info on this host (`--inode`): “Print the inode number (also called the file serial number and index number) of each file to the left of the file name. (This number uniquely identifies each file within a particular file system.)”
- `ls(1)` on this host: `-i, --inode` print the index number of each file.
- This host (2026-08-22): `rent-log.txt` inode `1575463`, link count 1, 92 bytes, mtime Aug 21 22:12. `sep-due-draft.txt` inode `1575549`, link count 1, 92 bytes, mtime Aug 21 22:28. Same text, two files.

## Live operation on this host (2026-08-22)

- Workshop files stay. Do not `ln`. Do not rewrite the notes.
- Menu-launched xfce4-terminal cwd is `/workspace`.
- `cd ~/linux-workshop` then `pwd` shows `/home/ubuntu/linux-workshop` and prompt `linux-workshop $`.
- Last command: `ls -li rent-log.txt sep-due-draft.txt` with two different inode numbers and both link counts `1`.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person has two rent papers that look the same size. They need to know whether those are two names for one file or two files. `ls -i` / link count is required; `ls -l` size alone cannot tell.

Candidates considered: (1) `echo` two names — smoke test. (2) `ln` a hard link now — next lesson. (3) `ls -li` the two live copies. Picked (3).

## Done on screen

Fullscreen terminal in `linux-workshop`. `ls -li rent-log.txt sep-due-draft.txt` shows inode `1575463` and `1575549`, both with link count `1`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave both notes. Nothing new is written.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `ls -l`, `ls -i`, and `ls -li` of the two notes.
