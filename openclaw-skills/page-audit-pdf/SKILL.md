---
name: page-audit-pdf
description: Create a focused client-ready SEO audit PDF/HTML for one target page and keyword using Deep Scan data, competitor/entity/speed/internal-link findings, and a 30/60/90-day action plan.
---

# Metadata

- Tier: reporting
- Priority: medium
- Dependencies: on-page-ai-mcp,target-page-access,pdf-capability-optional
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Single Page Audit PDF

## #SELF
You prepare a polished SEO audit for one page.

## #TASK
Create audit PDF/HTML for `{{TARGET_URL}}` targeting `{{TARGET_KEYWORD}}` for `{{CLIENT_NAME}}`.

## #PROCESS
1. Verify/read target page.
2. Run On-Page.ai Deep Scan.
3. Walk every major section and explain what data shows, why it matters, severity, and next action.
4. Check intent, title/H1, stale content, stuffing, entities, headings, content length, images, internal links, category alignment, TTFB, CLS, page experience.
5. Do not mention internal tool names in client-facing report.

## #REPORT
Create PDF and HTML: cover, executive summary, full page audit, competitor gap, entity/content gap, technical/speed, internal links, image/alt, topical/category alignment, priorities, 30/60/90-day plan.

## #SUCCESS
Successful when the page is fully audited and deliverables are polished, specific, and client-ready.
