---
name: dataforseo-rank-tracker-adapter
description: Use DataForSEO Google Organic SERP API as Emily's optional rank-tracking data source. Use to create baseline keyword rankings, weekly SERP snapshots, top 10/top 20/top 50/top 100 checks, desktop/mobile/local ranking checks, ranking URL detection, SERP feature notes, and not-found status for tracked keywords.
---

# Metadata

- Tier: measurement
- Priority: high
- Dependencies: dataforseo-api-optional,keyword-list,target-domain,project-profile,obsidian-vault
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# DataForSEO Rank Tracker Adapter

## #SELF
You turn DataForSEO SERP snapshots into project ranking evidence. DataForSEO is a ranking data source, not the strategist. Emily stores the history and interprets trends.

## #TASK
For the active project, collect Google organic SERP rankings for approved tracked keywords and write baseline/weekly snapshots into the project Obsidian vault.

## #WHEN TO USE
- Project onboarding baseline ranking capture.
- Weekly ranking checks.
- Keyword batch prioritization.
- Verifying whether a target domain entered/exited top 10/top 20/top 50/top 100.
- Detecting ranking URL changes or possible cannibalization.
- Local/device-specific rank checks where GSC average position is too blended.

## #DATA SOURCE ROLE
- DataForSEO gives raw SERP snapshots: keyword, location, language, device/OS, organic results, ranking fields, result URLs, and SERP features where requested.
- Emily must store snapshots over time. Do not assume DataForSEO keeps project history for us.
- On-Page.ai MCP is still used for on-page evidence and fixes; it is not the rank tracker.
- GSC remains the traffic/impression/CTR source. DataForSEO and GSC should be reconciled, not treated as interchangeable.

## #INPUTS REQUIRED
From the active project vault/profile:
- target domain and optional alternate domains/subdomains
- approved keyword list
- target URL / intended ranking page for each keyword if known
- location name or location code
- language code
- device and OS policy: desktop, mobile, or both
- rank depth policy: top 10, 20, 50, or 100
- check cadence and budget cap

If any required input is missing, create a setup task in `07-queue/` and mark the snapshot incomplete. Never invent locations, keywords, credentials, or ranks.

## #RECOMMENDED DEPTH POLICY
- Top 10: executive pulse and high-frequency checks.
- Top 20: low-hanging fruit detection.
- Top 50: most weekly project tracking.
- Top 100: onboarding baseline, priority money keywords, and diagnostics where the site may be far back.

For cost control, use deeper checks only for approved priority keywords. If previous rank is known, a later implementation may check nearby SERP pages, but record the actual depth/window used.

## #PROCESS
1. Load active project profile, keyword list, and prior ranking snapshot if any.
2. Confirm DataForSEO credentials/access status through the configured Bitwarden/session-manager secret reference without printing secrets.
3. For each approved keyword batch, request Google Organic SERP data with the configured location, language, device/OS, and depth.
4. Parse organic results and find matches for the target domain and approved alternate domains.
5. Record for each keyword:
   - date/time captured
   - keyword
   - target domain
   - intended target URL
   - ranking URL found
   - `rank_absolute`
   - `rank_group`
   - result title/snippet if available
   - result type
   - SERP features/AI Overview/local pack presence if available
   - device, OS, location, language
   - depth checked
   - check URL / task identifier if available
   - not-found status if no project URL appears within checked depth
   - confidence and data freshness
6. Detect ranking URL mismatch if the ranking URL differs from intended target URL.
7. Detect possible cannibalization if more than one project URL appears for the same keyword.
8. Save raw-safe snapshot and normalized table to Obsidian.
9. Hand normalized movement data to `baseline-rank-position-tracker` and `performance-tracker-reporter`.

## #OBSIDIAN OUTPUTS
Write to the active project vault:
- `08-tracking/rank-provider/dataforseo/YYYY-MM-DD-raw-summary.md`
- `08-tracking/snapshots/YYYY-MM-DD-dataforseo-rankings.csv`
- `08-tracking/weekly/YYYY-MM-DD.md` section: “DataForSEO SERP Snapshot”
- setup gaps to `07-queue/dataforseo-setup.md` when blocked

Do not store API keys, passwords, or authorization headers in the vault. Store only the Bitwarden secret reference, e.g. `bitwarden:dataforseo-api`.

## #FIELDS FOR CSV
Use these columns where available:

```csv
snapshot_date,keyword,location,language,device,os,depth_checked,target_domain,intended_url,ranking_url,rank_absolute,rank_group,result_type,title,serp_feature_notes,found,ranking_url_mismatch,possible_cannibalization,check_url,provider_task_id,confidence,notes
```

## #INTERPRETATION RULES
- `rank_absolute` is the absolute position across SERP elements returned by the provider.
- `rank_group` is position within a result group such as organic results.
- For SEO reporting, usually report organic position from organic results, but keep both values.
- If a keyword is not found within depth, report `not found in top {{DEPTH}}`, not “rank 101”.
- If device/location changed from baseline, do not compare as a clean trend; mark as methodology change.

## #REPORT
Include:
- keywords checked
- skipped/missing keywords
- cost/budget notes if available
- rankings found vs not found
- top 3/top 10/top 20/top 50/top 100 distribution
- ranking URL mismatches
- possible cannibalization
- low-hanging fruit positions 4-20
- priority losses
- keywords requiring On-Page.ai scan
- keywords likely requiring internal links
- keywords likely requiring authority/backlink support
- data gaps/blockers

## #SUCCESS
Successful when DataForSEO rankings are captured or blocked with exact setup reasons, snapshots are saved in the active Obsidian vault, and Emily can compare baseline/current positions without relying on chat memory.
