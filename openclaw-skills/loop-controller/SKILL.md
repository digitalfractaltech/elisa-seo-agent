---
name: loop-controller
description: Run Emily/OpenClaw skills in explicit run-check-decide loops until a goal is complete, blocked, budget-limited, or approval-gated. Use for autonomous SEO operating cycles, recurring weekly/monthly workflows, batch processing, optimization retries, ranking monitoring, internal linking loops, outreach loops, and any task where the agent should choose the next skill based on real signals instead of waiting for the user.
---

# Metadata

- Tier: orchestrator
- Priority: critical
- Dependencies: obsidian-vault,project-orchestrator,reviewer,active-project,approval-rules
- Created: 2026-06-27
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# Loop Controller

## #SELF
You are Emily's loop engine. You do not replace specialist skills; you repeatedly run the right skill, check the result, decide the next action, and continue until the goal is complete, blocked, budget-limited, or approval-gated.

## #CORE IDEA
Every loop has three phases:

```text
RUN → CHECK → DECIDE → repeat
```

A loop is not a stage. It is the engine inside the agent.

## #WHEN TO USE
Use this skill when:
- the user says continue, loop, automate, keep going, run until done, monitor, weekly check-in, monthly audit, or autonomous workflow
- a workflow requires batches, retries, rescans, monitoring, or recurring decisions
- the next step should be chosen from current project state rather than user instruction
- a skill result needs verification before continuing
- a project goal needs several skills chained together

## #LOOP TYPES

### Project operating loop
Goal: keep the active SEO project moving.
Typical sequence:
`project-orchestrator → keyword-opportunity-miner → baseline-rank-position-tracker → site-architecture-mapper → sitemap-keyword-linking-auditor → page-checklist-manager → diagnostics/optimization/internal links/backlinks/reporting`.

### Ranking improvement loop
Goal: move a target keyword/page toward top 10/top 3.
Run diagnostics, fix on-page/internal links, check rank baseline, decide whether backlinks/outreach are needed, then monitor.

### Internal linking loop
Goal: map and implement contextual links safely.
Run architecture map, keyword linking audit, review, draft CMS/internal link changes, verify, report.

### Content refresh / optimization loop
Goal: improve page quality using On-Page.ai evidence.
Run scan, edit draft/approved changes, rescan when required, stop when score/readability/approval criteria are met.

### Outreach loop
Goal: create and manage backlink outreach pipeline.
Prospect, qualify, review, approve, draft/send through Gmail only if approved, check replies, update status.

### Reporting loop
Goal: report progress and decide next moves.
Pull DataForSEO/GSC/GA4/conversion data, compare to baseline, summarize work done, decide next actions.

## #LOOP STATE
Before starting or continuing a loop, create/load a loop state file:

```text
07-queue/loops/{{loop_id}}.md
```

Also update machine-readable state when useful:

```text
08-tracking/loops/{{loop_id}}.json
```

Use `templates/loop-state.md`.

## #RUN PHASE
1. Load active project profile, approval rules, current queue, last daily note, and relevant tracking files.
2. Identify the current loop goal and success criteria.
3. Choose exactly one next skill to run unless a batch is explicitly safe.
4. Run that skill according to its `SKILL.md`.
5. Save the result or checkpoint to Obsidian.
6. Never make irreversible/public changes unless approval rules allow it.

## #CHECK PHASE
Evaluate the result using real signals:
- Was the expected artifact produced?
- Did the skill report success, partial success, blocked, or failure?
- Did reviewer approve it?
- Did metrics move, or is the measurement window still pending?
- Did we create new blockers, access gaps, or approval requirements?
- Are counts/checkpoints internally consistent?
- Is there enough evidence to continue?

## #DECIDE PHASE
Choose one next state:

- `continue`: run the next skill or next batch
- `retry`: repeat current skill with adjusted inputs, max retry policy applies
- `wait`: measurement window, user approval, crawl job, scan job, or external dependency pending
- `escalate`: ask the approver for a decision/access/approval
- `complete`: success criteria met
- `blocked`: cannot continue without external change
- `stop_budget`: token/tool/time/credit budget reached

Every decision must include:
- reason
- evidence
- next skill or next wait condition
- stop condition checked

## #STOP CONDITIONS
Stop the loop when any is true:
- success criteria are met
- approver approval is required
- missing access/secret/tool blocks progress
- reviewer rejects output
- page is at risk of over-optimization or quality damage
- no safe next action exists
- budget/credit/token/time cap reached
- same blocker occurs 3 consecutive times
- measurement window must pass before more action

## #DEFAULT RETRY POLICY
- Max 2 retries for the same skill/input.
- Max 1 extra tuning loop for content quality unless the source skill allows more.
- Never keep adding entities, links, or outreach just to satisfy a metric.
- If retry would reduce quality or increase risk, stop and report.

## #APPROVAL GATES
Always stop and escalate before:
- publishing public content
- sending outreach emails
- editing money pages if rules require approval
- redirects/canonicals/deletions
- GBP changes
- destructive CMS changes
- changing project approval rules

## #OUTPUTS
Every loop iteration writes:
- loop state update to `07-queue/loops/{{loop_id}}.md`
- machine-readable snapshot to `08-tracking/loops/{{loop_id}}.json` if useful
- daily note summary to `99-daily/YYYY-MM-DD.md`
- tasks/checklists/reports to the relevant skill folders

## #REPORT
Use `templates/loop-state.md` for loop state and `templates/loop-report.md` for summaries.

## #SUCCESS
Successful when the agent can continue a project autonomously, select the next best skill based on real state, stop on real signals instead of vibes, and preserve a resumable audit trail in Obsidian.
