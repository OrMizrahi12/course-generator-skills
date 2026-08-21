# Lesson 22 research brief

- **Lesson:** 22 — See LTS vs rolling vs immutable
- **After:** After the picture (Ubuntu LTS, Arch rolling, Silverblue/Aeon/NixOS): say this Ubuntu is an LTS-style box, not an atomic image
- **Audience:** Zero computer background; picture-first. 2026 distro reality without pretending we booted Silverblue.

## Feature

Linux boxes do not all **move** the same way. **LTS** (ubuntu.com release cycle): a numbered freeze, years of standard maintenance — this host’s model. **Rolling** (Arch Wiki): one install, continuous upgrades; the box keeps moving. **Immutable / atomic** (fedoraproject.org Silverblue): the whole system updates in one go, takes effect on reboot, previous image kept for rollback; rpm-ostree is the hybrid image/package tool. aeondesktop.org: Aeon uses transactional updates — running system unchanged until reboot. nixos.org: declarative builds, roll back, packages isolated. This lesson is those three pictures, then honest proof this host is a **traditional package box**, not an ostree image. It is not desktop vs server vs Android (lesson 23).

## Human job

A person who can name distro families still might think every Linux updates like this Ubuntu. They need labeled pictures of Ubuntu LTS, Arch rolling, and a sealed shipping container for Silverblue/Aeon/NixOS (never booted), then `ls /var/lib/dpkg/status` and `ls /ostree` on this host, because the dpkg database file exists and `/ostree` prints `No such file or directory`. That missing directory is “not an atomic image.”

If you install rpm-ostree or create `/ostree`, you fake this machine. If you boot Silverblue, you fake a second OS.

## Done on screen

1. HyperFrames: Ubuntu Circle of Friends (LTS); Arch + bicycle wheel (rolling); sealed container (immutable); Tux for this host. End cards: LTS / Atomic / This host.
2. Terminal 19pt: `ls /var/lib/dpkg/status` prints `/var/lib/dpkg/status`. `ls /ostree` prints `ls: cannot access '/ostree': No such file or directory`. Last frames hold that error.

## Sources used

- ubuntu.com/about/release-cycle — LTS every two years, years of standard maintenance
- wiki.archlinux.org, Arch Linux — rolling release, one-time install with continuous upgrades
- fedoraproject.org/atomic-desktops/silverblue — atomic updates on next reboot; rpm-ostree hybrid image/package system
- aeondesktop.org — transactional update; running system not affected until reboot
- nixos.org — declarative, reproducible, roll back
- This host: `/var/lib/dpkg/status` exists; `/ostree`, `/usr/bin/rpm-ostree` do not
- Wikimedia: File:Ubuntu CoF (from lesson 18); File:Arch Linux "Crystal" icon.svg; File:Bicycle_wheel.jpg; File:Fedora Silverblue logo (2018).svg; File:NixOS logo light-on-dark.svg; File:Container_sealed.jpg; File:Tux.svg

## Must be created on camera

Both `ls` commands typed. No Silverblue/Aeon/NixOS is booted. `/ostree` is not created off-camera.

## Terminal font

1.75× default (JetBrains Mono 19).
