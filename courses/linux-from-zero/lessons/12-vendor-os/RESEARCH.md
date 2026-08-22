# Lesson 12 research brief

- **Lesson:** 12 — See why Linux is different from a vendor OS
- **After:** After the picture: this system is inspectable (you can read `/etc`, `/proc`, licenses). Windows and Mac stay labeled as company OSes
- **Audience:** Zero computer background; picture-first. Act II.

## Feature

A vendor OS (Windows, macOS) is a **company product**: you run it; you do not open its `/etc`. linux.com: under the GPL you may copy and modify; doing that to Windows’s base code would be illegal. FSF: proprietary software is the opposite of the four freedoms. This lesson is **visibility and ownership** — you can read this machine’s config and kernel facts as files. It is not a Windows boot (lesson 13) and not Darwin vs Linux (lesson 14).

## Human job

A person just opened the GPL. They still think “open” is a logo, and that Windows/Mac are the same kind of box with a different sticker. They need company marks as **labeled pictures**, then `ls /etc` and `cat /proc/version` on this host, because those two commands are how you *see* inspectability: configuration names, then the kernel speaking as a file.

If you skip `/etc` and `/proc`, inspectable stays a slogan. If you boot Windows, you fake a machine this host is not.

## Done on screen

1. HyperFrames: Windows mark and Apple mark labeled company OSes / pictures only; a padlock photograph (closed vendor box); an open book (you may read); Tux for this machine.
2. Terminal 19pt: `ls /etc` lists real config names; `cat /proc/version` prints `Linux version 6.12.94+` and the gcc line. Last frames hold `/proc/version`.

## Sources used

- linux.com, *Why bother to use Linux?* — GPL lets you copy and modify; doing that to Windows base code would be illegal
- FSF / GNU free-software definition (archive; gnu.org HTML 403 from this network) — proprietary software withholds those freedoms
- This host: `/etc` is world-readable (147 names); `/proc/version` = Linux 6.12.94+
- Wikimedia: Windows mark; Apple logo; File:Padlock.jpg; File:Open_book.jpg; Tux

## Must be created on camera

Both commands typed. Windows and Mac are never booted.

## Terminal font

1.75× default (JetBrains Mono 19).
