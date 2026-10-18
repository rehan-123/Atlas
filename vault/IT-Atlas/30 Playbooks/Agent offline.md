---
type: "playbook"
level: "Junior"
severity: "P3 (P2 if a server)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Agent offline

> [!abstract] What this alert means
> The RMM agent on a device stopped checking in, so you can't see or manage that device right now.
>
> **Why it matters:** If it's a server, you're blind to it: no monitoring, patching or remote fixes until it's back.

**How urgent:** P3 (P2 if a server). See [[Severity levels]].

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **WAN**: Wide area network: links between sites, or to the internet.
> **threshold**: The value that triggers an alert.
> **ping**: A quick test that sends a small message to a device and waits for a reply.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## You'll see this when

- RMM shows the device offline or not checked in past the threshold

## First 5 minutes

1. Check whether it is a server or workstation, and whether other devices at the same site are also offline (site outage vs one device)
2. Ping it and check another signal: hypervisor console, other agents (EDR, backup), or the user
3. Check maintenance windows and recent patch reboots

## Find the cause

- Device up but agent offline: the agent service has stopped, crashed or cannot reach the RMM (proxy, DNS, TLS inspection, firewall)
- Whole site offline: treat it as a WAN or power incident, not an agent issue
- Device actually down: move to Server unreachable

## Where to look, by tool

| Tool | Agent / service | Logs |
|---|---|---|
| [[Kaseya VSA]] | Kaseya Agent (AgentMon.exe) | Agent Logs and Procedure History in the VSA console |
| [[Datto RMM]] | CagService | C:\ProgramData\CentraStage (agent data and logs); Job results and audit trail in the web portal |
| [[ConnectWise Automate]] | LTService, LTSvcMon | C:\Windows\LTSvc\LTErrors.txt |
| [[ConnectWise RMM]] | ITSPlatform (legacy Continuum agents use SAAZ* services) |  |
| [[N-able N-central]] | Windows Agent, Windows Agent Maintenance Service | C:\Program Files (x86)\N-able Technologies\Windows Agent\log |
| [[N-able N-sight RMM]] | Advanced Monitoring Agent | C:\Program Files (x86)\Advanced Monitoring Agent (agent folder and logs) |
| [[NinjaOne]] | NinjaRMMAgent | C:\ProgramData\NinjaRMMAgent\logs |
| [[Atera]] | AteraAgent | C:\Program Files\ATERA Networks\AteraAgent (agent folder) |
| [[Tactical RMM]] | tacticalrmm, Mesh Agent |  |

## Fix it

- Start or restart the agent service through another tool (EDR live response, remote PowerShell, ScreenConnect backstage)
- Reinstall the agent if the service won't start or its files are damaged
- Fix DNS or firewall rules if the agent cannot reach its server

## Ask for help (escalate) when

- A server stays unreachable after 15 minutes
- Several devices or a whole site are offline
- The agent was removed unexpectedly (possible tampering)

## Write it up

Copy this into the ticket and fill it in:

```
Device: 
Offline since: 
Other signals (ping / hypervisor / EDR): 
Cause: 
Action taken: 
Status:
```

## See also

[[RMM]] · [[Agent heartbeat]] · [[Server unreachable]] · [[Firewall WAN down]]
