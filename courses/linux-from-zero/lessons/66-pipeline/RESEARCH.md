# Lesson 66 — Build a pipeline

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 67 here.

## Feature

A pipe sends one command’s stdout into the next command’s stdin. `ls papers | tee receipt-list.txt` writes a workshop report and still shows the three receipt names.

## What it is / is not

- It is: list the three papers through the `papers` symlink, then pipe that listing into GNU `tee` so a workshop report is written while the names stay on screen.
- It is not: `echo`. It is not `grep` (next lesson). It is not `>` alone. Do not pre-create `receipt-list.txt`.

## Live sources (fetched this pass)

- GNU bash 5.2.21 pipelines: stdout of the left command is connected to stdin of the right. `|` is already a named key here (bar, Shift).
- GNU coreutils 9.4 `tee`: copy stdin to each file and to stdout. Probe: `ls papers | tee` printed the three receipt names and wrote the same three lines to a paper. Probe paper in `/tmp` was deleted.

## Live operation on this host (2026-08-22)

- `ls papers` lists `21 Aug receipt.txt`, `landlord-note.txt`, `late-notice.txt`.
- `ls papers > receipt-list.txt` hides the names; `cat` then shows them.
- `ls papers | tee receipt-list.txt` shows the names while writing the report.
- Workshop `receipt-list.txt` must be created on camera.

## Human job

Keep a workshop report of the three receipt names without losing the listing on screen. `>` alone hides the names. The pipe into `tee` is required.

Candidates considered: (1) `echo | cat` — smoke test. (2) `cat rent-log.txt | head -n 1` — already used head as last-frame family. (3) `ls papers | tee receipt-list.txt`. Picked (3).

## Done on screen

Fullscreen terminal. Last `cat receipt-list.txt` holds the three receipt names.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log. Leave `receipt-list.txt` after the take. If a failed take creates it, remove it off-camera so creation stays on camera.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `ls papers`, redirect-only `>`, `cat` of that paper, `ls papers | tee receipt-list.txt`, last `cat receipt-list.txt`.
