---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Web servers & proxies]]"
vendor: "[[F5]]"
deployment: "Linux, Windows, containers"
status: "current"
agent_service: "nginx"
aliases: []
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Nginx

> [!abstract] In plain words
> A fast web server and reverse proxy that sits in front of many websites and apps.
>
> **What kind of tool is this?** Web servers answer browser requests; reverse proxies sit in front of apps to add HTTPS, routing and caching.

**Made by:** [[F5]] · **Runs:** Linux, Windows, containers · **Category:** [[DevOps & Containers]] › [[Web servers & proxies]]

> [!info]+ Words on this page
> **HTTPS**: Encrypted HTTP (port 443).
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

High-performance web server, reverse proxy and load balancer; configuration in /etc/nginx; often terminates TLS in front of app servers.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`nginx`

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| 502 Bad Gateway | The app behind Nginx is down or the upstream address is wrong; check the error log |
| Config change broke the site | nginx -t tests the config before you reload |

## Where to find its logs

- `/var/log/nginx/error.log`
- `/var/log/nginx/access.log`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
nginx -t
systemctl reload nginx
tail -f /var/log/nginx/error.log
```

## See also

[[Apache HTTP Server]] · [[SSL & TLS]] · [[Website down]] · [[HAProxy]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
