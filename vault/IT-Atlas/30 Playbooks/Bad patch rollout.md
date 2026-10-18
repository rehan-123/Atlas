---
type: "playbook"
level: "Senior"
severity: "P1 or P2 depending on spread"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Bad patch rollout

> [!abstract] What this alert means
> An update deployed to many machines is causing failures: crashes, broken apps or boot problems.
>
> **Why it matters:** One bad patch can break hundreds of endpoints in hours; stopping the rollout early matters most.

**How urgent:** P1 or P2 depending on spread. See [[Severity levels]].

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **KB**: A Microsoft Knowledge Base number, which identifies a specific update (for example KB5034441).
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **domain controller**: A server running Active Directory that checks logins.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## You'll see this when

- Many tickets with the same symptom after Patch Tuesday
- RMM shows install failures or reboots looping
- Vendor advisory about a faulty update

## First 5 minutes

1. Pause the patch policy or approval in the RMM, WSUS or Intune ring
2. Identify the KB or version in common on affected machines
3. Check Microsoft release health and vendor known issues

## Find the cause

- Compare a working and a broken machine: update history, driver versions
- Check whether only one model, app or OS build is affected

## Fix it

- Uninstall the update (wusa /uninstall /kb:NUMBER or DISM) where safe
- Apply Microsoft's known-issue rollback or workaround
- Block the update until a fix is released

## Ask for help (escalate) when

- Servers or domain controllers affected
- Machines won't boot
- More than one client affected

## Write it up

Copy this into the ticket and fill it in:

```
Update: 
Affected devices: 
Rollout paused at: 
Workaround: 
Communication sent:
```

## See also

[[Patch rings]] · [[Patch failure or pending reboot]] · [[Windows Update]] · [[Patch Tuesday]]
