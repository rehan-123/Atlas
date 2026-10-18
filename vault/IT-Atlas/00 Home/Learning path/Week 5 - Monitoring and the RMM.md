---
type: "lesson"
level: "Junior"
tags:
  - "learning"
created: "2026-10-18"
updated: "2026-10-18"
---

# Week 5 - Monitoring and the RMM

> [!abstract] This week
> Learn how the NOC sees problems, and how to tell a real alert from noise.

## Read these, in order

- [ ] [[RMM]]
- [ ] [[Agent heartbeat]]
- [ ] [[Monitoring thresholds and baselines]]
- [ ] [[Alert fatigue]]
- [ ] [[SNMP]]
- [ ] [[WMI]]
- [ ] [[Agent offline]]
- [ ] [[Low disk space]]
- [ ] [[High CPU]]
- [ ] [[Windows service stopped]]
- [ ] [[Agent & service names]]

## Practice

- [ ] Pick one alert in your RMM and follow its playbook end to end.
- [ ] Find your RMM's agent service name on a PC (`Get-Service`) and check whether it's running.
- [ ] Look at a week of one server's CPU graph and say what 'normal' looks like.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- An agent is offline. What do you check before escalating?
> Whether the device is really down (ping, hypervisor, user) and whether the whole site is offline.

> [!question]- Why should every alert have an owner and a playbook?
> Otherwise alerts are ignored and real problems get missed.

---
Part of the [[Learning path]]. Previous: [[Week 4 - Windows and identity]]. Next: [[Week 6 - Backup and recovery]].
