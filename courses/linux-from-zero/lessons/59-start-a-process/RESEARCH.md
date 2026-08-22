# Lesson 59 — Start a program and find its process

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 60 here.

## Feature

A started program is a process. `ps` lists it by name while it is still running.

## What it is / is not

- It is: `tail -f rent-log.txt &` then `ps -C tail` showing that command. The kernel is keeping it alive.
- It is not: `jobs` / `fg` / `bg` (later). It is not `pstree`. It is not `echo`. Do not kill it on camera (that is later).

## Live sources (fetched this pass)

- `ps` from procps-ng 4.0.4. Probe: `sleep 180 &` then `ps -C sleep -o pid,user,cmd` listed `ubuntu sleep 180`; killed the probe so the start stays on camera.
- Human job uses `tail -f` on the real rent log, not `sleep`.

## Live operation on this host (2026-08-22)

- Last command: `ps -C tail -o pid,user,cmd` holding `tail -f rent-log.txt`.
- Ampersand is typed (HumanInput NAMED). Colon is not.
- If a leftover `tail -f` of the log is running before ffmpeg, kill those PIDs off-camera so start is on camera.
- After the take, stop the filmed `tail` off-camera so later lessons are not blocked.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Keep the rent log on screen while other work continues. Start `tail -f rent-log.txt` in the background, then find that running program with `ps`.

Candidates considered: (1) `sleep 180` — a timer, not the workshop papers. (2) `ps` of xfce4-terminal only — they did not start a second program. (3) `tail -f` of rent-log.txt — watching a real note. Picked (3).

## Done on screen

Fullscreen terminal in `~/linux-workshop`. `tail -f` starts. `ps -C tail -o pid,user,cmd` holds `tail -f rent-log.txt` under ubuntu.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. Leave the hard link and symlink. After the take, stop the extra `tail`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `tail -f rent-log.txt &`, `ps -C tail`, last `ps -C tail -o pid,user,cmd`.
