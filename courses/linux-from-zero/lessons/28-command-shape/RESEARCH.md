# Lesson 28 — See a command’s shape

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 29 here.

## Feature

Read one typed line as three parts: the command, the options, and the argument (operand). Then run a real line that uses all three.

## What it is / is not

- It is: GNU `ls` synopsis `ls [OPTION]... [FILE]...` plus POSIX utility syntax: options (flags after `-`), then operands. On this host the worked line is `ls -ld /home/ubuntu/rent-receipts`. `ls` is the command, `-ld` is grouped short options (`-l` long listing, `-d` list the directory itself), `/home/ubuntu/rent-receipts` is the operand.
- It is not: `echo`. It is not `ls --version` (lesson 24). It is not `ls /` or `ls /home/ubuntu` as the last-frame pair (lesson 4 / 13). It is not history, Tab, or quoting (later). It is not starting `~/linux-workshop`.

## Live sources (fetched this pass)

- Ubuntu Noble `ls(1)` GNU coreutils 9.4 — SYNOPSIS `ls [OPTION]... [FILE]...`; `-l` long listing; `-d, --directory` list directories themselves, not their contents. https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html
- POSIX.1 Utility Conventions — a utility name, then options / option-arguments, then operands. Options may be grouped behind one `-`. Options precede operands. https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html

## Live operation on this host (2026-08-21)

- `ls -ld /home/ubuntu/rent-receipts` → `drwxr-xr-x 2 ubuntu ubuntu 4096 Aug 21 19:56 /home/ubuntu/rent-receipts`
- Same output with `ls -l -d /home/ubuntu/rent-receipts`. Film the grouped form `-ld` (POSIX guideline 5).
- Empty `ls -l /home/ubuntu/rent-receipts` is only `total 0` — that hides that the folder exists as a directory. `-d` is required for this job.
- Open Terminal Emulator from the desktop menu. Fullscreen it. Font already JetBrains Mono 19.
- `rent-receipts` exists from lesson 25. Do not recreate it.

## Human job

A person has a `rent-receipts` folder and needs to inspect that folder as a thing (owner, date, that it is a directory) before putting a receipt file in it. `ls` alone lists the empty inside (`total 0`) and looks like nothing is there. The long listing of the directory itself is required, so the line must carry options and the real path.

Candidates considered: (1) `date +%F` — format operand is easy to confuse with an option. (2) `ls -l /home/ubuntu` — lists home, not the receipt folder as the subject. (3) `ls -ld /home/ubuntu/rent-receipts` — command, grouped options, operand, and a directory line. Picked (3).

## Done on screen

Fullscreen terminal. Line `ls -ld /home/ubuntu/rent-receipts` typed and run. Last frames hold the `drwxr-xr-x` line ending in `/home/ubuntu/rent-receipts`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35.

## Viewer must see created on camera

Opening Terminal Emulator, typing the three-part line, and the printed directory line. Do not pre-run `ls -ld`.
