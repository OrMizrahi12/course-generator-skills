# Lesson 23 research brief

- **Lesson:** 23 — See desktop vs server vs embedded vs Android
- **After:** After the picture: this XFCE session is a desktop-shaped Linux; Android is Linux-the-kernel in a phone box
- **Audience:** Zero computer background; picture-first. Same kernel, different boxes, different jobs. Do not name this computer’s exact distro yet (lesson 24).

## Feature

The same Linux kernel idea is packed into **different jobs**. A **desktop** is a session with a window manager and a wallpaper process — this host. A **server** is Linux in a rack, often with no sitting-down screen. **Android** (source.android.com kernel overview): the Android kernel is based on an upstream Linux LTS kernel; Google adds Android-specific patches as Android Common Kernels. The phone box is still Linux-the-kernel, not a different species. This lesson is those labeled pictures, then honest proof this session is **desktop-shaped**. It is not “name Ubuntu 24.04” (lesson 24).

## Human job

A person who can name distro families might still think Linux only looks like this XFCE screen. They need labeled pictures of a real desktop workstation, a datacenter rack row, and Android (robot + phones) — never booted as a second OS — then `ps -C xfce4-session -o pid,comm` and `ps -C xfdesktop -o pid,comm` on this host, because those processes are running. That process table is “desktop-shaped Linux.”

If you kill xfdesktop off-camera, you fake the session. If you boot Android, you fake a phone.

## Done on screen

1. HyperFrames: Mozilla-office desktop workstation; datacenter racks; Android robot + Galaxy phones. End cards: Desktop / Android / This host.
2. Terminal 19pt: `ps -C xfce4-session -o pid,comm` prints a PID and `xfce4-session`. `ps -C xfdesktop -o pid,comm` prints a PID and `xfdesktop`. Last frames hold that second process.

## Sources used

- source.android.com/docs/core/architecture/kernel — Android kernel is based on upstream Linux LTS; Android Common Kernels
- This host: `xfce4-session`, `xfwm4`, and `xfdesktop` are running (no XFCE panel)
- Wikimedia: File:Desktop Computer In Mozilla Taiwan Office (72739495).jpeg; File:Datacenter Server Racks (22370909788).jpg; File:Android robot.svg; File:Samsung Galaxy S7 (26089332033).jpg; File:Tux.svg

## Must be created on camera

Both `ps` commands typed. No Android/server OS is booted. xfdesktop is not killed off-camera.

## Terminal font

1.75× default (JetBrains Mono 19).
