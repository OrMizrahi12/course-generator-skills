# Lesson 35 — Create the Linux workshop

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 36 here.

## Feature

Create a real empty directory at home with `mkdir ~/linux-workshop` and prove it exists. The continuous project starts here.

## What it is / is not

- It is: GNU coreutils `mkdir` 9.4. Create the DIRECTORY if it does not already exist. `~/linux-workshop` uses tilde expansion (lesson 32) so the new folder is made under `$HOME`, not under `/workspace`. After creation, `ls -ld` shows a directory line.
- It is not: `touch` (that makes a file). It is not writing a note (lesson 36). It is not `echo`. It is not `mkdir -p` of a nested tree. It is not `cd` into the workshop as the lesson object.

## Live sources (fetched this pass)

- Ubuntu Noble `mkdir(1)` — coreutils 9.4-3ubuntu6.2. Create the DIRECTORY(ies), if they do not already exist. `-v` prints a message per created directory. https://manpages.ubuntu.com/manpages/noble/man1/mkdir.1.html
- This host: `mkdir --version` → GNU coreutils 9.4. `/usr/bin/mkdir`. `mkdir --help` matches that manpage. Manpages are not installed locally (`unminimize`).

## Live operation on this host (2026-08-21)

- `/home/ubuntu/linux-workshop` does **not** exist. Do not create it off-camera.
- `ls ~` currently prints `go` and `rent-receipts`.
- From `/workspace`, `mkdir ~/linux-workshop` must create `/home/ubuntu/linux-workshop`. Probe of `mkdir -v` in `/tmp` printed `mkdir: created directory '…'` then was removed.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.
- Keys already in HumanInput: `~` is Shift+grave.

## Human job

A person has August papers in `rent-receipts` and a course tree in `/workspace`. They need a dedicated workshop at home for later notes and tools. `mkdir ~/linux-workshop` is required: listing cannot invent the folder, and creating it under `/workspace` would put work in the wrong house.

Candidates considered: (1) `mkdir linux-workshop` from `/workspace` — wrong house. (2) `cd ~` then `mkdir` — extra walk, hides `~` on mkdir. (3) from `/workspace`, `pwd`, `mkdir ~/linux-workshop`, `ls ~` so the new name sits with `go` and `rent-receipts`, then `ls -ld ~/linux-workshop` holding the directory line. Picked (3).

## Done on screen

Fullscreen terminal. After `mkdir ~/linux-workshop`, last frames hold `ls -ld ~/linux-workshop` printing a `d` directory line for `/home/ubuntu/linux-workshop`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

This lesson **creates** `~/linux-workshop` on camera. Do not seed it.

## Viewer must see created on camera

Opening Terminal Emulator, `pwd` from `/workspace`, `mkdir ~/linux-workshop`, `ls ~` including the new name, and `ls -ld ~/linux-workshop`.
