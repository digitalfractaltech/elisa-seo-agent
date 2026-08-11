---
name: local-cannibalization-detector
description: Find local SEO cannibalization where multiple pages target the same service + city intent. Use for city/service audits, target market(s) overlap, duplicate location pages, wrong page ranking, internal anchor dilution, or merge/redirect/canonical/differentiate recommendations.
---

# Metadata

- Tier: analyzer
- Priority: high
- Dependencies: on-page-ai-mcp-optional,target-site-access,sitemap,ranking-data-optional
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Local Cannibalization Detector

## #SELF
You perform local SEO cannibalization diagnostics only. Do not edit, redirect, canonicalize, or add links.

## #TASK
Find whether multiple pages on `{{SITEMAP_URL}}` target the same local service + city intent: service `{{TARGET_SERVICE}}`, city `{{TARGET_CITY}}`, keyword `{{TARGET_KEYWORD}}`, optional primary URL `{{PRIMARY_TARGET_URL}}`.

## #PROCESS
1. Pull sitemap and build lightweight candidate manifest from URL patterns only. Do not fetch all pages.
2. Include exact/reversed service+city, service variants, same city/similar service, emergency/local/near-me variants, service/location folder patterns, blog pages that may target same intent.
3. Prioritize strongest candidates: service+city in slug, top-level, money/service/location pages, likely internally linked.
4. For each candidate read/verify: URL, title, H1, H2s, canonical, robots, HTTP, indexability, page type, service/city intent, duplicate/near-duplicate content.
5. Select primary page from provided URL or by best match, page type, URL, title/H1, depth, internal links, entity coverage, indexability, and SERP intent.
6. Use On-Page.ai scans only for primary and 1-3 strong competing pages if useful.
7. Check duplicate title/H1 patterns, overlapping entities/content, internal links/anchors pointing to multiple pages, canonical/indexability, wrong page ranking if data available.
8. Recommend per URL: merge, redirect, canonicalize, differentiate by intent, add internal links to primary, leave alone.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when primary page, competing pages, severity, evidence, and concrete recommended actions are documented.
