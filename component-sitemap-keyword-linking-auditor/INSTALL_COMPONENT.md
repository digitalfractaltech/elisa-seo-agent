# Install Component: sitemap-keyword-linking-auditor

This component is for systems where Emily is already installed and you only want to add the new skill.

## What it installs

```text
openclaw-skills/sitemap-keyword-linking-auditor/
```

It does not overwrite existing project Obsidian vaults.

## Safe install flow

1. Download/unzip this component somewhere.
2. Verify the folder contains:

```text
openclaw-skills/sitemap-keyword-linking-auditor/SKILL.md
component-manifest.json
```

3. Confirm the skills install path, usually:

```text
~/.openclaw/skills
```

4. Copy the skill folder:

```bash
mkdir -p ~/.openclaw/skills
cp -R openclaw-skills/sitemap-keyword-linking-auditor ~/.openclaw/skills/
```

5. Verify:

```text
~/.openclaw/skills/sitemap-keyword-linking-auditor/SKILL.md
```

## Optional orchestrator wiring

If your installed `project-orchestrator` does not already mention this skill, add it to the operating loop after `site-architecture-mapper` and before `page-checklist-manager`:

```text
Invoke `sitemap-keyword-linking-auditor` to catalogue existing keyword mentions and create an internal linking graph from actual page/post content.
```

If you do not patch the orchestrator, you can still call the skill directly on demand:

```text
Use sitemap-keyword-linking-auditor for this project. Audit the sitemap, catalogue approved keyword mentions, and create an internal linking opportunity map before any internal link implementation.
```
