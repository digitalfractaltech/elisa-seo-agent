# ELISA SEO Intelligence Agent

**ELISA** is a self-hosted, multi-agent SEO operating system for teams that want to turn SEO work into a measurable, repeatable process.

It combines project onboarding, keyword and ranking baselines, sitemap analysis, site-architecture mapping, page audits, internal-link planning, optional live SERP intelligence, CMS draft preparation, persistent project memory, progress tracking, and reporting.

The system is designed to run on the operator’s own machine. It is not a SaaS product and it does not require Ahrefs.

> Built by [Digital Fractal](https://digitalfractal.com/) as an open, adaptable foundation for practical AI-agent systems.

## Current repository status

This repository currently contains:

- OpenClaw skill workspaces and orchestration instructions
- The multi-project Obsidian vault model
- Loop and progress-tracking protocols
- Optional connector/component packages
- Installation and onboarding documentation
- The [ELISA landing page](elisa-seo-agent-landing-page.html)
- The design and implementation blueprint for the self-hosted web application

The production web application described in the blueprint is a separate implementation phase. This repository is the agent capability package, operating model, and reference implementation material—not a hosted service.

## What problem does it solve?

SEO work often becomes a collection of disconnected audits, spreadsheets, prompts, and one-off edits. ELISA gives the project a persistent operating model:

1. Onboard the website and business goals.
2. Establish a keyword, ranking, and traffic baseline.
3. Map the entire sitemap into a page hierarchy.
4. Catalogue keywords already present in pages and posts.
5. Identify internal-link, content, technical, and authority opportunities.
6. Prioritize the highest-impact work in controlled batches.
7. Prepare CMS changes as drafts for approval.
8. Measure results against the baseline and record what happened.

The agent decides what to do next from the active project state instead of relying on undocumented chat history or a shared memory file.

## Core capabilities

### Project onboarding and multi-project memory

- Collects the project URL, sitemap, money keywords, target locations, competitors, goals, approval rules, and available data sources.
- Creates a separate Obsidian-compatible vault for each project.
- Keeps project context separated so one client or website does not contaminate another.
- Uses onboarding checklists to show what is complete, missing, blocked, or waiting for approval.

### Baselines and performance tracking

- Captures explicit Google organic ranking snapshots with DataForSEO when configured.
- Uses Google Search Console for impressions, clicks, CTR, and average position.
- Can use analytics data for traffic and trend context when configured.
- Tracks weekly snapshots, movement, degradation, measurement windows, and expected outcomes.
- Produces on-demand reports explaining what was done, why it was done, the expected goal, and the current result.

### Site architecture and keyword mapping

- Reads the sitemap without fetching every page unnecessarily during manifest creation.
- Counts and classifies pages, posts, service pages, location-oriented pages, hubs, and support content.
- Maps top-level, secondary, and supporting content relationships.
- Catalogues keyword mentions already present in existing content.
- Finds opportunities to link relevant pages toward priority money pages.
- Re-runs the mapping process as new content is added.

### Page audits and optimization

- Runs page-level technical and on-page checklists.
- Reviews titles, headings, content depth, entity coverage, internal links, image alt text, category alignment, and performance signals.
- Supports light refreshes and controlled standard optimization while preserving human-written content.
- Keeps optimization separate from new content writing; content generation can be added later as an extension.
- Records skipped items, blockers, terms not added, changes made, and verification status.

### Internal linking

- Uses sitemap and page evidence instead of random anchor insertion.
- Creates site-wide and priority-page internal-link plans.
- Maps keyword mentions in existing pages and posts to target pages.
- Checks whether a source page already links to the target.
- Prepares contextual links inside main content and verifies the result.

### Optional SERP and AI-search intelligence

- [On-Page.ai](https://on-page.ai/pages/automate-seo/) can be connected when a project wants competitor entity analysis, related-word data, structure benchmarks, and additional SERP intelligence.
- On-Page.ai is optional; the core onboarding, sitemap, ranking, reporting, and project-memory workflow does not depend on it.
- AI-search visibility audits can evaluate how content supports modern search and answer experiences when the selected data sources support that analysis.

### Backlink opportunity research

- Recommends backlink opportunities where the evidence indicates an authority gap.
- Identifies listicle, resource-page, media, and partnership prospects for human review.
- Produces research and outreach preparation rather than uncontrolled bulk emailing.
- Gmail outreach is not part of the core workflow and remains an optional extension.

### Autonomous loops with safety gates

The loop controller runs the operating cycle:

```text
RUN → CHECK → DECIDE → RECORD → RUN AGAIN
```

The loop stops on a real signal:

- completion
- blocker
- approval gate
- budget or token cap
- missing data
- measurement window reached
- need for human judgment

This makes “continue” meaningful without allowing the agent to make unlimited or invisible changes.

### CMS and WordPress draft workflows

- Browser automation or CMS/API connectors can prepare edits.
- Internal links, headings, alt text, and approved on-page changes are saved as drafts, revisions, or previews.
- Publishing, redirects, canonicals, deletions, and other high-impact changes remain approval-gated by default.

## How the system works

```text
Project onboarding
      ↓
Obsidian project vault + checklist
      ↓
Keyword, ranking, and traffic baseline
      ↓
Sitemap and site-architecture map
      ↓
Keyword/page catalogue and opportunity queue
      ↓
Priority batch selection
      ↓
Audits, internal linking, and draft optimizations
      ↓
Human review and CMS draft verification
      ↓
Weekly rank/traffic comparison and reporting
      ↓
Loop controller selects the next evidence-based task
```

## Setup

### Requirements

- macOS, Linux, or another environment capable of running your OpenClaw-compatible agent runtime
- Python 3 for the included helper scripts
- An OpenClaw skill directory or compatible skill loader
- Obsidian if you want to browse project memory visually
- API access only for the providers you choose to connect

No provider is mandatory for every workflow. The selected workflow determines which data source is needed.

### 1. Download or clone the repository

Place the folder somewhere local. For example:

```text
~/Documents/elisa-seo-agent/
```

Do not put API keys, `.env` files, database files, exports, or private client data in the public repository.

### 2. Verify the package before installing

From the project folder:

```bash
test -d openclaw-skills
test -f openclaw-skills/manifest.json
test -d productized-vault-system
python3 -m json.tool openclaw-skills/manifest.json >/dev/null
echo "ELISA package structure looks valid"
```

The manifest currently registers 34 skills, including orchestration, loops, rank tracking, site architecture, keyword mapping, audits, optimization, reporting, and optional extensions.

### 3. Install the global skills without deleting existing skills

Confirm your local paths first. The defaults below are examples:

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

This copies the skill package into the configured skill directory. It does not delete unrelated skills or project vaults. Back up an existing skill folder before replacing it if you are updating an installation.

### 4. Start the agent and onboard a project

Tell the agent where the downloaded folder is and ask it to verify the install paths before copying anything. Then say:

```text
Start project onboarding. Create a new project vault for this website.
Ask me for the project URL, sitemap, money keywords, business goals,
target locations, competitors, approval rules, CMS access, and available
data providers. Show the onboarding checklist and do not start optimization
until the baseline and project profile are recorded.
```

The first project should create a vault similar to:

```text
<PROJECTS_ROOT>/<project-id>/
  00-strategy/
  01-theses/
  02-learnings/
  03-experiments/
  04-competitors/
  05-opportunities/
  06-anomalies/
  07-queue/
  08-tracking/
  09-reports/
  99-daily/
  README.md
```

All durable progress belongs in the active project vault. The system should not depend on `memory.md`, chat history, or skill-local run logs for project state.

## Provider configuration

Provider configuration is local and project-specific. Use only the services you need:

| Provider or connector | Purpose | Required? |
|---|---|---:|
| DataForSEO Google Organic SERP API | Explicit keyword/location/device rank snapshots | Optional, recommended for rank tracking |
| Google Search Console | Impressions, clicks, CTR, average position | Optional, recommended |
| Analytics provider | Traffic and trend context | Optional |
| On-Page.ai MCP | Competitor entities, related words, structure and SERP intelligence | Optional |
| OpenAI or another AI provider | Agent reasoning and task execution | At least one provider |
| WordPress/CMS access | Draft implementation | Optional |

For local development, credentials may be stored in a local ignored configuration file such as `config/local.env`. Never commit it. Never write raw credentials to an Obsidian vault, skill folder, report, prompt, log, or exported artifact. Teams that already use Bitwarden or another secret manager may integrate it optionally.

## Recommended first workflow

After onboarding, the orchestrator should normally proceed in this order:

1. Confirm the project profile and onboarding checklist.
2. Discover money keywords and related/low-hanging-fruit opportunities.
3. Capture the baseline rankings and traffic context.
4. Map the sitemap and classify the site hierarchy.
5. Catalogue keyword mentions and internal-link opportunities.
6. Prioritize the first batch, normally the highest-impact ten keywords/pages.
7. Run page audits and maintain page checklists.
8. Prepare internal-link and on-page changes as drafts.
9. Run verification and save the audit trail.
10. Perform the weekly measurement check-in and choose the next batch.

The user should be able to say “continue,” “run the weekly check-in,” or “prepare a report,” and the orchestrator should read the active vault state before choosing the next specialist skill.

## Optional components

The repository also contains independently installable component folders:

- `component-loop-controller/` — autonomous run/check/decide routing
- `component-sitemap-keyword-linking-auditor/` — sitemap-wide keyword and internal-link mapping
- `component-listicle-backlink-outreach-prospector/` — backlink prospect research
- `component-gmail-outreach-manager/` — optional email workflow extension; not required by the core system

Install components separately when needed. Do not overwrite an existing installation blindly; inspect the component manifest and back up the target skill before updating it.

## Safety and operating boundaries

- The system is self-hosted; there is no central ELISA SaaS account.
- Project vaults are isolated from one another.
- Publishing is approval-gated by default.
- New public content, redirects, canonicals, deletions, GBP changes, and money-page edits require explicit approval unless a project changes those rules.
- The system records blockers instead of inventing missing facts.
- Backlink research is not permission to send spam or make unreviewed claims.
- Optional providers may have their own pricing, limits, terms, and privacy policies.

## Public references and attribution

The SEO workflow catalog was directly inspired in part by [Eric Lancheres](https://x.com/ericlancheres), SEO researcher and founder of [On-Page.ai](https://on-page.ai/), especially the public guide [How To Automate Real SEO Work](https://on-page.ai/pages/automate-seo/). ELISA adapts those ideas into a project-aware, resumable, self-hosted orchestration system rather than reproducing a hosted service.

The agent-oriented operating model was also informed by related AI delivery work, including Digital Fractal’s [AI-powered workforce scheduling and resource-optimization platform case study](https://digitalfractal.com/case-study/ai-powered-workforce-scheduling-resource-optimization-platform-2/).

For implementation and AI-agent consulting, visit [Digital Fractal](https://digitalfractal.com/).

Third-party names and links are provided for attribution and implementation context. This project does not claim affiliation with those providers unless explicitly stated.

## Documentation map

- `OPENCLAW_INSTALL.md` — detailed OpenClaw installation notes
- `productized-vault-system/INSTALL_FROM_DOWNLOADED_FOLDER.md` — downloaded-folder installation flow
- `productized-vault-system/PROJECT_VAULT_STRUCTURE.md` — persistent project-memory structure
- `productized-vault-system/LOOP_PROTOCOL.md` — autonomous loop behavior
- `openclaw-skills/manifest.json` — registered skill inventory
- `elisa-seo-agent-landing-page.html` — public product landing page
- `docs/superpowers/specs/` — self-hosted web-application design specifications, when included
- `docs/superpowers/plans/` — implementation plans, when included

## Contributing

Useful contributions include:

- improving provider adapters without hard-coding credentials
- adding tests for manifest, vault, loop, and reporting behavior
- improving onboarding feedback and error messages
- adding safe, approval-gated CMS integrations
- documenting reproducible local setups
- improving the site-architecture and internal-linking analysis

Before submitting changes, check that no private project data, credentials, local paths, or client-specific assumptions have entered the repository.

## License

Add the project’s chosen open-source license before publishing the repository publicly. Until a license is added, do not assume that the contents may be reused beyond the permissions granted by the repository owner.
