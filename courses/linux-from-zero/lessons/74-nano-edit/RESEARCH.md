# Lesson 74 — Edit in nano

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 75 here.

## Feature

GNU nano 7.2 opens `sep-due-draft.txt`, changes Sep to Oct on disk, Write Out, exit. `cat` then shows `Next due 21 Oct.` Lesson 72 only rewrote the stream. This lesson saves the change.

## What it is / is not

- It is: edit the draft copy (inode 1575549, not the rent-log hard link). Last `cat sep-due-draft.txt` holds `Next due 21 Oct.`
- It is not: `echo`. It is not `sed -i`. It is not tar (next lesson). Do not edit `rent-log.txt` (would also change `due-call.txt`). Do not leave nano open as the last frame.

## Live sources (fetched this pass)

- `nano --version`: GNU nano 7.2 `/usr/bin/nano`. No local man page. nano-editor.org v7 manual: Write Out is `^O`, Exit is `^X`. Status bar shows `[ Wrote N lines ]`.
- Live `cat -A sep-due-draft.txt`: three sentences plus a trailing blank, still `Next due 21 Sep.` Same 92 bytes as rent-log, different inode.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- File already exists from lesson 37. Feature is changing it, not creating it.

## Human job

Move the draft due month from Sep to Oct and prove it is saved.

Candidates considered: (1) nano a new file — that was lesson 36. (2) edit rent-log — mutates the hard link. (3) cat the draft, nano change Sep→Oct, Write Out, Exit, cat again. Picked (3). Without nano the file on disk cannot change.

## Done on screen

Fullscreen terminal at `linux-workshop $`. Last `cat sep-due-draft.txt` holding `Next due 21 Oct.`

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not edit `rent-log.txt`. After this lesson `sep-due-draft.txt` will no longer match the log. That is the point.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `cat sep-due-draft.txt`, `nano sep-due-draft.txt`, Down to the due line, End, Backspace Sep, type Oct, `^O` Enter, `^X`, last `cat sep-due-draft.txt`.
