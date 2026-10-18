---
type: "guide"
level: "Junior"
area: "[[Printer & scanner problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Printer offline

> [!abstract] What's going on
> The printer shows 'Offline' or nothing happens when you print.

> [!tip] Think of it like
> Calling someone whose phone is switched off: check the printer is on, connected, and that the PC has its current number (IP address).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Printer & scanner problems]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **ping**: A quick test that sends a small message to a device and waits for a reply.
> **spooler**: The Windows service that queues print jobs before they go to the printer.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check the printer is on, has no error on its screen and has paper and toner.
2. Turn the printer off and on.
3. On the PC, open Settings > Bluetooth & devices > Printers & scanners, choose the printer and open the print queue.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Ping the printer's IP address and open its web page.
- Check whether the printer's IP changed (it should have a DHCP reservation).
- Restart the print spooler: `Restart-Service Spooler`.
- If it's shared from a print server, check the server and its queue (`Get-Printer -ComputerName SERVER`).
- Remove and re-add the printer, with the latest driver.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Printer off, jammed or out of paper | Fix on the printer. |
| Printer's IP address changed | Set a DHCP reservation and update the port. |
| Stuck spooler | Restart the spooler. |
| Print server down | Escalate to the NOC. |

## Escalate when

- Nobody can print to any printer (print server issue)
- Hardware fault on the printer: log a call with the printer supplier

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

> [!question]- Why should office printers have a DHCP reservation or fixed IP?
> So their address never changes; otherwise PCs keep sending jobs to the old address and the printer shows offline.

## See also

[[Print Server]] · [[DHCP]] · [[IP addresses]] · [[Print job stuck]]

## Field notes

Add your own tips and client quirks here.
