# Lesson 52 — Add a person to this Linux

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 53 here.

## Feature

`sudo adduser` creates a real login: home directory, primary group, passwd line. Prove the person exists with `getent passwd`, `id`, and `ls -ld` of their home.

## What it is / is not

- It is: `sudo adduser --disabled-password --comment Sam sam`, wait for adduser to finish, then `getent passwd sam` → `sam:x:1001:1001:Sam,,,:/home/sam:/bin/bash`, `id sam`, `ls -ld /home/sam`.
- It is not: `echo`. It is not faking sudo. It is not chmod (next lesson). It is not creating Sam off-camera.

## Live sources (fetched this pass)

- `adduser` 3.137ubuntu1 on this host. Non-interactive: `--disabled-password --comment Sam`. Live run created group `sam` (1001), user `sam` (1001), home `/home/sam`, shell `/bin/bash`, extra group `users`, then `deluser --remove-home` so creation stays on camera.
- `useradd -m -c Sam sam` also works here but defaults shell to `/bin/sh`. Ubuntu’s wrapper is `adduser`.
- `sudo -n true` works (passwordless). Do not fake a prompt.

## Live operation on this host (2026-08-22)

- After adduser, `ls /home/sam` as ubuntu is permission-denied (`drwxr-x---`). `ls -ld /home/sam` is readable.
- Last command: `getent passwd sam` with home `/home/sam` and shell `/bin/bash`.
- If a leftover `sam` exists before ffmpeg, `deluser --remove-home` off-camera so adduser is on camera.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.

## Human job

The landlord’s helper Sam needs a login on this machine so they can later look at the rent papers as themselves. `adduser` is required; a folder named sam is not a person.

Candidates considered: (1) `echo sam` — smoke test. (2) `useradd` without home — incomplete person. (3) `sudo adduser --disabled-password --comment Sam sam` then prove passwd, id, and home. Picked (3).

## Done on screen

Fullscreen terminal. `getent passwd sam` prints `sam:x:1001:1001:Sam,,,:/home/sam:/bin/bash`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log or papers. Leave `sam` after the take (later lessons may chown to them).

## Viewer must see created on camera

Opening Terminal Emulator, `sudo adduser --disabled-password --comment Sam sam`, adduser info lines, `getent passwd sam`, `id sam`, `ls -ld /home/sam`.
