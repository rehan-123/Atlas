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

# Set up out of office

> [!abstract] What's going on
> A user wants automatic replies while away.

> [!tip] Think of it like
> A note on the door saying when you'll be back and who to ask meanwhile.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **offboarding**: Removing a leaver's access while keeping their data for the business.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Outlook: File > Automatic Replies (classic) or Settings > Account > Automatic replies (new Outlook and web).
2. Set the dates, write separate inside and outside messages, and save.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Admins can set it for a user: Set-MailboxAutoReplyConfiguration -Identity USER -AutoReplyState Scheduled -StartTime DATE -EndTime DATE -InternalMessage TEXT -ExternalMessage TEXT.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Replies not sent externally | Check the external message is enabled. |

## Escalate when

- Leaver's mailbox needs a permanent auto-reply (follow offboarding policy)

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

> [!question]- Which cmdlet sets automatic replies for another user?
> `Set-MailboxAutoReplyConfiguration`.

## See also

[[Exchange Online]] · [[Leaver offboarding]]

## Field notes

Add your own tips and client quirks here.
