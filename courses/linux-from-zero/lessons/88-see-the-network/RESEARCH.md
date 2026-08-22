# Lesson 88 — See this computer on the network

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 89 here.

## Feature

Install `iproute2` because `ip` is missing, then `ip -br addr` and `ip route` on this host. Last `getent hosts 1.1.1.1` holds `1.1.1.1         one.one.one.one`.

## What it is / is not

- It is: seeing this machine’s addresses and a real DNS lookup. `ip` is not installed until this lesson. `ping` exists but `SOCK_RAW` is denied (no `cap_net_raw`). DNS still works.
- It is not: `echo`. It is not `ss` (lesson 89). It is not reading `/etc/resolv.conf` as the lesson object (lesson 90). It is not `curl` (lesson 91). Do not fake ping success.

## Live sources (fetched this pass)

- Ubuntu Noble `ip(8)` — show / manipulate routing, network devices, interfaces and tunnels. https://manpages.ubuntu.com/manpages/noble/man8/ip.8.html
- Probe: `ip` command not found. `hostname -I` prints `172.30.0.2 172.17.0.1`. `getent hosts 1.1.1.1` prints `1.1.1.1         one.one.one.one`. `ping -c 1 1.1.1.1` → Operation not permitted.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar. Display 1920×1080.
- Do not install `iproute2` off camera. `ip -br addr` first so the missing command is visible.

## Human job

A person needs this host’s addresses and proof a name exists on the network. Without `ip` they cannot list interfaces the iproute2 way.

Candidates considered: (1) `ping` — this host cannot open SOCK_RAW. (2) `hostname -I` only — hides `ip`. (3) missing `ip` → `apt-get install iproute2` → `ip -br addr` → `ip route` → last `getent hosts 1.1.1.1`. Picked (3).

## Done on screen

Fullscreen terminal. Last `getent hosts 1.1.1.1` holding `1.1.1.1         one.one.one.one`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `repeat-snap.sh` / `snap-repeat.log`. Do not rewrite them.

## Viewer must see created on camera

Opening Terminal Emulator, `ip -br addr` not found, `sudo apt-get install -y iproute2`, `ip -br addr`, `ip route`, last `getent hosts 1.1.1.1`.
