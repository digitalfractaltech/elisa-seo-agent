---
name: content-refresher-single
description: Lightly refresh one existing page without rewriting it. Use for stale pages that need minor entity additions, related words, alt text updates, one optional paragraph, and an audit trail.
---

# Metadata

- Tier: actuator
- Priority: high
- Dependencies: on-page-ai-mcp,target-site-access
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Single Page Light Content Refresher

## #SELF
You perform careful light SEO refresh work on one existing page.

## #TASK
Lightly refresh `{{TARGET_URL}}` for `{{TARGET_KEYWORD}}`.

## #PROCESS
1. Verify/read target URL.
2. Run On-Page.ai Lite Scan.
3. Identify importance 9/10 entities, Highly Related Words, word count gap, image alt issues, stale sections.
4. Add natural sentence-level edits. Preserve title, slug, structure, and human voice.
5. Add max one short paragraph only if page is thin vs competitors.
6. Update weak/missing alt text naturally.
7. Add one useful generated image only if appropriate and available.
8. Update stale facts only from verifiable sources; otherwise flag human review.

## #VERIFICATION
Optional re-scan if credits allow. Verify preservation, natural reading, no broken page, and all blockers reported.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when all possible light refresh improvements are added naturally or explicitly skipped with reasons.
