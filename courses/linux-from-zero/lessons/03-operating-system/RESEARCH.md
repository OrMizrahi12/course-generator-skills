# Lesson 3 research brief

- **Lesson:** 3 — See what an operating system is
- **After:** Name three layers on this screen — hardware, OS, apps — and prove the OS does a job (two apps share the machine; a file survives closing an app)
- **Audience:** Zero computer background; picture-first

## Feature

An operating system is **software that manages hardware and applications**: it allocates CPU, memory, devices, and file storage (IBM). linux.com: without the OS, the software would not function.

It is **not** Linux-the-brand yet, and not “the desktop wallpaper.” Linux is named in later lessons as one family of OS.

## Human job

A person now knows metal vs program. They need to see the **middle layer**, because two programs can run at once and a sentence can outlive the window that wrote it — that is the OS doing its job, not the app. IBM: process management (many processes) and file system management (organize and retrieve files). Required: start Mousepad, save a real file, keep the terminal running at the same time (`ps` shows both), close Mousepad, `cat` the file. If either proof is missing, the three-layer picture is only a poster.

## Done on screen

1. HyperFrames: three layers — CPU photograph (hardware), Xubuntu/XFCE desktop photograph (operating system), LibreOffice Writer (apps).
2. Mousepad, fullscreen, 19pt: type a real sentence, save `/tmp/still-here.txt` on camera.
3. Terminal 19pt: `ps -C mousepad,xfce4-terminal -o pid,pcpu,cmd` while both run; then `pkill -x mousepad`; `cat /tmp/still-here.txt` still prints the sentence. Last frames hold that file.

## Sources used

- IBM, *What is an operating system?* — OS manages hardware and applications; process management; file system management
- linux.com, *What is Linux?* — OS manages communication between software and hardware
- This host: Mousepad, xfce4-terminal, `/tmp`

## Must be created on camera

The saved file. The two running programs. Closing the editor. The surviving file contents. Do not pre-create `/tmp/still-here.txt`.

## Terminal font

1.75× default (JetBrains Mono 19) before the terminal shot.
