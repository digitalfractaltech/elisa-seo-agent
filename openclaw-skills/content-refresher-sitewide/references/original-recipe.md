# Original Recipe Reference

Source: On-Page.ai guide, recipe: 5. Site Wide Refresh for Old or Stale Pages

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF You are performing light SEO work.
You will need to build a detailed task list of the steps in order to complete your work. Continue until the task list is complete.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, edit the target pages, create reports, write scripts, execute scripts, etc.
#TASK
Perform a light SEO refresh on each page of the site using the sitemap: "
https://www.yoursite.com.com/sitemap_index.xml
".
Build the manifest using the sitemap's last modified dates, sorted oldest first, so posts / pages that have not been modified in the longest time are refreshed before newer posts / pages.
NOTE: Do not try to process the entire site in one giant run. Instead, first, build a lightweight manifest of all URLs that look like eligible posts & pages based on sitemap URLs and obvious URL-pattern exclusions. Then process ONLY the selected page range for this initial run. (Do not fetch, read, scan, or extract content from all sitemap URLs while building the manifest. Only fetch/read/scan target pages in the current batch.)
For this initial run, process manifest pages from: [1-10]
(Later, when I eventually say "continue and now do pages x", we'll load the existing manifest and continue from that page range. (Plan for this but don't do it yet). Do not rebuild or re-order the manifest unless I specifically ask you to.)
#PROCESS
1. 1. First, write a "runner" script that pulls the full sitemap, parses all child sitemaps, reads the URL and last modified date from the sitemap, then creates a lightweight manifest of all URLs that look like eligible posts & pages based on sitemap URLs and obvious URL-pattern exclusions. Sort the manifest by last modified date, oldest first.
2. We want the script to create the manifest of the URLs to process. In the manifest, include:
- manifest position / page number
- last modified date from sitemap
- target URL
- scan status
- entities added
- highly related words added
- short paragraph added
- image alt-text updated
- image added
- skipped reason
- final verification status
- current run status
- cumulative status across all runs
3. Then save the manifest in this directory so that if the process gets interrupted for any reason, we can continue and resume from where it left off.
Important:
- The manifest order is the source of truth.
- Page range 1-20 means manifest positions 1 through 20.
- Page range 21-40 means manifest positions 21 through 40.
- Do not re-order the manifest between runs.
- Do not fetch/read/scan all pages just to build the manifest.
- Only fetch/read/scan the target pages in the current batch.
- Sort the manifest by the sitemap's last modified date, oldest first.
- If a URL does not have a last modified date in the sitemap, keep it after the dated URLs and preserve sitemap order for those URLs.
4. The script / runner should process the selected page range in batches:
a) Take the next 20 pending target pages from the selected page range
b) Run the on-page Lite scans for those pages
c) Keep a maximum of 5 scans running at once
d) Wait for the on-page scans to complete
e) Add an appropriate quantity of important entities and Highly Related Words naturally into the text
f) Verify image alt-text
g) Add one short paragraph only if the content is shorter than average / thin compared to the competition
h) Add one generated image where useful if using Codex and the environment supports it
i) Save and update progress in the manifest
5. If for any reason the MCP connector cannot be called directly from the script, then use the script for the sitemap extraction, manifest, batching, tracking and reporting, and use the on-page-seo MCP connector manually inside this agent session for each URL in the batch. Update the manifest after each page. Do not update pages without the guidance of the on-page-seo report.
#BATCH SETTINGS
Total target pages to process this run: [10]
Page range to process this run: [1-10]
Batch size: [10]
Max scans running at once: [5]
Scan type: [Lite Scan]
Max new paragraph additions per page: [1]
Max generated images to add per page: [1]
Manifest file: sitename-content-refresh-manifest.json
Report file: sitename-content-refresh-report.html
## Exclude obvious non-content pages, we don't want to refresh these:
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
- Preserve previous scan statuses, entities added, Highly Related Words added, image alt-text updates, short paragraph additions, skipped reasons and verification status
- Skip pages that are already completed unless I specifically ask you to re-process them
- Continue with the next pending page in the requested range
#CONTENT REFRESH PROCESS
1. For each target page in the current batch, you'll have to determine the best keyword to use for the on-page Lite scan. (You have to infer it from the page title, H1, URL slug, and content.)
2. Then for each target page, run an on-page Lite scan using the on-page-seo tool.
3. When the on-page-seo Lite scan completes, go through the entity data and identify:
- entities with importance 9
- entities with importance 10
- Highly Related Words
- content length / word count compared to the competition
- image alt-text issues if available
- any obvious outdated sections that conflict with user intent
4. Add an appropriate quantity of entities with importance 9, 10 and 'Highly Related Words' naturally into the text. Light edits, preserve as much human text as possible. (Do not touch title). Prefer sentence level edits over full rewrites.
5. If any term cannot be added naturally without hurting readability, list it in the final report as “not added” with the reason.
6. This is a light content refresh. Preserve the human writing as much as possible. Preserve the title. Preserve the slug. Preserve the structure unless there is an obvious issue.
7. If the content is shorter than average, add a maximum of one new short paragraph of text.
8. The new short paragraph should:
- fit naturally into the existing page
- include missing importance 9 / 10 entities or Highly Related Words where natural
- add useful information to the reader
- not be longer than needed
9. If the content is not shorter than average, do not add a new paragraph just to add one. Only add the entities and Highly Related Words naturally into the existing text.
10. Verify that all the images have appropriate alt-text with entities inside them where natural.
11. If an image has missing or weak alt-text, update the alt-text so that it is descriptive and relevant to the page topic. Use entities where natural.
12. If appropriate, use your built-in image generator (Codex has a built in image generator) to add one new generated image where appropriate within the content if the environment supports it.
13. If there are obvious outdated sections that conflict with the user intent, you may:
- update stale dates, examples, screenshots, claims, or sections
- However you may only add facts that are verifiable from available sources
- In the event that current research is required and browsing is unavailable, flag the section for human review instead of inventing facts.
14. In the event that a page is too thin, broken, irrelevant, or cannot be refreshed naturally, note it in the manifest and the final report.
15. Continue going through the batch until each target page in the current batch has been processed.
16. When you complete the current batch, save the manifest and update the report.
#VERIFICATION
Do not re-scan after editing. The initial Lite scan before editing is the only scan required for this light refresh process.
17. Once the light refresh edits have been made, verify:
- The original title was preserved.
- The original slug was preserved.
- The structure was preserved unless there was an obvious issue.
- The page still reads naturally.
- The human writing was preserved as much as possible.
- Importance 9 / 10 entities were added naturally where possible.
- Highly Related Words were added naturally where possible.
- The new short paragraph was only added if the page was shorter than average / thin compared to competition.
- Image alt-text was checked and updated if necessary.
- The page was not broken during editing.
- The manifest was updated after the edit.
18. If any task cannot be completed due to access, environment, permissions, missing tools, unavailable data, failed scans, image generation not being available, or the page not being a good fit for light refresh. Note it in the final report.
19. Produce a simple HTML report file of the changes. Provide an audit trail within the report of the changes you made.
#REPORT
The final HTML report should include:
- sitemap used
- page range processed in this run
- total target pages processed
- total Lite scans performed
- total pages refreshed
- total pages skipped
- target URL
- manifest position / page number
- keyword / topic used for the scan
- entities with importance 9 / 10 added
- Highly Related Words added
- short paragraph added, yes/no
- image added, yes/no
- image alt-text updated, yes/no
- skipped pages
- access issues
- completed page range
- next recommended page range to process
- audit trail
#SUCCESS
You will be successful when all the target pages in the selected page range have been processed in controlled batches, all possible light refresh improvements have been added naturally, all skipped items have been explained, the manifest has been saved, and you have produced a simple HTML report outlining the changes, entities added, Highly Related Words added, image / alt-text updates, short paragraphs added and have provided an audit trail."
