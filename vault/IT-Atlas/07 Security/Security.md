---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# Security

Detection, response, filtering and hardening layers that a NOC monitors or runs alongside a SOC.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Layer controls: identity (MFA, conditional access), endpoint (EDR), email, DNS filtering, backups. No single tool is enough.
> - Have an incident response plan with roles and contacts before you need it; practise it.
> - Prioritize by exploitation in the wild (KEV lists), exposure and asset value, not CVSS alone.
> - Review admin rights and third-party access regularly; most breaches use valid credentials.

## [[EDR & MDR]]

EDR is modern antivirus: it records what happens on each computer and can stop and undo attacks. MDR adds a team of security people who watch it 24x7.

- [[Microsoft Defender for Endpoint]]
- [[SentinelOne]]
- [[CrowdStrike Falcon]]
- [[Huntress]]
- [[Sophos Intercept X]]
- [[Bitdefender GravityZone]]
- [[ESET PROTECT]]
- [[ThreatDown]]
- [[Webroot]]
- [[Datto EDR]]
- [[Blackpoint Cyber]]
- [[Arctic Wolf]]

## [[SIEM]]

A SIEM collects security logs from everywhere and looks for patterns that mean an attack.

- [[Microsoft Sentinel]]
- [[Splunk]]
- [[Wazuh]]
- [[Blumira]]

## [[Email security]]

Email security filters catch phishing, malware and fake senders before the mail reaches the user.

- [[Microsoft Defender for Office 365]]
- [[Proofpoint]]
- [[Mimecast]]
- [[Barracuda Email Protection]]
- [[Avanan]]

## [[DNS & web filtering]]

DNS filtering blocks bad or unwanted websites by refusing to look up their addresses.

- [[Cisco Umbrella]]
- [[DNSFilter]]
- [[WebTitan]]

## [[Vulnerability management]]

Vulnerability scanners look for missing patches and weak settings, so you can fix them before attackers find them.

- [[Tenable Nessus]]
- [[Qualys VMDR]]
- [[Rapid7 InsightVM]]
- [[ConnectSecure]]
- [[Microsoft Defender Vulnerability Management]]

## [[Privileged access & passwords]]

These tools store passwords safely and control who can use admin accounts.

- [[Windows LAPS]]
- [[Keeper]]
- [[Bitwarden]]
- [[N-able Passportal]]
- [[CyberArk]]

## [[SASE & ZTNA]]

These cloud services replace the old office VPN: users get to the apps they're allowed to use, from anywhere, with security checks on every connection.

- [[Zscaler]]
- [[Cloudflare Zero Trust]]
- [[Netskope]]
- [[Twingate]]
- [[Prisma Access]]
- [[Cato SASE Cloud]]

## [[Application control]]

Application control only lets approved programs run, so unknown or malicious software is blocked by default.

- [[ThreatLocker]]
- [[App Control for Business]]
- [[AppLocker]]

## [[Encryption]]

Disk encryption scrambles everything on a laptop's drive, so a lost or stolen device doesn't leak data.

- [[BitLocker]]
- [[FileVault]]

## Playbooks for this area

[[BitLocker recovery screens]] · [[Business email compromise]] · [[Email delivery problems]] · [[Screenshot verification failed]] · [[Suspected ransomware]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "07 Security"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
