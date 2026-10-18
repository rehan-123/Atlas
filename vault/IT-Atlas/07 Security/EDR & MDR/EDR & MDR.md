---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# EDR & MDR

> [!abstract] In plain words
> EDR is modern antivirus: it records what happens on each computer and can stop and undo attacks. MDR adds a team of security people who watch it 24x7.

Part of [[Security]].

- [[Microsoft Defender for Endpoint]]: Microsoft's security product built into Windows. It is the antivirus plus attack detection and response, managed from the Defender portal.
- [[SentinelOne]]: A modern security agent that detects attacks and can roll back damage such as encrypted files.
- [[CrowdStrike Falcon]]: A widely used security agent. Famous for a faulty update in July 2024 that crashed millions of Windows PCs worldwide.
- [[Huntress]]: Security built for MSPs: a human security team watches Defender, Microsoft 365 sign-ins and logs, and tells you what to fix.
- [[Sophos Intercept X]]: Sophos' security agent with strong anti-ransomware features.
- [[Bitdefender GravityZone]]: Bitdefender's business antivirus and detection platform.
- [[ESET PROTECT]]: ESET's business antivirus and management console.
- [[ThreatDown]]: Malwarebytes' business security products.
- [[Webroot]]: Lightweight cloud antivirus, long popular with MSPs.
- [[Datto EDR]]: Kaseya's attack detection agent, linked with Datto RMM.
- [[Blackpoint Cyber]]: A 24x7 security monitoring team for MSPs that can step in and stop attacks.
- [[Arctic Wolf]]: A 24x7 security monitoring service with its own team and sensors.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/EDR & MDR"
WHERE type = "tool"
SORT file.name ASC
```
