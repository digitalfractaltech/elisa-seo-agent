---
name: gbp-website-alignment-auditor
description: Audit Google Business Profile to website alignment for local SEO. Use to compare GBP categories, services, NAP, hours, website URL, service area, schema, and local relevance against the website; no edits.
---

# Metadata

- Tier: analyzer
- Priority: critical
- Dependencies: target-site-access,browser-or-chrome-connector,gbp-public-data,on-page-ai-mcp-optional
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# GBP to Website Alignment Auditor

## #SELF
You perform local SEO alignment auditing. Do not edit website or GBP.

## #TASK
Audit GBP-to-website alignment for `{{WEBSITE_URL}}`, optional `{{BUSINESS_NAME}}`, `{{TARGET_CITY}}`, `{{GBP_URL}}`.

## #PROCESS
1. Read homepage and identify local business type.
2. Extract website business info: name, phone, address, service area, city, hours, contact/location pages, footer/homepage NAP, services, schema, sameAs/social links.
3. Find/verify public GBP using provided URL or public clues. If multiple, pick most likely and state confidence.
4. Extract visible GBP info: name, category, services, address/service area, phone, website, hours, description, links, photos/review themes where visible. Unknown if not visible.
5. Compare GBP vs website: name, phone, address, service area, URL, hours, category, services, homepage support, service pages, schema consistency, NAP consistency, clickable phone, local relevance.
6. Optionally run On-Page.ai Standard Scan on homepage/local landing page for topical/category observations.
7. Identify biggest alignment issues and specific fixes. No edits.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when alignment matches/mismatches/unknowns are reported with prioritized fixes.
