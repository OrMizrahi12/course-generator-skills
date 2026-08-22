# Lesson 81 — Put a command on PATH

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 82 here.

## Feature

This session’s PATH is how bash finds a name with no slash. Last `due` (not `./due`) holds `Next due 21 Oct.` after `export PATH="$HOME/linux-workshop:$PATH"`.

## What it is / is not

- It is: Linux finds programs by searching PATH directories. Last frame is `due` by name.
- It is not: `echo`. It is not writing `.bashrc`. It is not compiling again. Do not rewrite `rent-log.txt`. Do not persist PATH across logins.

## Live sources (fetched this pass)

- Chet Ramey bash(1) (https://tiswww.case.edu/php/chet/bash/bash.html): if the name is neither a function nor a builtin and contains no slashes, bash searches each PATH directory for an executable of that name.
- `help export`: export NAME[=value] marks NAME for the environment of later commands.
- Host `due` exists from lesson 80: `/home/ubuntu/linux-workshop/due` ELF pie, prints `Next due 21 Oct.` `type due` is `not found` until PATH includes that directory.
- On this X keyboard, type `:` as Shift+semicolon.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- `due` is already compiled. Do not recreate it. The lesson object is this session’s PATH.

## Human job

Run the workshop due-date program by name from any prompt this session, without typing `./due`.

Candidates considered: (1) copy `due` into `/usr/local/bin` — needs sudo, persists, not “session PATH”. (2) `export PATH="$HOME/linux-workshop:$PATH"` then `due`. Picked (2). Without PATH, bash prints `due: command not found`.

## Done on screen

Fullscreen terminal. Last `due` holding `Next due 21 Oct.` No `./` on that line.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `due.c` and `due` in place. Do not write `.bashrc`. Do not rewrite `rent-log.txt`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `due` failing, `export PATH="$HOME/linux-workshop:$PATH"`, last `due` succeeding.
