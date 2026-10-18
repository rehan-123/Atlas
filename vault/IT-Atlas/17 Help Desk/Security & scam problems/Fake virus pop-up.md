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

# Fake virus pop-up

> [!abstract] What's going on
> A browser page shouts that your PC is infected and tells you to call a number.

> [!tip] Think of it like
> A stranger in a hi-vis vest saying your house is on fire and you must give him your keys. Real IT never asks you to call a number from a pop-up.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Security & scam problems]]

> [!info]+ Words on this page
> **Task Manager**: Windows tool (Ctrl+Shift+Esc) that shows running apps and what's using CPU, memory and disk.
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Don't call the number and don't let anyone connect to your PC.
2. Close the browser. If it won't close, open Task Manager (Ctrl+Shift+Esc) and end the browser task.
3. Reopen the browser and don't restore the last tabs.
4. If you already called them or let them connect, tell IT straight away.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- If the user allowed remote access: disconnect the network, remove the remote tool, scan with the EDR, reset passwords from another device.
- Check the browser for malicious extensions and notification permissions.
- Check whether payment details were given (the user should call their bank).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Scam web page only | Close the browser; clear site notifications. |
| Malicious extension | Remove it. |
| Scammer got remote access | Treat as a security incident. |

## Escalate when

- The user gave remote access or payment details

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

> [!question]- A scam pop-up won't close. What's the safe way to get rid of it?
> End the browser in Task Manager, then reopen it without restoring tabs.

## See also

[[Spotting phishing]] · [[Browser acting up]] · [[EDR threat detected]]

## Field notes

Add your own tips and client quirks here.
