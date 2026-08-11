---
name: internal-link-builder-quick
description: Fast lightweight internal linking pass for one target page. Use when the configured approver wants a simple scan, suggested source checks, and seamless link additions without a full internal linking project.
---

# Metadata

- Tier: actuator
- Priority: low
- Dependencies: on-page-ai-mcp,target-site-access
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

## Original Recipe Authority

Before running this skill in production, read `references/original-recipe.md`. The original recipe is authoritative when it is more specific than this concise `SKILL.md`.

# Quick Single-Page Internal Link Builder

## #SELF
You perform a lightweight internal linking pass.

## #TASK
Run a Standard Scan on `{{TARGET_URL}}`, retrieve internal link suggestions, verify source pages, and add seamless contextual links where valid.

## #NOTES
Check source pages have useful main content, do not already link to target, and are relevant. Prefer article/page body, not menus, sidebars, footers, or related post widgets. Skip and report invalid suggestions.

## #VERIFICATION
Verify links exist after edits.

## #REPORT
Produce a concise HTML audit trail with source URL, target URL, anchor, skipped reasons, and access issues.

## #SUCCESS
Successful when all valid suggestions are processed and reported.
