# Original Recipe Reference

Source: On-Page.ai guide, recipe: 8. Standard Optimization, Site Wide

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF You are performing SEO work.
You will need to build a detailed task list of the steps in order to complete your SEO optimization work. Continue until the task list is complete.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, edit the target pages, create reports, write scripts, execute scripts, etc.
#TASK
Perform a standard SEO optimization refresh across the site using the sitemap: "
https://www.yoursite.com/yoursitemap.xml
". Build the manifest using the sitemap's last modified dates, sorted oldest first, so posts / pages that have not been modified in the longest time are optimized before newer posts / pages.
NOTE: Do not try to process the entire site in one giant run. Instead, first, build a lightweight manifest of all URLs that look like eligible posts & pages based on sitemap URLs, sitemap last modified dates and obvious URL-pattern exclusions. Then process ONLY the selected page range for this initial run. (Do not fetch, read, scan, or extract content from all sitemap URLs while building the manifest. Only fetch/read/scan target pages in the current batch.)
For this initial run, process manifest pages from: [1-10]
(Later, when I eventually say "continue and now do pages x", we'll load the existing manifest and continue from that page range. (Plan for this but don't do it yet). Do not rebuild or re-order the manifest unless I specifically ask you to.)
#PROCESS
1. First, write a "runner" script that pulls the full sitemap, parses all child sitemaps, reads the URL and last modified date from the sitemap, then creates a lightweight manifest of all URLs that look like eligible posts & pages based on sitemap URLs and obvious URL-pattern exclusions. Sort the manifest by last modified date, oldest first.
2. We want the script to create the manifest of the URLs to process. In the manifest, include:
- manifest position / page number
- last modified date from sitemap
- target URL
- scan status
- keyword / topic used for the scan
- biggest issues found
- outdated sections updated or flagged
- keyword stuffing / entity over-usage issues found
- entities added
- Highly Related Words added
- important terms considered but not added
- sub-headlines changed, yes/no
- image added, yes/no
- image alt-text updated, yes/no
- Google category alignment with top 3 competitors
- before and after related_important entity score
- whether related_important is higher than the competition
- re-scans performed
- remaining blockers
- skipped reason
- final verification status
- current run status
- cumulative status across all runs
The manifest fields can remain empty until each page is actually processed. Do not fetch/read/scan all pages just to fill in the manifest.
3. Then save the manifest in this directory so that if the process gets interrupted for any reason, we can continue and resume from where it left off.
Important:
- The manifest order is the source of truth.
- Page range 1-10 means manifest positions 1 through 10.
- Page range 11-20 means manifest positions 11 through 20.
- Do not re-order the manifest between runs.
- Do not fetch/read/scan all pages just to build the manifest.
- Only fetch/read/scan the target pages in the current batch.
- Sort the manifest by the sitemap's last modified date, oldest first.
- If a URL does not have a last modified date in the sitemap, keep it after the dated URLs and preserve sitemap order for those URLs.
4. The script / runner should process the selected page range in batches:
a) Take the next 5 pending target pages from the selected page range
b) Run the on-page Standard scans for those pages
c) Keep a maximum of 3 scans running at once
d) Wait for the on-page scans to complete
e) Go through the Standard scan report sequentially
f) Determine the biggest issues on each page preventing it from ranking to it's full potential
g) Resolve the issue(s) found in the Standard scan report
h) Re-scan with a Standard scan to make sure that the related_important entity score is higher than the competition
i) If needed, perform the tuning loop a maximum of 2 times
j) Save and update progress in the manifest
k) Move to the next batch
5. If for any reason the MCP connector cannot be called directly from the script, then use the script for the sitemap extraction, manifest, batching, tracking and reporting, and use the on-page-seo MCP connector manually inside this agent session for each URL in the batch. Update the manifest after each page. Do not update pages without the guidance of the on-page-seo report.
6. Do not start the next batch until the current batch is scanned, processed, verified, and saved.
#BATCH SETTINGS
Total target pages to process this run: [10]
Page range to process this run: [1-10]
Batch size: [5]
Max scans running at once: [3]
Scan type: [Standard Scan]
Max related_important tuning loops per page: [2]
Max generated images to add per page: [3]
Manifest file: sitename-standard-optimization-manifest.json
Report file: sitename-standard-optimization-report.html
## Exclude obvious non-content pages, we don't want to optimize these:
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
- Preserve previous scan statuses, entities added, Highly Related Words added, image alt-text updates, generated images, related_important scores, re-scans performed, skipped reasons and verification status
- Skip pages that are already completed unless I specifically ask you to re-process them
- Continue with the next pending page in the requested range
#STANDARD OPTIMIZATION PROCESS
1. For each target page in the current batch, you'll have to determine the best keyword to use for the on-page Standard scan. (You have to infer it from the page title, H1, URL slug, and content.)
2. Then for each target page, run an on-page Standard scan using the on-page-seo tool.
3. When the on-page-seo Standard scan completes, go through the report sequentially and determine the biggest issues on the page preventing it from ranking to it's full potential.
Additionally, check:
- outdated content
- keyword stuffing issues
- excessive entity over-usage when compared to competitors
- proper sub-headline usage (H1, H2, H3) according to the report
- content length / word count compared to the competition
- image alt-text issues if available
- internal link opportunities if available
- Google category alignment compared to the top 3 competitors
- any obvious issue from the report that may be holding the page back
4. If there is outdated content, research the latest information where possible.
If there are outdated sections that conflict with the user intent, you may:
- update stale dates, examples, screenshots, claims, or sections
- However you may only add facts that are verifiable from available sources
- In the event that current research is required and browsing is unavailable, flag the section for human review instead of inventing facts.
5. Resolve the issue(s) found in the Standard scan report.
6. Add an appropriate quantity of entities with importance 7, 8, 9, 10 and 'Highly Related Words' naturally into the text. Light edits, preserve as much human text as possible. (Do not touch title). Preserve paragraphs and line breaks. Prefer sentence level edits over full rewrites.
7. If an important term cannot be added naturally without hurting readability, list it in the final report as “not added” with the reason.
8. Preserve the human writing as much as possible. Preserve the title. Preserve the slug. Preserve the structure unless there is an obvious issue.
9. Verify that the sub-headlines are relevant to the topic / search intent, verify that each sub-headline contains at least 1 entity.
If the sub-headlines are relevant and contain at least 1 entity from the important entity list, do not change them. Leave the sub-headlines as-is unless there are issues.
If there are no useful H2 sub-headlines, refer to the on-page-seo scan report to see if you should add any.
10. Verify that all the images have appropriate alt-text with entities inside them where natural.
11. If an image has missing or weak alt-text, update the alt-text so that it is descriptive and relevant to the page topic. Use entities where natural.
12. Verify that the Google category for our content aligns with the top 3 competitors on Google. If drastically different, there might be an issue.
If the category is drastically different, do not force a rewrite. Note the issue in the final report and make only natural changes that help the page better align with the search intent.
13. If appropriate, use your built-in image generator (Codex has a built in image generator) to add up to 3 new generated images where appropriate within the content if the environment supports it. This helps if the page is low on images and it helps to break up long blocks of text.
The images should:
- fit naturally into the existing page
- support the topic / search intent
- include appropriate alt-text with entities where natural
- improve the page instead of feeling randomly added
- they should be spaced out and not immediately follow another image
14. If the content is thin when compared to the average, add a new paragraph or small section of text where appropriate.
If applicable, the new text should:
- fit naturally into the existing page
- include missing importance 7, 8, 9 / 10 entities or Highly Related Words where natural
- add useful information to the reader
15. In the event that the page is too thin, broken, irrelevant, or cannot be optimized naturally, note it in the manifest and the final report.
#VERIFICATION
16. Once the standard optimization edits have been made, re-scan with a Standard scan to make sure that the related_important entity score from the on-page-seo report is higher than the competition.
17. If the related_important entity score is not higher than the competition, add more of the top entities, importance 7, 8, 9, 10 into the text in a natural fashion. Re-scan after completion.
Continue this process a maximum of 2 times until the related_important entity score is higher than the competition, or until you cannot add more entities naturally without hurting readability. (Do not change title. Preserve as much human text as possible. Do not add an FAQ.). We want to go above and beyond what competitors are doing.
18. Once the standard optimization edits have been made, verify:
- The original title was preserved.
- The original slug was preserved.
- The structure was preserved unless there was an obvious issue.
- Paragraphs and line breaks were preserved.
- The page still reads naturally.
- The human writing was preserved as much as possible.
- Entities with importance 7, 8, 9 / 10 were added naturally where possible.
- Highly Related Words were added naturally where possible.
- The related_important entity score is higher than the competition, or the remaining blocker is explained.
- The sub-headlines are relevant to the topic / search intent.
- The sub-headlines contain important entities where appropriate.
- Image alt-text was checked and updated if necessary.
- Up to 3 generated images were added if appropriate, or the reason they were not added is explained.
- The Google category aligns with the top 3 competitors, or the mismatch is explained.
- Outdated content was updated where possible.
- The page was not broken during editing.
- The manifest was updated after the edit.
19. Verify that the batch was saved before continuing.
20. If any task cannot be completed due to access, environment, permissions, missing tools, unavailable data, failed scan, image generation not being available, not enough credits for re-scan, or the page not being a good fit for standard optimization. Note it in the final report.
21. Produce a full HTML report file of the changes. Provide an audit trail within the report of the changes you made.
#REPORT
The final HTML report should include:
- sitemap used
- page range processed in this run
- total target pages processed
- total Standard scans performed
- total re-scans performed
- total pages optimized
- total pages skipped
- target URL
- manifest position / page number
- last modified date from sitemap
- keyword / topic used for the scan
- Standard scan status
- biggest issues found in the report
- outdated sections updated or flagged
- keyword stuffing / entity over-usage issues found
- entities added
- Highly Related Words added
- important terms considered but not added
- sub-headlines changed, yes/no
- image added, yes/no
- image alt-text updated, yes/no
- Google category alignment with top 3 competitors
- before and after related_important entity score
- whether related_important is higher than the competition
- re-scans performed
- remaining blockers
- skipped pages
- access issues
- completed page range
- next recommended page range to process
- audit trail
#SUCCESS
You will be successful when all the target pages in the selected page range have been processed in controlled batches, the biggest issues from the Standard scan have been identified and resolved where possible, all possible standard optimization improvements have been added naturally, the related_important entity score is higher than the competition or the remaining blocker is explained, all skipped items have been explained, the manifest has been saved, and you have produced a full HTML report outlining the changes, justifications, entities added, Highly Related Words added, image / alt-text updates, before and after related_important score and have provided an audit trail.
