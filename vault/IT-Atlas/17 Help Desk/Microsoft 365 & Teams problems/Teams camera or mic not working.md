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

# Teams camera or mic not working

> [!abstract] What's going on
> Your camera is black or others can't hear you in Teams.

> [!tip] Think of it like
> A stage with the right microphone unplugged: everything works, just not the device Teams is listening to.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Microsoft 365 & Teams problems]]

> [!info]+ Words on this page
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. In Teams: Settings > Devices; pick the right camera, mic and speaker and make a test call.
2. Close other apps that might be using the camera (Zoom, Camera app).
3. Check the laptop's physical camera shutter or mute key.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Windows Settings > Privacy & security > Camera and Microphone: allow access for apps and Teams.
- Update the camera or audio driver in Device Manager.
- Clear the new Teams cache: quit Teams, delete the contents of `%LocalAppData%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams`, restart Teams.
- Test the camera in the Windows Camera app to separate Teams from hardware.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Wrong device in Teams | Pick the right one. |
| Privacy settings block access | Allow it. |
| Another app holds the camera | Close it. |
| Driver or cache issue | Update the driver; clear the cache. |

## Escalate when

- Camera fails in every app (hardware)
- A company-wide Teams issue

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

> [!question]- Camera works in the Windows Camera app but not in Teams. What's ruled out?
> The hardware and driver. Look at Teams' device settings, app permissions and the Teams cache.

## See also

[[Microsoft Teams]] · [[No sound or microphone]] · [[Teams won't sign in or keeps loading]]

## Field notes

Add your own tips and client quirks here.
