# Lesson 68 — Search with a regular expression

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 69 here.

## Feature

A regular expression is a pattern, not a fixed phrase. Default GNU grep already uses basic regular expressions. `^` matches the empty string at the start of a line. Quote the pattern so the shell does not eat the caret.

## What it is / is not

- It is: one real regex on the rent log this person wrote. Fixed `grep 21` hits two lines. Quoted `grep '^21 '` keeps only the line that starts with the date.
- It is not: `echo`. It is not `-E` / `-P` / character classes / `find`. Do not rewrite the notes. Do not last with lesson 67’s `grep Sep`.

## Live sources (fetched this pass)

- GNU grep 3.11 `/usr/bin/grep` (`grep --version`, `grep --help`). Default is `-G` basic regular expressions. `-F` treats the pattern as a fixed string.
- man7.org grep(1): “Typically PATTERNS should be quoted when grep is used in a shell command.” Anchoring: “The caret ^ and the dollar sign $ are meta-characters that respectively match the empty string at the beginning and end of a line.”
- regex(7) on this host: `^` matches the null string at the beginning of a line.
- gnu.org HTML 403 this pass. Context7 quota exceeded this run.
- Live probe on `/home/ubuntu/linux-workshop/rent-log.txt`: `grep 21` prints `21 Aug rent is paid.` and `Next due 21 Sep.` `grep '^21 '` prints only the first. `grep -F '^21 '` prints nothing (exit 1). `grep '21 '` still prints both dated lines.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- `rent-log.txt` already exists from lesson 36. The feature is the regex, not creating the note.
- Type `'^21 '` with apostrophes. HumanInput must send Shift+6 for `^` (`asciicircum`).

## Human job

Find the opening dated line in the rent log. `21` also sits later in “Next due 21 Sep.” Without the start-of-line regex, grep cannot tell those two 21s apart.

Candidates considered: (1) `grep hello` — smoke test. (2) `grep -E` with `|` — steals extended syntax. (3) caret on the real dated line. Picked (3).

## Done on screen

Fullscreen terminal. Last `grep '^21 ' rent-log.txt` holding only `21 Aug rent is paid.`

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite rent-log or `.landlord.txt`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `cat rent-log.txt`, `grep 21 rent-log.txt`, last `grep '^21 ' rent-log.txt`.
