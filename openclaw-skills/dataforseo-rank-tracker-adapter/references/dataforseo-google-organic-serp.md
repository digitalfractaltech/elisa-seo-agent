# DataForSEO Google Organic SERP Reference

Use this only when implementing or validating the DataForSEO rank-tracking adapter.

## Useful docs

- Pricing page: https://dataforseo.com/pricing/serp/google-organic-serp-api
- Google SERP API overview: https://docs.dataforseo.com/v3/serp-google-overview/
- Pricing/depth FAQ: https://dataforseo.com/help-center/serp-api-pricing-depth-update-faq

## Core endpoint family

DataForSEO Google Organic SERP API supports Standard queue and Live modes. For scheduled Emily tracking, prefer Standard queue unless the project needs immediate results.

Common live advanced endpoint pattern:

```text
POST https://api.dataforseo.com/v3/serp/google/organic/live/advanced
```

Common task/queue pattern:

```text
POST https://api.dataforseo.com/v3/serp/google/organic/task_post
GET  https://api.dataforseo.com/v3/serp/google/organic/task_get/advanced/{task_id}
```

Confirm exact endpoint/method against current DataForSEO docs before implementation.

## Required request concepts

- `keyword`
- `location_name` or location code
- `language_code`
- `device`
- `os`
- `depth` or `max_crawl_pages`

## Ranking fields

- `rank_absolute`: absolute position in the returned SERP sequence.
- `rank_group`: position within a group/type, such as organic results.

For Emily reports, store both. Use organic-result matching for “organic rank” when available.

## Cost/depth notes

Current pricing charges the first page of 10 results at the base rate and additional SERP pages at a discounted rate. Top 100 checks require `depth: 100` or `max_crawl_pages: 10`, which costs more than top 10 checks.

## Matching project URLs

Match against:
- canonical project domain
- approved alternate domains/subdomains
- normalized URLs without protocol/trailing slash when comparing

Flag:
- not found within checked depth
- multiple project URLs for one keyword
- ranking URL differs from intended URL
- device/location mismatch from baseline
