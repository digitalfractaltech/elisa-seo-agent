---
name: keyword-opportunity-miner
description: Find and classify related keywords, low-hanging fruit, GSC opportunities, competitor/ SERP gaps, emerging queries, and keywords worth tracking. Use for continuous keyword discovery and opportunity prioritization.
---

# Metadata

- Tier: discovery
- Priority: critical
- Dependencies: gsc-optional,dataforseo-rank-tracker-adapter-optional,on-page-ai-mcp,ahrefs-data-optional,scrape-serp-optional,obsidian-vault
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# Keyword Opportunity Miner

## #SELF
You discover keyword opportunities from live data and classify what Emily should do with them.

## #TASK
Build or refresh the keyword universe for `{{WEBSITE_URL}}` and identify low-hanging fruit.

## #PROCESS
Use available evidence from:
- user-provided money keywords
- GSC queries/impressions/clicks/CTR/positions
- current DataForSEO ranking snapshots and GSC query data
- On-Page.ai scans and SERP evidence
- Ahrefs data if available, but do not require an Ahrefs project
- competitor SERPs
- autocomplete/PAA/related searches if available

Classify each opportunity:
- money keyword
- local keyword
- supporting keyword
- blog/resource topic
- comparison keyword
- FAQ/question keyword
- low-hanging fruit: positions 4-20, high impressions, weak CTR, or page-two rankings
- needs tracking
- needs existing page optimization
- needs new page recommendation
- needs internal links
- needs backlinks/off-page support

## #REPORT
Include keyword, current URL if any, current position/source, impressions/clicks if available, intent, page type recommendation, evidence, priority, expected business value, and next skill to invoke.

## #SUCCESS
Successful when Emily has a prioritized keyword opportunity map and a queue of tracking additions, page optimization candidates, and topic recommendations.
