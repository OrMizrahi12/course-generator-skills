# Lesson 64 — Change a process’s niceness

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 65 here.

## Feature

`nice -n 19` starts a program that yields the CPU. `ps` shows NI 19 next to NI 0.

## What it is / is not

- It is: start `sha256sum /dev/zero` at default NI 0, then `nice -n 19 sha256sum /dev/zero`, last `ps -o pid,ni,cmd -C sha256sum` holding both.
- It is not: `renice` on every ubuntu process. It is not `echo`. Do not leave the hashers running.

## Live sources (fetched this pass)

- GNU coreutils 9.4 `nice`. util-linux 2.39.3 `renice`. Probe: default hasher NI 0, `nice -n 19` hasher NI 19. Killed both so start stays on camera.
- Targeting a PID with `renice` needs `$()` or a typed number we do not know. Two starts with `nice` prove the NI column without guessing a PID.

## Live operation on this host (2026-08-22)

- Last command: `ps -o pid,ni,cmd -C sha256sum` holding NI 0 and NI 19.
- After ffmpeg, kill `sha256sum` by exact name.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Two hashers of `/dev/zero`. One is polite. `nice` is required so NI is not the same.

Candidates considered: (1) `renice -u ubuntu` — would change node and the shell. (2) `renice` with a hardcoded PID — unknown until run. (3) default hasher plus `nice -n 19`. Picked (3).

## Done on screen

Fullscreen terminal. Last `ps` shows two `sha256sum /dev/zero` lines, NI 0 and NI 19.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. Stop both hashers after the take.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, default `sha256sum /dev/zero &`, first `ps` NI 0, `nice -n 19 sha256sum /dev/zero &`, last `ps` with both NI values.
