# Lesson 32 — Find home

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 33 here.

## Feature

Print where you are standing with `pwd`, then name the user’s house with unquoted `~` and with `"$HOME"`, and prove the rent-receipts folder lives under that house.

## What it is / is not

- It is: Bash builtin `pwd` prints the current working directory. Unquoted `~` is tilde expansion: replaced with `$HOME`. `"$HOME"` is the same path as a variable. `getent passwd ubuntu` on this host lists home `/home/ubuntu`. Quoted `'~'` or `"~"` does not expand.
- It is not: `cd` (next walk). It is not `echo $HOME`. It is not starting `~/linux-workshop`. It is not `printenv` as the lesson object.

## Live sources (fetched this pass)

- Ubuntu Noble `pwd(1)` — GNU coreutils 9.4; print the current working directory. A shell builtin usually supersedes the binary. https://manpages.ubuntu.com/manpages/noble/man1/pwd.1.html
- ArchWiki Environment variables — `HOME` contains the path to the home directory of the current user. https://wiki.archlinux.org/title/Environment_variables
- This host: `pwd` is a shell builtin (`pwd [-LP]`). `getent passwd ubuntu` → `Ubuntu:/home/ubuntu:/bin/bash`.

## Live operation on this host (2026-08-21)

- Menu-launched xfce4-terminal cwd is `/workspace`. `pwd` prints `/workspace`. That is not home.
- `ls -ld ~` and `ls -ld "$HOME"` both print `drwxr-x--- … /home/ubuntu`.
- `ls -ld "$HOME/rent-receipts"` prints the directory that already holds the August papers.
- `ls -ld '~'` and `ls -ld "~"` fail: `cannot access '~'`. Quotes freeze the tilde, same class of mistake as quoting `*` in lesson 31.
- Do not `cd`. Do not create `~/linux-workshop`.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.
- Keys: `~` is Shift+grave, `$` is Shift+4, `"` is Shift+quotedbl.

## Human job

A person opened a terminal from the desktop to get back to August rent papers. The prompt says `workspace $`. They are standing in the course tree, not in the house. `pwd`, `~`, and `$HOME` are required to name the house that already holds `rent-receipts` without walking there yet.

Candidates considered: (1) `echo $HOME` — smoke test. (2) `cd ~` — that is walking, taught later. (3) `pwd`, `ls -ld ~`, `ls -ld "$HOME"`, then `ls -ld "$HOME/rent-receipts"` as proof the papers live under that house. Picked (3).

## Done on screen

Fullscreen terminal. `pwd` prints `/workspace`. `ls -ld ~` and `ls -ld "$HOME"` both name `/home/ubuntu`. Last frames hold `ls -ld "$HOME/rent-receipts"` printing that directory.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35.

## Viewer must see created on camera

Opening Terminal Emulator, `pwd`, unquoted `~`, quoted `"$HOME"`, and `ls -ld "$HOME/rent-receipts"`. Do not `cd` off-camera to fake a home prompt.
