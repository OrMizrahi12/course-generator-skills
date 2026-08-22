# Lesson 58 — Do one admin job as sudo

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 59 here.

## Feature

`sudo` runs one command as root, then you are still yourself. Root is a tool, not a new login.

## What it is / is not

- It is: `whoami` → ubuntu, `sudo whoami` → root, `rm -f` of Sam’s `/tmp` scratch fails (sticky), `sudo rm -f` succeeds, `whoami` is still ubuntu, `ls -l` cannot find the file.
- It is not: staying root. It is not apt (later). It is not chown (previous). It is not `echo`. Do not fake a password; this host is NOPASSWD.

## Live sources (fetched this pass)

- Sudo 1.9.15p5. `sudo -l`: `(ALL) NOPASSWD: ALL` for ubuntu on cursor.
- Live: `sudo whoami` prints `root`. `rm -f /tmp/sam-rent-scratch.txt` → Operation not permitted. `sudo rm -f` removes it. `whoami` still `ubuntu`. Restored Sam’s file off-camera so the delete is on camera.

## Live operation on this host (2026-08-22)

- Last command: `ls -l /tmp/sam-rent-scratch.txt` → `No such file or directory`.
- If the scratch is missing before ffmpeg, `sudo -u sam touch` off-camera so `sudo rm` is the on-camera job.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

Sam’s rent scratch is stuck in `/tmp` by the sticky bit. The tray must be cleared. `sudo rm` is required; ubuntu alone cannot delete it.

Candidates considered: (1) `sudo echo` — smoke test. (2) `sudo apt install` — next act. (3) `sudo rm` of the real leftover Sam file from lesson 56, then prove gone and still ubuntu. Picked (3).

## Done on screen

Fullscreen terminal. `sudo whoami` prints `root`. After `sudo rm -f`, `ls -l /tmp/sam-rent-scratch.txt` prints `No such file or directory`. Prompt is still `workspace $`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. After the take, Sam’s `/tmp` scratch is gone. Do not recreate it.

## Viewer must see created on camera

Opening Terminal Emulator, `whoami`, `sudo whoami`, the sticky `rm -f` failure, `sudo rm -f`, `whoami` still ubuntu, last missing-file `ls -l`.
