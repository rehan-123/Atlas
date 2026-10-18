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

# Suspicious USB drive

> [!abstract] What's going on
> Someone found an unknown USB stick or received one unexpectedly.

> [!tip] Think of it like
> A wrapped parcel on your doorstep that you didn't order: don't open it, report it.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Security & scam problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Don't plug it in, not even 'just to see whose it is'.
2. Hand it to IT.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Treat it as potentially malicious; analyse only on an isolated machine, if at all.
- Check whether USB storage is controlled by policy (Intune, Defender device control).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Curiosity | Awareness training; device control policies. |

## Escalate when

- It was plugged in already

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

> [!question]- Why are dropped USB sticks used in attacks?
> Curious people plug them in, which can run malware or capture keystrokes.

## See also

[[Spotting phishing]] · [[EDR threat detected]]

## Field notes

Add your own tips and client quirks here.
