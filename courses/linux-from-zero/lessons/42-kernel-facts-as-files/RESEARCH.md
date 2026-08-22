# Lesson 42 — See kernel facts as files

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 43 here.

## Feature

The kernel publishes live facts as files. `/proc` is procfs: process and system information. `/sys` is sysfs: kernel objects and devices. You read a real line from each.

## What it is / is not

- It is: listing `/proc` and `/sys` on this Ubuntu, proving `/proc/version` looks empty on disk (0 bytes) then `cat` prints this kernel’s version line, then reading `/sys/devices/system/cpu/online`.
- It is not: `echo`. It is not `uname` (lesson 24). It is not `/dev` (next lesson). It is not writing sysfs. It is not pretending PID 1 is systemd (this host’s PID 1 is tini).

## Live sources (fetched this pass)

- `proc(5)` on this host (man-db 2.12.0, manpages 6.7-2): “The proc filesystem is a pseudo-filesystem which provides an interface to kernel data structures. It is commonly mounted at /proc.” Most files are read-only; some are writable sysctls. https://man7.org/linux/man-pages/man5/proc.5.html
- Linux kernel docs — The /proc Filesystem: “The proc file system acts as an interface to internal data structures in the kernel.” Kernel data files live in `/proc` (not only per-PID dirs). https://kernel.org/doc/html/latest/filesystems/proc.html
- `sysfs(5)` on this host: “a filesystem for exporting kernel objects.” Commonly mounted at `/sys`. Files describe devices, modules, filesystems, and other kernel components. https://man7.org/linux/man-pages/man5/sysfs.5.html
- Linux kernel docs — sysfs: RAM-based filesystem exporting kobjects. Attributes are ASCII text files, preferably one value per file. Top-level layout includes `block/` `bus/` `class/` `devices/` `fs/` `kernel/` `module/`. https://kernel.org/doc/html/latest/filesystems/sysfs.html
- This host (2026-08-21): `/proc` and `/sys` are directories. `ls -l /proc/version` is 0 bytes; `file` says empty; `cat /proc/version` is `Linux version 6.12.94+ (root@35ea6acd4182) (gcc (Debian 12.2.0-14+deb12u1) 12.2.0, GNU ld (GNU Binutils for Debian) 2.40) #1 SMP PREEMPT_DYNAMIC Thu Aug 20 16:06:39 UTC 2026`. `cat /sys/devices/system/cpu/online` is `0-3`. `cat /proc/sys/kernel/hostname` is `cursor`. No DMI `sys_vendor` node.

## Live operation on this host (2026-08-21)

- Workshop files stay. Do not create, move, or delete them. Do not write under `/sys`.
- Menu-launched xfce4-terminal cwd is `/workspace`. Inspect `/proc` and `/sys` from there.
- `ls -ld /proc /sys` prints two `dr-xr-xr-x` directories.
- `ls /sys` is a short list (`block` `bus` `class` `dev` `devices` …). Do not `ls /proc` unfiltered (hundreds of PID dirs).
- `ls -l /proc/version` shows size 0. `file /proc/version` says empty. `cat /proc/version` still prints the 6.12.94+ line.
- `cat /proc/sys/kernel/hostname` prints `cursor` (procfs sysctl, not sysfs).
- Last command: `cat /sys/devices/system/cpu/online` prints `0-3`.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.
- HumanInput has no colon. Paths used here have none.

## Human job

A person needs this machine’s kernel version and how many CPUs are online without guessing and without treating `uname` as the only door. Those facts live in files the kernel serves. Without `/proc` and `/sys` they would think the kernel is a black box.

Candidates considered: (1) `echo` the strings `/proc` and `/sys` — smoke test, forbidden. (2) `cat /proc/1/comm` — true here (`tini`) but teaches init, not kernel facts as files, and would invite faking systemd. (3) `uname -sr` again — already the last frame of lesson 24. (4) List `/proc` and `/sys`, prove `/proc/version` is a 0-byte file that still prints this kernel, then `cat /sys/devices/system/cpu/online`. Picked (4).

## Done on screen

Fullscreen terminal. `cat /sys/devices/system/cpu/online` shows `0-3`. Above it, `cat /proc/version` still shows `Linux version 6.12.94+`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the three papers and the hidden note. Nothing new is written.

## Viewer must see created on camera

Opening Terminal Emulator, `ls -ld /proc /sys`, listing `/sys`, `ls -l` and `file` of `/proc/version`, `cat /proc/version`, `cat /proc/sys/kernel/hostname`, and `cat /sys/devices/system/cpu/online`.
