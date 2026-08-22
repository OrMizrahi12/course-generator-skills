# Lesson 70 — Feed names into the next command

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 71 here.

## Feature

`xargs` reads names from standard input and runs the next command with those names as arguments. GNU xargs splits on blanks by default, so `21 Aug receipt.txt` breaks. `-print0` plus `xargs -0` keeps each name whole.

## What it is / is not

- It is: findutils 4.9.0 `xargs` on the three rent receipts. Broken `find | xargs ls -l` cannot access `21`. Last `-print0 | xargs -0 ls -l` holds all three papers including `21 Aug receipt.txt`.
- It is not: `echo`. It is not `wc`/`cut`/`sort` (next lesson). It is not deleting files. Do not rewrite the receipts. Do not last with lesson 69’s find of `.landlord.txt`.

## Live sources (fetched this pass)

- `xargs --version`: GNU findutils 4.9.0 `/usr/bin/xargs`. Same package as find.
- man7.org xargs(1): “xargs - build and execute command lines from standard input.” “Because Unix filenames can contain blanks and newlines, this default behaviour is often problematic… it is better to use the -0 option… GNU find … -print0.”
- Live probe from `/home/ubuntu`: `find rent-receipts -name '*.txt'` prints three paths. Piped to `xargs ls -l` exits 123: `cannot access 'rent-receipts/21'`, `'Aug'`, `'receipt.txt'`. `-print0 | xargs -0 ls -l` lists all three. `find -exec ls -l {} +` also works; the film uses the xargs null path so the broken default is visible first.
- No local `man xargs`. `info xargs` exists. gnu.org HTML 403 this pass.
- `find linux-workshop/papers` does not descend the symlink under default `-P`. Film from `~` on `rent-receipts` instead.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Receipts already exist from lessons 30–31. Feature is feeding those names, not creating them.

## Human job

List sizes of every `.txt` receipt. One name has a space. Without `-0`, xargs feeds the next command the wrong pieces.

Candidates considered: (1) `find | xargs echo` — smoke. (2) xargs rm — destroys papers. (3) find the receipts, show the broken xargs, then `-print0 | xargs -0 ls -l`. Picked (3).

## Done on screen

Fullscreen terminal at `~ $`. Last `xargs -0 ls -l` holding the three receipt lines, including `21 Aug receipt.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite receipts. Do not `find .` from home (walks 503M `go`).

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `ls rent-receipts`, `find rent-receipts -name '*.txt'`, `find … | xargs ls -l` (break), last `find … -print0 | xargs -0 ls -l`.
