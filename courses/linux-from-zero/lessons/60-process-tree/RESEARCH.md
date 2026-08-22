# Lesson 60 — See the process tree

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 61 here.

## Feature

A process has a parent. `ps` can print PID and PPID, and `--forest` draws the child under the parent.

## What it is / is not

- It is: start `tail -f rent-log.txt &`, `echo $$` is the shell, `ps --ppid $$` lists the tail as a child, `ps --forest -C bash,tail` draws `\_ tail -f rent-log.txt`.
- It is not: `pstree` (not installed; do not apt). It is not `kill`. It is not `jobs`. It is not `echo` as the example.

## Live sources (fetched this pass)

- `ps` from procps-ng 4.0.4. `pstree` is missing. Probe: `ps -o pid,ppid,cmd --ppid $$` listed `tail -f rent-log.txt` as the child; `ps --forest -C bash,tail` drew `\_ tail -f rent-log.txt`. Killed the probe so start stays on camera.

## Live operation on this host (2026-08-22)

- Last command: `ps --forest -o pid,ppid,cmd -C bash,tail` holding the `\_ tail -f rent-log.txt` line.
- `echo $$` uses dollar. Ampersand starts tail. No colon.
- If a leftover `tail -f` of the log is running before ffmpeg, kill those PIDs off-camera.
- After the take, stop the filmed `tail`.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

The rent log is being watched. Show that the watcher is a child of this shell, not an orphan.

Candidates considered: (1) install pstree with apt — later package act. (2) `ps` of PID 1 only — not a process they started. (3) start tail again and prove PPID with `--forest`. Picked (3).

## Done on screen

Fullscreen terminal. `echo $$` prints the bash PID. `--ppid $$` lists `tail -f rent-log.txt`. Last forest line shows `\_ tail -f rent-log.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. After the take, stop the extra `tail`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `echo $$`, `tail -f rent-log.txt &`, `ps --ppid $$`, last forest `ps`.
