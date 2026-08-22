# Lesson 49 — Make a symlink

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 50 here.

## Feature

`ln -s` makes a symbolic link: a pointer name that is not a copy and not a hard link. The first character of `ls -l` is `l`.

## What it is / is not

- It is: `cd ~/linux-workshop`, `ln -s ~/rent-receipts papers`, then `ls -ld papers` showing `l` and `-> /home/ubuntu/rent-receipts`, `readlink papers`, and `ls papers` listing the three rent papers.
- It is not: `echo`. It is not `cp -r`. It is not `ln` without `-s` (that was lesson 48). It is not rewriting the rent log or the three papers.

## Live sources (fetched this pass)

- `ln(1)` GNU coreutils 9.4: “Create hard links by default, symbolic links with --symbolic.” “-s, --symbolic make symbolic links instead of hard links.” “Symbolic links can hold arbitrary text.”
- GNU coreutils info on this host: a symlink is a special file type that refers to a different file by name; operations open the target.
- This host (2026-08-22): probe `ln -s ~/rent-receipts papers` then `rm papers` so creation stays on camera. `ls -ld papers` was `lrwxrwxrwx ... papers -> /home/ubuntu/rent-receipts`. `readlink` printed `/home/ubuntu/rent-receipts`. `file papers` said `symbolic link`. `ls papers` listed `21 Aug receipt.txt`, `landlord-note.txt`, `late-notice.txt`.

## Live operation on this host (2026-08-22)

- Keep `due-call.txt` (hard link from 48). Create `papers` as a symlink on camera.
- Do not `ln` without `-s`. Do not copy the receipts folder.
- Last command: `ls -ld papers` with leading `l` and `-> /home/ubuntu/rent-receipts`.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person wants a short name `papers` inside the workshop that points at `/home/ubuntu/rent-receipts`, so they can list the three rent papers from the workshop without copying them. `ln -s` is required; a hard link cannot cross into a directory the same way, and `cp` would duplicate the papers.

Candidates considered: (1) `echo` a fake link — smoke test. (2) `ln` without `-s` — last lesson. (3) `ln -s ~/rent-receipts papers` then prove `l` and the three names. Picked (3).

## Done on screen

Fullscreen terminal in `linux-workshop`. `ls -ld papers` starts with `l` and shows `papers -> /home/ubuntu/rent-receipts`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `rent-log.txt`, `due-call.txt`, `sep-due-draft.txt`. Create `papers` as a symlink. Do not delete it after the take.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `ls -l`, `ln -s ~/rent-receipts papers`, `ls -ld papers`, `readlink papers`, `ls papers`.
