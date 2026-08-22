# Lesson 47 — Make a tiny filesystem and write on it

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 48 here.

## Feature

Mount a tmpfs, write a real scratch note on it, prove the tiny disk is there, then unmount so the note is discarded.

## What it is / is not

- It is: `mkdir ~/rent-scratch`, `sudo mount -t tmpfs -o size=8m tmpfs ~/rent-scratch`, nano a landlord-call scratch, `cat` it, `cd ~`, `sudo umount`, then `ls -l` empty and `df -h` back on overlay.
- It is not: `echo`. It is not a redirect. It is not writing in the workshop overlay. It is not a hard link or symlink. It is not using `/dev/shm` as the lesson object.

## Live sources (fetched this pass)

- `tmpfs(5)` on this host: a virtual memory filesystem; `sudo mount -t tmpfs -o size=10M tmpfs /mnt/mytmpfs`; “If a tmpfs filesystem is unmounted, its contents are discarded (lost).” Size suffix k, m, or g.
- `mount --help` / `umount --help` on this host (util-linux). `man mount` is not installed.
- This host (2026-08-22): `sudo -n true` works. Probe `sudo mount -t tmpfs -o size=8m tmpfs /tmp/l47-probe-mnt` then unmounted: `df -h` showed tmpfs 8.0M; after umount the probe file was gone. Reset before filming.

## Live operation on this host (2026-08-22)

- Workshop files stay. Do not `ln`. Do not write the scratch into `~/linux-workshop`.
- Create `~/rent-scratch` on camera. If a leftover dir exists, unmount and `rmdir` off-camera so `mkdir` is visible.
- `cd ~` before `umount` or the mount is busy.
- Nano 7.2: `^O` Write Out, Return, `^X` Exit. No colon in the note.
- Last command: `df -h ~/rent-scratch` showing overlay 252G, after `ls -l ~/rent-scratch` is empty.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person needs a throwaway pad for the 21 Sep landlord call that must not stay on the overlay disk. tmpfs is required; writing in the workshop would leave the note.

Candidates considered: (1) `echo hi > /dev/shm/x` — echo, redirect, not created. (2) write in `~/linux-workshop` — that is the overlay. (3) mount 8m tmpfs at `~/rent-scratch`, nano the call scratch, unmount. Picked (3).

## Done on screen

Fullscreen terminal. After umount, `ls -l ~/rent-scratch` is empty (`total 0`) and `df -h ~/rent-scratch` is overlay 252G, not tmpfs 8.0M.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the three papers and the hidden note. The scratch lives only on tmpfs and is discarded.

## Viewer must see created on camera

`mkdir ~/rent-scratch`, the mount, the nano file, Write Out, Exit, `cat`, umount, empty listing, overlay `df` again.
