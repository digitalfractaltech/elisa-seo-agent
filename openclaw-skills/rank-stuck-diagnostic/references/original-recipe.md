# Original Recipe Reference

Source: On-Page.ai guide, recipe: 11. Advanced Page Diagnostic: Why Is This Page Not Ranking?

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF
You are performing SEO diagnostic work. You will need to build a detailed task list of the steps in order to complete your SEO diagnostic work. Continue until the task list is complete.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, read the target page, create reports, etc.
#TASK
Perform a deep SEO diagnostic on the URL: "
https://www.yoursite.com/url/
" for the keyword: "keyword"
The goal is to determine why this page isn't ranking to it's full potential.
#DIAGNOSTIC PROCESS
1. Start by performing a deep SEO scan using the on-page-seo tool on the target URL.
2. Then read the MCP resources from the on-page-seo tool.
3. While the scan is running, verify and read the target URL page.
4. Before diagnosing content issues, check for technical / indexability issues that could prevent the page from ranking.
Additionally, check:
- Check the HTTP status code of the target URL. Confirm whether it returns 200, redirects, 404, 5xx, or anything unusual.
- Check if there is a redirect chain.
- Check if the page canonical points to itself or to another URL.
- Check if the page has a meta robots tag with noindex, nofollow, none, nosnippet, or any other directive that may affect indexing / ranking.
- Check if the HTTP headers contain an X-Robots-Tag with noindex, nofollow, none, nosnippet, or any other directive that may affect indexing / ranking.
- Check the robots.txt file to see if the target URL is blocked.
- Check the robots.txt file to see if important resources needed to render the page are blocked.
- Check whether the target URL appears in the sitemap, if a sitemap is available.
- Check if the main content is visible when reading / rendering the page.
- Check if the page requires login, geo access, cookies, or has a popup / overlay that blocks the main content.
- Check if the page has duplicate / near-duplicate pages on the same site targeting the same keyword or same search intent.
- Check if there are obvious canonicalization, duplicate content, or cannibalization issues.
- Check if structured data / schema is present if it would be expected for this page type.
5. When the on-page-seo scan completes, go through each section sequentially, identifying the biggest issues preventing the page from ranking to its full potential.
Additionally,
- Check to see if partial keyword is mentioned in the title / content. How does the title/H1 line up with the keyword? It shouldn't be the exact keyword but it should be related.
- Check for search intent alignment. What type of page is Google rewarding for this keyword? Article, product page, category page, homepage, local page, tool, comparison page, etc.
- Check for keyword stuffing issues.
- Check for excessive entity over-usage when compared to competitors.
- Check whether the page is missing important entities with importance 9, 10, and Highly Related Words.
- Check whether the related_important entity score is lower than the competition.
- Check for proper sub-headline usage (H1, H2, H3) according to the report. Not too many H1s, at least one useful H2.
- Check for excessively thin content (sub-450 words)
- Check word count versus competition.
- Check for outdated sections.
- Check the speed benchmark section of the report for TTFB and CLS issues. If the TTFB is too high, the page might struggle to rank. If CLS is materially above 0 or worse than competitors, this might also be associated with ranking issues.
- Check to see if the page has internal links pointing back to it and it's not an orphan page.
- Check internal link opportunities if available.
- Verify that the Google category for our content aligns with the top 3 competitors on Google. If drastically different, there might be an issue.
- Check any obvious issue from the report that may be holding the page back.
6. Identify the top 1, 2 or 3 biggest issues preventing the page from ranking to it's full potential. Not specified how many issues because it will vary.
7. Do not edit the page. Do not fix the page. Do not add entities. Do not add internal links. Do not change the title. This is diagnostic only.
#DIAGNOSTIC OUTPUT
8. For each major issue found, explain:
- what the issue is
- what the on-page-seo scan shows
- what you verified on the target page
- why this issue might be preventing the page from ranking
- how serious the issue is
- what should be done to fix it
Use priority levels:
- Critical
- High
- Medium
- Low
9. If the page has many small issues, group them together instead of listing every tiny issue. Focus on the top 1-3 issues that are most likely holding the page back.
10. If everything checks out on the page, say that clearly. If indexability, on-page, content, entity, speed, headings, internal links and category alignment all look fine, then explain that it's likely domain / link issues or outside-page factors.
#REPORT
Produce a simple diagnostic report.
The report should include:
- target URL
- keyword / topic used for the scan
- deep scan status
- top 1-3 issues found
- HTTP status code
- redirect chain issues, yes/no
- robots.txt blocking issues, yes/no
- meta robots noindex / nofollow issues, yes/no
- X-Robots-Tag issues, yes/no
- canonical tag issue, yes/no
- sitemap inclusion, yes/no / unknown
- rendered main content visible, yes/no
- structured data / schema issues, if applicable
- duplicate / cannibalization issue, yes/no
- search intent alignment
- title / H1 alignment
- keyword stuffing issues, yes/no
- entity over-usage issues, yes/no
- missing importance 9 / 10 entities
- missing Highly Related Words
- related_important entity score compared to competition
- word count / content length compared to competition
- sub-headline / heading issues
- outdated sections
- speed benchmark issues
- TTFB issues
- CLS issues
- internal link / orphan page issues
- Google category alignment with top 3 competitors
- likely reason the page is not ranking to it's full potential
- recommended fixes
- whether the issue appears to be indexability, technical, on-page, internal linking, content, entity-related, category-related, cannibalization-related, speed-related, or likely domain / link related
#SUCCESS
You will be successful when you have performed a deep SEO diagnostic, checked technical / indexability issues, gone through the on-page-seo report sequentially, identified the top 1-3 biggest issues preventing the page from ranking to it's full potential, explained the likely fixes, and clearly stated whether the issue appears to be indexability, technical, on-page, internal linking, content, entity-related, category-related, cannibalization-related, speed-related, or likely domain / link related.
