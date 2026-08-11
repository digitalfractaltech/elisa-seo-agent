---
name: baseline-rank-position-tracker
description: Create and maintain baseline keyword rankings, GSC traffic, landing page visibility, and weekly trend snapshots for each project. Use at project onboarding before strategy work begins, and during weekly check-ins to compare rankings, traffic, CTR, impressions, clicks, and conversion movement against baseline.
---

# Metadata

- Tier: measurement
- Priority: critical
- Dependencies: project-profile,keyword-list,gsc-optional,ga4-optional,dataforseo-rank-tracker-adapter-optional,conversion-data-source-optional,on-page-ai-mcp-optional,obsidian-vault
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# Baseline Rank Position Tracker

## #SELF
You establish the before-state for a project and maintain weekly trend snapshots. Do not recommend strategy until baseline is captured or the missing baseline data is explicitly documented.

## #TASK
Create or refresh baseline ranking and positioning for every tracked keyword in the active project.

## #WHEN TO USE
- During project onboarding, before SEO work begins.
- Before the first optimization campaign.
- Weekly check-ins.
- Monthly/quarterly strategy reviews.
- Whenever a new keyword is added to tracking.

## #BASELINE PROCESS
1. Load the active project profile and keyword list.
2. For every money keyword and approved tracking keyword, collect available baseline data:
   - keyword
   - target URL / intended page
   - ranking URL actually ranking, if different
   - organic position from DataForSEO if configured
   - DataForSEO rank_absolute / rank_group if DataForSEO is configured
   - SERP depth checked and not-found status if applicable
   - GSC average position
   - GSC impressions
   - GSC clicks
   - GSC CTR
   - GA4 organic sessions for ranking/target page if available
   - GA4 conversions/events if available
   - conversion events/leads/revenue by landing page if available
   - SERP features / AI Overview presence if available
   - local/map-pack presence if relevant and available
   - date captured
   - data source freshness
   - confidence
3. If DataForSEO is configured, invoke `dataforseo-rank-tracker-adapter` for location/device-specific Google organic SERP snapshots.
4. If DataForSEO is not configured, use GSC average position as partial baseline and mark limitations.
5. If GSC is missing, use DataForSEO only and mark traffic unknown.
6. If both ranking and GSC sources are missing, create a required setup task and do not invent rankings.
7. Note: On-Page.ai MCP is not a rank tracker; store its scores separately as optimization evidence.
8. Save baseline to:
   - `08-tracking/baseline-rankings.csv`
   - `08-tracking/baseline-rankings.md`
   - `08-tracking/snapshots/YYYY-MM-DD.csv`
9. Write a baseline summary to `99-daily/YYYY-MM-DD.md`.

## #WEEKLY CHECK-IN PROCESS
1. Pull the same metrics for the current week.
2. Compare current values to:
   - baseline
   - previous week
   - previous 4-week average where possible
3. Identify for each keyword:
   - improved
   - degraded
   - flat
   - volatile
   - data missing
4. Identify pages where the ranking URL changed from intended target URL.
5. Identify keywords with traffic improving but rank flat, rank improving but traffic flat, CTR drops, impression drops, or conversion changes.
6. Tie movement to completed experiments/tasks where possible.
7. Save weekly snapshot to:
   - `08-tracking/snapshots/YYYY-MM-DD.csv`
   - `08-tracking/weekly/YYYY-MM-DD.md`
8. Send summary to `performance-tracker-reporter`.

## #TREND INTERPRETATION
Classify trend by evidence:
- Ranking improvement: position improved by 2+ positions or entered top 10/top 3.
- Ranking degradation: position dropped by 2+ positions, exited top 10/top 3, or ranking URL changed to worse page.
- Traffic improvement: clicks/sessions up materially, considering impressions and seasonality.
- CTR issue: impressions stable/up but CTR down.
- Demand issue: rankings stable but impressions down.
- Conversion issue: traffic stable/up but conversion data or GA4 conversions down.
- Attribution issue: source_url null/unknown too high.

## #REPORT
The weekly report must include:
- baseline date
- current snapshot date
- keywords tracked
- keywords missing data
- top ranking gains
- top ranking losses
- top traffic gains
- top traffic losses
- CTR issues
- impression/demand changes
- ranking URL mismatches
- low-hanging fruit: positions 4-20
- keywords needing on-page audit
- keywords needing internal links
- keywords likely needing backlinks/off-page support
- conversion movement if available
- data gaps/blockers
- recommended next actions

## #SUCCESS
Successful when every tracked keyword has a baseline or a documented data gap, weekly snapshots are saved, and Emily can prove whether the project is improving or degrading against the starting position.
