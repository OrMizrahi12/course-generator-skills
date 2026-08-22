# Lesson 71 — Slice and count text

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 72 here.

## Feature

GNU coreutils 9.4 `wc`, `sort`, `uniq`, and `cut` on the two rent notes that already share the same 92 bytes. `wc` counts both. `sort` groups the duplicate lines. `uniq` collapses them. `cut -c1-12` keeps the first twelve characters of each line of `rent-log.txt`.

## What it is / is not

- It is: four filters on the real workshop notes. Last `cut -c1-12 rent-log.txt` holds `21 Aug rent `, `Keep the thr`, `Next due 21 `, and a blank fourth line.
- It is not: `echo`. It is not `sed` (next lesson) or `awk`. Do not rewrite the notes. Do not last with lesson 70’s `xargs -0 ls -l`. Do not type a colon (no `cut -d:`).

## Live sources (fetched this pass)

- `wc`/`sort`/`uniq`/`cut --version`: GNU coreutils 9.4. Local man pages exist. man7.org wc(1): “print newline, word, and byte counts for each file.” Host `wc rent-log.txt` is `4 15 92` (nano wrote 4 lines including a trailing blank).
- Live: `cat rent-log.txt sep-due-draft.txt | sort` prints each of the three sentences twice (blanks first). `| sort | uniq` prints each once. `cut -c1-12 rent-log.txt` slices the first twelve characters.
- `cut -d' '` on `ls-out.txt` only yields `-rw-r--r--` because GNU `ls -l` uses runs of spaces. Character `cut` is the honest slice on these notes.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Notes already exist from lessons 36–37. Feature is counting and slicing them, not creating them.

## Human job

Prove the draft is the same three sentences as the rent log, then slice the first twelve characters of the original.

Candidates considered: (1) `wc -l receipt-list.txt` only — skips sort/uniq/cut. (2) `cut -d:` on passwd — needs a colon this keyboard path does not type. (3) `wc` both notes, `cat | sort`, `sort | uniq`, last `cut -c1-12`. Picked (3). uniq is required: without it the sorted pipe still shows every line twice.

## Done on screen

Fullscreen terminal at `linux-workshop $`. Last `cut -c1-12 rent-log.txt` holding the three sliced lines.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite `rent-log.txt` or `sep-due-draft.txt`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `wc` of both notes, `cat | sort`, `cat | sort | uniq`, last `cut -c1-12 rent-log.txt`.
