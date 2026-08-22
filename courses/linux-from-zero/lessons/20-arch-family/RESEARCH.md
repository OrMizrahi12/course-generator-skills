# Lesson 20 research brief

- **Lesson:** 20 — See the Arch family
- **After:** After the picture (`pacman`, rolling, Arch/Manjaro/SteamOS): say rolling means the box keeps moving
- **Audience:** Zero computer background; picture-first. Contrast must be honest; we do not boot Arch here.

## Feature

The **Arch family** is a third Linux distro family. Arch Wiki: Arch is an independently developed GNU/Linux distro that follows a **rolling-release** model — one install, then continuous upgrades — backed by **pacman**. Rolling means the box keeps moving: packages are upgraded as they come; there is no Ubuntu-style numbered freeze. Manjaro.org: takes Arch’s power and makes it more accessible, still rolling. Collabora (Valve partner on Steam Deck): SteamOS 3 is based on Arch Linux and replaces Debian-based SteamOS 2; pacman is there in developer mode. This lesson is those labeled pictures, then honest proof this host is **not** in that family. It is not SUSE (lesson 21) and not the full LTS vs rolling vs immutable comparison (lesson 22).

## Human job

A person who just saw Fedora/RHEL might think the only other package tool is dnf. They need labeled pictures of the Arch crystal A, a bicycle wheel for rolling, Manjaro’s green bars, and a Steam Deck (SteamOS) — all pictures, never booted — then `ls /usr/bin/apt` and `ls /usr/bin/pacman` on this host, because the first path exists and the second prints `No such file or directory`. That missing file is the family line.

If you install pacman to make the command succeed, you fake this machine. If you boot Arch, you fake a second OS.

## Done on screen

1. HyperFrames: Arch crystal A; bicycle wheel (rolling); Manjaro bars; Steam Deck / SteamOS. End cards: Arch / SteamOS / This host.
2. Terminal 19pt: `ls /usr/bin/apt` prints `/usr/bin/apt`. `ls /usr/bin/pacman` prints `ls: cannot access '/usr/bin/pacman': No such file or directory`. Last frames hold that error.

## Sources used

- wiki.archlinux.org, Arch Linux — independently developed, rolling release, one-time install with continuous upgrades, pacman
- wiki.archlinux.org, Pacman — the package manager that keeps the system up to date
- manjaro.org — Arch made more accessible; rolling releases
- collabora.com, Portable Linux gaming with the Steam Deck — SteamOS 3 is based on Arch Linux (supersedes Debian-based SteamOS 2)
- wiki.archlinux.org, Steam Deck — SteamOS is Arch-based; not supported as vanilla Arch
- LPI Linux Essentials 1.1 (popular operating systems) — distro families as a map, not a boot
- This host: `/usr/bin/apt` exists; `/usr/bin/pacman` does not
- Wikimedia: File:Arch Linux "Crystal" icon.svg; File:Manjaro-logo.svg; File:SteamOS logo.svg; File:Steam Deck (front).png; File:Bicycle_wheel.jpg; File:Tux.svg

## Must be created on camera

Both `ls` commands typed. No Arch/Manjaro/SteamOS is booted. pacman is not installed off-camera.

## Terminal font

1.75× default (JetBrains Mono 19).
