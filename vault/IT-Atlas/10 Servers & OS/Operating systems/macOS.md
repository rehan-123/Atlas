---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Operating systems]]"
vendor: "[[Apple]]"
deployment: "Endpoints"
status: "current"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# macOS

> [!abstract] In plain words
> Apple's operating system for Macs, usually managed with Jamf or Intune.
>
> **What kind of tool is this?** The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

**Made by:** [[Apple]] · **Runs:** Endpoints · **Category:** [[Servers & Operating Systems]] › [[Operating systems]]

> [!info]+ Words on this page
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Apple's desktop OS, managed through MDM (Jamf, Intune, Addigy) and enrolled through Apple Business Manager.

## Where to find its logs

- `/var/log/install.log`
- log show --predicate 'process == "softwareupdated"' --last 1h

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
sw_vers
softwareupdate -l
profiles status -type enrollment
fdesetup status
log show --last 30m
```

## See also

[[Jamf Pro]] · [[Apple Business Manager]] · [[FileVault]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
