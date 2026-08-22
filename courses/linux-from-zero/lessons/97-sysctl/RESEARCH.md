# Lesson 97 — Read a sysctl

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 98 here.

## Feature

Read one real kernel knob two ways: `sysctl vm.swappiness` and `cat /proc/sys/vm/swappiness`. Last hold is `60`.

## What it is / is not

- It is: `sysctl` from procps-ng reading `/proc/sys`. This host’s swappiness is 60, the kernel default.
- It is not: writing a sysctl, `sysctl -w`, or editing `/etc/sysctl.conf`.
- It is not: overlay / cgroup / namespaces (lesson 98). It is not `echo`. It is not modules (lesson 96).

## Live sources (fetched this pass)

- Ubuntu Noble `sysctl(8)`: configure kernel parameters at runtime; keys are those listed under `/proc/sys/`; procps 4.0.4. https://manpages.ubuntu.com/manpages/noble/man8/sysctl.8.html
- Kernel vm sysctl: `swappiness` is 0–200; default 60; relative IO cost of swap vs filesystem paging. https://www.kernel.org/doc/html/latest/admin-guide/sysctl/vm.html

## Live operation on this host (2026-08-22)

- `sysctl --version` → sysctl from procps-ng 4.0.4 (`/usr/sbin/sysctl`).
- `sysctl kernel.hostname` → `kernel.hostname = cursor`.
- `sysctl vm.swappiness` → `vm.swappiness = 60`.
- `ls /proc/sys/vm/swappiness` shows the file. `cat /proc/sys/vm/swappiness` → `60`.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.

## Human job

A person needs the machine’s swap-vs-cache bias without guessing, and needs to see that `sysctl` and `/proc/sys` are the same knob.

Candidates considered: (1) `sysctl -w` — writes, not the lesson. (2) only `kernel.hostname` — already visible as the prompt’s machine name. (3) `sysctl kernel.hostname`, `sysctl vm.swappiness`, `ls` the proc file, last `cat /proc/sys/vm/swappiness`. Picked (3).

## Done on screen

Fullscreen terminal. Last `cat /proc/sys/vm/swappiness` holding `60`. Scrollback still shows `vm.swappiness = 60`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave workshop files. Do not write sysctl. Do not change swappiness.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `sysctl kernel.hostname`, `sysctl vm.swappiness`, `ls /proc/sys/vm/swappiness`, last `cat /proc/sys/vm/swappiness`.
