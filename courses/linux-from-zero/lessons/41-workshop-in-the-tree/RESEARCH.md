# Lesson 41 — Put the workshop in the right part of the tree

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 42 here.

## Feature

The tree has named places. FHS 3.0 puts people under `/home`, throwaways under `/tmp`, machine config under `/etc`, variable data under `/var`, the shareable hierarchy under `/usr`, and essential binaries under `/bin`. Human work stays in home.

## What it is / is not

- It is: inspecting `/home` `/tmp` `/etc` `/var` `/usr` `/bin` on this Ubuntu, then proving the rent log is not in `/tmp` or `/etc` and that `realpath` of the workshop is `/home/ubuntu/linux-workshop`.
- It is not: `echo`. It is not creating the workshop (that was lesson 35). It is not `/proc` or `/dev` (later lessons). It is not writing into `/tmp` or `/etc`.

## Live sources (fetched this pass)

- FHS 3.0 (19 March 2015) — `/` requires `bin` (essential command binaries), `etc` (host-specific system configuration), `tmp` (temporary files), `usr` (secondary hierarchy), `var` (variable data). `/home` is optional user home directories; no program should assume a specific home path. `/tmp` must exist; programs must not assume files there survive. https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s02.html https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s08.html https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s18.html
- Ubuntu Noble `hier(7)` from package `manpages` 6.7-2 (installed on camera in lesson 40). `/home` user homes; `/tmp` temporary files which may be deleted with no notice; `/etc` configuration local to the machine; `/var` files which may change in size; `/usr` shareable read-only data; `/bin` executables needed to bring the system up. STANDARDS: FHS 3.0. https://manpages.ubuntu.com/manpages/noble/man7/hier.7.html
- This host: `ls -ld` of the six. `/bin` is a symlink to `usr/bin` (merged /usr). `/home` holds `ubuntu`. `/tmp` mode `1777` (`drwxrwxrwt`). `ls /tmp/rent-log.txt` and `ls /etc/rent-log.txt` fail. `realpath ~/linux-workshop` is `/home/ubuntu/linux-workshop`.

## Live operation on this host (2026-08-21)

- Workshop files stay. Do not create, move, or delete them.
- Menu-launched xfce4-terminal cwd is `/workspace`. Inspect the six directories from there, then `cd ~/linux-workshop`.
- `ls -ld /home /tmp /etc /var /usr /bin` prints six lines; `/bin -> usr/bin`.
- `ls /home` lists `ubuntu`. `ls /var` and `ls /usr` are short. `ls -l /etc/os-release` is one config file. `ls -l /bin/ls` is the ls binary via the symlink.
- `ls /tmp/rent-log.txt` and `ls /etc/rent-log.txt` print `No such file or directory`. Then `cd ~/linux-workshop`, `pwd`, `realpath .` → `/home/ubuntu/linux-workshop`.
- Last command: `ls -l /home/ubuntu/linux-workshop/rent-log.txt` still shows the 92-byte paid-August note under home.
- Open Terminal Emulator from the desktop menu. Fullscreen. Font already JetBrains Mono 19.

## Human job

A person has the rent log in `~/linux-workshop` and needs to know that is the right place: `/tmp` can be wiped, `/etc` is the machine’s config, `/bin` is programs. Without inspecting those six names they would stash papers next to `ls` or in `/tmp`.

Candidates considered: (1) `echo` FHS names — smoke test, forbidden. (2) `mkdir /tmp/workshop` — teaches the wrong place. (3) Inspect the six live directories, prove `rent-log.txt` is missing from `/tmp` and `/etc`, `cd` into the workshop, `realpath .` is `/home/ubuntu/linux-workshop`, `ls -l` the rent log under `/home`. Picked (3).

## Done on screen

Fullscreen terminal. `ls -l /home/ubuntu/linux-workshop/rent-log.txt` shows the rent log under `/home`. `/tmp/rent-log.txt` and `/etc/rent-log.txt` did not exist.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Leave the three papers and the hidden note. Nothing new is written.

## Viewer must see created on camera

Opening Terminal Emulator, `ls -ld` of the six FHS names, looking inside `/home` `/var` `/usr` `/etc` `/bin`, the two missing `rent-log.txt` probes, walking into the workshop, `pwd`, `realpath .`, and `ls -l` of the rent log under `/home`.
