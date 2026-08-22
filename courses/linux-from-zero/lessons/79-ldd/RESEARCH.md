# Lesson 79 — See shared libraries

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 80 here.

## Feature

ldd (Ubuntu GLIBC 2.39) prints the shared objects `pstree` needs. Last `ldd /usr/bin/pstree` holds `libtinfo.so.6`, `libc.so.6`, the vdso, and `ld-linux-x86-64.so.2`.

## What it is / is not

- It is: a real binary is not one file alone. Last frame is ldd’s library list, not `file` alone.
- It is not: `echo`. It is not gcc. It is not writing a program. Do not type a colon. Do not rewrite `rent-log.txt`. Do not run ldd on an untrusted path.

## Live sources (fetched this pass)

- `ldd --version`: ldd (Ubuntu GLIBC 2.39-0ubuntu8.7) 2.39. `/usr/bin/ldd` is a bash script. Local man page `/usr/share/man/man1/ldd.1.gz`: ldd prints shared object dependencies; never use it on an untrusted executable.
- `file /usr/bin/pstree` (file 5.45): `ELF 64-bit LSB pie executable … dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2`.
- Live `ldd /usr/bin/pstree`: `linux-vdso.so.1`; `libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6`; `libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6`; `/lib64/ld-linux-x86-64.so.2`. Hex load addresses change each run.
- `ls -l /lib/x86_64-linux-gnu/libc.so.6` is a 2.1 MB ELF. `libtinfo.so.6` is a symlink to `libtinfo.so.6.4`.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- pstree exists from lesson 76. Do not compile anything.

## Human job

Prove why `pstree` can run: it is dynamically linked and borrows libc and libtinfo from disk.

Candidates considered: (1) `ldd /bin/ls` — man-page example, not this course’s tool. (2) `objdump -p | grep NEEDED` — colon in NEEDED, and it is the untrusted-file alternative. (3) `file /usr/bin/pstree` then `ldd /usr/bin/pstree`. Picked (3). Without ldd, `file` only says “dynamically linked”.

## Done on screen

Fullscreen terminal at `~ $`. Last `ldd /usr/bin/pstree` holding four mappings including `libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite `rent-log.txt`. Leave psmisc installed. Do not create a C file.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `file /usr/bin/pstree`, last `ldd /usr/bin/pstree`.
