# Emily Tool Setup Checklist

## Required before recipe skills run

- On-Page.ai MCP connected in OpenClaw: https://api.on-page.ai
- Target site access configured for read/edit operations.
- Obsidian vault exists: `{{VAULT_ROOT}}`.
- Skills live in: `{{SKILLS_ROOT}}`.
- Reviewer skill is used before any output is accepted.

## Optional/expected integrations

- The configured notification channel for daily digest/status.
- GSC for impressions, clicks, CTR, average position, and query/page performance.
- DataForSEO Google Organic SERP API for optional rank snapshots by keyword/location/device/depth.
- On-Page.ai MCP for on-page scans, entity gaps, internal link suggestions, and optimization evidence.
- GA4 and the active project's configured conversion data source if available.
- Ahrefs or another backlink/competitor data provider if available; no Ahrefs project is required by default.
- CMS/WordPress access for approved draft implementations.

## First recommended runs

1. `project-orchestrator` to create/register the project vault and collect project inputs.
2. `keyword-opportunity-miner` to build the first keyword universe.
3. `baseline-rank-position-tracker`; use `dataforseo-rank-tracker-adapter` if DataForSEO is configured.
4. `site-architecture-mapper` to classify hierarchy and internal-link relationships.
5. `rank-stuck-diagnostic` for any money keyword stuck outside top 10.
6. `standard-optimizer-single` only after the approver approves edits.
