# Lesson 18 research brief

- **Lesson:** 18 — See Ubuntu and LTS
- **After:** After the picture (Ubuntu, LTS, derivatives): read Ubuntu 24.04 LTS from `os-release`
- **Audience:** Zero computer background; picture-first. Narrows “Debian family” to this exact flavor.

## Feature

This computer’s distro is **Ubuntu**, and this release is an **LTS** (Long Term Support). ubuntu.com: LTS versions ship every two years and receive **5 years of standard security maintenance**. This host’s point release is Ubuntu **24.04.4 LTS** (Noble Numbat). ubuntu.com/desktop/flavours: Kubuntu, Xubuntu, and other flavors are community Ubuntu with different desktops, still the Ubuntu archive. This lesson names Ubuntu + LTS. It is not Fedora (lesson 19) and not a full `cat` of `/etc/os-release` (lesson 14).

## Human job

A person who just learned this box is Debian-family still cannot name the flavor or the support clock. They need labeled pictures of Ubuntu’s Circle of Friends, a wall calendar (LTS = years, not months), and official flavors Kubuntu/Xubuntu (pictures only), then `grep PRETTY_NAME= /etc/os-release` and `grep UBUNTU_CODENAME= /etc/os-release`, because those two lines are how you *see* Ubuntu 24.04.4 LTS / noble on disk without dumping the whole file.

If you `cat /etc/os-release`, you repeat lesson 14. If you `grep ID_LIKE=`, you repeat lesson 17. If you boot Kubuntu or Xubuntu, you fake a flavor this host is not (`NAME=Ubuntu`, XFCE session).

## Done on screen

1. HyperFrames: Ubuntu Circle of Friends; wall calendar (LTS years); Kubuntu + Xubuntu marks (flavors, pictures); Tux for this host.
2. Terminal 19pt: `grep PRETTY_NAME= /etc/os-release` prints `PRETTY_NAME="Ubuntu 24.04.4 LTS"`. `grep UBUNTU_CODENAME= /etc/os-release` prints `UBUNTU_CODENAME=noble`. Last frames hold that line.

## Sources used

- ubuntu.com, *Ubuntu release cycle* — LTS every two years; 5 years standard security maintenance; 24.04 LTS standard maintenance until May 2029
- ubuntu.com, *Ubuntu flavors* — Kubuntu (KDE), Xubuntu (Xfce), and others; community-owned, Ubuntu archive
- Ubuntu 24.04 LTS (Noble Numbat) release notes — security maintained 5 years until 31 May 2029
- This host: `PRETTY_NAME="Ubuntu 24.04.4 LTS"`; `UBUNTU_CODENAME=noble`; `lsb_release -ds` agrees (not filmed)
- Wikimedia: File:UbuntuCoF.svg; File:WallCalendar.jpg; File:Kubuntu_logo.svg; File:Xubuntu_logo.svg; File:Tux.svg

## Must be created on camera

Both greps typed. No other flavor is booted.

## Terminal font

1.75× default (JetBrains Mono 19).
