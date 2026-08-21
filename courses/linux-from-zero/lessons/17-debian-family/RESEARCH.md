# Lesson 17 research brief

- **Lesson:** 17 — See the Debian family
- **After:** After the picture (`dpkg`/`apt`, stable, Ubuntu/Mint as children): read `ID_LIKE=debian` on this machine
- **Audience:** Zero computer background; picture-first. Act III. This host *is* that family — first live distro-family proof.

## Feature

A **Debian family** distro shares Debian’s packaging tools (`dpkg`, APT) and, on modern systems, writes that kinship in `/etc/os-release` as `ID_LIKE=debian`. debian.org: Debian is a free OS with APT and tens of thousands of packages; a derivative is based on Debian’s work but has its own identity — Ubuntu is listed. Debian FAQ: Ubuntu and Linux Mint are Debian-based, not Debian itself. This lesson is the family. It is not Ubuntu LTS (lesson 18) and not Fedora/RHEL (lesson 19).

## Human job

A person who just learned a distro is a complete box still cannot name *which* box-family this computer belongs to. They need labeled pictures of the Debian swirl (parent, dpkg/apt, stable), Ubuntu’s Circle of Friends (child), and Linux Mint’s mark (another child, picture only), then `grep ID_LIKE= /etc/os-release` and `dpkg --version` on this host, because those two commands are how you *see* the family without opening the Ubuntu version string: `ID_LIKE=debian` and Debian’s own `dpkg` 1.22.6.

If you `cat /etc/os-release`, you steal lessons 14 and 18. If you boot Debian or Mint, you fake machines this host is not. If you reuse `apt --version`, you repeat lesson 16.

## Done on screen

1. HyperFrames: Debian OpenLogo swirl; Ubuntu Circle of Friends; Linux Mint mark; Tux for this host. End cards: Debian / Mint / This host.
2. Terminal 19pt: `grep ID_LIKE= /etc/os-release` prints `ID_LIKE=debian`. `dpkg --version` prints `Debian 'dpkg' package management program version 1.22.6 (amd64).` Last frames hold that first line.

## Sources used

- debian.org, *About Debian* — Debian is a free OS; APT; 70000+ packages; begun 1993 by Ian Murdock
- debian.org, *Debian derivatives* — a derivative is based on Debian with its own identity; Ubuntu is highlighted (“popularising Linux around the world”)
- debian.org FAQ 3.2 — Kali, Knoppix, Linux Mint, Ubuntu are Debian-based, not Debian
- This host: `ID_LIKE=debian` in `/etc/os-release`; `ID=ubuntu` (not filmed as the LTS name); `dpkg` 1.22.6
- Wikimedia: File:Debian-OpenLogo.svg; File:UbuntuCoF.svg; File:Linux Mint logo without wordmark.svg; File:Tux.svg

## Must be created on camera

Both commands typed. No other distro is booted.

## Terminal font

1.75× default (JetBrains Mono 19).
