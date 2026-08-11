---
name: image-alt-optimizer
description: Optimize images and alt text on an existing page using live SERP/image benchmarks. Use when images are missing, decorative, weakly described, duplicated, irrelevant, or the page is visually thin versus competitors.
---

# Metadata

- Tier: actuator
- Priority: medium
- Dependencies: on-page-ai-mcp,target-site-access,image-generation-optional
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Image and Alt Text Optimizer

## #SELF
You improve image context and alt text without keyword stuffing.

## #TASK
Optimize images and alt text on `{{TARGET_URL}}` for `{{TARGET_KEYWORD}}`.

## #PROCESS
1. Verify/read page.
2. Run On-Page.ai Standard Scan.
3. Review image/alt sections and competitor visual usage.
4. Check missing, weak, generic, duplicated, irrelevant alt text; page low on images; long blocks needing visuals.
5. Update alt text descriptively with entities only where natural.
6. Add generated images only if clearly useful, available, relevant, spaced out, and not random.
7. If image generation unavailable, provide prompts, placement, filenames, and alt text.
8. Preserve title, slug, structure, human text.

## #VERIFICATION
Verify page unbroken, images relevant, alt text natural, changes audited.

## #REPORT
Use `templates/output.md`.

## #SUCCESS
Successful when image/alt issues are reviewed, valid improvements made, and skipped/unavailable items reported.
