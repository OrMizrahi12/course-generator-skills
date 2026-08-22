# Lesson 99 — Run the workshop backup end to end

Locked to syllabus lesson 99 only. Live sources fetched on 22 Aug 2026. Filmed on this Ubuntu 24.04 host (`cursor`). The backup **command they wrote** is `linux-workshop/snap.sh` (lesson 83). This lesson **runs** it with a **dated** name, moves the archive **into** `~/linux-workshop/`, and **appends a log** there. Do not rewrite `snap.sh`. Do not reuse `snap-repeat.log`. Do not tar into the tree being packed.

## Live sources

- GNU tar 1.35 on this host. Ubuntu Noble `tar(1)` (live): https://manpages.ubuntu.com/manpages/noble/man1/tar.1.html — `-c` create, `-z` gzip, `-f` archive file.
- GNU coreutils 9.4 `date`. Ubuntu Noble `date(1)` (live): https://manpages.ubuntu.com/manpages/noble/en/man1/date.1.html — `%F` full date like `2026-08-22`. `%T` time `HH:MM:SS`.
- POSIX.1-2017 Shell Command Language §2.7.3 Appending Redirected Output (live): https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html — `[n]>>word` opens with `O_APPEND`. If the file does not exist, it is created. GNU bash 5.2.21 on this host.

## What this host actually shows (probed this pass)

```
/home/ubuntu/linux-workshop/snap.sh   executable 136 bytes
date +%F                              2026-08-22
./snap.sh                             usage: snap.sh outfile.tar.gz   (exit 1)
```

`snap.sh` runs `tar -czf "$1" -C /home/ubuntu linux-workshop`. Writing `$1` **inside** `linux-workshop` would pack a growing file. Write `../workshop-2026-08-22.tar.gz` first, then `mv` it in.

No `workshop-backup.log` yet. Do not create it off-camera.

## Human example (0% → 100% on camera)

A person wants one dated snapshot of the rent workshop **and** a line in a log they can grep later. `snap.sh` is required: it is the command they already wrote. From `~/linux-workshop`:

1. `cat snap.sh` — the command they wrote.
2. `date +%F` — `2026-08-22`.
3. `./snap.sh ../workshop-2026-08-22.tar.gz`
4. `mv ../workshop-2026-08-22.tar.gz .`
5. `ls -l workshop-2026-08-22.tar.gz`
6. `date '+%F %T workshop-2026-08-22.tar.gz' >> workshop-backup.log`
7. `cat workshop-backup.log` — last unique pair: one timestamped line naming that archive.

## Visual language

Same as lesson 1. Photos: unlabeled rope, knot, twine, jute (reuse from lesson 83). No brand marks.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.
