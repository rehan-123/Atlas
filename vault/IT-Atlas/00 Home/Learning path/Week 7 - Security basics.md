---
type: "lesson"
level: "Junior"
tags:
  - "learning"
created: "2026-10-18"
updated: "2026-10-18"
---

# Week 7 - Security basics

> [!abstract] This week
> Learn the security tools you'll see daily and what to do in the first minutes of an incident.

## Read these, in order

- [ ] [[Multi-factor authentication]]
- [ ] [[Least privilege]]
- [ ] [[EDR vs MDR vs XDR]]
- [ ] [[Microsoft Defender for Endpoint]]
- [ ] [[CVE & CVSS]]
- [ ] [[Patch Tuesday]]
- [ ] [[SPF, DKIM & DMARC]]
- [ ] [[EDR threat detected]]
- [ ] [[Suspected ransomware]]
- [ ] [[Account lockout storm]]

## Practice

- [ ] Run `Get-MpComputerStatus` and check real-time protection is on and signatures are recent.
- [ ] Look up a domain's SPF and DMARC records with `Resolve-DnsName -Type TXT`.
- [ ] Read the Suspected ransomware playbook twice; the first steps must become automatic.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Ransomware is spreading. Do you power machines off?
> No. Isolate them from the network and keep them on, to preserve evidence.

> [!question]- Which vulnerabilities do you patch first?
> Ones being actively exploited, especially on internet-facing devices.

---
Part of the [[Learning path]]. Previous: [[Week 6 - Backup and recovery]]. Next: [[Week 8 - Network gear and remote access]].
