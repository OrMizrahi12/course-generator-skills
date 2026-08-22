# Lesson 10 research brief

- **Lesson:** 10 — See the seven pieces of a Linux OS
- **After:** After linux.com’s picture (bootloader, kernel, init, daemons, graphical server, desktop, apps): match each piece you can see on this XFCE machine, and label the ones that are only a picture here (bootloader)
- **Audience:** Zero computer background; picture-first. Act II.

## Feature

linux.com lists **seven pieces** of a Linux operating system: bootloader, kernel, init, daemons, graphical server, desktop environment, applications. The kernel “is the one piece of the whole that is actually called Linux.” This lesson is the map of those pieces. On **this** host the bootloader is never a live screen (container, no `/lib/modules`, no GRUB menu). PID 1 is **tini**, not systemd — taught, not faked.

It is **not** distros (lesson 16), not process trees (lesson 60), not “open source” (lesson 11).

## Human job

A person now knows GNU/Linux is kernel plus GNU. They still cannot point at the running OS. They need the seven-piece picture, with GRUB marked as a picture only, then proof of the first program and the desktop session on this XFCE box — because those two are how you *see* init and desktop without pretending this machine booted from GRUB.

If you show systemd as PID 1, you lie about this host. If you skip init, the map has a hole.

## Done on screen

1. HyperFrames: GRUB screenshot labeled picture-only; Tux; a lit-match photograph for init; a honey bee for daemons; X.Org mark; XFCE mouse; an xfce4-terminal screenshot for apps. Seven-card hold.
2. Terminal 19pt: `ps -p 1 -o pid,comm` prints `1` and `tini`; `ls /usr/share/xsessions` prints `xfce.desktop`. Last frames hold both.

## Sources used

- linux.com, *What is Linux?* — seven pieces; kernel is the one piece actually called Linux; init often systemd (not true of *this* PID 1)
- This host: PID 1 `tini`; `/usr/share/xsessions/xfce.desktop`; display `:1` is TigerVNC with X.Org vendor string 21.1.11; no `/lib/modules`
- Wikimedia: GRUB v2.12 Fedora 41 screenshot; Tux; File:Matches.jpg; File:Honey_bee.jpg; File:X.Org_Logo.svg; File:Xfce_logo.svg; File:Xfce4-terminal.png

## Must be created on camera

Both commands typed. Do not fake a GRUB boot.

## Terminal font

1.75× default (JetBrains Mono 19).
