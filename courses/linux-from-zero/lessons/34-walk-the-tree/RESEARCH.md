# Lesson 34 — Walk the tree

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 35 here.

## Feature

Change the shell’s working directory with `cd`: an absolute path from `/`, a relative path with `.`, then one step back with `..`. The prompt and `pwd` move with you.

## What it is / is not

- It is: Bash builtin `cd`. Default DIR is `$HOME`. A DIR that begins with `/` skips `CDPATH`. `.` is this directory. `..` is processed by removing the immediately previous pathname component. After a successful change, `PWD` is the new directory and the prompt’s `\W` shows that basename (`workspace`, `~`, `rent-receipts`).
- It is not: `cd -` / `OLDPWD`. It is not `mkdir`. It is not `echo`. It is not starting `~/linux-workshop`. Listing a distant folder with `ls` is not walking.

## Live sources (fetched this pass)

- This host `help cd` (bash 5.2.21): `cd [-L|[-P [-e]] [-@]] [dir]`. Default DIR is `HOME`. If DIR begins with a slash, `CDPATH` is not used. `..` removes the immediately previous pathname component.
- GNU Bash Reference Manual §4.1 Bourne Shell Builtins — `cd` (static archive of gnu.org, Dec 2024). https://www.gnu.org.cach3.com/software/bash/manual/html_node/Bourne-Shell-Builtins.html (live gnu.org HTML returned 403 from this host)
- Ubuntu Noble POSIX `cd(1posix)` — change the working directory; absolute vs relative; `cd -` is `OLDPWD` and is out of this lesson. https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html

## Live operation on this host (2026-08-21)

- Menu-launched xfce4-terminal cwd is `/workspace`. Prompt is `workspace $`. `pwd` prints `/workspace`.
- `cd /home/ubuntu` (absolute, begins with `/`) → prompt `~ $`. `pwd` → `/home/ubuntu`.
- `cd ./rent-receipts` (relative, `.` plus the papers folder) → prompt `rent-receipts $`. `pwd` → `/home/ubuntu/rent-receipts`.
- `ls` there lists `21 Aug receipt.txt`, `landlord-note.txt`, `late-notice.txt`.
- `cd ..` → prompt `~ $`. `pwd` → `/home/ubuntu`.
- `~/linux-workshop` does not exist. Do not create it.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.
- Keys already in HumanInput: `/` period. No extra keys.

## Human job

A person is standing in the course tree (`/workspace`) and must actually walk to the August rent papers, then one step back to the house. Listing from afar is not enough. `cd` with an absolute path, a relative `.` path, and `..` is required.

Candidates considered: (1) `cd ~` then `cd rent-receipts` — skips teaching a `/` absolute path. (2) `cd -` to bounce — that is `OLDPWD`, not this lesson. (3) `pwd` from `/workspace`, `cd /home/ubuntu`, `pwd`, `cd ./rent-receipts`, `pwd`, `ls` of the three papers, `cd ..`, `pwd` holding `/home/ubuntu`. Picked (3).

## Done on screen

Fullscreen terminal. After walking into `rent-receipts` and listing the three papers, last frames hold `pwd` after `cd ..` printing `/home/ubuntu`, with prompt `~ $`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35. Do not create `~/linux-workshop`.

## Viewer must see created on camera

Opening Terminal Emulator, `pwd` from `/workspace`, `cd /home/ubuntu`, `cd ./rent-receipts`, `ls` of the papers, `cd ..`, and `pwd` of `/home/ubuntu`. Do not `cd` off-camera to fake a home prompt.
