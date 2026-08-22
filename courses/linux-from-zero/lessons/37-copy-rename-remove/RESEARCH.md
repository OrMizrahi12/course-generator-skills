# Lesson 37 — Copy, rename, and remove on purpose

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 38 here.

## Feature

Copy, rename, and remove files on purpose without destroying the project. GNU `cp` makes a second file. GNU `mv` changes a name. GNU `rm` unlinks a file. The original rent log must still exist after all three.

## What it is / is not

- It is: GNU coreutils 9.4 `cp SOURCE DEST`, `mv SOURCE DEST`, and `rm FILE` on regular files in `~/linux-workshop`. Copy the paid-August note, rename that copy to a September draft name, then remove a mistaken extra copy. The original `rent-log.txt` stays.
- It is not: `echo`. It is not `rm -r` on the workshop. It is not deleting `rent-log.txt`. It is not `cat`/`less` as the lesson object. It is not creating the copy off-camera.

## Live sources (fetched this pass)

- Ubuntu Noble `cp(1)` — copy files and directories. coreutils 9.4-3ubuntu6.2. `cp SOURCE DEST`. https://manpages.ubuntu.com/manpages/noble/man1/cp.1.html
- Ubuntu Noble `mv(1)` — rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY. https://manpages.ubuntu.com/manpages/noble/man1/mv.1.html
- Ubuntu Noble `rm(1)` — remove (unlink) FILE(s). By default does not remove directories. https://manpages.ubuntu.com/manpages/noble/man1/rm.1.html
- This host: `cp --version`, `mv --version`, `rm --version` → GNU coreutils 9.4. `/tmp` probe (deleted): `cp orig.txt copy.txt`, `mv copy.txt renamed.txt`, `rm oops.txt` left orig + renamed.

## Live operation on this host (2026-08-21)

- `~/linux-workshop/rent-log.txt` exists from lesson 36 (92 bytes, three rent sentences). Do not delete it. Do not seed `sep-draft.txt`, `sep-due-draft.txt`, or `oops.txt`.
- Menu-launched xfce4-terminal cwd is `/workspace`. `cd ~/linux-workshop` then `ls` shows `rent-log.txt`.
- `cp rent-log.txt sep-draft.txt` is silent on success. `ls` then shows both names.
- `mv sep-draft.txt sep-due-draft.txt` is silent. `ls` then shows the new name; `sep-draft.txt` is gone.
- `cp rent-log.txt oops.txt` makes a mistaken extra copy. `rm oops.txt` unlinks only that extra. `ls -l` then shows `rent-log.txt` and `sep-due-draft.txt` only.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person has a paid-August rent log. They need a September working copy they can change later without losing the paid note, they need that copy named clearly, and they need to throw away a mistaken extra copy. Without `cp` they would overwrite or rewrite. Without `mv` the draft keeps a vague name. Without `rm` the extra copy stays.

Candidates considered: (1) `echo copy > file` — smoke test, forbidden. (2) `rm rent-log.txt` — destroys the project. (3) `cd ~/linux-workshop`, `cp` the real note, `mv` the copy to `sep-due-draft.txt`, `cp` a mistaken `oops.txt`, `rm oops.txt`, `ls -l` proving the original remains. Picked (3).

## Done on screen

Fullscreen terminal. Cwd `~/linux-workshop`. `ls -l` shows `rent-log.txt` and `sep-due-draft.txt`. `oops.txt` is gone. The original note is still listed.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

`~/linux-workshop/rent-log.txt` already exists from lesson 36. Copies and the extra `oops.txt` are created on camera. Only `oops.txt` is removed.

## Viewer must see created on camera

Opening Terminal Emulator, walking into the workshop, `cp`, `mv`, the mistaken extra copy, `rm` of that extra, and `ls -l` with the original still there.
