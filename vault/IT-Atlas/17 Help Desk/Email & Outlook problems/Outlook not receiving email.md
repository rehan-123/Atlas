---
type: "guide"
level: "Junior"
area: "[[Email & Outlook problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Outlook not receiving email

> [!abstract] What's going on
> New emails aren't arriving, or someone says they sent something that never came.

> [!tip] Think of it like
> A post box: first check whether the letter reached the sorting office (the server) before blaming your letterbox (Outlook).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **message trace**: Exchange tool that shows whether an email arrived, where it went and why.
> **quarantine**: A holding area for suspicious emails or files, so they can't do harm.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check Outlook on the web: if the email is there, Outlook just needs to sync.
2. Check the Junk Email folder and any Other or Focused tab.
3. Look at the bottom of Outlook: does it say 'Working offline' or 'Disconnected'?

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Run a message trace in the Exchange admin center for the sender and time.
- Check inbox rules (`Get-InboxRule -Mailbox USER`) for rules moving or deleting mail.
- Check quarantine in Defender or the email filter (Mimecast, Proofpoint).
- Check the mailbox isn't full (`Get-EXOMailboxStatistics USER`).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Mail in Junk or Other | Mark as not junk; add a safe sender. |
| Inbox rule moving it | Fix or remove the rule (and check it isn't a hacker's rule). |
| Held in quarantine | Release it if it's safe. |
| Sender's problem | Message trace shows nothing arrived: the sender should check their bounce message. |

## Escalate when

- Nothing is arriving for the whole company
- A strange forwarding or delete rule exists (possible hacked account)

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

> [!question]- What tool proves whether an email reached Microsoft 365 at all?
> Message trace in the Exchange admin center.

## See also

[[Exchange Online]] · [[Email delivery problems]] · [[Email went to junk]] · [[Account hacked or sending spam]] · [[Mimecast]] · [[Proofpoint]]

## Field notes

Add your own tips and client quirks here.
