---
type: "guide"
level: "Mid"
area: "[[Email & Outlook problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Email went to junk

> [!abstract] What's going on
> A real email landed in Junk, or your emails go to other people's spam.

> [!tip] Think of it like
> A security guard who doesn't recognise a visitor's ID: give the guard a photo (safe sender) or fix the visitor's ID (SPF, DKIM, DMARC).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **SPF**: A DNS record listing which servers may send email for a domain.
> **DKIM**: An email signature that proves a message really came from your domain and wasn't changed.
> **DMARC**: An email rule that tells receivers what to do with mail that fails SPF or DKIM checks.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Right-click the email > Report or Mark as not junk.
2. Add the sender to Safe senders.
3. If your emails go to other people's spam, ask them to check their junk folder and tell IT.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Read the message headers (Authentication-Results) for SPF, DKIM and DMARC results.
- Check your domain's records: `Resolve-DnsName -Type TXT DOMAIN` and `_dmarc.DOMAIN`.
- Check whether the sender is on a blocklist or caught by an anti-spam policy.
- Allow-list carefully in the email filter, never a whole common domain like gmail.com.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Sender's SPF, DKIM or DMARC failing | The sender fixes their records. |
| Our domain's records missing or wrong | Fix SPF, DKIM and DMARC for our domain. |
| Over-strict policy | Tune the anti-spam policy. |
| Newsletter-style content | Safe sender list. |

## Escalate when

- Our outgoing mail is going to spam for many recipients
- A domain's DMARC policy needs changing

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

> [!question]- Which three DNS-based checks decide whether email is trusted?
> SPF, DKIM and DMARC.

## See also

[[SPF, DKIM & DMARC]] · [[Email delivery problems]] · [[Microsoft Defender for Office 365]] · [[Suspicious email]]

## Field notes

Add your own tips and client quirks here.
