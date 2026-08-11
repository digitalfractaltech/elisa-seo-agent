---
name: internal-link-builder-priority
description: Build up to three high-quality contextual internal links to one priority target page using On-Page.ai internal link suggestions. Use for money pages and important URLs needing stronger internal support.
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

# Priority Single-Page Internal Link Builder

## #SELF
You perform internal linking for one important target page.

## #TASK
Build contextual internal links pointing to `{{TARGET_URL}}` using optional keyword/topic `{{TARGET_KEYWORD}}`.

## #PROCESS
1. Verify/read target URL.
2. Infer keyword/topic if not provided.
3. Run On-Page.ai Standard Scan.
4. Read the top internal link source suggestions.
5. For each source: verify main content, verify it does not already link to target, skip invalid/non-content pages.
6. Add up to 3 natural contextual links in main content only. Choose anchor text from sentence context; avoid exact-match stuffing.

## #VERIFICATION
Verify each edited source page contains the link in main content and the target received all valid links possible.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when target is processed, valid links are added or skipped with reasons, and audit report is produced.
