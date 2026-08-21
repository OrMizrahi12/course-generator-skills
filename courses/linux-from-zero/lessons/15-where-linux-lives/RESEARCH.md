# Lesson 15 research brief

- **Lesson:** 15 — See where Linux actually lives
- **After:** After the picture (phones, TVs, cars, supercomputers, the internet, Android): prove this host is one real Linux computer in that world
- **Audience:** Zero computer background; picture-first. End of Act II.

## Feature

Linux is **already in the world**, not a hobby OS waiting for a desktop. linux.com: phones, thermostats, cars, refrigerators, TVs; most of the internet; all of the world’s top 500 supercomputers. Android’s kernel is an upstream Linux LTS plus Android patches (AOSP). This course machine is **one named Linux computer** in that same family. This lesson is that map plus live identity. It is not a distro family (lesson 16) and not “boot Android.”

## Human job

A person who just learned this is not Windows and not Darwin still thinks Linux is only the box in the course. They need labeled pictures of an Android phone, a living-room TV, a car cockpit, and a TOP500-class supercomputer, then `hostname` and `uname -a` on this host, because those two commands are how you *see* “this is one of them”: a name (`cursor`) and a full Linux identity line (`Linux cursor 6.12.94+ … GNU/Linux`).

If you skip the name, “everywhere” stays a poster. If you boot a phone or a supercomputer, you fake machines this host is not.

## Done on screen

1. HyperFrames: Android phone photograph + Android robot; Samsung TV; car infotainment; Summit supercomputer (Oak Ridge / IBM); Tux for this host.
2. Terminal 19pt: `hostname` prints `cursor`. `uname -a` prints `Linux cursor 6.12.94+ … x86_64 GNU/Linux`. Last frames hold that line.

## Sources used

- linux.com, *What is Linux?* — Linux is in phones, cars, TVs; most of the internet; all TOP500 supercomputers; Android is powered by Linux
- AOSP, *Kernel overview* — Android kernel is based on an upstream Linux LTS; ACKs add Android-specific patches
- TOP500 June 2025 list page — El Capitan / Frontier / Aurora / JUPITER (Linux-family systems). linux.com’s “all of the world’s top 500” is the claim we picture; we do not pretend this host is on that list
- This host: `hostname` = cursor; `uname -a` = Linux cursor 6.12.94+
- Wikimedia: File:Blackview A60 Smartphone…; File:Android robot.svg; File:A flat-screen television.jpg; File:Car interior 2.jpg; File:Summit (supercomputer).jpg; File:Tux.svg

## Must be created on camera

Both commands typed. No other OS is booted.

## Terminal font

1.75× default (JetBrains Mono 19).
