# Lesson 39 — Make and find a hidden file

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 40 here.

## Feature

A name that starts with `.` is hidden from ordinary `ls`. GNU `ls -a` (`--all`) does not ignore those names. Config and private notes often live this way. The workshop gets a real hidden file, then the viewer finds it.

## What it is / is not

- It is: creating `.landlord.txt` on camera in `~/linux-workshop`, proving `ls` omits it, then `ls -a` and `ls -ld .landlord.txt` finding it. GNU coreutils 9.4 `ls -a`: do not ignore entries starting with `.`.
- It is not: `echo`. It is not listing `~/.bashrc` again (that was home in lesson 33). It is not `chmod`. It is not creating the dotfile off-camera.

## Live sources (fetched this pass)

- Ubuntu Noble `ls(1)` — `-a, --all` do not ignore entries starting with `.`. `-A, --almost-all` does not list implied `.` and `..`. https://manpages.ubuntu.com/manpages/noble/en/man1/ls.1.html
- This host: `ls --version` → GNU coreutils 9.4. `/tmp` probe (deleted): `ls` printed only `visible.txt`; `ls -a` printed `.`, `..`, `.hidden.txt`, `visible.txt`.

## Live operation on this host (2026-08-21)

- Workshop already has `rent-log.txt` and `sep-due-draft.txt`. Do not delete them. Do not seed `.landlord.txt`.
- Menu-launched xfce4-terminal cwd is `/workspace`. `cd ~/linux-workshop`. `ls` shows the two visible names.
- `nano .landlord.txt` opens a new buffer whose name starts with a dot. Type a real landlord reminder (no colon; `:` is not on this filming keyboard map). `^O` Write Out, Enter, `^X` Exit.
- `ls` still shows only `rent-log.txt` and `sep-due-draft.txt`. `ls -a` adds `.`, `..`, and `.landlord.txt`. `ls -ld .landlord.txt` prints the hidden file’s directory line.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person keeps a landlord reminder next to the rent log but does not want it in a casual `ls` when they share the folder. A leading `.` is required. Without it, `ls` would list the reminder with the public papers.

Candidates considered: (1) `echo secret > .x` — smoke test, forbidden. (2) `cp rent-log.txt .rent-private.txt` — hidden, but a duplicate of an already-visible note. (3) `nano .landlord.txt`, write the 21 Sep call reminder, `ls` misses it, `ls -a` and `ls -ld` find it. Picked (3).

## Done on screen

Fullscreen terminal. Cwd `~/linux-workshop`. `ls -ld .landlord.txt` shows a regular file named `.landlord.txt`. Ordinary `ls` did not list it.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Visible files stay. The hidden file is created on camera.

## Viewer must see created on camera

Opening Terminal Emulator, walking into the workshop, `nano .landlord.txt`, Write Out and Exit, `ls` missing it, `ls -a` finding it, and `ls -ld .landlord.txt`.
