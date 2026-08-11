---
name: internal-link-builder-sitewide
description: Build internal links across a site in resumable batches from a sitemap manifest. Use when the configured approver asks for site-wide internal linking, batch processing, or contextual internal link additions based on On-Page.ai suggestions.
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

# Site-Wide Internal Link Builder

## #SELF
You perform controlled SEO internal linking. Build a task list. Use scripts for sitemap manifest, batching, resume, reporting; use On-Page.ai for relevance suggestions.

## #TASK
Build internal links across the site using `{{SITEMAP_URL}}`. Process only `{{PAGE_RANGE}}` in this run.

## #PROCESS
1. Create/load a lightweight manifest from all child sitemaps using URL patterns only. Do not fetch all pages.
2. Exclude non-content pages: category, tag, author, search, archive, cart, checkout, login, paginated, terms, privacy, maps/contact.
3. Manifest fields: position, target URL, scan status, suggested sources, checked sources, links added, skipped reason, verification, current/cumulative status.
4. Preserve manifest order forever unless the approver explicitly asks to rebuild.
5. Process selected range in batches: default 10 targets, max 5 scans running.
6. Infer keyword/topic from target title/H1/slug/content.
7. Run Standard Scan for each target. Check only suggested source pages, max 3 per target.
8. Add up to 3 natural contextual links per target from main content only, avoiding duplicates and messy repeated source edits.
9. Update manifest after every page and save before next batch.

## #VERIFICATION
Verify edited source pages contain the new main-content links and each target received up to 3 links where possible.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when selected manifest range is processed, valid links added, skipped items explained, manifest saved, and HTML report produced.
