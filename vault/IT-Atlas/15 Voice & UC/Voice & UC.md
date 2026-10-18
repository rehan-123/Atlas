---
type: "moc"
level: "All"
tags:
  - "moc"
  - "voice"
created: "2026-10-18"
updated: "2026-10-18"
---

# Voice & UC

> [!abstract] In plain words
> Business phone systems that run over the network or the internet.

Phone systems and unified communications.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Voice needs QoS end to end and a stable, low-jitter internet link; test before migrating.
> - Plan number porting and emergency calling (E911/location) carefully; they're regulatory, not optional.
> - Keep a fallback (mobile app, call forwarding) for when the site link is down.

## Tools

- [[3CX]]: A business phone system that runs as software on a server or in the cloud.
- [[Microsoft Teams Phone]]: Lets Teams make and receive normal phone calls.
- [[RingCentral]]: A cloud business phone system.
- [[Zoom Phone]]: Zoom's cloud phone system for business numbers and desk phones.
- [[Cisco Webex]]: Cisco's meetings and calling platform.
- [[Microsoft Teams Rooms]]: Meeting room systems that run Teams: a console on the table, cameras and a screen, signed in with a room account.
- [[Yealink]]: A common brand of desk phones and meeting room devices that work with Teams, Zoom and SIP phone systems.

## Playbooks for this area

[[Voice quality problems]]

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "15 Voice & UC"
WHERE type = "tool"
SORT file.name ASC
```
