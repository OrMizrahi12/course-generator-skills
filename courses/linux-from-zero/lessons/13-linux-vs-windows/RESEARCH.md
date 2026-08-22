# Lesson 13 research brief

- **Lesson:** 13 — See how Linux differs from Windows
- **After:** After the picture (NT kernel, `C:`, Win32, paid server licenses): prove the Linux side — one tree from `/`, no drive letter, inspectable
- **Audience:** Zero computer background; picture-first. Act II.

## Feature

Windows is a **different machine shape**, not a sticker swap. Microsoft’s kernel-mode executive lives in `Ntoskrnl.exe` (object, memory, process, I/O, config managers). Desktop programs talk through **Win32**. Disks get **drive letters** (`C:`). Windows Server Standard/Datacenter is a **paid Per Core/CAL** product: a CAL for each user or device. Linux on this host is one hierarchy from `/` with no `C:`. This lesson is that contrast, proven live. It is not a Windows boot, not Darwin vs Linux (lesson 14), and not “open vs closed” again (lesson 12).

## Human job

A person who just learned this OS is inspectable still thinks files live on `C:` because every Windows box they have used starts there. They need labeled pictures of NT / Win32 / `C:` / paid CALs, then `ls /` and `pwd` on this host, because those two commands are how you *see* “one tree, no drive letter”: names under `/`, then a path that begins with `/` and never a letter-colon.

If you skip `ls /`, “one tree” stays a slogan. If you boot Windows, you fake a machine this host is not.

## Done on screen

1. HyperFrames: Windows mark + CPU photograph labeled NT/Win32 pictures only; a real Windows **Laufwerk C:** properties dialog; bakery price tags for paid licenses; oak + Tux for one tree from `/`.
2. Terminal 19pt from `/home/ubuntu`: `ls /` lists this host’s root (`bin`, `home`, `usr`, also honest container names). `pwd` prints `/home/ubuntu`. Last frames hold that path. `ls /C:` is not typed; there is no such file.

## Sources used

- Microsoft Learn, *Windows Kernel-Mode Executive Support Library* — executive layer in `Ntoskrnl.exe`; HAL/drivers are not the executive
- Microsoft Learn, *User Mode and Kernel Mode* — apps in user mode; core OS in kernel mode
- Microsoft Learn, *Get Started with Win32 and C++* — desktop programs use Win32
- Microsoft, *Windows Server* licensing — Standard/Datacenter Per Core/CAL; a Windows Server CAL per user or device
- LPI Linux Essentials 4.1 Lesson 1 — Windows is proprietary; the license is often bundled with hardware
- linux.com, *Migrating to Linux: Disks, Files, and Filesystems* — Windows assigns `C:`; Linux presents one hierarchy from `/`; “there is no C:”
- This host: `ls /` has no `C:`; `ls /C:` fails; filmed `pwd` from home is `/home/ubuntu`
- Wikimedia: Windows mark; File:Intel Core i7-12700K (CPU); File:2025-02-27 … Zelda-Laufwerk (C).png; File:Dual Price Labels - Leva and Euro 02.jpg; File:Quercus_robur.jpg; File:Tux.svg; File:Hard disk.jpg (end card)

## Must be created on camera

Both commands typed. Windows is never booted.

## Terminal font

1.75× default (JetBrains Mono 19).
