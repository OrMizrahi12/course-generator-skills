# Lesson 98 — This Linux is a container

Locked to syllabus lesson 98 only. Live sources fetched on 22 Aug 2026. Filmed on this Ubuntu 24.04 host (`cursor`, kernel 6.12.94+). PID 1 is **tini**. This process sits in a **cgroup** named after a **pod**. Root `/` is **overlay**, not a disk partition. `/proc/self/ns` lists **namespaces**. There is **no** `/.dockerenv`. Do not claim Docker. Do not reverse the overlay. Do not enter another namespace.

## Live sources

- Overlay filesystem (kernel docs, live): https://www.kernel.org/doc/html/latest/filesystems/overlayfs.html — overlayfs is a union of an upper dir and a lower dir. One typical use is **containers**.
- `cgroups(7)` Ubuntu Noble (live): https://manpages.ubuntu.com/manpages/noble/man7/cgroups.7.html — `/proc/pid/cgroup` shows the cgroups of a process.
- `namespaces(7)` Ubuntu Noble (live): https://manpages.ubuntu.com/manpages/noble/man7/namespaces.7.html — `/proc/pid/ns/` contains a file per namespace; **one use of namespaces is to implement containers**.
- `df(1)` Ubuntu Noble (live): https://manpages.ubuntu.com/manpages/noble/man1/df.1.html — `-T` prints filesystem type.
- `findmnt(8)` Ubuntu Noble (live): https://manpages.ubuntu.com/manpages/noble/en/man8/findmnt.8.html — print a filesystem. `-n` no headings. `-o` columns.

## What this host actually shows (probed this pass)

```
df -hT /
Filesystem     Type     Size  Used Avail Use% Mounted on
overlay        overlay  193G   16G  178G   8% /
```

Used% moves as lesson files land. Type stays **overlay**.

```
findmnt -n -o SOURCE,FSTYPE,TARGET /
overlay overlay /
```

```
ls /proc/self/ns
cgroup  ipc  mnt  net  pid  pid_for_children  time  time_for_children  user  uts
```

```
cat /proc/1/cgroup
0::/system.slice/pod-2tfqlkm53fbljl2anubmdzxvxy-f76b9023
```

No `/.dockerenv`. `ip -br addr` still shows `docker0` **DOWN** from leftover Docker plumbing on the image — that is **not** proof this shell is a Docker container. The overlay + cgroup + namespaces are the proof.

## Human example (0% → 100% on camera)

Same rent workshop. From `~/linux-workshop`:

1. `df -hT /` — type **overlay**.
2. `findmnt -n -o SOURCE,FSTYPE,TARGET /` — `overlay overlay /`.
3. `ls /proc/self/ns` — namespace files.
4. `cat /proc/1/cgroup` — last unique pair: `0::/system.slice/pod-…`.

No `unshare`. No `nsenter`. No `chroot`. No writing to `/proc`.

## Visual language

Same as lesson 1. Photos: unlabeled packing boxes and crates (reuse from lesson 75). No Docker whale. No Kubernetes logo.
