---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# SMB signing and versions

> [!abstract] In one line
> Why SMB version and signing settings break file sharing between old and new devices.

> [!tip] Think of it like
> A newer, safer lock on the door: old keys stop working until they're cut again.

> [!info]+ Words on this page
> **NAS**: Network-attached storage: a box full of disks that shares files over the network.
> **SMB**: The Windows file-sharing protocol (port 445).
> *More in the [[Glossary]].*

## How it works

- SMBv1 is obsolete and insecure; it's removed or disabled on modern Windows. Old copiers and NAS devices may still need it: replace or update them.
- SMB signing protects against tampering; recent Windows versions require it by default in more cases, which can break old NAS devices.
- `Get-SmbConnection` shows the dialect in use; `Get-SmbServerConfiguration` shows signing and SMB1 settings.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- After a Windows update, scans to a network folder from an old copier stop working. What should you check?
> Whether the copier only supports SMBv1 or can't do SMB signing, which the updated server now requires.

## See also

[[File Server & DFS]] · [[Samba]] · [[Hardening baselines]] · [[Scan to email not working]]
