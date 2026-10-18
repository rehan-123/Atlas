---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# Email security

> [!abstract] In plain words
> Email security filters catch phishing, malware and fake senders before the mail reaches the user.

Part of [[Security]].

- [[Microsoft Defender for Office 365]]: Microsoft's email protection: it scans links and attachments and keeps suspicious mail in quarantine.
- [[Proofpoint]]: An email security filter that sits in front of the mailbox and stops spam and phishing.
- [[Mimecast]]: An email security filter with archiving and backup options.
- [[Barracuda Email Protection]]: Barracuda's email filtering and protection.
- [[Avanan]]: Email security that connects directly to Microsoft 365 or Gmail and scans mail inside the mailbox.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/Email security"
WHERE type = "tool"
SORT file.name ASC
```
