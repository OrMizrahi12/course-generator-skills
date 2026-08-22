# Lesson 96 — See kernel modules

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 97 here.

## Feature

`/proc/modules` is empty. `lsmod` is not installed. `/lib/modules` is missing. The kernel booted with `nomodule`. Last `ls /sys/module/virtio_blk` names a built-in module.

## What it is / is not

- It is: loadable modules vs built-in pieces. This host has **zero** loaded modules. One named built-in still appears under `/sys/module`.
- It is not: `insmod` / `modprobe` of a .ko. There is no `/lib/modules` tree. Do not install kmod just to print an empty table.
- It is not: `echo`. It is not lesson 94’s cmdline hold or lesson 95’s unit file.

## Live sources (fetched this pass)

- Ubuntu Noble `lsmod(8)`: formats `/proc/modules`. Provided by kmod. Not installed here. https://manpages.ubuntu.com/manpages/noble/man8/lsmod.8.html
- Kernel parameters: `nomodule` — Disable module load. Present on this `/proc/cmdline`. https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html
- `/proc/modules` is 0 bytes. `/lib/modules` does not exist. `/sys/module` lists 84 built-in names including `virtio_blk`.

## Live operation on this host (2026-08-22)

- `cat /proc/modules` prints nothing. `wc -c /proc/modules` → `0 /proc/modules`.
- `ls /lib/modules` → No such file or directory.
- `ls /sys/module | grep virtio_blk` → `virtio_blk`.
- `ls /sys/module/virtio_blk` → `parameters` and `uevent` (no `initstate`; this is built-in, not a loaded .ko).
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.

## Human job

A person needs to check whether any extra kernel pieces were loaded — and must not invent a module list when the file is empty.

Candidates considered: (1) `sudo apt install kmod` then empty `lsmod` — extra apt lesson. (2) fake a loaded module — forbidden. (3) prove `/proc/modules` is empty, `/lib/modules` missing, then name built-in `virtio_blk` under `/sys/module`. Picked (3).

## Done on screen

Fullscreen terminal. Last `ls /sys/module/virtio_blk` holding `parameters` and `uevent`. Scrollback still shows `0 /proc/modules` and the missing `/lib/modules` error.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave workshop files. Do not insmod. Do not create `/lib/modules`.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `wc -c /proc/modules`, `ls /lib/modules`, `ls /sys/module | grep virtio_blk`, last `ls /sys/module/virtio_blk`.
