# Lesson 24 — Name this computer’s exact Linux

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 25 here.

## Feature

Identification is three facts stacked, not a nickname. This computer is a Linux kernel, a GNU userland, and an Ubuntu 24.04 Debian-family distribution. The pictures in Acts I–III end here: the name is proven with commands on this host.

## What it is / is not

- It is: reading the kernel name and release, the GNU stamp on a coreutils tool, and the machine-readable distro fields in `/etc/os-release`.
- It is not: `hostnamectl` (this host is not booted with systemd as PID 1, so that command fails). It is not a pretty marketing string first. It is not pretending this box is Fedora, Arch, or Silverblue.

## Live sources (fetched this pass)

- Ubuntu Noble manpage `os-release(5)` — `/etc/os-release` is the identification file. `ID=` is a lower-case OS identifier; example `ID=ubuntu` with `ID_LIKE=debian`. `VERSION_ID=` is the version label (example `VERSION_ID=11.04` in the spec). https://manpages.ubuntu.com/manpages/noble/man5/os-release.5.html
- Ubuntu Noble manpage `uname(1)` from GNU coreutils 9.4 — `-s` kernel name, `-r` kernel release; combined `-sr` prints both. https://manpages.ubuntu.com/manpages/noble/man1/uname.1.html
- Canonical Ubuntu release cycle — 24.04 LTS released April 2024; standard security through May 2029. https://ubuntu.com/about/release-cycle
- Wikipedia: GNU/Linux naming controversy — a typical desktop/server distro is the Linux kernel plus GNU userland (coreutils, bash, glibc, …); Android is a Linux kernel without GNU. https://en.wikipedia.org/wiki/GNU/Linux_naming_controversy

`gnu.org` HTML returned 403 from this network (same as earlier lessons). FSF naming is cited via Wikipedia plus the live GNU stamp on `ls --version`.

## Live operation on this host (2026-08-21)

- `uname -sr` → `Linux 6.12.94+`
- `ls --version` first line → `ls (GNU coreutils) 9.4`
- `grep ID= /etc/os-release` → `VERSION_ID="24.04"` then `ID=ubuntu` (`ID_LIKE=debian` does not match this pattern; `ID=` is not a substring of `ID_LIKE=`)
- `hostnamectl` → fails: “System has not been booted with systemd as init system (PID 1).”

Do not film `hostnamectl`. Do not boot another distro. Do not reuse lesson 18’s `PRETTY_NAME` / `UBUNTU_CODENAME`, lesson 17’s `grep ID_LIKE=`, or lesson 8’s separate `uname -s` then `uname -r` as the last-frame pair.

## Human job

A person must write down the exact Linux on this computer because support, packages, and later workshop steps depend on kernel + userland + distro together. The identification commands are required: a nickname like “Linux” is not enough.

## Done on screen

Three typed commands, all results held on the last frames:

1. `uname -sr` → `Linux 6.12.94+`
2. `ls --version` → `ls (GNU coreutils) 9.4` at the top of that output
3. `grep ID= /etc/os-release` → `VERSION_ID="24.04"` and `ID=ubuntu`

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35. Nothing in `~/linux-workshop/` this lesson.

## Viewer must see created on camera

The three identification commands and their full output. No off-camera setup of the answers.
