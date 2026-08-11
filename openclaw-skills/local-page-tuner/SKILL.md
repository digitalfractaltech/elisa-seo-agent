---
name: local-page-tuner
description: Tune an existing local service/location page based on what wins in the target city. Use after local diagnosis or for target market(s) local pages needing service-city relevance, local proof, service/location entities, headings, alt text, schema/NAP notes, and a simple audit trail.
---

# Metadata

- Tier: actuator
- Priority: critical
- Dependencies: on-page-ai-mcp,target-site-access
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Local Page Tuner

## #SELF
You perform local SEO tuning on one existing page.

## #TASK
Tune `{{TARGET_URL}}` for `{{TARGET_KEYWORD}}` in `{{TARGET_CITY}}` for `{{BUSINESS_NAME}}` / `{{BUSINESS_TYPE}}`.

## #PROCESS
1. Verify/read page.
2. Run On-Page.ai Standard Scan.
3. Identify local relevance blockers: service+city clarity, service entity, city/area mentions, local proof, service area, nearby areas, NAP, clickable phone, hours, LocalBusiness schema, schema/page match, stale content, stuffing, entity overuse, headings, word count, images, internal links, category alignment.
4. Add service entities, location entities, importance 7/8/9/10 entities, and Highly Related Words naturally.
5. Preserve title, slug, paragraphs, line breaks, human writing.
6. Improve local subheadlines only where weak; avoid exact-match robot headings.
7. Update alt text with service/location entities where natural.
8. Add local proof only if truthful/verifiable. Never invent reviews, certifications, addresses, projects, or claims.
9. Update stale content only from verifiable sources; otherwise flag human review.

## #VERIFICATION
Verify page clearly targets service+city, reads naturally, title/slug preserved, local proof truthful, category mismatch explained if present, page unbroken.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when local relevance issues are improved where possible, skipped items explained, and audit trail produced.
