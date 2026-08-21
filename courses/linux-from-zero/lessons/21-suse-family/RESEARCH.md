# Lesson 21 research brief

- **Lesson:** 21 — See the SUSE family
- **After:** After the picture (`zypper`, openSUSE, SLES): another enterprise/desktop line, still Linux
- **Audience:** Zero computer background; picture-first. Completes the four classic packaging families. Contrast must be honest; we do not boot openSUSE here.

## Feature

The **SUSE family** is the fourth classic Linux packaging family. documentation.suse.com: **Zypper** is the command-line package manager for installing, updating, and removing packages, and for managing repositories — used on SUSE Linux Enterprise. opensuse.org: “Embrace the chameleon”; community distros for desktops, servers, and containers; Leap (stable) and Tumbleweed (rolling) are flavors, not a different kernel species. suse.com: SUSE Linux Enterprise Server is the commercially supported enterprise line. This lesson is those labeled pictures, then honest proof this host is **not** in that family. It is not the full LTS vs rolling vs immutable comparison (lesson 22).

## Human job

A person who just saw apt, dnf, and pacman families might think there is no fourth box. They need labeled pictures of the openSUSE Geeko, a real chameleon, and the SUSE wordmark (SLES) — all pictures, never booted — then `ls /usr/bin/apt` and `ls /usr/bin/zypper` on this host, because the first path exists and the second prints `No such file or directory`. That missing file is the family line.

If you install zypper to make the command succeed, you fake this machine. If you boot openSUSE, you fake a second OS.

## Done on screen

1. HyperFrames: openSUSE Geeko wordmark; veiled chameleon photo; SUSE wordmark (SLES). End cards: openSUSE / SLES / This host.
2. Terminal 19pt: `ls /usr/bin/apt` prints `/usr/bin/apt`. `ls /usr/bin/zypper` prints `ls: cannot access '/usr/bin/zypper': No such file or directory`. Last frames hold that error.

## Sources used

- documentation.suse.com, Zypper package manager — command-line package manager for SUSE Linux Enterprise
- opensuse.org — Embrace the chameleon; Leap stable, Tumbleweed rolling; community distros
- suse.com/products/server — SUSE Linux Enterprise Server, commercially supported enterprise Linux
- This host: `/usr/bin/apt` exists; `/usr/bin/zypper` does not
- Wikimedia: File:OpenSUSE Logo.svg; File:Suse-white-logo-green.svg; File:Chamaeleo_calyptratus.jpg; File:Tux.svg

## Must be created on camera

Both `ls` commands typed. No openSUSE/SLES is booted. zypper is not installed off-camera.

## Terminal font

1.75× default (JetBrains Mono 19).
