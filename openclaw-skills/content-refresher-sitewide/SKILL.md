---
name: content-refresher-sitewide
description: Refresh old or stale site pages in controlled sitemap batches, oldest modified first. Use for site-wide light SEO refreshes that preserve content while adding missing entities, related words, alt text, and small updates.
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

# Site-Wide Light Content Refresher

## #SELF
You perform light SEO refreshes across a site in resumable batches.

## #TASK
Lightly refresh eligible content pages from `{{SITEMAP_URL}}`, sorted by sitemap lastmod oldest first. Process only `{{PAGE_RANGE}}`.

## #PROCESS
1. Build/load manifest from sitemap URLs + lastmod only; do not fetch all pages.
2. Exclude obvious non-content pages.
3. Sort dated URLs oldest first; undated after dated preserving sitemap order.
4. Process selected range in batches; default 10, max 5 Lite scans running.
5. Infer keyword/topic per page.
6. Run On-Page.ai Lite Scan.
7. Add importance 9/10 entities and Highly Related Words naturally. Preserve title, slug, structure, human writing.
8. Add at most one short paragraph only if content is thin vs competition.
9. Check/update image alt text where weak/missing.
10. Add at most one useful generated image if appropriate and available.
11. Update outdated sections only with verifiable facts; otherwise flag human review.
12. Update manifest after each page.

## #VERIFICATION
No mandatory re-scan. Verify title/slug/structure preserved, writing natural, additions appropriate, page unbroken, manifest saved.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when selected range is processed, improvements/skips are recorded, manifest saved, and HTML report produced.
