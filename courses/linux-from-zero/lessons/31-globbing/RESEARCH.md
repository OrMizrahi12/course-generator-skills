# Lesson 31 — Match names with globbing

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 32 here.

## Feature

Let the shell expand `*` into every matching filename, then pass that list to `ls`. One pattern selects a set. Quotes freeze the star, so the pattern must stay unquoted.

## What it is / is not

- It is: Bash pathname expansion. `*` matches any string except `/`. Expansion runs after word splitting, so a match that contains spaces stays one word. This host: `globstar` off, `nullglob` off, `failglob` off, `dotglob` off. A quoted `*.txt` is a literal name.
- It is not: `?` or `[abc]`. It is not `**` / globstar. It is not `echo`. It is not `~/linux-workshop` (starts at 35). It is not hidden files.

## Live sources (fetched this pass)

- Bash Hackers — Pathname expansion. The program never sees the glob; it sees the matching names. Expansion is after word splitting. https://bash-hackers.gabe565.com/syntax/expansion/globs/
- Linux `glob(7)` — `*` matches any string including empty; `/` is never matched; a leading `.` must be matched explicitly. https://man7.org/linux/man-pages/man7/glob.7.html
- Arch `glob(7)` text — same POSIX rules. https://man.archlinux.org/man/glob.7.en.txt

## Live operation on this host (2026-08-21)

- GNU bash 5.2.21. `extglob` on. `globstar` off. `nullglob` off.
- Throwaway probe in `/tmp` (destroyed): three `.txt` names including `21 Aug receipt.txt`. `ls *.txt` listed all three. `ls '*.txt'` printed `cannot access '*.txt'`.
- `rent-receipts` currently holds only `21 Aug receipt.txt` from lesson 30. Do not pre-create `late-notice.txt` or `landlord-note.txt`. Create those two on camera so the glob has a set.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.
- Asterisk is Shift+8 (`XK_asterisk`). Quotes around a glob are the wrong move this time.

## Human job

A person has August rent papers in `rent-receipts`: the receipt with spaces, plus a late notice and a landlord note they drop in as they arrive. They need every `.txt` listed at once without retyping the spaced name. Globbing is required. Quoting the star would look for a file literally named `*.txt` and fail.

Candidates considered: (1) `ls *` in `/workspace` — too many course files, not a human job. (2) `?` and character classes — extra syntax. (3) Create two more `.txt` names on camera, show quoted `*.txt` miss, then unquoted `ls -l /home/ubuntu/rent-receipts/*.txt` list all three. Picked (3).

## Done on screen

Fullscreen terminal. Two new `.txt` files created in `rent-receipts`. Quoted glob fails. Unquoted `ls -l /home/ubuntu/rent-receipts/*.txt` holds three lines, including `21 Aug receipt.txt`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35.

## Viewer must see created on camera

Opening Terminal Emulator, the two extra `.txt` files, the quoted miss, and the unquoted glob listing. Do not seed `late-notice.txt` or `landlord-note.txt` off-camera.
