# Lesson 90 — Read DNS client config

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 91 here.

## Feature

Read `/etc/resolv.conf` and `/etc/hosts`, then look names up. Last `getent hosts cursor` holds `127.0.0.1       cursor`.

## What it is / is not

- It is: the two client files this host actually uses. `resolv.conf` has `nameserver 10.0.0.2`. `/etc/hosts` maps `127.0.0.1` to `localhost` and to `cursor`. `getent hosts example.com` uses the resolver. `getent hosts cursor` uses the hosts file.
- It is not: `echo`. It is not `ss` (lesson 89). It is not `ip` (lesson 88). It is not `curl` (lesson 91). Do not rewrite either file.

## Live sources (fetched this pass)

- Ubuntu Noble `resolv.conf(5)` — resolver configuration. https://manpages.ubuntu.com/manpages/noble/man5/resolv.conf.5.html
- Ubuntu Noble `hosts(5)` — static table lookup for host names. https://manpages.ubuntu.com/manpages/noble/man5/hosts.5.html
- Probe: `cat /etc/resolv.conf` → `nameserver 10.0.0.2`. `getent hosts cursor` → `127.0.0.1       cursor`. `getent hosts example.com` returns IPv6 addresses.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.

## Human job

A person needs to see which nameserver this box asks, and that `cursor` is a local hosts line, not DNS.

Candidates considered: (1) only `cat` both files — no lookup. (2) `getent hosts 1.1.1.1` — already the last command of lesson 88. (3) `cat` both, `getent hosts example.com`, last `getent hosts cursor`. Picked (3). Without the files they cannot explain either answer.

## Done on screen

Fullscreen terminal. Last `getent hosts cursor` holding `127.0.0.1       cursor`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the 8765 listener. Do not curl. Do not rewrite hosts.

## Viewer must see created on camera

Opening Terminal Emulator, `cat /etc/resolv.conf`, `cat /etc/hosts`, `getent hosts example.com`, last `getent hosts cursor`.
