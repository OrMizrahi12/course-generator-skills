# Lesson 2 research brief

- **Lesson:** 2 — See hardware vs software
- **After:** Point at the metal vs the running program, and start a real program that uses the CPU
- **Audience:** Zero computer background; picture-first

## Feature

Hardware is the **physical parts**. Software is a **program**: instructions that tell the hardware what to do. They are not the same thing.

It is **not** an operating system lesson. The OS sits between these two (linux.com, IBM). That is lesson 3.

## Human job

A person just learned the CPU is metal. They want to see a **program** using that metal, because a photograph of a chip does not look like “doing work.” IBM’s own example is a word-processing application telling the CPU how to display text. On this XFCE machine that program is **Mousepad**. Starting Mousepad is required; typing real words is required; proving the process is alive with `ps` is required. Without the running program, the two-column picture is only a poster.

## Done on screen

1. HyperFrames: real CPU photograph labeled hardware, real word-processor screenshot (LibreOffice Writer, brand visible) labeled software, then both together: software uses the hardware.
2. Mousepad, fullscreen: a real sentence typed, visible as a running program.
3. Terminal (font 1.75× default): `ps -C mousepad -o pid,pcpu,cmd` while Mousepad is still running. Last frames hold that finished process line.

## Sources used

- IBM, *What is computer hardware?* — hardware vs software; word-processing app tells the CPU how to display text
- linux.com, *What is Linux?* — the OS manages communication between software and hardware (named here only as the gap, not taught)
- This host: Mousepad 0.6.1, `python3` available, JetBrains Mono 19 terminal

## Must be created on camera

Mousepad opening from empty. The typed sentence. The `ps` proof of that same process. Do not start Mousepad off-camera.

## Terminal font

1.75× default (JetBrains Mono 19) before recording the terminal shot.
