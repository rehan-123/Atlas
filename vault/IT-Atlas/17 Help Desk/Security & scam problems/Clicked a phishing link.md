---
type: "guide"
level: "Junior"
area: "[[Security & scam problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Clicked a phishing link

> [!abstract] What's going on
> Someone clicked a link or opened an attachment in a suspicious email, or typed their password into a fake page.

> [!tip] Think of it like
> Letting a stranger into the building: you don't hide it, you tell security straight away so they can follow him.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Security & scam problems]]

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **malware**: Any harmful software: viruses, ransomware, spyware and the like.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Tell IT immediately. You won't be in trouble; quick reporting limits the damage.
2. If you typed your password, say so; IT will change it.
3. Don't forward the email to colleagues. Use the Report button.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- If credentials were entered: reset the password, revoke sessions and check MFA methods for anything new.
- Check sign-in logs for unusual locations and check inbox rules and forwarding.
- If a file was opened: isolate the device in the EDR and run a full scan.
- Search for and remove the same email from other mailboxes (Defender Threat Explorer or the email filter).
- Block the sender and link domain.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Password typed into a fake page | Reset, revoke sessions, review sign-ins. |
| Attachment opened | Isolate and scan the device. |
| Only clicked, nothing entered | Scan, check browser, monitor. |

## Escalate when

- Signs of compromise in sign-in logs or rules
- Malware detected
- Several people clicked

## Write it up

Copy this into the ticket and fill it in:

```
User and contact: 
Device: 
Problem (in their words): 
Exact error message: 
Started when / what changed: 
What I checked: 
What fixed it: 
User confirmed it's fixed (yes/no): 
```

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A user typed their password into a fake Microsoft page an hour ago. List three first actions.
> Reset the password, revoke sign-in sessions, check sign-in logs and inbox rules (and MFA methods) for attacker activity.

## See also

[[Spotting phishing]] · [[Account hacked or sending spam]] · [[Multi-factor authentication]] · [[EDR threat detected]] · [[Microsoft Defender for Office 365]]

## Field notes

Add your own tips and client quirks here.
