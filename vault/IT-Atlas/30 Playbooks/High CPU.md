---
type: "playbook"
level: "Junior"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# High CPU

> [!abstract] What this alert means
> The processor has been very busy for a long time.
>
> **Why it matters:** Everything on the machine slows down; it can also be a sign of malware.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **Task Manager**: Windows tool (Ctrl+Shift+Esc) that shows running apps and what's using CPU, memory and disk.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **threshold**: The value that triggers an alert.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **malware**: Any harmful software: viruses, ransomware, spyware and the like.
> *More in the [[Glossary]].*

## You'll see this when

- CPU above threshold for a sustained period

## First 5 minutes

1. Identify the process (Task Manager, `Get-Process | Sort CPU -Desc`, top)
2. Check whether it is expected (backup, AV scan, patching, end-of-month jobs)
3. Check user impact

## Find the cause

- Process Explorer shows which thread and module; Procmon shows what it is doing
- svchost.exe: find the service inside it (`tasklist /svc /fi "imagename eq svchost.exe"`)
- On VMs, check host CPU ready time; the guest may be starved, not busy

## Fix it

- Reschedule heavy jobs outside business hours
- Restart a runaway service after capturing details
- Add vCPU only after proving it is a capacity issue

## Ask for help (escalate) when

- Unknown process using CPU (possible cryptominer)
- Production impact longer than 30 minutes

## Write it up

Copy this into the ticket and fill it in:

```
Host: 
Process: 
Duration: 
Cause: 
Action:
```

## See also

[[Sysinternals Suite]] · [[Monitoring thresholds and baselines]] · [[High memory]]
