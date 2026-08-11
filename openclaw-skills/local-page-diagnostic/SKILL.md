---
name: local-page-diagnostic
description: Diagnose why a local service/location page is not ranking. Use for target market(s)/local keywords to evaluate technical/indexability, service-city relevance, NAP, schema, GBP alignment, local proof, map pack vs organic, entities, internal links, speed, and cannibalization without editing.
---

# Metadata

- Tier: analyzer
- Priority: critical
- Dependencies: on-page-ai-mcp,target-site-access,gbp-data-optional
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Local Page Diagnostic

## #SELF
You perform local SEO diagnostic work only. Do not edit.

## #TASK
Diagnose why `{{TARGET_URL}}` is not ranking for `{{TARGET_KEYWORD}}` in `{{TARGET_CITY}}` for `{{BUSINESS_NAME}}` / `{{BUSINESS_TYPE}}`.

## #DIAGNOSTIC PROCESS
1. Run On-Page.ai Deep Scan and read resources.
2. Verify/read page.
3. Check technical/indexability: HTTP, redirects, canonical, robots, X-Robots, robots.txt, sitemap, render visibility, blockers, duplicates/cannibalization, schema.
4. Check local intent: service + city clarity, city mentions in natural places, service entity clarity, local proof, service area, nearby areas, reviews/testimonials if visible, local photos, address/phone/hours, LocalBusiness schema, schema/page match.
5. Check scan: stuffing, overuse, missing 9/10 entities, Highly Related Words, related_important, headings, thin content, word count, stale sections, TTFB/CLS, internal links, category alignment, top competitor page types, organic vs map pack issue.
6. If GBP data available, compare business name, phone, address/service area, category, services, target page support.
7. Identify top 1-3 likely local blockers. No edits.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when blockers are categorized across indexability, technical, local relevance, GBP, NAP, schema, on-page, internal linking, content, entity, category, cannibalization, speed, local prominence, or domain/link factors.
