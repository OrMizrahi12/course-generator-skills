# Lesson 16 research brief

- **Lesson:** 16 — See what a distribution is
- **After:** After the picture (kernel + GNU + package manager + defaults + installer): say why kernel.org tells beginners to download a distro, not a kernel tarball. Distro is the thing a human installs.
- **Audience:** Zero computer background; picture-first. Start of Act III.

## Feature

A Linux **distribution** is a complete Linux system: kernel plus GNU userland plus a package manager, defaults, and an installer. kernel.org *New to Linux?*: “you don't want to download the kernel, which is just a component in a working Linux system. Instead, you want what is called a distribution of Linux, which is a complete Linux system.” This lesson is that box. It is not the Debian family (lesson 17) and not Ubuntu LTS (lesson 18).

## Human job

A person who just learned Linux lives in phones and supercomputers still thinks “Linux” is a kernel tarball from kernel.org. They need labeled pictures of the engine (kernel only), Tux plus GNU (still incomplete), a USB installer stick (the thing a human actually installs), and a cardboard box (the complete packaged system), then `ls /etc/apt` and `apt --version` on this host, because those two commands are how you *see* this machine already has a distro’s package manager, not a naked kernel.

If you skip `/etc/apt`, “distro” stays a poster. If you `cat /etc/os-release`, you steal lesson 14/18. If you boot another distro, you fake a machine this host is not.

## Done on screen

1. HyperFrames: Suzuki engine bay (kernel only); Tux + GNU head; Kingston USB installer stick; cardboard moving box (complete system). End cards: Kernel / Installer / Distro.
2. Terminal 19pt: `ls /etc/apt` lists `sources.list`, `sources.list.d`, `keyrings`. `apt --version` prints `apt 2.8.3 (amd64)`. Last frames hold that line.

## Sources used

- kernel.org, *About Linux Kernel* / *New to Linux?* — do not download the kernel; download a distribution, a complete Linux system; mirrors at mirrors.kernel.org
- linux.com, *What is Linux?* — a vendor or project that bundles the kernel with user-space programs, an installer, and management utilities has made a Linux distribution
- This host: `ls /etc/apt` → apt.conf.d, auth.conf.d, keyrings, preferences.d, sources.list, sources.list.d, trusted.gpg.d; `apt --version` → apt 2.8.3 (amd64); `dpkg --version` → 1.22.6 (not filmed; live proof that a Debian-family package manager is here)
- Wikimedia: File:Car_engine.jpg; File:Tux.svg; File:Heckert_GNU_white.svg; File:Kingston Technology DataTraveler G4 USB flash drive USB 3.0 32 Gb.jpg; File:Cardboard_box.jpg

## Must be created on camera

Both commands typed. No other distro is booted. No kernel tarball is downloaded.

## Terminal font

1.75× default (JetBrains Mono 19).
