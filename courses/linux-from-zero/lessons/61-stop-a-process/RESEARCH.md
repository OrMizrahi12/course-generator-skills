# Lesson 61 — Stop a process on purpose

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 62 here.

## Feature

SIGINT (Ctrl+C) and `kill` stop a running program. Then `ps` must miss it.

## What it is / is not

- It is: start `tail -f rent-log.txt` in the foreground, Ctrl+C, `ps` no longer lists that rent-log tail. Then `sleep 90 &` and `kill %1`, `ps -C sleep` is empty.
- It is not: `jobs` / `fg` / `bg`. It is not `pkill` of every tail (would hit `/dev/null`). It is not `echo`.

## Live sources (fetched this pass)

- `/usr/bin/kill`. `kill -l` lists 2) SIGINT. Probe: `kill` on a `sleep` PID left `ps -p` gone. `timeout --signal=INT` on tail printed the rent log then exited. Probe processes killed so start stays on camera.

## Live operation on this host (2026-08-22)

- Last command: `ps -C sleep` with only the header (no sleep row).
- After Ctrl+C, `ps -C tail -o pid,user,cmd` may still show the host `tail -f /dev/null` (PID 2619). That is not the rent-log watcher.
- Do not `pkill -x tail`.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

The rent-log watcher from the last two lessons must stop. Ctrl+C on the live `tail -f`, then `kill` on a parked `sleep`, prove both are gone.

Candidates considered: (1) `pkill tail` — would also stop the host `/dev/null` keeper. (2) SIGINT on the real `tail -f rent-log.txt`, then `kill %1` on `sleep 90`. Picked (2).

## Done on screen

Fullscreen terminal. After Ctrl+C the prompt returns. `ps -C tail` has no `rent-log.txt`. After `kill %1`, `ps -C sleep` has no process row.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. Do not kill PID 2619.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `tail -f rent-log.txt`, Ctrl+C, `ps` of tail, `sleep 90 &`, `kill %1`, last empty `ps -C sleep`.
