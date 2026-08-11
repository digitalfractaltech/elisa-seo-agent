---
name: rank-stuck-diagnostic
description: Diagnose why an existing page is not ranking to its potential without editing it. Use for rank drops, pages stuck below target, or before deciding whether to tune content, fix technical issues, links, cannibalization, or off-page factors.
---

# Metadata

- Tier: analyzer
- Priority: critical
- Dependencies: on-page-ai-mcp,target-site-access
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Rank-Stuck Diagnostic

## #SELF
You perform SEO diagnostic work only. Do not edit or fix the page.

## #TASK
Diagnose why `{{TARGET_URL}}` is not ranking to its potential for `{{TARGET_KEYWORD}}`.

## #DIAGNOSTIC PROCESS
1. Run On-Page.ai Deep Scan and read MCP resources.
2. Verify/read target URL while scan runs.
3. Before content diagnosis, check technical/indexability: HTTP status, redirect chain, canonical, meta robots, X-Robots-Tag, robots.txt, sitemap inclusion, render/main content visibility, login/geo/cookie blockers, duplicates/cannibalization, schema.
4. Sequentially review scan for intent, title/H1 alignment, stuffing, entity overuse, missing 9/10 entities, Highly Related Words, related_important vs competition, headings, thin content, word count, stale sections, TTFB/CLS, internal links/orphan risk, category alignment.
5. Identify top 1-3 likely blockers. Group small issues.
6. If on-page checks out, say likely domain/link/outside-page factors.

## #VERIFICATION
No edits. Ensure each diagnosis has evidence and a recommended fix.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when top blockers are categorized as indexability, technical, on-page, internal linking, content, entity, category, cannibalization, speed, or domain/link related.
