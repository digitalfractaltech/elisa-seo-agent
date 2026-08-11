# Original Recipe Reference

Source: On-Page.ai guide, recipe: 2. Site Wide Internal Links

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF You are performing SEO internal linking work. You will need to build a detailed task list of the steps in order to complete your SEO internal linking work. Continue until the task list is complete.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, edit the target pages, create reports, write scripts, execute scripts, etc.
#TASK
Build internal links across the entire site using the sitemap:
"https://www.yoursite.com/sitemap_index.xml"
NOTE: Do not try to process the entire site in one giant run. Instead, first, build a lightweight manifest of all URLs that look like eligible posts & pages based on sitemap URLs and obvious URL-pattern exclusions. Then process ONLY the selected page range for this initial run. (Do not fetch, read, scan, or extract content from all sitemap URLs while building the manifest. Only fetch/read/scan target pages in the current batch and source pages suggested by the on-page-seo scan.)
For this initial run, process manifest pages from: [1-75]
(Later, when I eventually say "continue and now do pages x", we'll load the existing manifest and continue from that page range. (Plan for this but don't do it yet). Do not rebuild or re-order the manifest unless I specifically ask you to.)
#PROCESS
1. First, write a "runner" script that pulls the full sitemap, parses all child sitemaps and creates a lightweight manifest of all URLs that look like eligible posts & pages based on sitemap URLs and obvious URL-pattern exclusions.
2. We want the script to create the manifest of the URLs to process. In the manifest, include:
- manifest position / page number
- target URL
- scan status
- source pages suggested
- source pages checked
- links added, including source URL, target URL and anchor text
- skipped reason
- final verification status
- current run status
- cumulative status across all runs
3. Then save the manifest in this directory so that if the process gets interrupted for any reason, we can continue and resume from where it left off.
Important:
- The manifest order is the source of truth.
- Page range 1-250 means manifest positions 1 through 250.
- Page range 251-1000 means manifest positions 251 through 1000.
- Do not re-order the manifest between runs.
- Do not duplicate links that were already added in previous runs.
4. The script / runner should process the selected page range in batches:
a) Take the next 10 pending target pages from the selected page range
b) Run the on-page standard scans for those pages
c) Keep a maximum of 5 scans running at once
d) Wait for the on-page scans to complete
e) Add the internal links suggested from the internal link opportunities suggested section. You will need to edit the pages.
f) Verify links were added
g) Save and update progress in the manifest
h) Move to the next batch
5. If for any reason the MCP connector cannot be called directly from the script, then use the script for the sitemap extraction, manifest, batching, tracking and reporting, and use the on-page-seo MCP connector manually inside this agent session for each URL in the batch. Update the manifest after each page.
6. Do not start the next batch until the current batch is scanned, processed, verified, and saved.
#BATCH SETTINGS
Total target pages to process this run: [75]
Page range to process this run: [1-75]
Batch size: [10]
Max scans running at once: [5]
Max internal links to add per target page: [3]
Max source pages to check per target page: [3]
Max total internal links to add this run: [750]
Manifest file: sitename-internal-linking-manifest.json
Report file: sitename-internal-linking-report.html
## Source page pool:
When it comes to building links, you may use ALL eligible content pages from the full manifest as possible source pages (not only the current batch). The current batch is only the list of target pages we are trying to build links TO. (However, do not manually inspect all source pages from the manifest. Use the source pages suggested by the on-page-seo standard scan, then check only those suggested source pages.)
## Exclude obvious non-content pages, we don't want to build links here:
- category pages
- tag pages
- author pages
- search pages
- archive pages
- cart / checkout pages
- login pages
- paginated pages
- terms of service pages, privacy policy, maps / contact us pages.
#RESUME / CONTINUE PROCESS
The manifest should be built in a way that supports resuming and continuing. If a manifest already exists:
- Load the existing manifest
(Do not rebuild it unless I specifically ask you to and do not re-order it)
- Continue from the requested page range
- Preserve previous scan statuses, source pages checked, links added, skipped reasons and verification status
- Skip pages that are already completed unless I specifically ask you to re-process them
- Continue with the next pending page in the requested range
#INTERNAL LINKING PROCESS
1. For each target page in the current batch, you'll have to determine the best keyword to use for the on-page standard scan. (You have to infer it from the page title, H1, URL slug, and content.)
2. Then for each target page, run an on-page standard scan using the on-page-seo tool.
3. When the on-page-seo scan completes, within the report, you'll have the 3 pages with most relevance for internal links.
4. For each of the 3 suggested internal link source pages, check them to see if they are already present and/or linking from the main content.
##When you receive an on-page standard scan report:
- Verify that the suggested source page has main content. ie: it's not a category page, tag page, search page, author page, archive page, etc. If that type of page is suggested, then we just skip/ignore that internal link recommendation.
- Verify that the source page does not already link to the target page from the main content.
(If the source page already links to the target page from the main content, mark it as already done and move to the next one.)
- If the source page does not have useful main content, skip it and note the reason in the report.
- If the source page is relevant, has main content, and is not already linking to the target page, then perform a minor edit the text to seamlessly add a natural anchor text link within the main content. (The anchor text should be chosen naturally based on the sentence and surrounding paragraph.)
- Prefer links inside the actual article / page content, not menus, sidebars, footers, related post boxes, etc.
- In the event that you cannot add a natural link because the content is completely irrelevant, then note it in the manifest and the final report.
5. For each target, you'll want to create up to 3 seamless contextual internal links.
6. In the event that a same source page is suggested multiple times, keep track of previous edits so that we don't edit the same page in a messy way.
7. If a target page has no good internal link opportunities (nothing was returned in the standard on-page scan or no good / valid links were in the scan), note it in the report.
8. Continue going through the batch until each target page in the current batch has been processed.
9. When you complete the current batch, save the manifest, update the report, then move to the next batch until you've processed the pre-determined amount of URLs this run.
#VERIFICATION
10. Once internal links have been added, verify each edited source page and confirm that the internal link exists in the main content.
11. Verify that each target URL received the correct number of internal links, up to 3 where possible.
12. Verify that the batch was saved before continuing.
13. If any task cannot be completed due to access, environment, permissions, missing tools, no main content, already existing links, unavailable data or failed scans. Note it in the final report.
14. Produce a full HTML report file of the changes. Provide an audit trail within the report of the changes you made.
#REPORT
The final HTML report should include:
- sitemap used
- total URLs pulled from sitemap
- total eligible URLs in the manifest
- page range processed in this run
- total target pages selected in this run
- batch size used
- number of batches processed
- total target pages processed
- total standard scans performed
- total source pages checked
- total internal links added
- total pages skipped
- target URL
- manifest position / page number
- keyword / topic used for the scan
- suggested source pages from the on-page-seo scan
- source pages checked
- anchor text used
- final source URL
- final target URL
- skipped pages
- failed scans
- access issues
- completed page ranges
- next recommended page range to process
- complete audit trail
#SUCCESS
You will be successful when all the target pages in the selected page range have been processed in controlled batches, all possible seamless contextual internal links have been added from relevant source pages, all skipped items have been explained, the manifest has been saved, and you have produced a complete HTML report outlining the changes, justifications, source URLs, target URLs, anchor text used and have provided an audit trail.
