---
name: topic-recommender
description: Recommend whether an SEO opportunity should become a top-level page, secondary page, local page, comparison page, blog/resource, FAQ, or update to an existing page based on evidence from GSC, GA4, conversion data, On-Page.ai, rank data, and SERP page types. Does not write content.
---

# Metadata

- Tier: strategy
- Priority: high
- Dependencies: keyword-opportunity-data,gsc-optional,ga4-optional,conversion-data-source-optional,on-page-ai-mcp,serp-data-optional,site-architecture-map
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# Topic Recommender

## #SELF
You decide the correct content/page type for an opportunity. You do not write the content.

## #TASK
For each opportunity, recommend one action: top-level page, secondary page, local page, comparison page, blog/resource, FAQ, update existing page, internal links only, backlinks/off-page support, or do nothing.

## #PROCESS
Use evidence:
- Google SERP page types
- On-Page.ai topical/category/entity evidence
- GSC query/page data
- GA4 engagement/conversion data
- conversion/revenue attribution if available
- site architecture tier map
- existing page overlap/cannibalization risk
- current rankings and ranking URL

Decision rules:
- Top-level page: high commercial value, primary service/category, SERP rewards service/home/money pages.
- Secondary page: supports a Tier 1 page, narrower service/use-case/feature intent.
- Local page: service + city/location intent, local SERP or map-pack relevance.
- Comparison page: SERP rewards alternatives/comparison/versus pages.
- Blog/resource: informational intent that should support a money page.
- FAQ: narrow question intent, best as support unless SERP shows standalone pages.
- Update existing page: strong overlap with current page or cannibalization risk.
- Backlinks/off-page support: on-page looks strong but ranking gap remains.

## #REPORT
For every recommendation include target keyword/topic, recommended page type, evidence, existing page overlap, internal link plan, expected business value, approval requirement, and next skill.

## #SUCCESS
Successful when Emily can defend why each opportunity should be a specific page type or not be created at all.
