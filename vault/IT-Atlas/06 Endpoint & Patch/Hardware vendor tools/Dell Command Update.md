---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[Hardware vendor tools]]"
vendor: "[[Dell]]"
deployment:
status: "current"
aliases:
  - "DCU"
tags:
  - "tool"
  - "endpoint"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Dell Command Update

> [!abstract] In plain words
> Dell's tool that installs the right drivers, BIOS and firmware updates for a Dell PC.
>
> **What kind of tool is this?** Hardware vendor tools keep a laptop's drivers, BIOS and firmware up to date, which Windows Update doesn't fully cover.

**Made by:** [[Dell]] · **Category:** [[Endpoint & Patch Management]] › [[Hardware vendor tools]]

> [!info]+ Words on this page
> **BIOS**: The low-level setup program that starts a PC before Windows loads (UEFI on modern PCs).
> **CLI**: Command-line interface: typing commands instead of clicking.
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Driver, BIOS and firmware updater for Dell business systems with a CLI (dcu-cli.exe) for scripted updates through an RMM.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
"C:\Program Files\Dell\CommandUpdate\dcu-cli.exe" /scan
"C:\Program Files\Dell\CommandUpdate\dcu-cli.exe" /applyUpdates -reboot=disable
```

## Good to know

- BIOS updates can trigger BitLocker recovery; suspend BitLocker first (Suspend-BitLocker -MountPoint C: -RebootCount 1).

## See also

[[Drivers]] · [[BitLocker]] · [[Patch management]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
