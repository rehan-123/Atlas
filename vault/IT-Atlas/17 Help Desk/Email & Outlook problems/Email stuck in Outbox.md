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

# Email stuck in Outbox

> [!abstract] What's going on
> An email sits in the Outbox and won't send.

> [!tip] Think of it like
> A parcel too heavy for the van: it waits at the door until you make it lighter.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check you're online and Outlook isn't set to Work Offline (Send/Receive tab).
2. Check the attachment size: Microsoft 365 usually allows around 20 to 35 MB per email. Share a OneDrive link instead.
3. Open the stuck email, then close it and click Send/Receive All Folders.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Move the stuck email to Drafts, remove the attachment and resend.
- Check whether the user can send from Outlook on the web.
- Check whether the account is blocked from sending (Defender restricted users after spam).
- Rebuild the profile if many messages are stuck.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Attachment too big | Send a OneDrive or SharePoint link. |
| Working offline | Turn off Work Offline. |
| Account blocked from sending | Investigate for compromise before unblocking. |
| Damaged profile | New profile. |

## Escalate when

- The account was blocked for sending spam
- No one can send email

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

> [!question]- Why might Microsoft block a user from sending email?
> Because the account sent spam-like volumes of mail, usually after being hacked. Treat it as a security incident.

## See also

[[Exchange Online]] · [[Account hacked or sending spam]] · [[Outlook won't open]]

## Field notes

Add your own tips and client quirks here.
