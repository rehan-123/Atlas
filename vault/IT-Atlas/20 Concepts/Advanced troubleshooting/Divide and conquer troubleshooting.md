---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Divide and conquer troubleshooting

> [!abstract] In one line
> Cutting a big problem in half again and again until the cause is cornered.

> [!tip] Think of it like
> Finding the dead bulb in old Christmas lights by testing half the string at a time.

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **subnet**: A range of IP addresses that form one network segment.
> *More in the [[Glossary]].*

## How it works

- Find a point where it works and a point where it doesn't; test in the middle.
- Network: does it work by IP but not name (DNS)? from the same subnet but not another (routing/firewall)?
- Apps: does it work for another user (profile), another PC (device), the web version (client)?
- Change one thing at a time and write down each result.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- An app fails for one user on every PC, but works for others on the same PC. Where is the problem?
> In that user's account or profile (permissions, settings, licence), not the device.

## See also

[[Troubleshooting method]] · [[OSI model]]
