# Install Component: gmail-outreach-manager

Use this when Emily is already installed and you only want to add approved Gmail outreach sending/response tracking.

## Install

Verify the component contains:

```text
openclaw-skills/gmail-outreach-manager/SKILL.md
component-manifest.json
```

Copy only the skill folder into your existing skills path:

```bash
mkdir -p ~/.openclaw/skills
cp -R openclaw-skills/gmail-outreach-manager ~/.openclaw/skills/
```

If `~/.openclaw/skills/manifest.json` exists, back it up and add `gmail-outreach-manager` to the `skills` array if missing, then update `skill_count`.

Do not overwrite project vaults. Do not store Gmail secrets in Obsidian.
```
