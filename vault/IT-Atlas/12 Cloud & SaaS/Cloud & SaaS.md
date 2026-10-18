---
type: "moc"
level: "All"
tags:
  - "moc"
  - "cloud"
created: "2026-10-18"
updated: "2026-10-18"
---

# Cloud & SaaS

Microsoft 365, public cloud and productivity suites.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Treat each tenant as an environment needing baselines: MFA, conditional access, audit logging, Secure Score review.
> - Govern Copilot and AI tools by fixing oversharing and labels first.
> - Use landing zones, tagging and budgets in Azure/AWS to keep security and cost under control.

## [[Microsoft 365 workloads]]

The services inside Microsoft 365 (mail, files, Teams) and the API used to manage them.

- [[Microsoft 365]]
- [[Exchange Online]]
- [[SharePoint & OneDrive]]
- [[Microsoft Teams]]
- [[Microsoft Graph]]
- [[Microsoft 365 admin center]]

## [[Public cloud]]

Public clouds rent out servers, storage and networking by the hour from huge data centers.

- [[Microsoft Azure]]
- [[Azure Arc]]
- [[Amazon Web Services]]
- [[Google Cloud]]

## [[Productivity suites]]

Office suites for mail, documents and calendars other than Microsoft 365.

- [[Google Workspace]]
- [[Zoom Workplace]]
- [[Slack]]
- [[Dropbox]]
- [[Box]]

## [[AI assistants]]

AI assistants answer questions, write drafts and summarize information from your work data. Admins control what data they can see.

- [[Microsoft 365 Copilot]]
- [[Microsoft Copilot Studio]]
- [[Azure OpenAI Service]]
- [[ChatGPT Enterprise]]
- [[Gemini for Google Workspace]]

## Playbooks for this area

[[Azure VM unreachable]] · [[Email delivery problems]] · [[SaaS backup failing]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "12 Cloud & SaaS"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
