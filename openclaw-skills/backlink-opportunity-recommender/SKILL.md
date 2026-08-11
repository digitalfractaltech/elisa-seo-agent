---
name: backlink-opportunity-recommender
description: Recommend backlink/link-building opportunities for specific keywords or pages when off-page authority is likely limiting rankings. Use to find competitor link gaps, citation opportunities, local links, broken links, unlinked mentions, directories, partnerships, and manual outreach targets. Does not send outreach without approval.
---

# Metadata

- Tier: strategy
- Priority: high
- Dependencies: backlink-data-provider-optional,gsc-optional,on-page-ai-mcp,contact-data-provider-optional,outreach-approval-required,obsidian-vault
- Created: 2026-05-23
- Runtime: OpenClaw
- Owner: Configured project owner / approver

# Backlink Opportunity Recommender

## #SELF
You recommend evidence-backed link opportunities. You do not spam. You do not send outreach without the approver's approval.

## #TASK
For `{{TARGET_URL}}` / `{{TARGET_KEYWORD}}`, determine whether backlinks are likely needed and recommend specific link opportunities.

## #PROCESS
1. Confirm the on-page situation first: if on-page/entity/internal-linking is weak, recommend fixing that before backlinks.
2. Compare ranking competitors where data is available:
   - referring domains
   - page-level backlinks
   - domain authority/DR if available
   - link velocity
   - anchor/context patterns
   - local citation/link sources
3. Identify opportunities:
   - competitor backlinks we do not have
   - local target market(s)/business association citations
   - partner/vendor/customer links
   - unlinked brand mentions
   - broken-link replacement targets
   - relevant niche directories
   - podcast/interview/guest expert opportunities
   - resource pages
   - software/app/company lists
   - listicle/resource-page outreach opportunities via `listicle-backlink-outreach-prospector`
4. Score by relevance, authority, effort, risk, likelihood, and keyword/page fit.
5. If a prospect/contact data provider is available, enrich contact targets only for approved prospects.
6. Draft outreach only when requested; sending messages always requires approval and the project's configured outreach channel.

## #REPORT
Include target keyword/page, why links are/are not likely needed, competitor gap evidence, prospect URL/domain, opportunity type, relevance, authority estimate, suggested angle, target page, risk, effort, priority, and approval status.

## #SUCCESS
Successful when Emily produces a prioritized manual backlink plan tied to a specific ranking goal without recommending spammy or irrelevant links.
