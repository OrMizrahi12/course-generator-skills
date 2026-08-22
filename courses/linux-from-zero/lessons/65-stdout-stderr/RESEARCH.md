# Lesson 65 — Catch stdout and stderr

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 66 here.

## Feature

A command has two outgoing streams. `>` catches stdout. `2>` catches stderr. `/dev/null` throws a stream away.

## What it is / is not

- It is: run a real `ls` of the workshop rent log plus a missing name, catch the listing into `ls-out.txt`, catch the missing-name noise into `ls-err.txt`, then send both streams to `/dev/null`.
- It is not: `echo`. It is not a pipe (`|`). It is not `&>`. Do not pre-create the two papers.

## Live sources (fetched this pass)

- GNU bash 5.2.21-2ubuntu4 on this host. Chet Ramey’s bash(1) (2025 April 7): REDIRECTION — operators are processed left to right; omitted number before `>` is fd 1 (stdout); `2>` is stderr; `ls > dirlist 2>&1` vs `ls 2>&1 > dirlist` order example.
- Linux man-pages 6.7 `null(4)`: data written to `/dev/null` is discarded. This host’s `/dev/null` is character special `(1/3)`.
- GNU coreutils `ls`: listing of a missing name writes the listing on stdout and `cannot access` on stderr, exit 2.

## Live operation on this host (2026-08-22)

- `ls -l rent-log.txt nosuch-sep.txt` prints the rent-log line on stdout and `ls: cannot access 'nosuch-sep.txt': No such file or directory` on stderr, exit 2.
- `> ls-out.txt` alone still leaves the missing-name line on the terminal; the paper holds only the listing.
- `> ls-out.txt 2> ls-err.txt` splits them. `> /dev/null 2> /dev/null` silences both; exit is still 2.
- Probe papers in `/tmp` were deleted. Workshop `ls-out.txt` / `ls-err.txt` must be created on camera.

## Human job

Keep the rent-log listing and the missing-name noise as two workshop papers, then throw the same command’s streams into `/dev/null`. Without redirect, stderr pollutes the listing.

Candidates considered: (1) `echo` into a file — smoke test. (2) `ls` of only a missing name — no stdout paper. (3) rent-log plus missing `nosuch-sep.txt`, split, then `/dev/null`. Picked (3).

## Done on screen

Fullscreen terminal. Last `ls -l ls-out.txt ls-err.txt` holds both papers. The `/dev/null` command just above produced no listing and no noise.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. Leave `ls-out.txt` and `ls-err.txt` after the take. If a failed take creates them, remove them off-camera so `>` creation stays on camera.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, unredirected `ls` of both names, stdout-only redirect, `cat ls-out.txt`, split `2>`, both cats, `/dev/null` of both streams, last `ls -l` of the two papers.
