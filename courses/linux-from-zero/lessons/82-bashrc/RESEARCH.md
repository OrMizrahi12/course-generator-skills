# Lesson 82 — Make the shell remember you

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 83 here.

## Feature

Write `alias due=/home/ubuntu/linux-workshop/due` into `~/.bashrc`, `source` it, then `due` by name from `~ $`. Last `due` holds `Next due 21 Oct.`

## What it is / is not

- It is: bashrc is how an interactive shell remembers you. Last frame is the later command after the alias exists on disk.
- It is not: `echo`. It is not a session-only `export PATH` (lesson 81). It is not a backup script. Do not rewrite `rent-log.txt`. Do not rewrite PS1.

## Live sources (fetched this pass)

- Chet Ramey bash(1) (https://tiswww.case.edu/php/chet/bash/bash.html): when an interactive shell that is not a login shell starts, bash reads `~/.bashrc` if it exists. `help alias`: `alias [-p] [name[=value] ...]`.
- This host’s `~/.bashrc` is 5 lines (NVM, PS1, cargo PATH). No `due` alias. `alias due` is `not found`.
- `~/.profile` sources `.bashrc` if the file exists. GNU nano 7.2.
- `due` binary exists from lesson 80 at `/home/ubuntu/linux-workshop/due`.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. xfce4-terminal is interactive and already sources this `.bashrc` (PS1 matches).

## Human job

Run the workshop due-date program by name in this shell after a restart of the prompt, without exporting PATH again.

Candidates considered: (1) `alias ll='ls -l'` — smoke test. (2) persist PATH in bashrc — repeats lesson 81’s object. (3) alias `due` to the workshop binary in `.bashrc`, source, run `due` from home. Picked (3). Without the bashrc line, `due` is not found in a fresh interactive shell.

## Done on screen

Fullscreen terminal at `~ $`. Last `due` holding `Next due 21 Oct.` after `source .bashrc`. Mid-path `type due` shows the alias.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Append one alias line to `.bashrc` on camera. Leave NVM, PS1, and cargo PATH. Leave `due.c` / `due`. Do not write a backup script.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `cat .bashrc`, nano appending the alias, save, `source .bashrc`, `type due`, last `due`.
