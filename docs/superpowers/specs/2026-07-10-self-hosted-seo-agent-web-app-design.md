# Self-Hosted SEO Agent Web Application Design

**Date:** 2026-07-10  
**Status:** Design approved by the user  
**Product name:** Elisa SEO Agent  
**Distribution:** Open source through GitHub; self-hosted only

## Goal

Build a free, open-source SEO operations application that users run on their own machines with Docker Compose. The application turns the existing SEO skill package into a navigable local web interface that can onboard multiple projects, connect user-owned AI and SEO services, establish ranking baselines, map entire websites, prioritize evidence-based work, prepare CMS drafts, track progress, and resume work after interruption.

The application must preserve the existing skill-driven workflow while making the system understandable to non-specialist users: every screen must explain what is happening, what is blocking progress, and what the next action is.

## Product boundaries

### Included in the first product

- Self-hosted local web application
- Docker Compose installation
- Multiple isolated projects
- Project switching
- Hybrid persistence: SQLite plus Markdown/Obsidian-compatible vaults
- Local plaintext API configuration for self-hosted use
- Multiple AI providers
- Sitemap import and site architecture mapping
- Keyword import and money-page mapping
- Baseline rank tracking
- Google Search Console measurements
- Optional Google Analytics measurements
- DataForSEO rank tracking adapter
- Page audits and checklists
- Keyword opportunity and low-hanging-fruit discovery
- Keyword prioritization in batches, defaulting to the top 10 opportunities
- Existing-content optimization workflows
- Internal-link planning and implementation queues
- WordPress draft/revision implementation
- Optional On-Page.ai adapter
- AI/LLM search visibility audits
- Backlink opportunity recommendations
- Weekly monitoring and reporting
- Pause/resume-safe jobs and autonomous loops
- Approval gates, audit trails, errors, blockers, and next-action guidance
- Public static landing page
- GitHub README, setup documentation, provider guides, demo data, and contribution guidance

### Explicitly excluded from v1

- SaaS hosting or hosted user accounts
- Cloud tenancy or mandatory cloud storage
- Gmail outreach or automated external email
- Local SEO/GBP workflows
- Automatic publishing to a CMS
- Mandatory Ahrefs or another all-in-one SEO subscription
- Automatic creation of new content
- Required On-Page.ai access
- Required Bitwarden access

Existing OpenClaw skills that fall outside this web-application scope may remain in the broader skill package, but they must not be exposed or routed by the v1 web application unless their connector and workflow are intentionally enabled.

## Deployment model

The user installs the application from GitHub:

```bash
git clone https://github.com/your-org/seo-agent
cd seo-agent
docker compose up
```

The working repository name is \`elisa-seo-agent\`. The application runs locally and is accessed through a browser. It does not require a hosted account.

Supported host environments for the initial release:

- macOS through Docker Desktop
- Windows through Docker Desktop
- Linux through Docker Engine/Compose

The repository will provide `.env.example`, setup instructions, health checks, troubleshooting, backup/restore instructions, and a sample project.

## Architecture

The recommended architecture is a local web control plane plus background workers:

```text
Browser
  ↓
Web UI/API
  ↓
SQLite + project vault
  ↓
Job queue
  ↓
SEO worker and loop controller
  ↓
DataForSEO, GSC, GA4, optional On-Page.ai, CMS, AI providers
```

### Runtime services

```text
web
  Dashboard, onboarding, project switching, reports, approvals

worker
  SEO skills, crawls, audits, optimization jobs, CMS drafts

scheduler
  Weekly checks, recurring monitoring, loop wake-ups

browser
  Optional Playwright browser for CMS workflows

storage
  SQLite database plus mounted project vault/filesystem
```

Long-running SEO work must not execute inside the web request process. The web service creates jobs; workers execute them and write progress to SQLite and the project vault.

Suggested repository structure:

```text
seo-agent/
├── app/
├── worker/
├── scheduler/
├── browser/
├── packages/
├── skills/
├── vault-templates/
├── landing-page/
├── docs/
├── examples/
├── tests/
├── docker-compose.yml
├── .env.example
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## User workflow

### 1. Install and launch

The user starts Docker Compose and opens the local dashboard. The first screen explains the product, local storage model, required/optional services, and setup steps.

### 2. First-run environment checks

The application checks:

- Docker services are running
- Required directories are writable
- SQLite is available
- Project vault directory is available
- Browser automation is available when needed
- At least one AI provider is configured
- Optional connectors that are configured are reachable

Users can continue in reduced mode when optional services are missing.

### 3. Configure AI providers

The user can configure multiple providers, models, permissions, fallbacks, and budgets. Initial provider targets:

- OpenAI
- Anthropic
- Google Gemini
- Ollama/local models
- Generic OpenAI-compatible endpoints

The application routes tasks through a provider abstraction rather than hard-coding a vendor into SEO skills.

### 4. Create a project

The onboarding wizard collects:

- Project name
- Website URL
- Sitemap URL
- Business model
- Services/products
- Target locations
- Money keywords
- Money pages
- Competitors
- SEO goal
- Ranking location, language, and device
- GSC connection
- GA4 connection
- DataForSEO connection
- Optional On-Page.ai connection
- WordPress/CMS connection
- Approval rules
- Weekly monitoring schedule

The user can import keywords by CSV or paste them into the interface. Existing rankings and analytics may also be imported from CSV.

### 5. Capture the baseline

Before strategy execution, the application records the initial position for every tracked keyword, including:

- Keyword
- Ranking URL
- Search engine
- Country/location
- Language
- Device
- Search depth
- Capture date
- Data source
- Current rank or unavailable status

It also records GSC clicks, impressions, CTR, average position, and optional GA4 organic traffic/conversion values.

### 6. Map the website

The application processes the sitemap and permitted crawl data, displaying intermediate progress such as:

```text
Found 428 sitemap URLs
311 eligible content URLs
42 money/service pages
176 blog posts
63 location pages
30 excluded utility/archive URLs
```

The map identifies page types, tiers, hierarchy, existing links, orphan pages, duplicates, canonical/redirect signals, page keywords, likely money pages, support pages, and blog relationships.

### 7. Discover and prioritize opportunities

The system combines user keywords, GSC queries, DataForSEO data, existing content, site architecture, and optional On-Page.ai evidence to identify:

- Keywords ranking positions 11–30
- High-impression/low-CTR opportunities
- Ranking declines
- Wrong-page targeting
- Missing pages
- Weak money pages
- Content gaps
- Internal-link opportunities
- Cannibalization risks
- Top-level, secondary, blog, and local topic opportunities when relevant to the project evidence

The default queue focuses on the top 10 highest-impact opportunities, then processes the next 10 and subsequent supporting batches.

### 8. Audit pages

The system runs appropriate audits and creates page checklists for:

- Standard on-page issues
- Stuck-page diagnosis
- AI/LLM visibility
- Image and alt-text issues
- Subheadline relevance
- Cannibalization
- Internal-linking opportunities
- Local workflows are excluded from v1 and are not routed by the application

Each checklist records evidence, priority, recommendation, approval state, completion state, and verification result.

### 9. Prepare and implement existing-content changes

The first release focuses on optimizing existing content. It may:

- Add relevant entities where evidence supports them
- Improve headings when needed
- Improve image alt text
- Refresh outdated sections when facts are verifiable
- Fix internal links
- Improve page structure
- Improve local relevance only when the future local scope is enabled

It must preserve human-written content and avoid unnecessary rewrites. New-content generation is not part of the initial workflow.

### 10. Create CMS drafts

WordPress is the first CMS target. The application uses the WordPress REST API where available and browser automation as a fallback. Changes are saved as drafts, revisions, or pending review. Publishing is disabled by default and requires explicit project approval.

### 11. Build internal-link structures

The internal-link workflow:

1. Maps the site hierarchy.
2. Catalogues existing keyword mentions.
3. Maps money pages to support pages.
4. Proposes contextual source/target links.
5. Checks for duplicate links.
6. Creates an implementation queue.
7. Applies approved links as CMS drafts.
8. Verifies the final source/target relationship.
9. Saves the audit trail.

### 12. Monitor and continue

Weekly checks compare current rankings and traffic against the baseline and previous snapshots. The system reports gains, losses, new opportunities, technical issues, and next actions.

## UI and feedback model

Every important screen must answer:

1. What is happening?
2. Is anything blocking progress?
3. What should happen next?

The project header displays status, the next recommended action, blocker count, pending approvals, and active jobs.

Long-running tasks display current step, processed/total work, batch, estimated remaining time where available, last checkpoint, pause, cancel, and live log controls.

Errors must be human-readable and actionable. Each error includes:

- What failed
- Why it may have failed
- Whether work is blocked
- What remains safe
- Recommended fix
- Retry button
- Details/log access

The blocker center classifies issues as blocking, warning, or informational and provides a direct next action.

Empty states must explain what is missing and link to the setup step that resolves it.

## Persistence and resumability

### SQLite

SQLite stores operational state:

- Projects
- AI providers
- Integrations
- Keywords
- Pages
- Sitemap records
- Ranking snapshots
- GSC/GA4 snapshots
- Jobs
- Checkpoints
- Loop states
- Approvals
- CMS drafts
- Internal-link proposals
- Reports
- Errors and blockers

### Project vault

Each project gets an Obsidian-compatible Markdown vault:

```text
project-vault/
├── 00-strategy/
│   ├── project-profile.md
│   ├── onboarding-checklist.md
│   ├── money-keywords.md
│   ├── competitors.md
│   ├── tool-access-map.md
│   └── approval-rules.md
├── 01-theses/
├── 02-learnings/
├── 03-experiments/
├── 04-competitors/
├── 05-opportunities/
│   ├── keywords/
│   ├── internal-linking/
│   └── backlinks/
├── 06-anomalies/
├── 07-queue/
│   ├── setup-tasks.md
│   ├── page-checklists/
│   └── loops/
├── 08-tracking/
│   ├── baseline-rankings.csv
│   ├── snapshots/
│   ├── weekly/
│   └── loops/
├── 09-reports/
│   ├── audits/
│   ├── weekly/
│   ├── internal-linking/
│   └── on-demand/
├── 99-daily/
└── README.md
```

SQLite is authoritative for execution and dashboard state. The vault is authoritative for human-readable project memory, decisions, reports, checklists, loop state, and audit history. External services remain authoritative for their own measurements, which are timestamped when imported.

### Job states

```text
queued
running
checking
waiting_for_approval
paused
blocked
completed
failed
```

Jobs checkpoint after safe units such as a sitemap batch, page audit, keyword group, CMS draft, internal-link proposal, or ranking snapshot.

On restart, stale running jobs are reconciled, completed work is preserved, and work resumes from the last safe checkpoint. Idempotency keys prevent duplicate links, drafts, or snapshots.

## Integrations

### AI providers

All providers use a common interface with model selection, task permissions, fallback priority, budget limits, availability, and privacy controls.

The app must not send the same project content to every configured provider unless the user explicitly permits that behavior.

### DataForSEO

Primary explicit rank-tracking adapter for baseline and weekly keyword position snapshots.

### Google Search Console

Search performance source for clicks, impressions, CTR, average position, queries, and page-level performance.

### Google Analytics

Optional traffic and conversion source.

### On-Page.ai

Optional connector. It unlocks live entity/competitor/SERP-specific functions but is not required for core application operation. Without it, the app must clearly mark those features unavailable rather than imitate their evidence.

### WordPress/CMS

First CMS connector. REST API first, browser automation fallback, drafts/revisions by default, explicit publishing approval.

## Credential handling

Local plaintext configuration is permitted for the self-hosted version:

```text
config/local.env
```

Rules:

- `local.env` is gitignored.
- Credentials are not stored in the project vault.
- Credentials are not stored in SQLite.
- Credentials are not included in reports or exports.
- Credentials are never printed in logs or errors.
- UI values are masked after saving.
- `.env.example` contains placeholders only.
- The UI warns that anyone with machine/file access may read the credentials.

Bitwarden is optional and not required for v1.

## Orchestration and loops

The existing skills become registered capabilities with metadata describing their requirements, optional requirements, outputs, approval needs, and resumability.

The orchestrator:

- Reads active project state
- Checks dependencies and integrations
- Selects eligible skills
- Creates jobs
- Routes them to workers
- Evaluates results
- Updates queues and vault state
- Decides the next action

The loop controller implements:

```text
RUN → CHECK → DECIDE → RECORD
```

It may continue, retry, pause, wait for approval, wait for measurement, escalate, mark blocked, stop at a budget cap, or complete.

Approval is required by default for CMS edits, internal-link implementation, drafts, publishing, project-goal changes, and any future external communication.

## Landing page and distribution

The landing page is a static public site in the GitHub repository and can be deployed through GitHub Pages. It will include:

- Hero message focused on open-source self-hosted SEO intelligence
- Problem statement
- Workflow diagram
- Feature overview
- Multiple-AI-provider explanation
- Self-hosting/privacy explanation
- Supported/optional integration distinction
- Dashboard screenshots or mockups
- Docker installation command
- GitHub link
- Configurable referral links with clear disclosure
- Open-source license and contribution links
- FAQ
- Reddit/community links

Primary CTA: download/clone from GitHub. Secondary CTA: read setup documentation.

## Release phases

### Phase 1: Local foundation

Docker, dashboard, SQLite, project vaults, project switching, local configuration, AI provider setup, first-run checks, backup/restore.

### Phase 2: Discovery and baseline

Sitemap import, progress reporting, page inventory, hierarchy mapping, keyword import, money-page mapping, DataForSEO baseline, GSC, optional GA4.

### Phase 3: Opportunity and audit system

Keyword opportunities, low-hanging fruit, prioritization, page checklists, AI routing, optional On-Page.ai, AI-search visibility, cannibalization, topic recommendations.

### Phase 4: Implementation workflows

Internal-link queues, WordPress integration, draft/revision creation, before/after comparisons, approval gates, verification, resumable CMS jobs.

### Phase 5: Monitoring and autonomy

Weekly snapshots, trend reports, decline detection, loop-controller integration, pause/resume, retries, blockers, on-demand reports.

### Phase 6: Public launch

Landing page, README, provider guides, demo project, screenshots, FAQ, contribution guide, license, issue templates, roadmap, and Reddit launch material.

## Success criteria

The first public release is successful when a new user can:

1. Clone the GitHub repository.
2. Start the application with Docker Compose.
3. Configure multiple AI providers.
4. Create and switch between projects.
5. Complete onboarding with a visible checklist.
6. Import a sitemap and keywords.
7. See intermediate site-mapping progress.
8. Capture a ranking baseline.
9. View page/keyword relationships and priority opportunities.
10. Run page audits and see evidence-backed next steps.
11. Pause and resume a long-running job without duplicate work.
12. Prepare an approved WordPress draft without publishing.
13. View reports comparing baseline and current results.
14. Restore project state from a local backup.

## Open design decisions resolved

- Deployment: self-hosted only through GitHub and Docker Compose.
- Storage: hybrid SQLite plus Markdown/Obsidian-compatible vault.
- Credentials: local plaintext configuration allowed; Bitwarden optional.
- AI: multiple providers supported through adapters.
- On-Page.ai: optional connector, never a required dependency.
- Gmail outreach: excluded.
- Local SEO/GBP: excluded.
- Automatic content generation: excluded from v1.
- CMS: WordPress first; draft/revision mode by default.
- Monitoring: weekly by default, with manual run-now.
- Keyword intake: CSV and direct paste.
- Rank settings: location, language, device, engine, depth, and cadence per project.
- Public presence: static GitHub landing page plus documentation.
- Progress: checkpointed, resumable, idempotent.
