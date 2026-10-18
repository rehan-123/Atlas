---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[Encryption]]"
vendor: "[[Microsoft]]"
deployment: "Built into Windows"
status: "current"
aliases: []
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# BitLocker

> [!abstract] In plain words
> Windows' built-in disk encryption. Make sure every recovery key is saved somewhere you can find it.
>
> **What kind of tool is this?** Disk encryption scrambles everything on a laptop's drive, so a lost or stolen device doesn't leak data.

**Made by:** [[Microsoft]] · **Runs:** Built into Windows · **Category:** [[Security]] › [[Encryption]]

> [!info]+ Words on this page
> **TPM**: A security chip in the computer that stores encryption keys, used by BitLocker.
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **BIOS**: The low-level setup program that starts a PC before Windows loads (UEFI on modern PCs).
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> *More in the [[Glossary]].*

## In more detail

Windows full-disk encryption using the TPM, with recovery keys escrowed to Entra ID, Active Directory or your RMM.

## Alerts you'll see

- Devices unencrypted
- Recovery key not escrowed
- Machines asking for recovery keys after BIOS or firmware updates

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Unexpected recovery prompt | Usually TPM measurements changed (firmware, Secure Boot, boot order); suspend BitLocker before firmware updates |
| Need the recovery key | Look it up in Entra ID, AD or your RMM by the key ID shown on screen |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
manage-bde -status
manage-bde -protectors -get C:
Suspend-BitLocker -MountPoint C: -RebootCount 1
Get-BitLockerVolume
```

## See also

[[Microsoft Intune]] · [[Microsoft Entra ID]] · [[CrowdStrike Falcon]] · [[FileVault]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
