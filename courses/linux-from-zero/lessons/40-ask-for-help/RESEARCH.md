# Lesson 40 — Ask the system for help

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 41 here.

## Feature

`--help` is built into GNU programs. `man` pages the full manual. On this minimized Ubuntu, `man` is a stub and the pages were deleted. Restore the pages, then `man ls` shows `ls - list directory contents`.

## What it is / is not

- It is: GNU coreutils 9.4 `ls --help` (Usage plus `-a, --all`), then `/usr/bin/man` printing the Ubuntu minimized stub, then restoring man pages on camera (`dpkg` excludes, reinstall `coreutils` `man-db` `manpages`, undivert `man`), then man-db 2.12.0 paging `ls(1)`.
- It is not: `echo`. It is not `unminimize` of the whole image (that would `apt-get upgrade` and reinstall 200+ packages). It is not installing man pages off-camera. It is not a new file in the workshop.

## Live sources (fetched this pass)

- Ubuntu Noble `ls(1)` — list directory contents. `-a, --all` do not ignore entries starting with `.`. `--help` display this help and exit. Provided by coreutils 9.4. https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html
- Ubuntu Noble `man(1)` — an interface to the system reference manuals. man-db 2.12.0. https://manpages.ubuntu.com/manpages/noble/man1/man.1.html
- This host: `ls --help` prints GNU coreutils help including `-a, --all`. `/usr/bin/man` is a 320-byte shell stub from package `unminimize` 0.2.1 (`dpkg-divert` to `/usr/bin/man.REAL`). `/usr/bin/man.REAL --version` is `man 2.12.0`. `man.REAL ls` prints `No manual entry for ls`. `/etc/dpkg/dpkg.cfg.d/excludes` has `path-exclude=/usr/share/man/*`. `ls.1.gz` is missing even though `dpkg -L coreutils` lists it. Package `manpages` 6.7-2 is not installed. `groff-base` 1.23.0 is installed. `sudo -n true` works.

## Live operation on this host (2026-08-21)

- Workshop files from prior lessons stay: `rent-log.txt`, `sep-due-draft.txt`, `.landlord.txt`. Do not edit them.
- Menu-launched xfce4-terminal cwd is `/workspace`. `cd ~/linux-workshop`. `ls -a` still lists `.landlord.txt`.
- `ls --help` dumps GNU ls help (long; the visible end is the GNU coreutils help URL and `--help` / `--version` lines).
- `man ls` prints the four-line minimized stub and tells the user to run `unminimize`. Full `unminimize` is out of scope for this film (upgrade + reinstall every package with man pages). The stub is honest. The restore that actually puts `ls(1)` back is: move the dpkg excludes file aside, `apt-get update`, `apt-get install --reinstall -y coreutils man-db manpages`, remove the stub, `dpkg-divert --remove --rename /usr/bin/man`.
- Then `man ls` opens less on `LS(1)` with NAME `ls - list directory contents` and `-a, --all` on the first screen. Hold there. Do not `q` before the last frames.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person used `ls -a` to find `.landlord.txt` and needs to know what `-a` means without guessing. `--help` is required because it ships inside `ls`. `man` is required for the full page, and on this image the pages must be installed first. Without those they would invent flags.

Candidates considered: (1) `echo --help` — smoke test, forbidden. (2) Full `unminimize` — restores man pages but also upgrades the image and reinstalls 200+ packages. (3) `ls --help`, `man ls` stub, restore `ls(1)` on camera, `man ls` holds on NAME and `-a`. Picked (3).

## Done on screen

Fullscreen terminal. Cwd `~/linux-workshop`. `man ls` shows `LS(1)` NAME `ls - list directory contents`. `--help` already printed GNU ls help. The workshop files are unchanged.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the three papers and the hidden note. Nothing new is written in the workshop.

## Viewer must see created on camera

Opening Terminal Emulator, walking into the workshop, `ls -a`, `ls --help`, `man ls` as the stub, moving dpkg excludes, apt reinstall of `coreutils` `man-db` `manpages`, undiverting `man`, and `man ls` paging the real `ls(1)` page.
