---
name: page-recovery
description: Recover an indexed SEO page that is stuck below its expected ranking. Use for a target URL and keyword when the page exists, has rankings/impressions, and needs deep scan, careful on-page fixes, internal links, verification rescans, and an HTML audit trail.
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

# Page Recovery

## #SELF
You are performing SEO recovery work. Build a detailed task list and continue until complete. You have access to On-Page.ai MCP, the target site, page reading/editing, reports, and approved publishing/edit tools.

## #TASK
Perform a deep SEO scan and recovery audit for `{{TARGET_URL}}` targeting `{{TARGET_KEYWORD}}`.

## #RECOVERY PROCESS
1. Run an On-Page.ai Deep Scan on the target URL/keyword.
2. Read available MCP resources and the target URL while the scan runs.
3. Check: keyword stuffing, entity over-usage vs competitors, H1/H2/H3 structure, sub-450 thin content, stale sections, TTFB, CLS, category alignment, and internal link source suggestions.
4. Identify critical issues preventing full ranking potential.
5. If internal link sources are suggested and valid, add up to 3 seamless contextual links from main content only, subject to approval policy.

## #OPTIMIZATION PROCESS
1. Add importance 9/10 entities and Highly Related Words naturally. Preserve title and human text. Prefer sentence edits.
2. Improve headings only if weak/misaligned; otherwise preserve them.
3. Improve image alt text naturally.
4. Add up to 3 useful images only if generation/upload is available and appropriate; otherwise report unavailable.
5. Update stale sections only with verifiable facts; flag human review if current research is needed.

## #VERIFICATION
1. Re-scan with Standard Scan.
2. Ensure related_important entity score is higher than competition.
3. If not, perform one light natural tuning pass, re-scan once more, then stop and explain blockers.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when tasks are complete, changes are audited, before/after scores are recorded, and blockers are explicitly reported.
