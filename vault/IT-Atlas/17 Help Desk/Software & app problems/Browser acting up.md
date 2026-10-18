---
type: "guide"
level: "Junior"
area: "[[Software & app problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Browser acting up

> [!abstract] What's going on
> Pages look broken, sign-ins loop, pop-ups appear or the browser is slow.

> [!tip] Think of it like
> A cluttered handbag: clear out old receipts (cache) and dodgy items (extensions) and it works again.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Software & app problems]]

> [!info]+ Words on this page
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **cookie**: Small note a website stores in your browser, for example to remember that you're signed in.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Try a private window; if it works, clear cache and cookies.
2. Update the browser and restart it.
3. Remove extensions you don't recognise.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check browser policies (Intune or Group Policy) for blocked sites or extensions.
- Reset the browser profile (Edge: Settings > Reset settings).
- Check proxy and web filter logs if certain sites fail.
- Check notification permissions for spammy sites.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Old cache or cookies | Clear them. |
| Bad extension | Remove it. |
| Web filter blocking parts of a site | Allow the needed domains. |

## Escalate when

- Malicious extension found on many PCs

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

> [!question]- A site works in a private window but not normally. What's the likely cause?
> Cached data, cookies or an extension in the normal profile.

## See also

[[Cache and cookies]] · [[Website won't load]] · [[Fake virus pop-up]]

## Field notes

Add your own tips and client quirks here.
