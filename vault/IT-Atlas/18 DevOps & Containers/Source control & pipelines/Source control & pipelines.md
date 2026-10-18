---
type: "moc"
level: "All"
tags:
  - "moc"
  - "devops"
created: "2026-10-18"
updated: "2026-10-18"
---

# Source control & pipelines

> [!abstract] In plain words
> Source control keeps every version of code and scripts. CI/CD pipelines test and deploy changes automatically when someone pushes.

Part of [[DevOps & Containers]].

- [[GitHub]]: The most popular place to store code and scripts in Git repositories, with pull requests for reviewing changes.
- [[GitHub Actions]]: GitHub's built-in automation: workflows run on every push or on a schedule to test, build and deploy.
- [[Azure DevOps]]: Microsoft's suite for code (Repos), work items (Boards) and pipelines (Pipelines).
- [[GitLab]]: An all-in-one platform for Git repositories, CI/CD and issue tracking, available as cloud or self-hosted.
- [[Jenkins]]: An older, very flexible open-source automation server for building and deploying software.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "18 DevOps & Containers/Source control & pipelines"
WHERE type = "tool"
SORT file.name ASC
```
