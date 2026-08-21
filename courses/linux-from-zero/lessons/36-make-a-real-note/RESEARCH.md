# Lesson 36 — Make a real note

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 37 here.

## Feature

Write a file with real sentences in the empty workshop. GNU nano 7.2 is the editor. Write Out (`^O`) puts the words on disk. A file is a noun: the note exists after save.

## What it is / is not

- It is: GNU nano 7.2 opening a new buffer named `rent-log.txt`, typing real rent facts, then `^O` Write Out. Ubuntu Noble nano 7.2-2ubuntu0.2. The two bottom lines show `^O Write Out` and `^X Exit`.
- It is not: `echo`. It is not `hello.txt`. It is not `cat`/`less` as the lesson object (reading is later). It is not `cp`/`mv`/`rm`. It is not creating the file off-camera.

## Live sources (fetched this pass)

- Ubuntu Noble `nano(1)` — Nano's ANOther editor, inspired by Pico. Commands use Control. https://manpages.ubuntu.com/manpages/noble/man1/nano.1.html
- GNU nano 7 manual — https://www.nano-editor.org/dist/v7/nano.html
- This host: `nano --version` → GNU nano 7.2. Probe in `/tmp` (deleted): fullscreen nano shows title `GNU nano 7.2`, help `^O Write Out` and `^X Exit`, empty white buffer.

## Live operation on this host (2026-08-21)

- `~/linux-workshop` exists and is empty (`.` and `..` only). Do not seed `rent-log.txt`.
- Menu-launched xfce4-terminal cwd is `/workspace`. `cd ~/linux-workshop` then `nano rent-log.txt`.
- Type three real lines. `^O`, Enter confirms `File Name to Write: rent-log.txt`. Status: Wrote N lines.
- Last frames hold the saved note in nano so the words are visible. Do not exit before the hold.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person just opened an empty workshop. They need a written log that 21 Aug rent is paid, where the three papers live, and when the next due date is. An empty directory cannot store that. Nano Write Out is required.

Candidates considered: (1) `echo paid > file` — smoke test, forbidden. (2) mousepad GUI — extra window, not the terminal path this act uses. (3) `cd ~/linux-workshop`, `ls` empty, `nano rent-log.txt`, type the three rent facts, `^O` Write Out, hold on the saved sentences. Picked (3).

## Done on screen

Fullscreen GNU nano 7.2. Title names `rent-log.txt`. Three rent sentences visible. Write Out has run. Help line still shows `^O Write Out`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

`~/linux-workshop` already exists from lesson 35. The note is created on camera.

## Viewer must see created on camera

Opening Terminal Emulator, walking into the empty workshop, `nano rent-log.txt`, the typed sentences, and Write Out.
