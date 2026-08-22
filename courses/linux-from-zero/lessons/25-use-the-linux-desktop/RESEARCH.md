# Lesson 25 — Use the Linux desktop

Locked to this lesson only. Do not re-plan the syllabus. Do not research lesson 26 here.

## Feature

The graphical desktop is a real room. Open the XFCE file manager (Thunar), make a folder you can see, close the window, open the file manager again. The folder is still there.

## What it is / is not

- It is: Thunar 4.18.8 as the default handler for `inode/directory` (`thunar.desktop`). Create Folder from the File menu. Persistence: close, reopen, the folder remains.
- It is not: typing `mkdir` in a terminal (that is later). It is not the workshop at `~/linux-workshop` (lesson 35). It is not a smoke-test `hello` folder.

## Live sources (fetched this pass)

- Xfce Docs Thunar 4.18 start — Thunar is the XFCE file manager. https://docs.xfce.org/xfce/thunar/4.18/start
- Xfce Docs Thunar 4.18 working with files and folders — File menu **Create Folder** creates a new folder in the current folder with a name you choose. Close Window closes this instance. https://docs.xfce.org/xfce/thunar/4.18/working-with-files-and-folders

## Live operation on this host (2026-08-21)

- `thunar --version` → Thunar 4.18.8 (Xfce 4.18)
- `xdg-mime query default inode/directory` → `thunar.desktop`
- No XFCE panel. Desktop right-click applications menu includes **File Manager** (third item under Run Program / Terminal Emulator).
- Thunar File → **Create Folder...** (Shift+Ctrl+N) opens dialog **Create New Folder**, field **Enter the name:**, default `New Folder`.
- Home listing currently shows a `go` directory. No `rent-receipts` yet. Create that name on camera.
- This host has no `~/Desktop` directory. Create the folder in home (`/home/ubuntu`), which Thunar titles `ubuntu`.

## Human job

A person needs a place for this month’s rent receipts before they scan them. They make a `rent-receipts` folder in home with the file manager, close it, and open the file manager again to prove the folder is still there.

## Done on screen

Last frames of the reopened fullscreen Thunar show a folder named `rent-receipts` in `/home/ubuntu` (status: more than the original `go` folder).

## Terminal font

No terminal in this lesson. Desktop GUI only.

## Workshop

Still starts at lesson 35. Do not create `~/linux-workshop` here.

## Viewer must see created on camera

Opening File Manager from the desktop menu, Create Folder, the name `rent-receipts`, Close, open File Manager again, the folder still visible. Do not pre-create `rent-receipts`.
