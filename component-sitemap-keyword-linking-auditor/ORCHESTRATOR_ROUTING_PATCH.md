# Optional Project Orchestrator Routing Patch

Add this skill after `site-architecture-mapper` and before `page-checklist-manager` in the operating loop.

Recommended loop segment:

```text
4. Invoke `site-architecture-mapper` to map hierarchy and content tiers.
5. Invoke `sitemap-keyword-linking-auditor` to catalogue existing keyword mentions and create an internal linking graph from actual page/post content.
6. Invoke `page-checklist-manager` to create/update page checklists.
7. Invoke diagnostic/on-page skills for pages needing work.
8. Invoke internal-link implementation skills only after mapping/review/approval.
```

Recommended recurring routing:

```text
- On project onboarding: run `keyword-opportunity-miner`, `baseline-rank-position-tracker`, `site-architecture-mapper`, then `sitemap-keyword-linking-auditor` before any sitewide link implementation.
- Monthly: rerun `sitemap-keyword-linking-auditor` for new/changed pages or the next sitemap range.
- After publishing/importing a meaningful batch of new posts/pages: rerun `site-architecture-mapper` lightweight update, then `sitemap-keyword-linking-auditor` for affected URLs.
```
