---
type: "playbook"
level: "Mid"
severity: "P2 (P1 for critical servers)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# VM won't start

> [!abstract] What this alert means
> A virtual machine fails to power on or start.
>
> **Why it matters:** The service on that VM is down until it starts.

**How urgent:** P2 (P1 for critical servers). See [[Severity levels]].

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **VHDX**: A virtual hard disk file used by Hyper-V and FSLogix.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **datastore**: In VMware, the storage where virtual machines' disk files live.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Hypervisor shows a power-on error
- Monitoring shows the VM down after maintenance

## First 5 minutes

1. Read the exact error in vCenter or Hyper-V Manager / event log
2. Check host free memory and datastore free space
3. Check whether the VM has a snapshot or backup lock (a stuck backup job)

## Find the cause

- Datastore full (swap file can't be created)
- File lock held by another host or a backup proxy
- Missing or moved virtual disk
- Hyper-V: VM configuration version or permissions on the VHDX
- Not enough memory on the host

## Fix it

- Free datastore space or reduce memory reservation
- Release the lock (stop the backup job, restart the backup proxy or management agent)
- Re-attach the disk from its real path
- Start the VM on another host

## Ask for help (escalate) when

- Disk files corrupted or missing
- Several VMs on the same storage affected

## Write it up

Copy this into the ticket and fill it in:

```
VM: 
Host: 
Error: 
Cause: 
Action: 
Services verified:
```

## See also

[[Hyper-V]] · [[VMware vSphere]] · [[Snapshot age]] · [[Hypervisor host disconnected]]
