# Install ELISA SEO Skills into OpenClaw

This package is project-neutral. Client names, websites, keywords, goals, credentials, approval rules, and provider settings belong in each project’s separate Obsidian vault or local configuration.

For the complete public overview, see the root [`README.md`](README.md). This file focuses on installing the OpenClaw skill package from a downloaded folder.

## Package contents

- `openclaw-skills/` — the 34 registered global skills
- `productized-vault-system/` — project-vault templates and loop protocols
- `component-*/` — optional installable extensions
- `docs/` — self-hosted web-application design and implementation plans
- `elisa-seo-agent-landing-page.html` — public landing page

## Recommended runtime layout

Use machine-specific paths. These are examples only:

```text
<HOME>/.openclaw/skills/                 # global skills shared by projects
<HOME>/.openclaw/elisa-system/           # global system instructions
<HOME>/Documents/ELISAProjects/          # one Obsidian vault per project
<HOME>/Documents/ELISAProjects/<id>/
```

Before installing, confirm the downloaded package folder and these target paths with the operator. Never assume a path from another machine.

## Install from a downloaded folder

From the downloaded repository folder:

```bash
export SKILLS_ROOT="$HOME/.openclaw/skills"
export SYSTEM_ROOT="$HOME/.openclaw/elisa-system"
export PROJECTS_ROOT="$HOME/Documents/ELISAProjects"

mkdir -p "$SKILLS_ROOT" "$SYSTEM_ROOT" "$PROJECTS_ROOT"
cp -R openclaw-skills/. "$SKILLS_ROOT/"
cp productized-vault-system/LOOP_PROTOCOL.md "$SYSTEM_ROOT/LOOP_PROTOCOL.md"
cp openclaw-skills/EMILY_PRIMARY_DIRECTIVE.md "$SYSTEM_ROOT/ELISA_PRIMARY_DIRECTIVE.md"
cp openclaw-skills/TOOL_SETUP_CHECKLIST.md "$SYSTEM_ROOT/TOOL_SETUP_CHECKLIST.md"
cp productized-vault-system/PROJECT_SWITCHING.md "$SYSTEM_ROOT/PROJECT_SWITCHING.md"
```

`EMILY_PRIMARY_DIRECTIVE.md` is retained as a legacy-compatible source filename from the original package; the installed system file is named `ELISA_PRIMARY_DIRECTIVE.md`.

Do not delete existing skills or project vaults. Back up an existing skill folder before replacing it during an update.

## Verify the installation

```bash
test -f "$SKILLS_ROOT/manifest.json"
test -f "$SKILLS_ROOT/project-orchestrator/SKILL.md"
test -f "$SKILLS_ROOT/site-architecture-mapper/SKILL.md"
test -f "$SKILLS_ROOT/sitemap-keyword-linking-auditor/SKILL.md"
test -f "$SKILLS_ROOT/dataforseo-rank-tracker-adapter/SKILL.md"
test -f "$SYSTEM_ROOT/ELISA_PRIMARY_DIRECTIVE.md"
test -f "$SYSTEM_ROOT/PROJECT_SWITCHING.md"
echo "ELISA installation checks passed"
```

## Start onboarding

After installation, ask the agent:

```text
Start project onboarding. Create a new project vault for this website.
Ask me for the project URL, sitemap, money keywords, business goals,
target locations, competitors, approval rules, CMS access, and available
data providers. Show the onboarding checklist and do not start optimization
until the baseline and project profile are recorded.
```

The orchestrator should create the project vault before using project-specific SEO knowledge. Durable state belongs in that vault, not in `memory.md`, chat history, or skill-local run logs.

## Provider configuration

Configure only the services required by the selected workflow:

- At least one AI provider for agent reasoning
- DataForSEO for explicit Google organic rank snapshots, when enabled
- Google Search Console for impressions, clicks, CTR, and average position, when enabled
- Analytics for traffic context, when enabled
- On-Page.ai MCP for optional competitor entity and SERP intelligence
- CMS/API or browser access for draft preparation, when enabled

Credentials may be stored in local ignored configuration such as `config/local.env`. Never store raw credentials in skills, vaults, reports, logs, prompts, or exports. Bitwarden or another secret manager may be added optionally.

## First workflow sequence

1. `project-orchestrator` — onboard the project and create its vault
2. `keyword-opportunity-miner` — discover related and low-hanging-fruit keywords
3. `baseline-rank-position-tracker` — capture the initial ranking baseline
4. `keyword-batch-prioritizer` — select the first high-impact batch
5. `site-architecture-mapper` — map sitemap hierarchy and page types
6. `sitemap-keyword-linking-auditor` — catalogue keyword mentions and link opportunities
7. `page-checklist-manager` — create page-level audit checklists
8. `performance-tracker-reporter` — record results and produce reports
9. Optimization and CMS-draft skills — only after project approval rules permit them

The `loop-controller` can run these in evidence-based cycles and stop on completion, blockers, approval gates, budget caps, or measurement windows.

## Optional components

Install these separately when needed:

- `component-loop-controller/`
- `component-sitemap-keyword-linking-auditor/`
- `component-listicle-backlink-outreach-prospector/`
- `component-gmail-outreach-manager/` — optional extension, not required by the core workflow

Local SEO/GBP workflows and Gmail outreach are optional extensions, not required for the core self-hosted SEO system.
