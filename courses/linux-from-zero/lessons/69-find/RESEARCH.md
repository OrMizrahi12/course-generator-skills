# Lesson 69 — Find files by name

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 70 here.

## Feature

GNU find walks a directory tree and prints paths whose **base name** matches a shell pattern. From home, `ls` cannot see `rent-log.txt`. `find linux-workshop -name rent-log.txt` walks that tree. A second find by the hidden name `.landlord.txt` still matches, because `-name` tests the base name including the leading dot.

## What it is / is not

- It is: findutils 4.9.0 `/usr/bin/find` on this person’s workshop. Last `find linux-workshop -name '.landlord.txt'` holding `linux-workshop/.landlord.txt`.
- It is not: `echo`. It is not `xargs` / `-exec` (next lesson). It is not `-type` / `-mtime`. Do not rewrite notes. Do not last with lesson 68’s grep.

## Live sources (fetched this pass)

- `find --version`: GNU findutils 4.9.0. `find --help`: default path is current directory; default expression is `-print`. Tests include `-name PATTERN`.
- man7.org find(1): “find - search for files in a directory hierarchy.” `-name pattern`: “Base of file name (the path with the leading directories removed) matches shell pattern pattern.” Quote the pattern so the shell does not expand it (`find . -name *.c` is a documented pitfall).
- No local `man find` (same dpkg exclude as grep.1). `/usr/share/info/find.info.gz` is present. gnu.org HTML 403 this pass.
- Live probe from `/home/ubuntu`: `ls` does not list `rent-log.txt`. `find linux-workshop -name rent-log.txt` prints `linux-workshop/rent-log.txt`. `find linux-workshop -name '.landlord.txt'` prints `linux-workshop/.landlord.txt`. `~/go` is 503M; do not `find .` from home on camera.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Start in `/workspace` (`workspace $`). `cd ~` then `ls`, then find. Papers already exist.

## Human job

The rent log and the hidden landlord note live under `linux-workshop`. From home, `ls` only shows folder names. Find walks the tree by the name they remember.

Candidates considered: (1) `find . -name hello` — smoke test. (2) `find .` from home — walks 503M `go`. (3) find rent-log then the hidden landlord note from `~`. Picked (3).

## Done on screen

Fullscreen terminal at `~ $`. Last find holds `linux-workshop/.landlord.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log or `.landlord.txt`. Do not `find .` from home.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `ls`, `find linux-workshop -name rent-log.txt`, last `find linux-workshop -name '.landlord.txt'`.
