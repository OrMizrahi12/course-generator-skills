# Lesson 87 — Repeat a job without sitting there

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 88 here.

## Feature

Write `repeat-snap.sh`: a `while` loop that runs `snap.sh` three times with `sleep 1`, appending `date '+%F %T'` to `snap-repeat.log` each pass. Last `cat snap-repeat.log` holds three timestamps.

## What it is / is not

- It is: repeating a real backup without a person watching each click. This host has **no crontab** and **no systemd user bus**. PID 1 is `tini`. The honest scheduler here is a loop plus a log.
- It is not: `echo` as the whole job. It is not a fake `systemctl enable --user` timer. It is not `crontab` (the binary is not installed). It is not a `for` over receipt files (lesson 85). Do not rewrite `snap.sh`. Do not pretend this is lesson 99’s dated workshop archive.

## Live sources (fetched this pass)

- `help while`: `while COMMANDS; do COMMANDS-2; done`. Runs COMMANDS-2 while COMMANDS exits zero.
- GNU `sleep --help`: pause for NUMBER seconds. Suffix `s` is the default.
- GNU `date --help`: `+FORMAT`. Live `date '+%F %T'` prints `2026-08-22 12:31:00`.
- Probe: `crontab` not found. `systemctl is-system-running` → `offline`. `systemctl --user` → Failed to connect to bus. `/proc/1/comm` is `tini`.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. Display 1920×1080.
- `snap.sh` from lesson 84 requires `$1`. Call it with `/tmp/workshop-repeat.tar.gz`. Do not create `repeat-snap.sh` or `snap-repeat.log` off camera.

## Human job

Take three snapshots a second apart and leave a written trail so you can walk away.

Candidates considered: (1) invent a crontab line that never runs — a lie. (2) `systemctl --user` timer — the bus is missing. (3) `while` + `sleep 1` + `date` log + `snap.sh` three times. Picked (3). Without the loop they would sit and type `./snap.sh` three times.

## Done on screen

Fullscreen terminal. `./repeat-snap.sh` returns. Last `cat snap-repeat.log` holds three `YYYY-MM-DD HH:MM:SS` lines.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `snap.sh` / `twice.sh` / `due`. Create `repeat-snap.sh` and `snap-repeat.log` on camera.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, nano `repeat-snap.sh` with `while`/`sleep`/`date`/`snap.sh`, `chmod +x`, `./repeat-snap.sh`, last `cat snap-repeat.log`.
