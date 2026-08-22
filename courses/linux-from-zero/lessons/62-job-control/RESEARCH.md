# Lesson 62 — Park a process in the background

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 63 here.

## Feature

Job control parks a running program: Ctrl+Z stops it, `bg` lets it run behind the prompt, `fg` brings it back, `jobs` lists the parked job.

## What it is / is not

- It is: start `tail -f rent-log.txt` in the foreground, Ctrl+Z, `jobs` shows Stopped, `bg` then `jobs` shows Running, `fg` then Ctrl+Z then `bg` again, last `jobs` still Running.
- It is not: `kill`. It is not `&` as the only park (already used to start). It is not `echo`. Do not pkill the host `/dev/null` tail.

## Live sources (fetched this pass)

- bash builtin `jobs`. `help jobs` on this host. Probe: `tail -f rent-log.txt &` then `jobs` printed `[1]+ Running tail -f rent-log.txt &`. Killed the probe so start stays on camera. Interactive Ctrl+Z is SIGTSTP (HumanInput `ctrl_key('z')`).

## Live operation on this host (2026-08-22)

- Last command: `jobs` holding `[1]+ Running tail -f rent-log.txt &`.
- After the take, stop the filmed rent-log tail off-camera. Leave PID 2619.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Keep watching the rent log, but type other commands. Park the watcher with job control; `&` at start is not the lesson.

Candidates considered: (1) `sleep 90` then jobs — a timer, not the papers. (2) start with `&` only — hides Ctrl+Z/`fg`. (3) foreground `tail -f`, Ctrl+Z, `bg`, `fg`, last `jobs` Running. Picked (3).

## Done on screen

Fullscreen terminal. After Ctrl+Z, `jobs` shows Stopped. After `bg`, Running. Last `jobs` still shows Running `tail -f rent-log.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. After the take, stop the extra `tail`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `tail -f rent-log.txt`, Ctrl+Z, `jobs`, `bg`, `jobs`, `fg`, Ctrl+Z, `bg`, last `jobs`.
