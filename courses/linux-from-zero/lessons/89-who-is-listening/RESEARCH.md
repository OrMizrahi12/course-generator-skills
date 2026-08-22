# Lesson 89 — See who is listening

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 90 here.

## Feature

Start a real listener on this host, then `ss` shows it. Last `ss -lnt sport = :8765` holds `127.0.0.1:8765` LISTEN.

## What it is / is not

- It is: `ss` from iproute2 6.1.0 listing TCP listen sockets. A workshop HTTP listener on 8765 is created on camera so the row is one they started.
- It is not: `echo`. It is not `ip addr` (lesson 88). It is not `/etc/resolv.conf` (lesson 90). It is not `curl` of the server (lesson 91). Do not invent a closed port as LISTEN.

## Live sources (fetched this pass)

- Ubuntu Noble `ss(8)` — dump socket statistics. https://manpages.ubuntu.com/manpages/noble/man8/ss.8.html
- This host: `ss --version` → ss utility, iproute2-6.1.0. Probe: `ss -lnt` lists LISTEN rows including `127.0.0.1:5901`. `ss -lnt sport = :5901` holds two LISTEN rows for 5901. Port 8765 is free.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.
- Do not start the 8765 server off camera.

## Human job

A person started a tiny workshop server and needs to see that it is listening, without guessing.

Candidates considered: (1) only `ss -lnt` of host ports they did not start — real but not created. (2) `netstat` — old path. (3) `ss -lnt`, then `python3 -m http.server 8765 --bind 127.0.0.1 --directory ~/linux-workshop &`, last `ss -lnt sport = :8765`. Picked (3). Without `ss` they cannot see the LISTEN row.

## Done on screen

Fullscreen terminal. Last `ss -lnt sport = :8765` holding LISTEN on `127.0.0.1:8765`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `ip` / `repeat-snap.sh`. Do not curl. Do not rewrite snap-repeat.log.

## Viewer must see created on camera

Opening Terminal Emulator, `ss -lnt`, starting the 8765 listener in the background, last `ss -lnt sport = :8765`.
