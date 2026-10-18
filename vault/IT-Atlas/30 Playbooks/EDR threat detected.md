---
type: "playbook"
level: "Mid"
severity: "P2 (P1 if not mitigated or spreading)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# EDR threat detected

> [!abstract] What this alert means
> The security agent found something malicious or suspicious.
>
> **Why it matters:** If it wasn't fully stopped, an attacker may be active on the machine.

**How urgent:** P2 (P1 if not mitigated or spreading). See [[Severity levels]].

> [!info]+ Words on this page
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## You'll see this when

- EDR or AV alert

## First 5 minutes

1. Check the status: blocked, quarantined, or not mitigated
2. Check the process tree and user
3. Check whether other machines show the same indicator

## Find the cause

- Not mitigated: isolate the machine
- Admin tool flagged (PsExec, RMM scripts): confirm it was legitimate activity
- Repeated detections: persistence still present

## Fix it

- Remediate or roll back in the EDR console
- Reset the user's password if credentials may be stolen
- Exclusions only for confirmed false positives, scoped narrowly

## Ask for help (escalate) when

- Not mitigated
- Lateral movement
- Credential theft tools (Mimikatz and similar)

## Write it up

Copy this into the ticket and fill it in:

```
Device / user: 
Detection: 
Status: 
Action: 
False positive?:
```

## See also

[[EDR & MDR]] · [[Suspected ransomware]] · [[EDR vs MDR vs XDR]]
