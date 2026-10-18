---
type: "guide"
level: "Junior"
area: "[[Microsoft 365 & Teams problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Teams won't sign in or keeps loading

> [!abstract] What's going on
> Teams is stuck on a loading screen, shows an error, or is very slow.

> [!tip] Think of it like
> A browser with a cluttered memory: clearing its cache gives it a fresh start.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Microsoft 365 & Teams problems]]

> [!info]+ Words on this page
> **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **token**: A temporary digital key used to prove you're allowed in.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Quit Teams fully (right-click the taskbar icon > Quit) and reopen.
2. Try Teams on the web (teams.microsoft.com).
3. Restart the PC.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Clear the Teams cache (new Teams folder: `%LocalAppData%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams`).
- Reset the app: Settings > Apps > Microsoft Teams > Advanced options > Reset.
- Check the user is licensed for Teams and not blocked by Conditional Access (sign-in logs).
- Check the Microsoft 365 service health page for Teams incidents.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Damaged cache | Clear it or reset the app. |
| Sign-in token problem | Sign out and in; clear credentials. |
| Microsoft outage | Check service health and tell users. |
| Licence missing | Assign the license. |

## Escalate when

- Service health shows a Microsoft incident (inform users, nothing to fix locally)
- Many users affected

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

> [!question]- Teams works on the web but not in the app. Where's the problem?
> On the PC: the Teams app, its cache or the stored sign-in, not the account.

## See also

[[Microsoft Teams]] · [[Cache and cookies]] · [[Can't sign in to Microsoft 365]]

## Field notes

Add your own tips and client quirks here.
