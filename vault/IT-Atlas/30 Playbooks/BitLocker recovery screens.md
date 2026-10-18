---
type: "playbook"
level: "Mid"
severity: "P3 (P2 if many devices)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# BitLocker recovery screens

> [!abstract] What this alert means
> One or many PCs are asking for a BitLocker recovery key at startup.
>
> **Why it matters:** Users can't work until the key is entered; many at once usually means a BIOS, firmware or policy change triggered it.

**How urgent:** P3 (P2 if many devices). See [[Severity levels]].

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **BIOS**: The low-level setup program that starts a PC before Windows loads (UEFI on modern PCs).
> **TPM**: A security chip in the computer that stores encryption keys, used by BitLocker.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Users report a blue BitLocker recovery screen
- Several devices of the same model affected after updates

## First 5 minutes

1. Get the key ID from the screen and look it up in Entra ID/Intune or AD
2. Check whether a BIOS/firmware update or TPM change happened
3. Pause the update that caused it if many devices are affected

## Find the cause

- BIOS or firmware update without suspending BitLocker
- Secure Boot or TPM changes
- Docking or boot-order changes on some models

## Fix it

- Enter the recovery key, then Suspend-BitLocker -MountPoint C: -RebootCount 1 and resume after
- Update the rollout to suspend BitLocker before firmware updates

## Ask for help (escalate) when

- Recovery key not found
- More than a handful of devices affected

## Write it up

Copy this into the ticket and fill it in:

```
Devices: 
Key IDs: 
Trigger: 
Keys found in: 
Prevention:
```

## See also

[[BitLocker]] · [[Computer won't start Windows]] · [[Dell Command Update]]
