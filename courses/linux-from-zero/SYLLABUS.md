# Linux From Zero — See It, Then Do It

**Promise:** A person who has never heard the word Linux can watch a picture of each idea, then do that same idea on a real GNU/Linux machine, until they can run their own workshop like a power user.

**Audience and level:** Complete beginner (no computer background). Visual language is simple enough for a small child. Hands stay on real Linux the whole way, ending at daily power-user competence — not exam trivia, not kernel C.

**How every lesson is built (course rule, not a shot list):**

1. A HyperFrames visualization of **this** concept (one picture-story, no narration).
2. The same concept done for real on **this** Ubuntu 24.04 GNU/Linux machine, 0% to 100% on camera: create, path, result.

HyperFrames is the picture engine ([heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)). Linux is the subject. Visuals never replace a command that the viewer must see run.

Windows and macOS appear only as **labeled pictures**. We do not boot them. The Linux side of every comparison is proven on this machine.

**Continuous project:** `~/linux-workshop/` — a personal drawer that becomes a real toolbox: notes, tools, archives, and a backup the viewer wrote themselves.

**Practice machine (honest):** Ubuntu 24.04.4 LTS (Debian family), Linux kernel 6.12.x, XFCE desktop, bash, apt. PID 1 on this host is `tini` in a container with an overlay root — not systemd on bare metal. That fact is taught, not hidden.

---

## Spine

### Act I — What a computer even needs

These four lessons exist because "Linux" is a meaningless stamp until the viewer has a picture of an operating system, then a picture of Linux as one OS among others, then a picture of how it differs from Windows and from Mac.

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 1 | See what an operating system is | Point at this screen and name three layers: hardware, operating system, apps — and prove the OS is doing a job (two programs share the machine; a file still exists after an app closes) | IBM: an OS is the software that manages hardware and apps. Without this picture, "Linux" is just a word |
| 2 | See what Linux is | After the picture: open the live [kernel.org / Linux.com definition](https://www.linux.com/what-is-linux/) on this computer and match it — Linux is an operating system, like Windows and macOS are operating systems | linux.com: "Just like Windows, iOS, and Mac OS, Linux is an operating system." Name the family before naming this machine |
| 3 | See how Linux is different from Windows | After the three-house picture: show the Linux side live — one file tree from `/`, no `C:`, the system is inspectable. Windows stays a labeled picture (NT kernel, drive letters, vendor OS) | LPI 4.1 and Microsoft's own user-mode/kernel-mode docs. One difference, proven on the Linux side |
| 4 | See how Linux is different from Mac | After the picture: show the Linux side live — this OS is not tied to Apple hardware; it is a distro on this machine, not Darwin/XNU. macOS stays a labeled picture (Unix-like, Apple's kernel) | Apple: macOS sits on XNU/Darwin. Same "Unix-like" neighborhood, different kernel, different rules |

### Act II — Put a word on this computer

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 5 | Name the operating system this computer is running | Point at this screen and prove, with a real command, that **this** computer is Linux | Now "Linux" has a meaning, so identifying this machine is a proof, not the first sentence of the course |
| 6 | See the kernel as the engine | Show the running kernel version from the system itself | kernel.org: Linux **is** the kernel; the rest of the course sits on this fact |
| 7 | See GNU tools sitting on that kernel | Tell kernel apart from the GNU programs they type, with real `--version` proof | Stops the myth that "Linux" means every file on disk |
| 8 | Name this distribution | Read `/etc/os-release` and say this is Ubuntu 24.04, Debian family | kernel.org: a beginner wants a distro, not a raw kernel tarball |
| 9 | Tell Linux distro families apart | Map Debian/Ubuntu → apt, Fedora/RHEL → dnf, Arch → pacman, SUSE → zypper, and run **apt** here | LPI 1.1: families differ by packages, defaults, and release model — not by a different species of kernel |

### Act III — Get hands on the tree

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 10 | Open a terminal and run a command | Open the terminal and get real output from a command they typed | The terminal is the hands; the picture of kernel/shell now has a door |
| 11 | Read the prompt | Decode `user`, host, and path from the prompt on this account | Before walking, know whose house and which room |
| 12 | Find home | Use `pwd`, `~`, and `$HOME` to land in this user's home | All later work lives relative to here |
| 13 | List what is here | Use `ls` (including long and hidden views) on a real directory | See before you move |
| 14 | Walk the tree | `cd` with absolute paths, relative paths, `.`, `..`, and back to home | The filesystem is a tree; walking comes before building |
| 15 | Create the Linux workshop | `mkdir ~/linux-workshop` and prove the folder exists | The continuous project starts as a real object, not a story |
| 16 | Make a real note in the workshop | Create a file with real content and show that content | Files are the nouns of Linux |
| 17 | Copy, rename, and remove on purpose | `cp`, `mv`, `rm` inside the workshop without destroying the project | LPI 2.4: case sensitivity and names on real files |
| 18 | Read a file without breaking it | `cat`, `less`, `head`, `tail` on a workshop note | Looking is safer than editing |
| 19 | Make and find a hidden file | Create a dotfile in the workshop and list it | Linux config is often a hidden file |

### Act IV — Maps, help, and identity

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 20 | Ask the system for help | Use `--help` and `man` (installing man pages on this minimized image if they are missing) to find a flag they need | Help is a skill; on this host, restoring docs is part of the path, not off-camera magic |
| 21 | Put the workshop in the right part of the tree | Inspect `/home`, `/tmp`, `/etc`, `/var`, `/usr` and keep human work in home | FHS 3.0: the map of Linux, used, not recited |
| 22 | Treat devices and kernel facts as files | Read a real line from `/proc` and see a real node in `/dev` | Unix "everything is a file"; LPI 4.3 |
| 23 | See who you are | `whoami`, `id`, and your line in `/etc/passwd` | Security starts with identity |
| 24 | Lock a workshop file | `chmod` so the note is private, prove it with `ls -l` | LPI 5.3: rwx as bits on a file they care about |
| 25 | Do one admin job as sudo | Use sudo for one real privileged step, then return to being a normal user | Arch Wiki / LPI 5.1: root is a tool, not a lifestyle |

### Act V — Software and running programs

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 26 | Install a real tool with apt and use it | Search, install, and **run** a package that the workshop needs | This distro's difference is apt; a package is not installed until it does work |
| 27 | Start a program and find its process | Start something and identify it with `ps` | The kernel's job is running processes |
| 28 | Stop a process on purpose | Interrupt or `kill` that process and prove it is gone | Programs do not vanish by magic |

### Act VI — Unix power on the workshop

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 29 | Build a workshop report with redirects and pipes | Save command output to a file and pipe a filter | LPI 3.2: the Unix power move |
| 30 | Search inside workshop files | `grep` a phrase they actually wrote | Extracting data from files they own |
| 31 | Find a file by name | `find` a workshop file without remembering the full path | The tree is bigger than one folder |
| 32 | Edit a workshop note in nano | Change a file, save, and verify the new text | LPI 3.3: an editor the viewer can finish |
| 33 | Pack the workshop into an archive | `tar` + gzip a snapshot they can list and restore | LPI 3.1: backups are real files |

### Act VII — Turn work into a tool

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 34 | Run a workshop command by name | Put a directory on `PATH` for a session and run a command without the full path | LPI 2.1: how Linux finds programs |
| 35 | Write a backup script and run it | A `#!/bin/bash` script that archives the workshop | LPI 3.3 (highest weight): commands become a tool |
| 36 | Make the script take arguments and fail honestly | Arguments, `if`, and a non-zero exit when input is wrong | Real scripts are not `echo hello` |
| 37 | Loop the script over real files | A `for` loop that does useful work on workshop files | Automation over a set they created |

### Act VIII — Share, point, talk, remember

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 38 | Point at a file with a symlink | `ln -s` in the workshop, then use the link | LPI 5.4: a name that is not a copy |
| 39 | Ask the network who this computer is | `ip` plus a real reachability or DNS lookup that produces output | LPI 4.4: this machine on a network |
| 40 | Read the system's memory of what happened | Pick a real line from `dmesg` or `/var/log` and say what it means | LPI 4.3: logs; `journalctl` is used only if it actually talks on this host |

### Act IX — How this Linux is really built

| # | Title | After this lesson the viewer can | Why it comes next |
|---|---|---|---|
| 41 | See how a normal Linux boots — and how **this** one started | After the boot picture: show PID 1 here (`tini`) and read a real systemd unit file Ubuntu still ships | LFS101 startup, without faking systemd as PID 1 |
| 42 | Make a tiny filesystem and write on it | Mount a `tmpfs` (or write on a real extra mount) and prove the file lives there | Filesystems are mountable trees, not a single disk cartoon |
| 43 | See that this Linux is a container | Inspect overlay on `/`, cgroup, and namespace facts on **this** host | 2026 Linux reality; this machine is the example |
| 44 | Run the workshop backup end to end | One command they wrote produces a dated archive plus a log in `~/linux-workshop/` | Reproduction test: the course's own project finishes on camera |

---

## Out of scope

- Installing Linux on bare metal, dual-boot, partitioning a physical disk, or writing a GRUB config (cannot be finished 0–100% on this host)
- Linux From Scratch; compiling a kernel; writing kernel modules
- Living as systemd PID 1 on this host (taught as contrast in lesson 41, never faked)
- Kubernetes, Docker-as-the-course, cloud certifications, RHCSA/LFCS cram
- Printing (LFS101 chapter 17)
- vi/emacs as the editor of record (nano is the editor; vim exists here but is not the path)
- SELinux policy, nftables firewall design, kernel C
- Booting Windows or macOS (comparison is HyperFrames + Linux-side proof only)

---

## Sources (live)

- What an OS is: [IBM — What is an Operating System?](https://www.ibm.com/think/topics/operating-systems)
- What Linux is, next to Windows and Mac: [linux.com/what-is-linux](https://www.linux.com/what-is-linux/)
- Linux kernel: [What is Linux?](https://www.kernel.org/linux.html)
- Windows kernel/user split: [Microsoft — User mode and kernel mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode)
- macOS kernel: [Apple — XNU / Darwin architecture](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Architecture/Architecture.html)
- LPI 4.1: differences between Windows, OS X, and Linux — [exam-010-objectives](https://www.lpi.org/our-certifications/exam-010-objectives/)
- Distros vs kernel: kernel.org — beginners need a distribution
- FHS 3.0: [Linux Foundation refspec](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.txt)
- Linux Foundation LFS101 outline: [Introduction to Linux](https://training.linuxfoundation.org/training/introduction-to-linux/)
- Red Hat RH104 topic list: [Getting Started with Linux Fundamentals](https://www.redhat.com/en/services/training/getting-started-with-linux-fundamentals)
- Debian Reference (2026): [debian-reference](https://www.debian.org/doc/manuals/debian-reference/)
- Arch Wiki: [General recommendations](https://wiki.archlinux.org/title/General_recommendations)
- systemd unit files: [systemd.unit(5)](https://www.freedesktop.org/software/systemd/man/systemd.unit)
- Ubuntu on this host: `/etc/os-release` (Ubuntu 24.04.4 LTS), `apt` 2.8.x
- HyperFrames: [github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes), [quickstart](https://hyperframes.heygen.com/quickstart)

This spine is a draft. Lesson count, act boundaries, and the container lesson can be edited before any recording starts.
