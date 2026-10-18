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

# Screen or second monitor not working

> [!abstract] What's going on
> A monitor shows 'No signal', flickers, or Windows doesn't see the second screen.

> [!tip] Think of it like
> A TV on the wrong HDMI input: the box is working, the TV just isn't looking at it.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check both ends of the cable and that the monitor is on.
2. Press Windows+P and choose Extend or Duplicate.
3. Unplug the dock's power for 30 seconds and plug it back in.
4. Use the monitor's buttons to pick the right input.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Settings > System > Display > Detect.
- Press Windows+Ctrl+Shift+B to restart the graphics driver.
- Update the graphics driver and the dock firmware from the manufacturer.
- Try a different cable or port to isolate the dock, cable or monitor.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Wrong input or projection mode | Change input; Windows+P. |
| Dock needs a reset or firmware update | Power-cycle and update it. |
| Bad cable | Swap the cable. |
| Graphics driver | Update or reinstall it. |

## Escalate when

- The monitor stays black on a known-good PC and cable (faulty monitor)
- Many docks of the same model fail after an update

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

> [!question]- What keyboard shortcut restarts the Windows graphics driver?
> Windows+Ctrl+Shift+B.

## See also

[[Drivers]] · [[Keyboard or mouse not working]]

## Field notes

Add your own tips and client quirks here.
