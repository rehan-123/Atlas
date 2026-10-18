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

# Crash dump analysis

> [!abstract] In one line
> Reading a memory dump after a blue screen or app crash to find the driver or module responsible.

> [!tip] Think of it like
> A flight recorder: after a crash, it tells you what the plane was doing in the last seconds.

> [!info]+ Words on this page
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> *More in the [[Glossary]].*

## How it works

- Kernel dumps live in `C:\Windows\MEMORY.DMP` and `C:\Windows\Minidump`; app dumps via WER or ProcDump.
- Open in WinDbg, set symbols (`.symfix`, `.reload`), then run `!analyze -v`.
- Look at **MODULE_NAME**, **IMAGE_NAME** and the stack: a third-party driver is the usual cause.
- `lmvm DRIVER` shows the driver's version and date to compare with the vendor's latest.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which WinDbg command gives the automatic analysis of a crash?
> !analyze -v

## See also

[[Blue screen (BSOD)]] · [[Drivers]] · [[Sysinternals Suite]]
