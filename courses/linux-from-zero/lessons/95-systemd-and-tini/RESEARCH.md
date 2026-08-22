# Lesson 95 — See systemd as the usual init — and tini as this init

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 96 here.

## Feature

Read a real Ubuntu unit file. Show PID 1 is `tini` here. Do not fake `systemctl start`. Last `cat /lib/systemd/system/dbus.service` holds the shipped unit.

## What it is / is not

- It is: systemd as the usual GNU/Linux init (unit files on this disk), and tini 0.19.0 as **this** host’s PID 1.
- It is not: `systemctl start`, enabling a unit, or pretending systemd is PID 1.
- It is not: lesson 94’s last command (`cat /proc/1/comm`). That file is shown mid-path only.
- It is not: kernel modules (lesson 96). It is not `echo`.

## Live sources (fetched this pass)

- linux.com: init bootstraps user space; systemd is a widely used init. https://www.linux.com/what-is-linux/
- Ubuntu Noble `systemd.service(5)`: a `.service` file encodes a process systemd would supervise. Version on this host: systemd 255.4-1ubuntu8.15. https://manpages.ubuntu.com/manpages/noble/man5/systemd.service.5.html
- freedesktop `systemd.unit(5)`: unit files are ini-style `[Unit]` / type section. https://www.freedesktop.org/software/systemd/man/systemd.unit
- tini: a tiny but valid init for containers. https://github.com/krallin/tini — this host: `tini version 0.19.0 - git.de40ad0` at `/tini`.

## Live operation on this host (2026-08-22)

- `systemctl is-system-running` → `offline` (exit 1). systemd is installed; it is not PID 1.
- `cat /proc/1/comm` → `tini`. Args: `/tini -- /pod-daemon ...`.
- `/lib/systemd/system` has 127 `*.service` files (same tree as `/usr/lib/systemd/system`).
- `/lib/systemd/system/dbus.service` is 16 lines: `[Unit]` Description=D-Bus System Message Bus, `[Service]` Type=notify, ExecStart of dbus-daemon. File is shipped; dbus is not started here.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.

## Human job

A person needs to see what a normal Ubuntu init *would* read — a real unit file — and see that **this** computer’s first process is tini, without starting anything.

Candidates considered: (1) `systemctl start dbus` — forbidden, would fail or fake. (2) only `cat /proc/1/comm` — already lesson 94’s hold. (3) `systemctl is-system-running`, `cat /proc/1/comm`, `ls` the unit path, last `cat` dbus.service. Picked (3).

## Done on screen

Fullscreen terminal. Last `cat /lib/systemd/system/dbus.service` holding `[Unit]`, `Description=D-Bus System Message Bus`, and `[Service]` `Type=notify`. Earlier line `offline` and `tini` still in the scrollback.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave workshop files. Do not write a unit. Do not run `systemctl start`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `systemctl is-system-running`, `cat /proc/1/comm`, `ls /lib/systemd/system/dbus.service`, last `cat /lib/systemd/system/dbus.service`.
