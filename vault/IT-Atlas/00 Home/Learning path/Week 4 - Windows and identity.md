---
type: "lesson"
level: "Junior"
tags:
  - "learning"
created: "2026-10-18"
updated: "2026-10-18"
---

# Week 4 - Windows and identity

> [!abstract] This week
> Learn how logins work in a Windows domain and Microsoft 365, and where Windows records what happened.

## Read these, in order

- [ ] [[Active Directory]]
- [ ] [[Kerberos]]
- [ ] [[Group Policy]]
- [ ] [[Windows DNS Server]]
- [ ] [[Microsoft Entra ID]]
- [ ] [[Microsoft Entra Connect]]
- [ ] [[Windows Event Log]]
- [ ] [[Windows Event ID reference]]
- [ ] [[NTP]]

## Practice

- [ ] Run `gpresult /r` and find which Group Policies apply to you.
- [ ] Open Event Viewer and filter the System log for errors in the last 24 hours.
- [ ] In a lab or with supervision, run `dcdiag /e /q` and `repadmin /replsummary` and read the output.
- [ ] Find event 4740 (account locked out) in a domain controller's Security log.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Clocks are 10 minutes apart. What breaks?
> Kerberos logins.

> [!question]- Where do Microsoft 365 users sign in?
> Microsoft Entra ID.

> [!question]- A user is locked out repeatedly. Which event shows where the bad attempts come from?
> 4740 on the PDC emulator; it names the caller computer.

---
Part of the [[Learning path]]. Previous: [[Week 3 - How networks work]]. Next: [[Week 5 - Monitoring and the RMM]].
