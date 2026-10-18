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

# Outlook search not working

> [!abstract] What's going on
> Searching in Outlook finds nothing, or misses recent emails.

> [!tip] Think of it like
> A library index card box that's out of date: the books are there, the index isn't.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Restart Outlook.
2. Try the same search in Outlook on the web.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Classic Outlook: File > Options > Search > Indexing Options; check Outlook is included and rebuild the index if needed.
- Check the Windows Search service is running.
- Check how much mail is kept offline (cached mode slider); older mail is searched on the server.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Index incomplete | Rebuild the index. |
| Windows Search stopped | Start the service. |
| Old mail not cached | Search the server or increase offline period. |

## Escalate when

- Search broken for many users

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

> [!question]- Search works in Outlook on the web but not in the desktop app. Where's the problem?
> The local search index on the PC.

## See also

[[Outlook won't open]] · [[Exchange Online]]

## Field notes

Add your own tips and client quirks here.
