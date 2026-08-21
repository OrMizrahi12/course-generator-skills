# Lesson 27 — Read the prompt

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 28 here.

## Feature

Read the shell prompt as a short nameplate, then ask the computer for the three facts it hid: user, host, and full path.

## What it is / is not

- It is: Bash `PS1` on this host. Live value is `\[\e[36m\]\W\[\e[0m\] $` — cyan `\W` (basename of `$PWD`; home would show as `~`) and a `$`. Debian’s default in `/etc/bash.bashrc` is `\u@\h:\w\$`. This machine overrode that in `~/.bashrc`. A desktop-launched terminal here often starts in `/workspace`, so the prompt prints `workspace $`. That word is a folder, not a person.
- It is not: customizing the prompt. It is not `whoami` (lesson 4) or `hostname` (lesson 15). It is not `echo`. It is not finding home with `~` / `$HOME` (later). It is not starting `~/linux-workshop`.

## Live sources (fetched this pass)

- ArchWiki Bash/Prompt customization — `PS1` is the primary prompt; Bash expands backslash escapes. gnu.org Bash manual HTML returned 403 from this network. https://wiki.archlinux.org/title/Bash/Prompt_customization
- SS64 bash prompt variables — `\u` username, `\h` hostname up to the first dot, `\w` working directory, `\W` basename of `$PWD`, `\$` `$` or `#`. https://ss64.com/bash/syntax-prompt.html
- Ubuntu Noble `id(1)` GNU coreutils 9.4 — `-u` effective user ID, `-n` print a name. `id -un` is the account name. https://manpages.ubuntu.com/manpages/noble/man1/id.1.html
- Ubuntu Noble `uname(1)` — `-n` / `--nodename` prints the network node hostname. https://manpages.ubuntu.com/manpages/noble/man1/uname.1.html
- Ubuntu Noble `pwd(1)` — print the full filename of the current working directory. https://manpages.ubuntu.com/manpages/noble/en/man1/pwd.1.html

## Live operation on this host (2026-08-21)

- `~/.bashrc` sets `PS1="\[\e[36m\]\W\[\e[0m\] $ "`. Agent shells and desktop Terminal Emulator both use it.
- Right-click wallpaper → **Terminal Emulator**. Window ~1502×1022 until fullscreened. Font already JetBrains Mono 19.
- Menu-launched terminal cwd is `/workspace` (same as lesson 26). Prompt: cyan `workspace` then ` $`.
- `id -un` → `ubuntu`. `uname -n` → `cursor`. `pwd` → `/workspace`.
- Debian default `\u@\h:\w\$` would have shown `ubuntu@cursor:/workspace$`. This host’s `\W` hid user and host and shortened the path.
- `hostnamectl` still fails (PID 1 is tini). Do not film it.
- `rent-receipts` exists from lesson 25. Do not recreate it.

## Human job

A person just ran `date` for a rent receipt and still sees `workspace $`. That looks like a username. Before they write a receipt path they must know whose account, which computer, and which folder they are in. Decoding the prompt is required; guessing from the cyan word is how files land in the wrong house.

Candidates considered: (1) `echo "$PS1"` — shows the template, not the three facts. (2) `cat ~/.bashrc` — how the prompt was made, not how to read it. (3) Open Terminal Emulator and run `id -un`, `uname -n`, `pwd` — the mismatch is on screen. Picked (3).

## Done on screen

Fullscreen terminal opened from the desktop menu. Prompt `workspace $` visible. Then `id -un` prints `ubuntu`, `uname -n` prints `cursor`, `pwd` prints `/workspace`. Last frames hold the full path under that prompt.

## Terminal font

JetBrains Mono 19 already set (1.75× default). Filming setup, not on-camera.

## Workshop

Still starts at lesson 35.

## Viewer must see created on camera

Opening Terminal Emulator from the desktop menu (the prompt is the lesson object), the cyan `workspace $`, typing the three commands, and the three printed facts. Do not spawn the terminal off-camera. Do not pre-run the three commands.
