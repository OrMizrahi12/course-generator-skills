# Lesson 77 — See what a package actually contains

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 78 here.

## Feature

dpkg 1.22.6 lists every path `psmisc` installed. `dpkg -L psmisc | wc -l` is 110. `grep /usr/bin` shows the seven binaries. Last `ls -l /usr/bin/pstree` holds the real file.

## What it is / is not

- It is: a package is files. Last frame is the pstree binary on disk, not a description paragraph.
- It is not: `echo`. It is not `apt show` (metadata). It is not `ldd`. It is not `sources.list`. Do not type a colon. Do not rewrite `rent-log.txt`. Do not uninstall psmisc.

## Live sources (fetched this pass)

- `dpkg --version`: Debian dpkg 1.22.6 (amd64). Ubuntu package `1.22.6ubuntu6.5`. No local man page. Ubuntu noble manpage: `-L, --listfiles package-name` lists files installed to the system from that package. (`https://manpages.ubuntu.com/manpages/noble/man1/dpkg.1.html`)
- `dpkg -s psmisc`: Status `install ok installed`, Version `23.7-1build1` (from lesson 76).
- Live list: `dpkg -L psmisc` is 110 lines. `/usr/bin` members: `fuser`, `killall`, `peekfd`, `prtstat`, `pslog`, `pstree`, `pstree.x11`. `ls -l /usr/bin/pstree` is `-rwxr-xr-x 1 root root 36168 Mar 31 2024`.
- `apt show psmisc` is metadata (Version, Depends, Description). That is not this lesson.

## Live operation on this host (2026-08-22)

- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19.
- psmisc is already installed from lesson 76. Do not purge it. Do not install anything off-camera.

## Human job

Prove what apt actually put on disk, because a package is files, not a name in a cache.

Candidates considered: (1) `apt show psmisc` — description text, not files. (2) dump all 110 `dpkg -L` lines — they scroll off JetBrains Mono 19. (3) `type pstree`, count with `wc -l`, bound the binaries with `grep /usr/bin`, then `ls -l /usr/bin/pstree`. Picked (3). Without `dpkg -L` the viewer never sees the package as paths.

## Done on screen

Fullscreen terminal at `~ $`. Last `ls -l /usr/bin/pstree` holding `-rwxr-xr-x 1 root root 36168 Mar 31  2024 /usr/bin/pstree`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Do not rewrite `rent-log.txt`. Leave psmisc installed.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~`, `type pstree`, `dpkg -L psmisc | wc -l`, `dpkg -L psmisc | grep /usr/bin`, last `ls -l /usr/bin/pstree`.
