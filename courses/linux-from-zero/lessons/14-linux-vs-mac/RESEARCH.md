# Lesson 14 research brief

- **Lesson:** 14 — See how Linux differs from Mac
- **After:** After the picture (XNU/Darwin, Apple hardware bundle, Unix-like cousin): prove this is not Darwin — it is a Linux distro on non-Apple hardware
- **Audience:** Zero computer background; picture-first. Act II.

## Feature

A Mac is a **Unix-like cousin**, not another Linux. Apple’s kernel is **XNU** (“X is Not Unix”), a Mach + FreeBSD hybrid that, with other core parts, is called **Darwin**. macOS adds Apple’s proprietary layers on top and ships as a **hardware bundle**. kernel.org: Linux is a Unix clone written from scratch by Linus and others. This host’s kernel name is `Linux`, and `/etc/os-release` names **Ubuntu**. This lesson is that contrast. It is not a Mac boot, not Windows `C:` (lesson 13), and not “where Linux lives” (lesson 15).

## Human job

A person who just saw one tree from `/` still thinks “Unix-like means Mac.” They need labeled pictures of Darwin/XNU, Apple hardware, and BSD as cousin, then `uname -s` and `cat /etc/os-release` on this host, because those two files/commands are how you *see* “not Darwin”: the kernel prints `Linux`, then the distro names itself Ubuntu.

If you skip `uname -s`, Darwin vs Linux stays a slogan. If you boot macOS, you fake a machine this host is not. This container has no DMI vendor file; hardware proof is the picture of a Mac keyboard versus this Linux distro name.

## Done on screen

1. HyperFrames: Apple mark labeled XNU/Darwin pictures only; MacBook Command-key photograph (Apple hardware bundle); BSD daemon (Unix-like cousin); Tux for this Linux.
2. Terminal 19pt: `uname -s` prints `Linux`. `cat /etc/os-release` prints `NAME="Ubuntu"` and `PRETTY_NAME="Ubuntu 24.04.4 LTS"`. Last frames hold os-release.

## Sources used

- Apple OSS, *xnu* README — XNU is the Darwin kernel for macOS/iOS; hybrid Mach + FreeBSD + I/O Kit; “X is Not Unix”
- Apple Developer Archive, *Kernel Architecture Overview* — Darwin is kernel + core OS; macOS adds proprietary graphics/app layers; Mach + BSD + I/O Kit
- kernel.org, *What is Linux?* — Linux is a Unix clone written from scratch; a distribution is the complete system
- LPI 4.1 Lesson 1 — macOS reports Darwin from `uname -s`
- This host: `uname -s` = Linux; `/etc/os-release` = Ubuntu 24.04.4 LTS; no `/sys/class/dmi/id`
- Wikimedia: Apple mark; File:Macbook Pro 2020 color photography.jpg; File:Daemon-phk.svg (Beastie); File:Tux.svg

## Must be created on camera

Both commands typed. macOS is never booted.

## Terminal font

1.75× default (JetBrains Mono 19).
