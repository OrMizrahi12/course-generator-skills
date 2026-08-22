# Lesson 44 — See file types

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 45 here.

## Feature

The first character of `ls -l` is a map: `-` regular file, `d` directory, `l` symbolic link, `c` character device (and `b` block). You read that letter on real names.

## What it is / is not

- It is: `ls -l` / `ls -ld` of this machine’s rent log, workshop directory, `/etc/os-release` symlink, and `/dev/null`, then one last `ls -ld` of all four so `-` `d` `l` `c` sit together.
- It is not: `echo`. It is not `file` as the last verb (lesson 43). It is not inodes or link counts (next lesson). It is not creating a symlink (later). It is not `cat /dev/vda`.

## Live sources (fetched this pass)

- GNU coreutils info on this host (`coreutils.info.gz`, “What information is listed”): the file type is one of `-` regular file, `b` block special, `c` character special, `d` directory, `l` symbolic link, `p` FIFO, `s` socket, and a few exotic letters. https://www.gnu.org/software/coreutils/manual/html_node/What-information-is-listed.html
- `ls(1)` on this host (coreutils 9.4): `-l` long listing; `-d` list directories themselves. Default sort is alphabetical when several names are given.
- This host (2026-08-22): `ls -l ~/linux-workshop/rent-log.txt` starts with `-`. `ls -ld ~/linux-workshop` starts with `d`. `ls -l /etc/os-release` starts with `l` and shows `-> ../usr/lib/os-release`. `ls -l /dev/null` starts with `c`. One `ls -ld` of those four names prints, after GNU sort: `/dev/null` `c`, `/etc/os-release` `l`, workshop `d`, rent-log `-`.

## Live operation on this host (2026-08-22)

- Workshop files stay. Do not create, move, or delete them. Do not make a new symlink.
- Menu-launched xfce4-terminal cwd is `/workspace`.
- Type `~/linux-workshop/...` (tilde expands). No colon.
- Last command: `ls -ld ~/linux-workshop/rent-log.txt ~/linux-workshop /etc/os-release /dev/null` with four first characters visible.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person has a rent note, a workshop folder, a config name that is a pointer, and `/dev/null`. They need to tell those four kinds apart from `ls -l` without guessing from the name. The first character is required; `file` already named `/dev/null` in lesson 43.

Candidates considered: (1) `echo - d l c` — smoke test, forbidden. (2) `file` again on `/dev/null /dev/vda` — last frame of 43. (3) `ls -l` each of the four live names, then one `ls -ld` of all four. Picked (3).

## Done on screen

Fullscreen terminal. `ls -ld` of the four names shows first characters `c` `l` `d` `-` on `/dev/null`, `/etc/os-release`, the workshop, and `rent-log.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the three papers and the hidden note. Nothing new is written.

## Viewer must see created on camera

Opening Terminal Emulator, `ls -l` of the rent log, `ls -ld` of the workshop, `ls -l` of `/etc/os-release`, `ls -l` of `/dev/null`, and the four-name `ls -ld`.
