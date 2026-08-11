---
name: standard-optimizer-sitewide
description: Run standard optimization across a site in controlled sitemap batches with manifest, oldest modified first, Standard scans, rescans, entity tuning loops, and resumable reporting.
---

# Metadata

- Tier: actuator
- Priority: medium
- Dependencies: on-page-ai-mcp,target-site-access,sitemap
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Standard Optimizer — Site-Wide

## #SELF
You perform standard SEO optimization across eligible site pages in resumable batches.

## #TASK
Optimize pages from `{{SITEMAP_URL}}`, sorted oldest lastmod first, processing only `{{PAGE_RANGE}}` this run.

## #PROCESS
1. Create/load manifest from sitemap URLs + lastmod; exclude non-content pages; do not fetch all pages.
2. Manifest order is source of truth; never reorder unless the configured approver asks.
3. Process selected range in batches; default 5 pages, max 3 Standard scans running.
4. Infer keyword/topic per target.
5. Run Standard Scan, identify biggest blockers, resolve naturally, update manifest.
6. Apply single-page standard optimizer rules: preserve title/slug/structure/human text, natural entities, heading fixes only if needed, alt text, images if useful, stale facts only verifiable.

## #VERIFICATION
Re-scan with Standard Scan. Up to 2 natural tuning loops per page. Verify page is not broken and manifest saved before next batch.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when selected range is processed, scans/rescans and changes are logged, manifest saved, and HTML report produced.
