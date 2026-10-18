---
type: "guide"
level: "Junior"
area: "[[Mac problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Mac app won't open

> [!abstract] What's going on
> macOS says an app 'can't be opened' or is from an unidentified developer.

> [!tip] Think of it like
> A doorman who only lets in guests with a checked ID: Gatekeeper blocks apps that Apple can't verify.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Mac problems]]

> [!info]+ Words on this page
> **Company Portal**: Intune's app store where users install approved work apps.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **malware**: Any harmful software: viruses, ransomware, spyware and the like.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Don't bypass warnings for apps you weren't told to install.
2. Install company apps from Self Service (Jamf) or Company Portal (Intune).

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- If the app is approved: System Settings > Privacy & Security > Open Anyway.
- Check whether the MDM blocks it, or whether it needs approval for system extensions or Full Disk Access.
- Reinstall the latest version (older versions may not support the current macOS).
- Check the Console app for crash reports.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Unsigned or unknown app | Use the approved source. |
| Missing privacy or extension approval | Approve via MDM profile. |
| Old version incompatible with macOS | Update the app. |

## Escalate when

- The app is not approved by the company
- Security warning says the app is malware

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

> [!question]- Where do you allow an approved app that macOS blocked?
> System Settings > Privacy & Security > Open Anyway (or approve it through the MDM).

## See also

[[macOS]] · [[Jamf Pro]] · [[Install software request]]

## Field notes

Add your own tips and client quirks here.
