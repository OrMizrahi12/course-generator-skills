# Lesson 86 — Put a function in the script

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 87 here.

## Feature

Write `twice.sh` with a `pack()` function. Call `pack` twice with two archive paths. Last `ls -l` holds both files.

## What it is / is not

- It is: `name () { COMMANDS ; }` used twice. Same body. Two destinations.
- It is not: `echo` as the whole job. It is not a `for` loop (already filmed). It is not a cron timer. Do not rewrite `snap.sh`.

## Live sources (fetched this pass)

- `help function`: `function name { COMMANDS ; }` or `name () { COMMANDS ; }`. When invoked, arguments become `$1`…`$n`. Runs in the calling shell.
- Chet Ramey bash(1): functions execute in the calling shell; no new process. Positional parameters are replaced during the call.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Do not create `twice.sh` off camera. `{` `}` `(` `)` type on this keyboard.

## Human job

Pack the workshop twice, to two names, without copying the tar line.

Candidates considered: (1) a function that echoes hello twice — smoke test. (2) `pack()` wrapping `tar -czf "$1" … linux-workshop`, called for `/tmp/workshop-fn-a.tar.gz` and `/tmp/workshop-fn-b.tar.gz`. Picked (2). Without the function they would paste the tar line twice.

## Done on screen

Fullscreen terminal. `twice.sh` contains `pack()` and two calls. `./twice.sh` returns. Last `ls -l /tmp/workshop-fn-a.tar.gz /tmp/workshop-fn-b.tar.gz` holds two regular files with sizes.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `snap.sh` (args/`if`) and `receipt-loop.txt`. Create `twice.sh` on camera.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, nano `twice.sh` with `pack()` used twice, `chmod +x`, `./twice.sh`, last `ls -l` of both archives.
