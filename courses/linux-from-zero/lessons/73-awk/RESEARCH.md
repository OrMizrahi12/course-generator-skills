# Lesson 73 — Extract columns with awk

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 74 here.

## Feature

This host’s `awk` is mawk 1.3.4 (`/usr/bin/awk`, no gawk). Fields on a line: `$5` is the size, `$NF` is the last name. On the real `ls-out.txt` report from lesson 65, `awk '{print $5, $NF}'` prints `92 rent-log.txt`.

## What it is / is not

- It is: one awk print of columns on `ls-out.txt`. Last line `92 rent-log.txt`.
- It is not: `echo`. It is not GNU gawk. It is not `cut -d:` (no colon). It is not nano (next lesson) or tar. Do not rewrite `ls-out.txt`. Lesson 71 already showed `cut -d' '` fails on `ls -l` spaces; awk fields are why this lesson exists.

## Live sources (fetched this pass)

- `awk --version`: mawk 1.3.4 20240123. Package `mawk 1.3.4.20240123-1build1`. No local man page. invisible-island.net mawk(1): “mawk - pattern scanning and text processing language.” Programs are pattern `{action}` pairs. Quote the program so the shell does not eat `$` and braces.
- Live `cat ls-out.txt`: `-rw-r--r-- 2 ubuntu ubuntu 92 Aug 21 22:12 rent-log.txt`. `$5` is `92`. `$NF` is `rent-log.txt`. `awk '{print $5, $NF}' ls-out.txt` prints `92 rent-log.txt`.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- `ls-out.txt` already exists from lesson 65. Feature is extracting its columns, not creating the report.

## Human job

Read the size and name off the saved `ls -l` line. `cut` cannot, because GNU `ls -l` uses runs of spaces.

Candidates considered: (1) awk on passwd with `-F:` — needs a colon. (2) awk on rent-log words — not a column report. (3) cat `ls-out.txt`, print `$NF`, last print `$5, $NF`. Picked (3).

## Done on screen

Fullscreen terminal at `linux-workshop $`. Last `awk '{print $5, $NF}' ls-out.txt` holding `92 rent-log.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite `ls-out.txt`. Do not steal nano.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `cat ls-out.txt`, `awk '{print $NF}' ls-out.txt`, last `awk '{print $5, $NF}' ls-out.txt`.
