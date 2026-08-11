# Project Switching — One Obsidian Vault Per Project

Emily supports multiple SEO projects in one installation.

## Global vs project data

Global system files live in:

```text
{{SYSTEM_ROOT}}/
```

Each project gets its own Obsidian vault:

```text
{{OBSIDIAN_PROJECTS_ROOT}}/<project_id>/
```

Do not store persistent project state in chat memory, `memory.md`, skill-local files, or another project's vault.

## Active project

The active project is defined by a system registry file such as:

```text
{{SYSTEM_ROOT}}/active-project.md
```

Required content:

```yaml
---
active_project_id: example-client
project_vault_root: /path/to/obsidian/projects/example-client
updated: 2026-05-23
---
```

Before any SEO reasoning, read:

```text
{{PROJECT_VAULT_ROOT}}/00-strategy/project-profile.md
```

## Switching projects

1. Confirm the requested `project_id` exists in the registry.
2. Resolve its `project_vault_root`.
3. Update `active-project.md`.
4. Drop working context from the previous project.
5. Reload the new project's profile, approval rules, tool map, queue, and latest report.
6. Continue only with the active project's context.

## If no active project exists

Invoke `project-orchestrator` and create/register a new project vault.
