# Lesson 19 research brief

- **Lesson:** 19 — See the Fedora / RHEL family
- **After:** After the picture (`rpm`/`dnf`, Fedora, RHEL, CentOS Stream): show this machine has `apt` and not `dnf` — different family, same kernel idea
- **Audience:** Zero computer background; picture-first. Contrast must be honest; we do not boot Fedora here.

## Feature

The **Fedora / RHEL family** is a second Linux distro family. It packages software as **RPM** and manages it with **dnf**, not apt. Fedora Project: Fedora is the community distro; `dnf` downloads packages from repositories; Fedora is the **upstream** of Red Hat Enterprise Linux. Red Hat: Fedora is the community upstream; RHEL is the commercially supported enterprise OS (10-year lifecycle vs Fedora’s shorter cycle). CentOS Stream sits midstream, tracking just ahead of RHEL. This lesson is that family as labeled pictures, then honest proof this host is **not** in it. It is not Arch (lesson 20) and not “install Fedora.”

## Human job

A person who just named Ubuntu LTS might think every Linux box uses apt. They need labeled pictures of Fedora’s infinity mark, the Red Hat fedora, and the CentOS mark (all pictures — we never boot them), then `ls /usr/bin/apt` and `ls /usr/bin/dnf` on this host, because the first path exists and the second prints `No such file or directory`. That missing file is the family line.

If you install dnf to make the command succeed, you fake this machine. If you boot Fedora, you fake a second OS.

## Done on screen

1. HyperFrames: Fedora infinity; Red Hat hat (RHEL); CentOS mark; Tux for this host. End cards: Fedora / RHEL / This host.
2. Terminal 19pt: `ls /usr/bin/apt` prints `/usr/bin/apt`. `ls /usr/bin/dnf` prints `ls: cannot access '/usr/bin/dnf': No such file or directory`. Last frames hold that error.

## Sources used

- fedoraproject.org FAQ — Fedora community distro; dnf manages packages from repositories; Fedora is upstream of RHEL
- redhat.com, Fedora vs RHEL — Fedora is the upstream community distro; RHEL is commercially supported with a 10-year lifecycle
- centos.org, CentOS Stream — continuously delivered distro that tracks just ahead of RHEL, midstream between Fedora and RHEL
- This host: `/usr/bin/apt` exists; `/usr/bin/dnf` and `/usr/bin/rpm` do not
- Wikimedia: File:Fedora_logo.svg; File:Red_Hat_logo.svg; File:CentOS_logo.svg; File:Tux.svg

## Must be created on camera

Both `ls` commands typed. No Fedora/RHEL/CentOS is booted. dnf is not installed off-camera.

## Terminal font

1.75× default (JetBrains Mono 19).
