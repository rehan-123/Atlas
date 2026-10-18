---
type: "playbook"
level: "Mid"
severity: "P1 or P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Hypervisor host disconnected

> [!abstract] What this alert means
> A server that runs virtual machines isn't responding to its management console.
>
> **Why it matters:** The VMs on it may be down, or simply can't be managed.

**How urgent:** P1 or P2. See [[Severity levels]].

> [!info]+ Words on this page
> **ESXi**: VMware's hypervisor, the software installed on the physical server that runs VMs.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **HA**: High availability: designed so one failure doesn't cause downtime.
> **NIC**: Network interface card: a computer's network adapter.
> **VLAN**: A virtual network that separates traffic on the same physical switches.
> **cluster**: Several servers working together so one can take over if another fails.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- ESXi host not responding in vCenter
- Hyper-V cluster node down

## First 5 minutes

1. Check whether VMs are still running (often they are; only management is lost)
2. Check HA: did VMs restart elsewhere?
3. Open the out-of-band console

## Find the cause

- Management agents hung (ESXi hostd and vpxa)
- Management network problem
- Host crashed (PSOD on ESXi, bugcheck on Hyper-V)
- Storage paths lost

## Fix it

- Restart management agents on ESXi
- Fix the management NIC or VLAN
- For a crash, collect logs and dumps before rebooting

## Ask for help (escalate) when

- VMs down
- Host crashed
- Storage problems on multiple hosts

## Write it up

Copy this into the ticket and fill it in:

```
Host: 
VMs affected: 
HA action: 
Cause: 
Action:
```

## See also

[[VMware vSphere]] · [[Hyper-V]] · [[Failover Clustering]] · [[Server unreachable]]
