# Lesson 1 research brief

- **Lesson:** 1 — See what a computer is made of
- **After:** Name CPU, memory, disk, and screen, then show this machine’s CPU (and the other three parts) from real commands
- **Audience:** Zero computer background; picture-first

## Feature

A computer is **physical parts**. Four of them matter first: CPU (thinks), memory (holds what is being used), disk (keeps files when power is gone), screen (shows).

It is **not** Linux, not an operating system, and not software. Those are later lessons.

## Human job

A person wants to know what **this** box in front of them is made of, because they have never looked inside a computer. Naming the four parts with real photographs is required; then matching each part on **this** machine is required. Without the four-part picture, `lscpu` is a wall of text.

## Done on screen

1. HyperFrames: real photos of a CPU, a RAM stick, a storage drive, and a monitor, each labeled, then all four together.
2. Terminal (font 1.75× default): this machine reports Intel Xeon CPU(s), ~16 GiB memory, 256G disks, 1920×1080 screen. Last frames hold that finished output.

On-camera commands (compact enough that 19pt fullscreen still shows the fact, not only the tail of `lscpu`): `head /proc/cpuinfo`, `free -h`, `lsblk`, `xrandr`.

## Sources used

- IBM, *What is computer hardware?* — CPU, RAM, storage drives, monitor as core physical parts
- This host: `lscpu` (Intel Xeon, 4 CPUs), `/proc/meminfo` (~16 GB), `lsblk` (256G disks), `xrandr` (1920×1080)

## Must be created on camera

The visualization playing (photos + labels). The terminal inspection of this machine (commands typed, full output). Opening the terminal may be on camera; font 19pt is filming setup, confirmed before ffmpeg.

## Terminal font

1.75× default (JetBrains Mono 19) before recording.
