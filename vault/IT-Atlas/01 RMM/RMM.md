---
type: "moc"
level: "All"
tags:
  - "moc"
  - "rmm"
created: "2026-10-18"
updated: "2026-10-18"
---

# RMM

> [!abstract] In plain words
> An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

Remote monitoring and management: the agent on every endpoint. Monitoring, scripting, patching, remote access and alerting from one console. The RMM agent is the NOC's eyes; when it goes offline you are blind.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Standardize agent deployment and naming per client; drift in policies is the main source of missed alerts.
> - Treat the RMM as tier 0: it can run code as SYSTEM on every endpoint. Enforce MFA, IP restrictions and least-privilege technician roles.
> - Review monitoring sets quarterly: remove noise, add checks for every incident that wasn't alerted.
> - Keep scripts in Git with review; an untested script pushed to 2,000 endpoints is an outage.

## Tools

- [[Kaseya VSA]]: Kaseya's RMM. Every managed computer runs the VSA agent, and from the console you can run scripts (called agent procedures), patch, monitor and remote in.
- [[Datto RMM]]: A cloud RMM now owned by Kaseya. You'll use it to see device health, run ready-made scripts (components) and remote in with Web Remote.
- [[ConnectWise Automate]]: ConnectWise's older, very scriptable RMM, formerly called LabTech. Powerful, but its console takes time to learn.
- [[ConnectWise RMM]]: ConnectWise's newer cloud RMM, built from the Continuum product.
- [[N-able N-central]]: N-able's bigger RMM for MSPs with many clients. A 'probe' at each site can also check devices that have no agent.
- [[N-able N-sight RMM]]: N-able's simpler RMM for small businesses. It runs regular health checks on each device and flags failures.
- [[NinjaOne]]: A popular, easy-to-use cloud RMM known for fast patching, with backup and documentation built in.
- [[Atera]]: An all-in-one RMM and ticketing tool for small MSPs, charged per technician rather than per device.
- [[Syncro]]: Another all-in-one RMM plus ticketing and billing tool for small MSPs.
- [[SuperOps]]: A newer tool that combines RMM and ticketing in one product.
- [[Pulseway]]: An RMM best known for its phone app: you can check and fix machines from your mobile.
- [[Level]]: A newer, lightweight cloud RMM focused on speed and simple remote access.
- [[Tactical RMM]]: A free, open-source RMM you host yourself. Popular for labs and practice.
- [[Barracuda RMM]]: Barracuda's RMM, formerly called Managed Workplace.
- [[ManageEngine Endpoint Central]]: ManageEngine's tool for patching, installing software and managing Windows, Mac and Linux machines.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "01 RMM"
WHERE type = "tool"
SORT file.name ASC
```
