---
type: "guide"
level: "Junior"
area: "[[Windows PC problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# No sound or microphone

> [!abstract] What's going on
> You can't hear anything, or others can't hear you on calls.

> [!tip] Think of it like
> A radio tuned to the wrong station: the music is playing, just not where you're listening.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check the volume isn't muted (speaker icon on the taskbar) and the headset isn't muted by its own button.
2. Click the speaker icon and choose the right output device (headset, speakers or monitor).
3. Unplug the headset and plug it back in; try another USB port.
4. In the meeting app, check its own device settings.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Settings > System > Sound: check the input and output devices and the input level.
- Settings > Privacy & security > Microphone: make sure microphone access is on for apps.
- Update or reinstall the audio driver in Device Manager.
- Test with a different headset to rule out hardware.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Wrong device selected | Pick the right device in Windows and in the app. |
| Microphone blocked by privacy settings | Allow microphone access. |
| Driver problem after an update | Reinstall or roll back the audio driver. |
| Faulty headset or port | Swap the headset or port. |

## Escalate when

- Hardware faulty and still under warranty
- Many users lose audio after the same update

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

> [!question]- Teams can't hear the user but other apps can. Where do you look first?
> Teams' own device settings (it may be using a different microphone), then Windows microphone privacy settings.

## See also

[[Teams camera or mic not working]] · [[Drivers]]

## Field notes

Add your own tips and client quirks here.
