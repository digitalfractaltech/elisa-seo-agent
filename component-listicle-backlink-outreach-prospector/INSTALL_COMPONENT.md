# Install Component: listicle-backlink-outreach-prospector

Use this when Emily is already installed and you only want to add the backlink/listicle outreach skill.

## Install

Verify the component contains:

```text
openclaw-skills/listicle-backlink-outreach-prospector/SKILL.md
component-manifest.json
```

Then copy only the skill folder into your existing skills path:

```bash
mkdir -p ~/.openclaw/skills
cp -R openclaw-skills/listicle-backlink-outreach-prospector ~/.openclaw/skills/
```

Do not overwrite project vaults.

## Optional orchestrator wiring

Add this after `backlink-opportunity-recommender` routing:

```text
Invoke `listicle-backlink-outreach-prospector` when the opportunity type is listicles, resource pages, roundups, or editorial outreach.
```

You can also call it directly:

```text
Use listicle-backlink-outreach-prospector for {{TARGET_URL}} and {{TARGET_KEYWORD}}. Find qualified listicle/resource-page backlink opportunities, score them, and create an approval-gated outreach queue. Do not send outreach.
```
