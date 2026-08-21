# Lesson 38 — Read a file without breaking it

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 39 here.

## Feature

Read a file without opening an editor. GNU `cat` dumps the whole file. GNU `head` prints the start. GNU `tail` prints the end. GNU `less` pages it and `q` leaves without writing. Looking is safer than editing.

## What it is / is not

- It is: GNU coreutils 9.4 `cat`, `head -n`, `tail -n` on the real `rent-log.txt`, then GNU `less` (package `less` 590-2ubuntu2.1) as a pager. This minimized Ubuntu has no `less` until it is installed. `q` quits less. The note is not rewritten.
- It is not: `echo`. It is not nano Write Out. It is not `cp`/`mv`/`rm`. It is not installing `less` off-camera. It is not a hidden-file lesson.

## Live sources (fetched this pass)

- Ubuntu Noble `cat(1)` — concatenate files and print on the standard output. coreutils 9.4. https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html
- Ubuntu Noble `head(1)` — output the first part of files. Default 10 lines; `-n NUM` sets the count. https://manpages.ubuntu.com/manpages/noble/man1/head.1.html
- Ubuntu Noble `tail(1)` — output the last part of files. Default 10 lines; `-n NUM` sets the count. https://manpages.ubuntu.com/manpages/noble/man1/tail.1.html
- Ubuntu Noble `less(1)` — opposite of more. https://manpages.ubuntu.com/manpages/noble/man1/less.1.html
- This host: `cat`/`head`/`tail` are GNU coreutils 9.4. `less` is not installed (`command not found`). Candidate package `less` 590-2ubuntu2.1. `more` exists and is not the lesson object. `/tmp` probe (deleted): `cat` dumped four lines; `head -n 2` the first two; `tail -n 1` the last.

## Live operation on this host (2026-08-21)

- `~/linux-workshop/rent-log.txt` exists (92 bytes, three rent sentences). Do not edit it. `sep-due-draft.txt` also exists from lesson 37; leave it.
- Menu-launched xfce4-terminal cwd is `/workspace`. `cd ~/linux-workshop`.
- `cat rent-log.txt` prints the three sentences to the terminal.
- `head -n 2 rent-log.txt` prints the first two lines. `tail -n 1 rent-log.txt` prints `Next due 21 Sep.`
- `less rent-log.txt` fails with `command not found` until `sudo apt-get install -y less` finishes. Then `less rent-log.txt` pages the note. `q` returns to the prompt. The file is unchanged.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person needs to read the paid-August rent log without opening nano, which can accidentally change it. `cat` shows the whole note. `head` and `tail` peek at the start and the due date. `less` is the pager for looking, and on this minimized image it must be installed first. Without those tools they would edit to look.

Candidates considered: (1) `echo` the note — smoke test, forbidden. (2) `more` — installed here, not the syllabus pager. (3) `cd ~/linux-workshop`, `cat`/`head`/`tail` the real note, install `less` on camera after `command not found`, page the note, `q`, `tail -n 1` still shows the due date. Picked (3).

## Done on screen

Fullscreen terminal. Cwd `~/linux-workshop`. `tail -n 1 rent-log.txt` prints `Next due 21 Sep.` The note was looked at, not rewritten.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

`rent-log.txt` already exists from lesson 36. Do not Write Out. Do not `rm`. Install `less` on camera.

## Viewer must see created on camera

Opening Terminal Emulator, walking into the workshop, `cat`/`head`/`tail` of the real note, `less` missing, `apt-get install` of `less`, paging the note, `q`, and `tail -n 1` still showing the due date.
