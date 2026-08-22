# Lesson 75 — Pack and unpack an archive

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 76 here.

## Feature

GNU tar 1.35 with `-z` (gzip 1.12) packs `linux-workshop` into `linux-workshop.tar.gz`, lists the members, then extracts into `/tmp/workshop-snap`. Last `cat` of the restored draft shows `Next due 21 Oct.`

## What it is / is not

- It is: one gzip-compressed tar of the real workshop, listed, then restored beside the original. Last frame holds the restored `sep-due-draft.txt`.
- It is not: `echo`. It is not apt (next lesson). It is not `sed -i`. Do not rewrite `rent-log.txt`. Do not type a colon. Do not follow `papers` with `-h`.

## Live sources (fetched this pass)

- `tar --version`: GNU tar 1.35 `/usr/bin/tar`. Ubuntu package `1.35+dfsg-3build1`. gnu.org HTML 403. Ubuntu manpage noble: `-c` create, `-t` list, `-x` extract, `-f` archive name, `-z` filter through gzip, `-C DIR` change directory (order-sensitive). Authoritative longer manual is https://www.gnu.org/software/tar/manual (blocked here).
- `gzip --version`: gzip 1.12. Ubuntu manpage: gzip is a complement to tar; GNU tar `-z` invokes gzip transparently. No local man page on this host.
- Live probe then deleted: `tar -czf` of `linux-workshop` is 603 bytes, `file` says `gzip compressed data, from Unix, original size modulo 2^32 10240`. `tar -tzf` includes `.landlord.txt` and stores `papers` as a symlink (`lrwxrwxrwx ... papers -> /home/ubuntu/rent-receipts`). Extract `-C /tmp/workshop-snap` restores `sep-due-draft.txt` with `Next due 21 Oct.` while `rent-log.txt` in the snapshot still says Sep.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- Workshop exists from lesson 35. The archive must be created on camera.

## Human job

Snapshot the workshop so the Oct draft can be restored into `/tmp/workshop-snap` without touching the live tree.

Candidates considered: (1) `gzip` a single file — misses tar. (2) uncompressed `.tar` — misses gzip. (3) pack, `file`, list, mkdir restore dir, extract `-C`, cat the restored draft. Picked (3). Without tar+gzip there is no snapshot to restore.

## Done on screen

Fullscreen terminal at `~ $`. Last `cat /tmp/workshop-snap/linux-workshop/sep-due-draft.txt` holding `Next due 21 Oct.`

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite `rent-log.txt`. Leave `linux-workshop.tar.gz` in home after the take. Restore lives under `/tmp/workshop-snap`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `ls linux-workshop`, `tar -czf linux-workshop.tar.gz linux-workshop`, `ls -lh linux-workshop.tar.gz`, `file linux-workshop.tar.gz`, `tar -tzf linux-workshop.tar.gz`, `mkdir /tmp/workshop-snap`, `tar -xzf linux-workshop.tar.gz -C /tmp/workshop-snap`, last `cat /tmp/workshop-snap/linux-workshop/sep-due-draft.txt`.
