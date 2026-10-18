---
type: "lesson"
level: "Junior"
tags:
  - "learning"
created: "2026-10-18"
updated: "2026-10-18"
---

# Week 9 - Servers, virtualization, storage and cloud

> [!abstract] This week
> Understand where servers really run, and the hardware and cloud underneath them.

## Read these, in order

- [ ] [[Hypervisors]]
- [ ] [[VMware vSphere]]
- [ ] [[Hyper-V]]
- [ ] [[Failover Clustering]]
- [ ] [[RAID levels]]
- [ ] [[Dell iDRAC]]
- [ ] [[Microsoft 365]]
- [ ] [[Exchange Online]]
- [ ] [[Snapshot age]]
- [ ] [[RAID degraded]]
- [ ] [[Hypervisor host disconnected]]

## Practice

- [ ] On a Hyper-V host (supervised), run `Get-VM` and `Get-VMSnapshot -VMName *`.
- [ ] Open an iDRAC or iLO page and find its hardware log.
- [ ] Run a message trace in Exchange Online for one of your own emails.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why is an old VM snapshot a problem?
> It keeps growing, fills storage and slows the VM.

> [!question]- A RAID 5 disk failed. What's the first thing you confirm?
> That the last backup is good, then order the exact replacement part.

---
Part of the [[Learning path]]. Previous: [[Week 8 - Network gear and remote access]]. Next: [[Week 10 - Running the NOC]].
