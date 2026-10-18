---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Web servers & proxies]]"
vendor: "[[Apache Software Foundation]]"
deployment:
status: "current"
agent_service: "apache2 / httpd"
aliases:
  - "Apache"
  - "httpd"
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Apache HTTP Server

> [!abstract] In plain words
> One of the oldest and most common web servers, especially on Linux.
>
> **What kind of tool is this?** Web servers answer browser requests; reverse proxies sit in front of apps to add HTTPS, routing and caching.

**Made by:** [[Apache Software Foundation]] · **Category:** [[DevOps & Containers]] › [[Web servers & proxies]]

> [!info]+ Words on this page
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **HTTPS**: Encrypted HTTP (port 443).
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Modular web server (httpd/apache2) with virtual hosts, .htaccess and mod_ssl; common for PHP sites.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`apache2 / httpd`

## Where to find its logs

- `/var/log/apache2/error.log (Debian/Ubuntu)`
- `/var/log/httpd/error_log (RHEL)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
apachectl configtest
systemctl reload apache2
apachectl -S
```

## See also

[[Nginx]] · [[IIS]] · [[Website down]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
