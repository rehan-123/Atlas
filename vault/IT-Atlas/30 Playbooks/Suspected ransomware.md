---
type: "playbook"
level: "Senior"
severity: "P1"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Suspected ransomware

> [!abstract] What this alert means
> Signs that files are being encrypted by an attacker.
>
> **Why it matters:** Every minute counts: the faster you isolate machines, the less is lost.

**How urgent:** P1. See [[Severity levels]].

> [!info]+ Words on this page
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **immutable**: Can't be changed or deleted until a set date, even by an admin.
> *More in the [[Glossary]].*

## You'll see this when

- Mass file renames or encryption
- Ransom notes
- EDR ransomware detection
- Backups or shadow copies deleted

## First 5 minutes

1. Isolate affected machines from the network (EDR isolation or pull the cable); do not power them off
2. Disable the compromised accounts and protect backup consoles (change credentials, confirm MFA)
3. Escalate to the security lead and the client immediately

## Find the cause

- Identify patient zero and the encryption scope
- Check backups and immutable copies are intact
- Preserve evidence for incident response and insurance

## Fix it

- Follow the incident response plan; involve the cyber insurer and IR firm before restoring
- Restore from clean, verified backups only after the attacker's access is removed

## Ask for help (escalate) when

- Always: this is a P1 security incident

## Write it up

Copy this into the ticket and fill it in:

```
Detected: 
Scope: 
Isolation actions: 
Accounts disabled: 
Backups status: 
Escalated to:
```

## See also

[[EDR threat detected]] · [[Immutability & air gap]] · [[3-2-1-1-0 rule]] · [[Huntress]] · [[Microsoft Defender for Endpoint]]
