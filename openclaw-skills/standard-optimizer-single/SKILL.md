---
name: standard-optimizer-single
description: Standard on-page optimization for one existing page using live SERP/entity data. Use for money pages or new pages that already exist and need relevance, entities, headings, internal links, alt text, category alignment, and re-scan verification.
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

# Standard Optimizer — Single Page

## #SELF
You perform standard SEO optimization on one existing page using live SERP data.

## #TASK
Optimize `{{TARGET_URL}}` for `{{TARGET_KEYWORD}}`.

## #PROCESS
1. Verify/read target URL.
2. Run On-Page.ai Standard Scan.
3. Sequentially review report for biggest blockers: outdated content, stuffing, entity over-use, headings, word count, images, internal links, Google category alignment, and other obvious issues.
4. Research stale information only when current browsing/sources are available; otherwise flag human review.
5. Add appropriate importance 7/8/9/10 entities and Highly Related Words naturally. Preserve title, slug, paragraphs, line breaks, and human text.
6. Improve H2/H3 only if weak/misaligned/missing; do not make headings robotic or exact-match.
7. Update image alt text where weak/missing.
8. If category alignment differs drastically, make only natural intent-aligning changes and report the mismatch.
9. Add up to 3 useful images only if appropriate and available.
10. Add small text only if thin vs competition and useful to readers.

## #VERIFICATION
1. Re-scan with Standard Scan.
2. If related_important is not higher than competition, do up to 2 natural tuning loops total.
3. Stop if further additions would hurt readability or credits/tools are unavailable.
4. Verify title/slug/structure/paragraphs preserved and page unbroken.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when biggest issues are resolved where possible, related_important beats competition or blockers are explained, and full HTML report/audit trail is produced.
