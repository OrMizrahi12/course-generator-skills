# Lesson 63 — Watch load and memory

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 64 here.

## Feature

`free` snapshots RAM. `top` shows load and who is using it while a program is still running.

## What it is / is not

- It is: `free -h` on this 15Gi host (swap 0B), start `sha256sum /dev/zero &` as a real hasher, `ps -C sha256sum`, then `top` holding that command and the Mem line.
- It is not: `nice`. It is not `echo`. Do not leave sha256sum running after the take.

## Live sources (fetched this pass)

- `free` from procps-ng 4.0.4. Live `free -h`: Mem 15Gi, used ~2.2Gi, Swap 0B.
- `/usr/bin/top`. Probe `dd` to `/dev/null` finished in milliseconds (46 GB/s) so it never appeared in top. Hasher `sha256sum /dev/zero` stays on CPU.
- GNU coreutils 9.4 `sha256sum`.

## Live operation on this host (2026-08-22)

- Last command: interactive `top` holding `sha256sum` and MiB Mem ~16014.
- After ffmpeg, kill `sha256sum` PIDs by exact name from `/proc`. Do not pkill `-f`.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

See whether this machine still has room while a hasher runs on `/dev/zero`. `free` then `top` are required; a finished `dd` is too fast here.

Candidates considered: (1) `dd` of `/dev/null` — finishes before top. (2) `free` alone — nothing running. (3) `sha256sum /dev/zero &` then `free` and `top`. Picked (3).

## Done on screen

Fullscreen terminal. `free -h` shows 15Gi and Swap 0B. `top` still lists `sha256sum`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. Stop the hasher after the take.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `free -h`, `sha256sum /dev/zero &`, `ps -C sha256sum`, last `top`.
