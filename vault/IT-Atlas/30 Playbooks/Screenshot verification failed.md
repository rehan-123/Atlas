---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Screenshot verification failed

> [!abstract] What this alert means
> The automatic boot test of a backup didn't show a working login screen.
>
> **Why it matters:** That backup might not boot when you really need it.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Backup boot test (screenshot, SureBackup, Recovery Assurance) failed

## First 5 minutes

1. Open the screenshot or test report: what is on screen?

## Find the cause

- BitLocker recovery prompt in the test VM
- CHKDSK or update pending at boot
- Driver or boot configuration problem in the virtual environment
- Machine was mid-update when the backup ran
- Test timed out because the VM boots slowly

## Fix it

- Retry with the next backup point
- Run CHKDSK on the protected machine
- Adjust boot wait time
- Check the latest backup is application-consistent

## Ask for help (escalate) when

- Two consecutive points fail to boot
- Any sign the protected system itself won't boot

## Write it up

Copy this into the ticket and fill it in:

```
Machine: 
What the screenshot showed: 
Action: 
Next test result:
```

## See also

[[Backup verification]] · [[Datto BCDR]] · [[BitLocker]]
