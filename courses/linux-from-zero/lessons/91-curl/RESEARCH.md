# Lesson 91 — Fetch something with curl

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 92 here.

## Feature

`curl -o example.html http://example.com/` writes a real HTTP 200 page into the workshop. Last `cat example.html` holds `Example Domain`.

## What it is / is not

- It is: curl 8.5.0 fetching a live HTTP response onto disk. Probe: `curl -o /dev/null -w '%{http_code}' http://example.com/` → 200.
- It is not: `echo`. It is not `getent` (lesson 90). It is not `ss` (lesson 89). Do not start a new server. Do not rewrite `due.c`.

## Live sources (fetched this pass)

- Ubuntu Noble `curl(1)` — transfer a URL. https://manpages.ubuntu.com/manpages/noble/man1/curl.1.html
- This host: `curl --version` → curl 8.5.0. Live `http://example.com/` returns HTTP 200.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.
- Do not create `example.html` off camera.

## Human job

A person needs the Example Domain page as a file in the workshop, not only a name lookup.

Candidates considered: (1) `curl http://example.com/` to the terminal — not saved. (2) curl the 8765 server — it is down. (3) `curl -o example.html http://example.com/`, `ls -l`, last `cat example.html`. Picked (3). Without `-o` the page never lands in the workshop.

## Done on screen

Fullscreen terminal. Last `cat example.html` holding `Example Domain`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Create `example.html` on camera. Leave `due.c`.

## Viewer must see created on camera

Opening Terminal Emulator, `curl -o example.html http://example.com/`, `ls -l example.html`, last `cat example.html`.
