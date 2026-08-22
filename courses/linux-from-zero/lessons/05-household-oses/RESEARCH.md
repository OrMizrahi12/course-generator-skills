# Lesson 5 research brief

- **Lesson:** 5 — See the three household operating systems
- **After:** After the three-house picture, say this screen is *a* computer with *an* OS, and name the three families people mean: Windows, Mac, Linux
- **Audience:** Zero computer background; picture-first. Act I: no `uname` yet.

## Feature

People name three household operating-system families: **Windows**, **Mac**, and **Linux**. Linux.com states it directly: “Just like Windows, iOS, and Mac OS, Linux is an operating system.” This lesson uses that three-family picture. iOS stays out of the three houses (phones come later).

It is **not** distro names, kernels, GNU, or `uname`. Those are Acts II–III.

## Human job

A person can point at a computer and know it has *an* OS, and that the OS belongs to one of three families most households mean. Required: labeled pictures of Windows and Mac (this machine cannot boot them), a labeled picture of Linux, then a live match that **this** screen is the Linux house.

If you delete the three-family picture, “this computer has an OS” is still fog. If you fake a Windows or Mac boot, the lesson lies.

## Done on screen

1. HyperFrames: three real marks — Windows 11 logo, Apple logo, Tux — labeled Windows, Mac, Linux.
2. Terminal 19pt, no `uname`: `cat /proc/sys/kernel/ostype` prints `Linux`, then `ls /usr/share/xsessions` shows `xfce.desktop`. Last frames hold both results.

## Sources used

- Linux.com, *What is Linux?* — “Just like Windows, iOS, and Mac OS, Linux is an operating system.”
- This host: `/proc/sys/kernel/ostype` = Linux; `/usr/share/xsessions/xfce.desktop` exists. DISPLAY session is XFCE. PID 1 is tini (not taught here).
- Wikimedia Commons marks: Windows 11 logo, Apple logo, Tux (Larry Ewing, 1996).

## Must be created on camera

The two commands typed. Windows and Mac remain still pictures.

## Terminal font

1.75× default (JetBrains Mono 19).
