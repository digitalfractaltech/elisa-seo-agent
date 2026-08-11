---
name: keyword-batch-prioritizer
description: Prioritize and batch large keyword sets so Emily tackles the highest-impact keywords first without exceeding context, time, or tool limits. Use to select top 10 priority keywords, next batches, low-hanging fruit, and weekly focus sets across many keywords.
---

# Metadata

- Tier: strategy
- Priority: critical
- Dependencies: keyword-universe,baseline-tracking,gsc-optional,conversion-data-optional,site-architecture-map
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# Keyword Batch Prioritizer

## #SELF
You prevent Emily from trying to optimize every keyword at once. You create focus batches based on value, opportunity, difficulty, and operational limits.

## #TASK
Prioritize the active project's keyword universe into actionable batches.

## #DEFAULT POLICY
Unless the project defines a different policy:
1. Focus first on the top 10 highest-impact keywords/pages.
2. Then the next 10.
3. Then supporting/long-tail batches.
4. Re-rank weekly based on new data.

## #INPUTS
Use available evidence:
- money keyword list
- baseline rankings
- GSC impressions/clicks/CTR/position
- DataForSEO positions and GSC average position
- conversion/revenue data if available
- On-Page.ai scan opportunities
- site architecture tier
- current page checklist status
- business priority
- difficulty/competition signals
- local vs national intent
- internal link readiness
- backlink need
- token/tool/time constraints

## #SCORING
Score each keyword 0-100 using:
- business value / commercial intent
- current position opportunity: positions 4-20 get priority
- impression/click potential
- conversion evidence if available
- page readiness: existing page > no page when optimizing existing content
- effort required
- competition difficulty
- strategic tier: Tier 1 > Tier 2 > Tier 3
- urgency: degradation/anomaly gets boosted
- dependency readiness: has target page, data, approval path

## #BATCH TYPES
Create:
- Batch A: Top 10 immediate focus
- Batch B: Next 10
- Low-hanging fruit batch: positions 4-20 or high impressions/low CTR
- Diagnostic batch: ranking drops/anomalies
- Internal linking batch
- Backlink support batch
- Content/topic recommendation batch, if content creation is in scope later

## #PROCESS
1. Load keyword universe and baseline tracking.
2. Score every keyword.
3. Group by page/cluster to avoid scattering effort.
4. Detect cannibalization/overlap before assigning multiple keywords to separate pages.
5. Select current focus batch within token/tool/time limits.
6. For each selected keyword, assign next skill:
   - `rank-stuck-diagnostic`
   - `local-page-diagnostic`
   - `standard-optimizer-single`
   - `internal-link-builder-priority`
   - `backlink-opportunity-recommender`
   - `topic-recommender`
7. Save batch plan to `07-queue/keyword-batches/`.
8. Update weekly based on performance.

## #REPORT
Include:
- total keywords considered
- keywords excluded and why
- scoring method
- Batch A top 10
- Batch B next 10
- low-hanging fruit batch
- page/cluster grouping
- next skill per keyword
- expected impact
- dependencies/blockers
- next review date

## #SUCCESS
Successful when Emily has a bounded, evidence-based keyword focus set and a clear next-action plan instead of trying to tackle the whole keyword universe at once.
