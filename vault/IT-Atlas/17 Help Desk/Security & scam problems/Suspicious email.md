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

# Suspicious email

> [!abstract] What's going on
> An email feels off: urgent, unexpected, asks for money, passwords or to open a file.

> [!tip] Think of it like
> A letter from 'your bank' in handwriting you don't recognise: check it through the bank's real number, not the one in the letter.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Security & scam problems]]

> [!info]+ Words on this page
> **SPF**: A DNS record listing which servers may send email for a domain.
> **DKIM**: An email signature that proves a message really came from your domain and wasn't changed.
> **DMARC**: An email rule that tells receivers what to do with mail that fails SPF or DKIM checks.
> **phishing**: Fake messages designed to trick people into clicking or giving away passwords.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Don't click links, open attachments or reply.
2. Check the real sender address (not just the name) and hover over links to see where they go.
3. Use the Report button in Outlook, or forward it to IT as an attachment if asked.
4. If it asks to change bank details or pay urgently, call the person on a number you already know.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Read the headers for SPF, DKIM and DMARC results and the real sending server.
- Check whether others received it and remove it from all mailboxes.
- Block the sender or domain in the email filter.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Phishing | Report, remove, block. |
| Real but unusual email | Confirm by phone, then release. |
| Lookalike domain of a partner | Warn staff and block the domain. |

## Escalate when

- A payment or bank-detail change was already made
- The email came from a real partner's hacked account

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

> [!question]- What's the safest way to confirm an email asking you to change a supplier's bank details?
> Call the supplier on a phone number you already have, not one in the email.

## See also

[[Spotting phishing]] · [[Clicked a phishing link]] · [[SPF, DKIM & DMARC]] · [[Email went to junk]]

## Field notes

Add your own tips and client quirks here.
