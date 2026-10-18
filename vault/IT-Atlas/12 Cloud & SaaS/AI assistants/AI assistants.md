---
type: "moc"
level: "All"
tags:
  - "moc"
  - "cloud"
created: "2026-10-18"
updated: "2026-10-18"
---

# AI assistants

> [!abstract] In plain words
> AI assistants answer questions, write drafts and summarize information from your work data. Admins control what data they can see.

Part of [[Cloud & SaaS]].

- [[Microsoft 365 Copilot]]: Microsoft's AI assistant inside Word, Excel, Outlook, Teams and other apps. It can only see what the user already has access to.
- [[Microsoft Copilot Studio]]: A tool for building your own AI agents and chatbots that can answer from your documents and run actions.
- [[Azure OpenAI Service]]: OpenAI's models (like GPT) hosted inside Azure, so companies can build AI apps with Azure security and data controls.
- [[ChatGPT Enterprise]]: The business version of ChatGPT, with admin controls, single sign-on and a promise not to train on company data.
- [[Gemini for Google Workspace]]: Google's AI assistant inside Gmail, Docs, Sheets and Meet.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "12 Cloud & SaaS/AI assistants"
WHERE type = "tool"
SORT file.name ASC
```
