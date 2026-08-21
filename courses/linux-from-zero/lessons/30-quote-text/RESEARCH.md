# Lesson 30 — Quote text so the shell does not eat it

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 31 here.

## Feature

Put single quotes around a filename that contains spaces so Bash treats it as one word, not three. Create that file with `touch`, then list it.

## What it is / is not

- It is: Bash word-splitting on IFS (space, tab, newline). Single quotes make every character between them literal. The quotes are removed before `touch` runs (quote removal). GNU coreutils `touch` 9.4 creates a missing FILE empty.
- It is not: globbing (next). It is not double quotes vs `$`. It is not `echo`. It is not starting `~/linux-workshop`. It is not teaching `rm` as the lesson — `rm` is only the honest cleanup of the three pieces the unquoted `touch` created.

## Live sources (fetched this pass)

- Wooledge Quotes (edited 2025-08-20) — single quotes remove special meaning; quotes are not passed to the command; unquoted spaces split words. https://mywiki.wooledge.org/Quotes
- ArchWiki Bash — this host’s interactive shell is GNU Bash. https://wiki.archlinux.org/title/Bash
- This host: GNU bash 5.2.21(1)-release. `touch` GNU coreutils 9.4. Local `man bash` / `man touch` are stripped on this minimized image.

## Live operation on this host (2026-08-21)

- IFS bytes: `20 09 0a` (space, tab, newline).
- Throwaway probe in `/tmp` (destroyed): `touch rent-receipts/21 Aug receipt.txt` created `rent-receipts/21` plus `Aug` and `receipt.txt` in the current directory. Quoted `touch 'rent-receipts/21 Aug receipt.txt'` created one empty file whose name contains two spaces.
- Menu-launched xfce4-terminal cwd is `/workspace`. Unquoted `touch /home/ubuntu/rent-receipts/21 Aug receipt.txt` will create `21` in the folder and pollute `/workspace` with `Aug` and `receipt.txt`. Those three names must be removed on camera before the last frames.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.
- `rent-receipts` exists from lesson 25 and is empty. Do not recreate it. Do not pre-create the spaced filename.

## Human job

A person is filing August 2026 rent. The scan should be one file named `21 Aug receipt.txt` inside `rent-receipts`. Without quotes the shell looks broken: three empty files, two of them in the wrong house. Quotes are required so the spaces stay inside the name.

Candidates considered: (1) double quotes around the same path — also works here, but teaches `$` later. (2) backslash-escape each space — ugly and easy to miss. (3) Unquoted `touch` of the real receipt name, show the three pieces, `rm` them, then single-quoted `touch` and `ls -l` of that one file. Picked (3).

## Done on screen

Fullscreen terminal. Unquoted `touch` splits the name. `ls` shows `21` in the folder and `Aug` plus `receipt.txt` in `/workspace`. Those three pieces are removed. Quoted `touch` then quoted `ls -l` hold one empty file: `/home/ubuntu/rent-receipts/21 Aug receipt.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35.

## Viewer must see created on camera

Opening Terminal Emulator, the unquoted `touch` (the mistake), both listings, the cleanup, the quoted `touch`, and the quoted `ls -l` of the one spaced name. Do not seed that file off-camera.
