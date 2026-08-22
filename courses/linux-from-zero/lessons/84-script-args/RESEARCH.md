# Lesson 84 — Make it take arguments and fail honestly

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 85 here.

## Feature

Rewrite `snap.sh` so `$1` is the archive path. With no argument it prints usage on stderr and `exit 1`. With a path it writes the archive and exits 0. Last `ls -l /tmp/workshop-named.tar.gz` holds that file.

## What it is / is not

- It is: arguments, `if`, and a non-zero exit. Last frame is the named archive after a failed run that left `echo $?` as `1`.
- It is not: `echo` as the whole job. It is not a `for` loop. Do not rewrite `rent-log.txt`. Do not invent a second script.

## Live sources (fetched this pass)

- Chet Ramey bash(1): positional parameters `$1`–`$9`; zero exit status means success, non-zero means failure.
- `help if`: if COMMANDS; then COMMANDS; fi. Exit status of the last command executed.
- `help test`: `-z STRING` is true if the string is empty.
- On this X keyboard, `?` is Shift+slash (`echo $?`).

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- `snap.sh` from lesson 83 hard-codes `~/workshop-bak.tar.gz`. Edit it on camera. Do not pre-edit.

## Human job

Name the backup file when you run the script, and refuse a silent default if you forget the name.

Candidates considered: (1) a new `hello.sh` that checks `$1` — smoke test. (2) rewrite `snap.sh` to require `$1`, fail with usage/`exit 1`, then succeed writing `/tmp/workshop-named.tar.gz`. Picked (2). Without `if`/`$1` the script still dumps to a hidden default.

## Done on screen

Fullscreen terminal. After `./snap.sh` with no args, usage on stderr and `echo $?` is `1`. After `./snap.sh /tmp/workshop-named.tar.gz`, `echo $?` is `0`. Last `ls -l /tmp/workshop-named.tar.gz` holds a regular file with size.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Replace `snap.sh` on camera. Leave `due.c` / `due` / `.bashrc` alias. Leave `~/workshop-bak.tar.gz` from lesson 83.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `cat snap.sh`, nano rewrite with `if`/`$1`/`exit 1`, `./snap.sh` failing, `echo $?`, `./snap.sh /tmp/workshop-named.tar.gz`, `echo $?`, last `ls -l /tmp/workshop-named.tar.gz`.
