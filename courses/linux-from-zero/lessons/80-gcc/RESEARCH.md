# Lesson 80 — Build a tiny program from source

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 81 here.

## Feature

Write `due.c` in the workshop, compile it with Ubuntu gcc 13.3 (`gcc -o due due.c`), and run `./due`. Last frame is the binary printing `Next due 21 Oct.`

## What it is / is not

- It is: software is not only apt. Last frame is the compiled program’s output, not the C file alone.
- It is not: `echo`. It is not putting `due` on PATH. It is not writing `.bashrc`. Do not type a colon. Do not rewrite `rent-log.txt`. Do not `apt install gcc` (gcc 13.3 is already on this host).

## Live sources (fetched this pass)

- `gcc --version`: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0. `/usr/bin/gcc` → `gcc-13`. No local `man gcc`.
- GNU GCC Overall Options (https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html, fetched 2026-08-22): `-o file` places the primary output in `file`. Without `-o`, the executable is `a.out`.
- `gcc --help`: `-o <file> Place the output into <file>.`
- GNU nano 7.2 is the workshop editor (lessons 36, 74).

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- gcc is already installed. The lesson object is `due.c` and the binary `due`, both created on camera.
- On this X keyboard, XK_less types `>`. Film tools type `<` as Shift+comma.

## Human job

The Sep-to-Oct due line lives in `sep-due-draft.txt`. Print that date from a program the workshop owns, not from cat. Without gcc, there is no binary to run.

Candidates considered: (1) `hello.c` / `a.out` — smoke test. (2) compile `due.c` that prints `Next due 21 Oct.` and run `./due`. Picked (2). Without gcc the task cannot finish.

## Done on screen

Fullscreen terminal in `~/linux-workshop`. Last `./due` holding `Next due 21 Oct.`

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Create `due.c` and `due` on camera. Do not rewrite `rent-log.txt`. Do not copy `due` onto PATH.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, nano writing `due.c` from empty, save, `gcc -o due due.c`, last `./due`.
