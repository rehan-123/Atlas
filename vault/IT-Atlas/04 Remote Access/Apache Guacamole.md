---
type: "tool"
level: "Junior"
category: "[[Remote Access]]"
vendor: "[[Apache Software Foundation]]"
deployment: "Self-hosted (open source)"
status: "current"
aliases: []
tags:
  - "tool"
  - "remote-access"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Apache Guacamole

> [!abstract] In plain words
> Lets you open RDP or SSH sessions in a web browser, with nothing installed on your computer.
>
> **What kind of tool is this?** Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

**Made by:** [[Apache Software Foundation]] · **Runs:** Self-hosted (open source) · **Category:** [[Remote Access]]

> [!info]+ Words on this page
> **RDP**: Remote Desktop Protocol: Windows' built-in remote desktop, on port 3389.
> **SSH**: Secure Shell: encrypted command-line login, mostly for Linux and network devices (port 22).
> **TCP**: A connection-based network protocol that confirms delivery.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> *More in the [[Glossary]].*

## In more detail

Clientless remote desktop gateway: RDP, VNC and SSH in a browser through HTML5.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 4822/TCP guacd (internal)
- 8080/TCP Tomcat web app (behind a reverse proxy)

## See also

[[RDP]] · [[RD Gateway]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
