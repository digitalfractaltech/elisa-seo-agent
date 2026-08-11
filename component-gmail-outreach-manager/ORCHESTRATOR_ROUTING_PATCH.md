# Optional Project Orchestrator Routing Patch

Add Gmail/outreach channel status to onboarding if outreach sending/response tracking is desired.

Add this routing rule:

```text
Invoke `gmail-outreach-manager` only for approved send/response tracking batches after `listicle-backlink-outreach-prospector` and reviewer approval.
```

Recommended backlink/outreach chain:

```text
backlink-opportunity-recommender
→ listicle-backlink-outreach-prospector
→ reviewer
→ approver approval
→ gmail-outreach-manager
→ performance-tracker-reporter
```
