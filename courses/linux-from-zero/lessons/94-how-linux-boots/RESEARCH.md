# Lesson 94 — See how a normal Linux boots

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 95 here.

## Feature

After the GRUB → kernel → initramfs → init picture: inspect what **this** host actually exposes. `/boot` is empty. Last `cat /proc/1/comm` holds `tini`.

## What it is / is not

- It is: the usual Linux boot chain as a picture, then live proof of the kernel command line and PID 1 on this machine.
- It is not: writing GRUB, packing an initramfs, or faking a bootloader on an empty `/boot`.
- It is not: reading a systemd unit file or treating tini as systemd (lesson 95).
- It is not: `echo`. Last command is not `dmesg` (lesson 92) and not `cat /etc/timezone` (lesson 93).

## Live sources (fetched this pass)

- linux.com seven pieces: bootloader (GRUB) hands off to the kernel; init bootstraps user space. https://www.linux.com/what-is-linux/
- Kernel command-line parameters: bootloader passes arguments; `/proc/cmdline` is readable once the system is up. https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html
- Kernel procfs Table 1-5: `/proc/cmdline` is the kernel command line from the bootloader and any embedded image args. https://www.kernel.org/doc/html/latest/filesystems/proc.html
- Ubuntu Noble `proc_cmdline(5)`: `/proc/cmdline` — arguments passed to the Linux kernel at boot time, often via GRUB. https://manpages.ubuntu.com/manpages/noble/en/man5/proc_cmdline.5.html
- Kernel initrd guide: bootloader loads kernel + initial RAM disk; later `/sbin/init` runs as PID 1. https://docs.kernel.org/admin-guide/initrd.html
- GNU GRUB HTML manual: gnu.org returned 403 this pass. Bootloader stays a labeled picture.

## Live operation on this host (2026-08-22)

- `/boot` exists and contains only `.` and `..` (empty). No GRUB, no vmlinuz, no initrd.
- No EFI firmware (`/sys/firmware/efi` absent).
- `/proc/cmdline` includes `console=ttyS0`, `root=/dev/vda`, `nomodule`, `pci=off`, virtio_mmio devices, and `systemd.unified_cgroup_hierarchy=1`. That last token is a kernel parameter, not proof that PID 1 is systemd.
- `ps -p 1 -o pid,comm` → `1 tini`. `cat /proc/1/comm` → `tini`. PID 1 args: `/tini -- /pod-daemon ...`.
- Open Terminal Emulator from the desktop menu. Font already JetBrains Mono 19. White terminal, no menubar.

## Human job

A person needs to see the usual boot chain, then check whether **this** computer actually has a bootloader on disk — without inventing GRUB files.

Candidates considered: (1) invent a GRUB menu on this host — forbidden. (2) only `uname -r` — does not show the chain or PID 1. (3) `ls -la /boot`, `cat /proc/cmdline`, `ps -p 1 -o pid,comm`, last `cat /proc/1/comm`. Picked (3).

## Done on screen

Fullscreen terminal. Last `cat /proc/1/comm` holding `tini`. `/boot` listing showed only `.` and `..`. cmdline showed `root=/dev/vda`.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave `example.html` and `snap-repeat.log`. Do not write GRUB config. Do not install a bootloader.

## Viewer must see created on camera

Opening Terminal Emulator, `cd ~/linux-workshop`, `ls -la /boot`, `cat /proc/cmdline`, `ps -p 1 -o pid,comm`, last `cat /proc/1/comm`.
