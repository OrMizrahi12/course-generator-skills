# Linux From Zero — See It, Then Do It

**Promise:** A person who has never heard the words *operating system* or *Linux* can watch pictures until those words have meaning, then do real work on a real GNU/Linux machine until they can run and understand a Linux system in depth.

**Audience and level:** Zero computer background. Opening acts are picture-first (a child could follow the drawing). After the pictures, the hands go as deep as a working Linux administrator: files, users, processes, packages, scripts, disks, boot, network, and the truth of this machine.

**Honest scope of “A to Z”:**  
This is Linux as a **system you can see and operate** — from first picture through power-user administration of a running GNU/Linux box.  
It is **not** writing the Linux kernel, not Linux From Scratch, and not installing on bare metal (those cannot finish 0–100% on this host). Those boundaries are listed at the end, not hidden inside the spine.

**How every lesson is built:**

1. A HyperFrames visualization of **this** concept (especially dense in Acts I–III).
2. The same concept proven on **this** Ubuntu 24.04 GNU/Linux machine, 0% to 100%: create, path, result.
3. If the lesson uses a terminal: font at about **1.75×** desktop default (three-quarters larger, e.g. 11pt → 19pt) before recording. The window still fills the screen.

Windows, macOS, other distros, bootloaders, and Android appear as **labeled pictures** unless this machine can prove the Linux side live. We never fake a boot of another OS.

**Continuous project:** `~/linux-workshop/` — starts when the hands start, then becomes notes, tools, archives, and a backup the viewer wrote.

**Practice machine:** Ubuntu 24.04.4 LTS (Debian family), Linux 6.12.x, XFCE, bash, apt. PID 1 here is `tini` on overlay — taught, not faked as systemd-on-bare-metal.

---

## Spine

### Act I — Pictures: what a computer even is

Lots of visualization. No `uname` yet. The job in each lesson is to **match the picture to something real on this screen**.

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 1 | See what a computer is made of | Name CPU, memory, disk, and screen, then show this machine’s CPU from `/proc` or `lscpu` | Hardware is the stage; nothing “Linux” makes sense before a computer is a picture |
| 2 | See hardware vs software | Point at the metal vs the running program, and start a real program that uses the CPU | IBM/linux.com: the OS sits between these two |
| 3 | See what an operating system is | Name three layers on this screen — hardware, OS, apps — and prove the OS does a job (two apps share the machine; a file survives closing an app) | An OS is software that manages hardware and programs |
| 4 | See the four jobs an OS does | Match files, programs, users, and devices on this desktop to the picture | Prepares the Linux-specific pictures without naming Linux yet |
| 5 | See the three household operating systems | After the three-house picture, say this screen is *a* computer with *an* OS, and name the three families people mean: Windows, Mac, Linux | linux.com: Linux is an OS “just like Windows and Mac OS” |

### Act II — Pictures: what Linux is, and why it is not the others

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 6 | See what Unix is | After the family-tree picture: this Linux box still speaks Unix ideas (users, files as a tree). Unix is the grandparent, not the stickers on this screen | Linux cloned Unix ideas; Mac is Unix-certified; Windows is not Unix |
| 7 | See what GNU is | After the picture of the GNU project: show a real GNU program’s `--version` on this machine | The userland most people type is GNU; the kernel is not |
| 8 | See what the Linux kernel is | After Linus / 1991 / engine picture: still do **not** treat “Linux” as the whole disk — the kernel is the engine in the picture | kernel.org: Linux **is** the kernel |
| 9 | See GNU/Linux as a whole system | Combine kernel + GNU + other pieces into one picture of “a Linux computer” | Stops both myths: “Linux is only a kernel” and “Linux is every file” |
| 10 | See the seven pieces of a Linux OS | After linux.com’s picture (bootloader, kernel, init, daemons, graphical server, desktop, apps): match each piece you can see on this XFCE machine, and label the ones that are only a picture here (bootloader) | This is the map of the whole OS before distros |
| 11 | See why Linux is open | After the four freedoms picture: open a real GPL text shipped with a GNU tool on this disk | Open source is a rule about copies, not a vibe |
| 12 | See why Linux is different from a vendor OS | After the picture: this system is inspectable (you can read `/etc`, `/proc`, licenses). Windows and Mac stay labeled as company OSes | The difference is ownership, visibility, and who is allowed to change it |
| 13 | See how Linux differs from Windows | After the picture (NT kernel, `C:`, Win32, paid server licenses): prove the Linux side — one tree from `/`, no drive letter, inspectable | LPI 4.1 + Microsoft kernel-mode docs. Windows is never booted here |
| 14 | See how Linux differs from Mac | After the picture (XNU/Darwin, Apple hardware bundle, Unix-like cousin): prove this is not Darwin — it is a Linux distro on non-Apple hardware | Apple’s own kernel architecture vs kernel.org |
| 15 | See where Linux actually lives | After the picture (phones, TVs, cars, supercomputers, the internet, Android): prove this host is one real Linux computer in that world | linux.com: Linux is already everywhere; this course is one of those machines |

### Act III — Pictures: distributions, all of them that matter

A distro is not a different kernel species. It is a different **box** around the same idea.

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 16 | See what a distribution is | After the picture (kernel + GNU + package manager + defaults + installer): say why kernel.org tells beginners to download a distro, not a kernel tarball | Distro is the thing a human installs |
| 17 | See the Debian family | After the picture (`dpkg`/`apt`, stable, Ubuntu/Mint as children): read `ID_LIKE=debian` on this machine | This host *is* that family — first live distro proof |
| 18 | See Ubuntu and LTS | After the picture (Ubuntu, LTS, derivatives): read Ubuntu 24.04 LTS from `os-release` | Narrows “Debian family” to this exact flavor |
| 19 | See the Fedora / RHEL family | After the picture (`rpm`/`dnf`, Fedora, RHEL, CentOS stream): show this machine has `apt` and not `dnf` — different family, same kernel idea | Contrast must be honest; we do not boot Fedora here |
| 20 | See the Arch family | After the picture (`pacman`, rolling, Arch/Manjaro/SteamOS): say rolling means the box keeps moving | LPI 1.1 + Arch Wiki |
| 21 | See the SUSE family | After the picture (`zypper`, openSUSE, SLES): another enterprise/desktop line, still Linux | Completes the four classic packaging families |
| 22 | See LTS vs rolling vs immutable | After the picture (Ubuntu LTS, Arch rolling, Silverblue/Aeon/NixOS): say this Ubuntu is an LTS-style box, not an atomic image | 2026 distro reality without pretending we booted Silverblue |
| 23 | See desktop vs server vs embedded vs Android | After the picture: this XFCE session is a desktop-shaped Linux; Android is Linux-the-kernel in a phone box | Same kernel, different boxes, different jobs |
| 24 | Name this computer’s exact Linux | Prove: Linux kernel + GNU userland + Ubuntu 24.04 Debian-family distro, with real commands | Now identification is the **end** of the pictures, not the first sentence |

### Act IV — Hands: the desktop, then the terminal

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 25 | Use the Linux desktop | Open the file manager, make a folder you can see, close it, open it again | The graphical server + XFCE are real; the terminal is next, not instead |
| 26 | Open a terminal and run a command | Get real output from a command they typed | Hands |
| 27 | Read the prompt | Decode user, host, and path | Whose house |
| 28 | See a command’s shape | Split a line into command, options, arguments on a real command | Syntax before navigation tricks |
| 29 | Use history and completion | Re-run a previous command; complete a path with Tab | Humans do not retype everything |
| 30 | Quote text so the shell does not eat it | Make a filename with a space and use it safely | Quoting is why beginners think Linux is “broken” |
| 31 | Match names with globbing | Select a set of workshop files with `*` | Patterns before copying lots of files |
| 32 | Find home | `pwd`, `~`, `$HOME` | All later files live here |
| 33 | List what is here | `ls`, long view, hidden view | See before you move |
| 34 | Walk the tree | `cd` absolute, relative, `.`, `..` | The tree is walkable |
| 35 | Create the Linux workshop | `mkdir ~/linux-workshop` and prove it | Continuous project starts |
| 36 | Make a real note | A file with real content | Files are nouns |
| 37 | Copy, rename, and remove on purpose | `cp` `mv` `rm` without destroying the project | LPI / LPIC file management |
| 38 | Read a file without breaking it | `cat` `less` `head` `tail` | Looking is safer than editing |
| 39 | Make and find a hidden file | A dotfile in the workshop | Config is often hidden |
| 40 | Ask the system for help | `--help` and `man` (install man pages on this minimized image if missing) | Help is a skill |

### Act V — Hands: the filesystem for real

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 41 | Put the workshop in the right part of the tree | Inspect `/home` `/tmp` `/etc` `/var` `/usr` `/bin` and keep human work in home | FHS 3.0 |
| 42 | See kernel facts as files | Read a real line from `/proc` and `/sys` | Everything-is-a-file, kernel side |
| 43 | See devices as files | Find a real node in `/dev` and say what kind of file it is | Devices are files too |
| 44 | See file types | From `ls -l`, tell file, directory, link, device apart | The first character is a map |
| 45 | See that a name is not the file | `ls -i` / link count: inode vs name | Prepares hard links |
| 46 | Measure disk and directory size | `df` and `du` on real paths | Storage is not the tree drawing |
| 47 | Make a tiny filesystem and write on it | Mount `tmpfs`, write, prove, unmount | Filesystems are mountable trees |
| 48 | Make a hard link | Two names, one inode, in the workshop | LPIC 104.6 |
| 49 | Make a symlink | A pointer name that is not a copy | LPI 5.4 |

### Act VI — Hands: people and locks

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 50 | See who you are | `whoami` `id` and your `/etc/passwd` line | Identity |
| 51 | See users and groups | Read `/etc/group` and say which groups this account is in | Access is not only “me” |
| 52 | Add a person to this Linux | Create a user (or group) with sudo and prove they exist | LPIC 107.1 — if sudo blocks, stop and report; do not fake |
| 53 | Lock a file with letters | `chmod u/g/o` + `ls -l` on a workshop file | rwx as language |
| 54 | Lock a file with numbers | `chmod 644` / `755` and prove it | Numeric mode |
| 55 | See umask | Create a file, show umask, explain the default bits | Defaults are a policy |
| 56 | Use the sticky bit on a shared directory | A directory where people cannot delete each other’s files | `/tmp` is the real example |
| 57 | Change ownership | `chown` / `chgrp` on a workshop file | Locks belong to someone |
| 58 | Do one admin job as sudo | One real privileged step, then back to a normal user | Root is a tool |

### Act VII — Hands: programs that are alive

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 59 | Start a program and find its process | `ps` on something they started | Kernel’s job |
| 60 | See the process tree | Parent/child of a real process | Processes are a family |
| 61 | Stop a process on purpose | SIGINT / `kill`, prove it is gone | Signals |
| 62 | Park a process in the background | `jobs`, `fg`, `bg` on a real job | Job control |
| 63 | Watch load and memory | `top` or `free` while something runs | The machine is finite |
| 64 | Change a process’s niceness | `nice`/`renice` on a workshop command | LPIC 103.6 |

### Act VIII — Hands: Unix power

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 65 | Catch stdout and stderr | Redirect both, including `/dev/null`, on a real command | Streams |
| 66 | Build a pipeline | Pipe a filter into a workshop report | The Unix move |
| 67 | Search inside files | `grep` a phrase they wrote | Extract |
| 68 | Search with a regular expression | One real regex on workshop or log text | LPIC 103.7 |
| 69 | Find files by name | `find` a workshop file | The tree is big |
| 70 | Feed names into the next command | `xargs` (or `find -exec`) on real files | Glue |
| 71 | Slice and count text | `cut` `sort` `uniq` `wc` on a real report | Filters |
| 72 | Rewrite a file with sed | One real substitution, verified | Stream edit |
| 73 | Extract columns with awk | One real awk on the report | LPIC text processing |
| 74 | Edit in nano | Change, save, verify | Editor of record |
| 75 | Pack and unpack an archive | `tar` + gzip a workshop snapshot you can restore | Backups |

### Act IX — Hands: software on this distro

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 76 | Install a real tool with apt and use it | Search, install, run | Debian-family hands |
| 77 | See what a package actually contains | `dpkg -L` (or `apt show`) on a package they installed | A package is files |
| 78 | See where apt looks for software | Read Ubuntu’s sources on this host | Repos are policy |
| 79 | See shared libraries | `ldd` on a real binary | LPIC 102.3 |
| 80 | Build a tiny program from source | Write, compile with `gcc`, run the binary in the workshop | Software is not only apt |
| 81 | Put a command on PATH | Session PATH + a workshop command by name | How Linux finds programs |
| 82 | Make the shell remember you | A real alias or `bashrc` line that changes a later command | LPIC 105.1 |

### Act X — Hands: turn work into a tool

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 83 | Write a backup script and run it | `#!/bin/bash` that archives the workshop | LPI 3.3 |
| 84 | Make it take arguments and fail honestly | Args, `if`, non-zero exit | Real scripts |
| 85 | Loop over real files | `for` that does useful work | Automation |
| 86 | Put a function in the script | One function used twice | Structure |
| 87 | Repeat a job without sitting there | A cron line, a systemd user timer if the bus exists, or an honest loop + log if this host has no scheduler — **never fake systemd timers** | LPIC 107.2 |

### Act XI — Hands: network, time, memory of the system

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 88 | See this computer on the network | `ip` plus a real reachability or DNS lookup | LPI 4.4 / LPIC 109 |
| 89 | See who is listening | `ss` on real sockets | Ports are not magic |
| 90 | Read DNS client config | `/etc/resolv.conf` and `/etc/hosts` used in a real lookup | LPIC 109.4 |
| 91 | Fetch something with curl | A real HTTP response saved into the workshop | Network as a tool |
| 92 | Read the system’s memory of what happened | A real line from `dmesg` or `/var/log` | Logs |
| 93 | See time and locale | `date`, timezone or `locale`, one real setting inspected | LPIC 107.3 / 108.1 |

### Act XII — Hands: how this Linux is really built

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 94 | See how a normal Linux boots | After GRUB → kernel → initramfs → init picture: inspect what this host *does* expose (`/proc/cmdline`, PID 1) | linux.com bootloader/kernel/init — bootloader is a picture if `/boot` is empty |
| 95 | See systemd as the usual init — and tini as **this** init | Read a real Ubuntu unit file; show PID 1 is `tini` here | No fake `systemctl start` |
| 96 | See kernel modules | `lsmod` (or `/proc/modules`) and name one loaded module | The kernel is not one blob in practice |
| 97 | Read a sysctl | One real `/proc/sys` or `sysctl` value | Kernel knobs |
| 98 | See that this Linux is a container | Overlay on `/`, cgroup, namespaces on **this** host | 2026 Linux; this machine is the example |
| 99 | Run the workshop backup end to end | One command they wrote → dated archive + log in `~/linux-workshop/` | Reproduction test |

---

## Out of scope (named, so the A–Z claim stays honest)

Cannot finish 0–100% on this host, so they are pictures + disclosure, not fake labs:

- Bare-metal install, dual-boot, partitioning a physical disk, writing GRUB
- Linux From Scratch; compiling the Linux kernel; writing kernel modules
- Booting Windows, macOS, Fedora, Arch, or SUSE
- systemd as live PID 1 (`systemctl` against this host’s init)
- Mail servers (MTA), printing, accessibility stacks, X11 *installation*
- Kubernetes, Docker-as-the-course, cloud certifications, exam cram
- SELinux policy writing, nftables firewall design, kernel C
- vi/emacs as the editor of record (nano is the editor)

---

## Sources (live)

- Seven pieces of Linux, distros, why Linux, open source tenets: [linux.com/what-is-linux](https://www.linux.com/what-is-linux/)
- Kernel definition: [kernel.org/linux.html](https://www.kernel.org/linux.html)
- What an OS is: [IBM — Operating systems](https://www.ibm.com/think/topics/operating-systems)
- Windows kernel/user: [Microsoft — User mode and kernel mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode)
- macOS kernel: [Apple — XNU / Darwin](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Architecture/Architecture.html)
- LPI Essentials 010: [exam-010-objectives](https://www.lpi.org/our-certifications/exam-010-objectives/)
- LPIC-1 101/102 (depth target for the hands): [exam-101-102-objectives](https://www.lpi.org/our-certifications/exam-101-102-objectives/)
- FHS 3.0: [refspecs.linuxfoundation.org](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.txt)
- LFS101 outline: [Introduction to Linux](https://training.linuxfoundation.org/training/introduction-to-linux/)
- Arch Wiki: [General recommendations](https://wiki.archlinux.org/title/General_recommendations)
- HyperFrames: [github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

This spine is a draft. Recording does not start until it is accepted.
