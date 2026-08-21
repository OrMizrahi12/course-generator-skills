# Lesson 29 — Use history and completion

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 30 here.

## Feature

Re-run a command you already typed by recalling it from the shell’s history, then finish a path with Tab so you do not retype or misspell a long folder name.

## What it is / is not

- It is: GNU Readline on Bash 5.2.21. Up is `previous-history` (`\e[A`). Tab is `complete` (`\C-i`). Filename completion fills a unique prefix. This host’s default is ordinary previous-history, not history-search-backward.
- It is not: `!!` or `Ctrl-R`. It is not customizing `~/.inputrc`. It is not quoting (next). It is not `echo`. It is not starting `~/linux-workshop`.

## Live sources (fetched this pass)

- ArchWiki Readline — Up shows the last command; Tab attempts to complete the current word; a second Tab lists matches if ambiguous. https://wiki.archlinux.org/title/Readline
- ArchWiki Bash — Tab completion is enabled by default for commands, filenames, and variables. https://wiki.archlinux.org/title/Bash
- SS64 `history` — pressing Up returns previous commands. https://ss64.com/bash/history.html
- Ubuntu Noble `file(1)` 5.45 — classify a file; filesystem tests report a directory. https://manpages.ubuntu.com/manpages/noble/man1/file.1.html

## Live operation on this host (2026-08-21)

- `bind -q previous-history` → `\C-p`, `\eOA`, `\e[A`. `complete` → `\C-i`.
- `compgen -f /home/ubuntu/rent` → only `/home/ubuntu/rent-receipts`. One Tab finishes that name.
- `file /home/ubuntu/rent-receipts` → `/home/ubuntu/rent-receipts: directory`
- New xfce4-terminal still loads `~/.bash_history` (older course commands). After you type a new line in this session, one Up recalls **that** line first. Film types the line on camera before Up.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.
- `rent-receipts` exists from lesson 25. Do not recreate it.

## Human job

A person already listed `rent-receipts` with a long path. They need that listing again before dropping a scan in it, and they must not mistype the folder name. History is required for the re-run; Tab is required to finish `rent` into `rent-receipts` on a new `file` check that proves it is a directory, not a file they might overwrite.

Candidates considered: (1) `Ctrl-R` — incremental search, extra UI, not the first habit. (2) `!!` — hidden, easy to fire the wrong line. (3) Type `ls -ld /home/ubuntu/rent-receipts`, Up+Return, then `file /home/ubuntu/rent`+Tab+Return. Picked (3).

## Done on screen

Fullscreen terminal. The long `ls -ld` line typed once, recalled with Up, run again. Then `file /home/ubuntu/rent` completed by Tab and run. Last frames hold `file` printing `directory`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35.

## Viewer must see created on camera

Opening Terminal Emulator, typing the first full command (that is the history entry), Up recalling it, typing the `file` prefix, Tab expanding it, and the printed `directory` line. Do not seed that `file` command off-camera.
