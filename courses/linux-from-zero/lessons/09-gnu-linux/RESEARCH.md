# Lesson 9 research brief

- **Lesson:** 9 — See GNU/Linux as a whole system
- **After:** Combine kernel + GNU + other pieces into one picture of “a Linux computer”
- **Audience:** Zero computer background; picture-first. Act II.

## Feature

A working Linux computer is **not** the kernel alone and **not** every file on disk. Stallman’s GNU essay: Linux is the kernel — “an essential part of an operating system, but useless by itself”; the usual combination is GNU userland plus that kernel, **GNU/Linux**. kernel.org: the kernel is “just a component in a working Linux system.” linux.com: the kernel “is the one piece of the whole that is actually called ‘Linux’.” This lesson joins the two pictures from lessons 7 and 8 into one machine.

It is **not** the seven-piece linux.com map (lesson 10), not distros (Act III), not the four freedoms (lesson 11).

## Human job

A person just named GNU (`ls --version`) and the kernel (`uname -r`) in two different lessons. They will now collapse those into one word — either “Linux is only the engine” or “every file is Linux.” They need both halves on **one** screen because that is how you see this computer as a system: the kernel speaking its release, then a GNU program speaking its version.

If you skip one command, you re-teach lesson 7 or 8. If you list `/`, you teach the disk, not the combination.

## Done on screen

1. HyperFrames: Tux (kernel), Heckert GNU head (userland), a whole-car photograph vs the engine bay from lesson 8.
2. Terminal 19pt: `uname -r` prints `6.12.94+`; `ls --version` prints `ls (GNU coreutils) 9.4`. Last frames hold both.

## Sources used

- GNU Project / Stallman, *Linux and the GNU System* (archive of gnu.org/gnu/linux-and-gnu.html) — “Linux is the kernel… useless by itself”; whole system is GNU with Linux as kernel; call the combination GNU/Linux
- kernel.org, *About Linux Kernel* — kernel is a component; newcomers want a distribution
- linux.com, *What is Linux?* — kernel is “the one piece of the whole that is actually called ‘Linux’”
- This host: `uname -r` = 6.12.94+; `ls --version` = GNU coreutils 9.4
- gnu.org HTML still 403 from this network; essay text from the GNU project archive cited above
- Wikimedia: Tux; Heckert GNU white; File:Car_engine.jpg; File:2019 Honda Civic LX Sedan.jpg

## Must be created on camera

Both commands typed. Do not paste version banners.

## Terminal font

1.75× default (JetBrains Mono 19).
