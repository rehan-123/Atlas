---
type: "guide"
level: "Mid"
area: "[[New starters & leavers]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Leaver offboarding

> [!abstract] What's going on
> Closing access for someone who has left, while keeping their data for the business.

> [!tip] Think of it like
> Collecting keys when someone moves out, and changing the locks they could still open.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[New starters & leavers]]

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **Wi-Fi**: Wireless network connection using radio signals.
> **retention**: How long backups or logs are kept.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Managers: tell IT the leaving date and time, and who should get the person's email and files.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- At the leaving time: block sign-in, reset the password and revoke sessions.
- Convert the mailbox to a shared mailbox (or forward it) per policy, and give the manager access.
- Give the manager access to the user's OneDrive files before the license is removed.
- Remove from groups, remove the license, and remove MFA methods and devices.
- Collect and wipe the laptop and phone; check shared passwords they knew and change them.
- Don't delete the account straight away; follow the retention policy.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Sudden departure | Block sign-in immediately. |
| Data needed later | Shared mailbox and OneDrive access before license removal. |
| Shared admin or Wi-Fi passwords | Rotate them. |

## Escalate when

- The leaver was an admin or had access to finances
- There's a dispute or the leaver may be hostile: coordinate with HR

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

> [!question]- Why convert a leaver's mailbox to a shared mailbox?
> Shared mailboxes don't need a license (up to a size limit), and colleagues can keep reading the mail.

## See also

[[Microsoft Entra ID]] · [[Exchange Online]] · [[SharePoint & OneDrive]] · [[New starter setup]] · [[Lost or stolen device]]

## Field notes

Add your own tips and client quirks here.
