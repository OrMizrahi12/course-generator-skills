# Lesson 76 — Install a real tool with apt and use it

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 77 here.

## Feature

apt 2.8.3 searches the Ubuntu noble cache for `psmisc`, `sudo apt install` fetches 23.7-1build1, and `pstree` then draws this shell’s ancestors. Last `pstree -A -s $$` holds the tree.

## What it is / is not

- It is: search, install, then run a command that was missing. Last frame is `pstree`, not the apt progress bar.
- It is not: `echo`. It is not `dpkg -L` or a long `apt show` (next lesson). It is not gcc. Do not type a colon. Do not `apt upgrade`.

## Live sources (fetched this pass)

- `apt --version`: apt 2.8.3 `/usr/bin/apt`. Ubuntu package 2.8.3. No local man page. Ubuntu noble manpage: `search` looks up regex in available packages; `install` performs the action; prefer `apt-cache`/`apt-get` in scripts, `apt` is the end-user interface.
- `apt-cache search pstree` is empty on this host (short Description does not mention pstree). `apt-cache search psmisc` hits `psmisc - utilities that use the proc file system`. Policy: Installed (none), Candidate 23.7-1build1 from `http://archive.ubuntu.com/ubuntu noble/main`.
- Simulate: `The following NEW packages will be installed: psmisc`. Homepage http://psmisc.sf.net/. `command -v pstree` is missing until install.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- `sudo -n true` works. Do not create the package off-camera.

## Human job

Get `pstree` onto this machine because lesson 60 had to use `ps --forest`. Search the package, install it, run it on this shell.

Candidates considered: (1) install `tree` and list the workshop — weaker callback. (2) install psmisc, run pstree on `$$`. Picked (2). Without apt the binary does not exist.

## Done on screen

Fullscreen terminal at `~ $`. Last `pstree -A -s $$` holding an ASCII ancestor tree that includes this bash.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite `rent-log.txt`. Leave psmisc installed.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `type pstree`, `apt-cache search psmisc`, `sudo apt install psmisc`, confirm Y, wait until unpack finishes, `type pstree`, last `pstree -A -s $$`.
