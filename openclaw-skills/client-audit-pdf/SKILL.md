---
name: client-audit-pdf
description: Create a polished client-ready full website SEO audit PDF/HTML from representative pages using Deep Scans. Use for client reports, sales audits, or agency deliverables; hides internal tool names and explains findings in client-friendly language.
---

# Metadata

- Tier: reporting
- Priority: low
- Dependencies: on-page-ai-mcp,target-site-access,pdf-capability-optional
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Full Client Website Audit PDF

## #SELF
You represent the configured agency/company. You prepare a polished SEO audit for a client.

## #TASK
Create a website audit PDF/HTML for `{{CLIENT_SITE}}` and `{{CLIENT_NAME}}`. Audit homepage plus one representative product/money/article/landing page, up to 2-3 pages total.

## #PROCESS
1. Read homepage, determine site type, choose representative pages if not provided.
2. Run Deep Scans on selected pages with inferred keywords.
3. Walk every major scan section; do not collapse into summary only.
4. Check intent, title/H1, stale content, stuffing, entity gaps/overuse, headings, word count, images, internal links/orphan risk, category alignment, speed, TTFB, CLS.
5. Explain in client-friendly language without mentioning internal tool/process names.

## #REPORT
Create PDF and HTML. Include cover, executive summary, page audits, competitor gaps, entity/content gaps, technical/speed, internal links, image/alt, topical alignment, priority recommendations, 30/60/90-day plan.

## #SUCCESS
Successful when selected pages are audited, every section is explained with useful data, and branded PDF/HTML deliverables are created or print-ready HTML is provided.
