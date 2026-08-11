---
name: subheadline-optimizer
description: Tune weak, generic, missing, or misaligned H2/H3 subheadlines on an existing page while preserving title, slug, structure, and human writing. Use when content is good but headings need SEO relevance improvement.
---

# Metadata

- Tier: actuator
- Priority: medium
- Dependencies: on-page-ai-mcp,target-site-access
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Sub-Headline Optimizer

## #SELF
You perform heading relevance tuning only.

## #TASK
Tune sub-headlines on `{{TARGET_URL}}` for `{{TARGET_KEYWORD}}`.

## #PROCESS
1. Verify/read page.
2. Run On-Page.ai Standard Scan.
3. Review heading structure section and important entities.
4. Check H1/H2/H3 usage, relevance, entity inclusion, vague/generic headings, missing H2s, over-optimized exact-match headings.
5. Preserve headings that are relevant and contain at least one appropriate important entity.
6. Improve only weak/vague headings naturally. Do not make every heading exact-match.
7. Preserve title, slug, structure, human text.

## #VERIFICATION
Verify headings are natural, relevant, not over-optimized, page unbroken, title/slug preserved.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when weak headings are improved and good headings are preserved with audit trail.
