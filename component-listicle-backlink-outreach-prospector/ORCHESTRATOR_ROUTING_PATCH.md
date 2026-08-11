# Optional Project Orchestrator Routing Patch

Add this routing rule:

```text
Invoke `backlink-opportunity-recommender` when ranking need appears off-page/link-related; invoke `listicle-backlink-outreach-prospector` when the opportunity type is listicles, resource pages, roundups, or editorial outreach.
```

Recurring use:

```text
- When a priority page is on-page/internal-link ready but still authority-limited: run `backlink-opportunity-recommender`.
- If listicle/resource-page outreach is appropriate: run `listicle-backlink-outreach-prospector`.
- Outreach sending remains approval-gated.
```
