# Lesson 78 — See where apt looks for software

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 79 here.

## Feature

Ubuntu 24.04 stores apt sources in deb822 `/etc/apt/sources.list.d/ubuntu.sources`. `sources.list` only says they moved. Last `grep '^URIs'` holds `archive.ubuntu.com` and `security.ubuntu.com`.

## What it is / is not

- It is: read where apt is allowed to fetch. Last frame is the two Ubuntu URIs, not an `apt update`.
- It is not: `echo`. It is not `ldd`. It is not editing sources. It is not Chrome. Do not type a colon. Do not rewrite `rent-log.txt`.

## Live sources (fetched this pass)

- Ubuntu noble `sources.list(5)`: `/etc/apt/sources.list` and `/etc/apt/sources.list.d/` list sources; `.list` is one-line style, `.sources` is deb822. Filenames may only use letters, digits, `_`, `-`, `.`. (`https://manpages.ubuntu.com/manpages/noble/man5/sources.list.5.html`) No local man page.
- Live `/etc/apt/sources.list` (270 bytes) is four comments: sources moved to `/etc/apt/sources.list.d/ubuntu.sources` in deb822.
- Live `ubuntu.sources`: Types `deb`; URIs `http://archive.ubuntu.com/ubuntu/` and `http://security.ubuntu.com/ubuntu/`; Suites `noble noble-updates noble-backports` and `noble-security`; Components `main universe restricted multiverse`.
- `ls /etc/apt/sources.list.d` also shows host `google-chrome.list` and `google-chrome.sources`. Honest, not the lesson.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Read only. Do not write sources. Do not `apt update`.

## Human job

Find where apt is allowed to look, because a package cache is policy, not magic.

Candidates considered: (1) `apt-cache policy` — long, colon-heavy output. (2) dump all of `ubuntu.sources` — comments scroll off. (3) `ls /etc/apt`, `cat sources.list`, `ls sources.list.d`, `grep '^URIs' ubuntu.sources`. Picked (3). Without reading those files the viewer never sees the warehouse.

## Done on screen

Fullscreen terminal at `~ $`. Last `grep '^URIs' /etc/apt/sources.list.d/ubuntu.sources` holding:

```
URIs: http://archive.ubuntu.com/ubuntu/
URIs: http://security.ubuntu.com/ubuntu/
```

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite `rent-log.txt`. Leave psmisc installed. Leave sources unchanged.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `ls /etc/apt`, `cat /etc/apt/sources.list`, `ls /etc/apt/sources.list.d`, last `grep '^URIs' /etc/apt/sources.list.d/ubuntu.sources`.
