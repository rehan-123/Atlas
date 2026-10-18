---
type: "concept"
level: "Mid"
category: "[[Security concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# CVE & CVSS

> [!abstract] In one line
> CVE IDs name vulnerabilities; CVSS scores their severity from 0 to 10.

> [!tip] Think of it like
> A CVE is a vulnerability's ID number; CVSS is its danger score from 0 to 10.

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **CVE**: A public ID number for a specific security vulnerability.
> **vulnerability**: A weakness an attacker can use.
> *More in the [[Glossary]].*

## How it works

- Prioritize what is actually exploited, not just high scores: CISA's Known Exploited Vulnerabilities (KEV) catalog and EPSS help.
- Internet-facing edge devices (firewalls, VPNs, remote access, file transfer) with exploited CVEs are emergencies.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Should you always patch the highest CVSS score first?
> Not always. Patch what's actively exploited first, especially internet-facing devices.

## See also

[[Vulnerability management]] · [[Patch Tuesday]]
