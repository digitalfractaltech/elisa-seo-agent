# Original Recipe Reference

Source: On-Page.ai guide, recipe: 14. Local Page Diagnostic: Why Is This Local Page Not Ranking?

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF You are performing local SEO diagnostic work. You will need to build a detailed task list of the steps in order to complete your local SEO diagnostic work. Continue until the task list is complete.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, read the target page, create reports, etc.
#TASK
Perform a deep local SEO diagnostic on the URL: "
https://www.yoursite.com/url/
" for the keyword: "
keyword
"
Target city / area: "
city / area
"
Business name: "
business name
"
Business type / service: "
business type / service
"
The goal is to determine why this local page isn't ranking to it's full potential.
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
- Check if the page has duplicate / near-duplicate pages on the same site targeting the same keyword, same city, same service, or same search intent.
- Check if there are obvious canonicalization, duplicate content, or cannibalization issues.
- Check if structured data / schema is present if it would be expected for this page type.
5. When the on-page-seo scan completes, go through each section sequentially, identifying the biggest issues preventing the page from ranking to its full potential.
Additionally,
- Check to see if partial keyword is mentioned in the title / content. How does the title/H1 line up with the keyword? It shouldn't be the exact keyword but it should be related.
- Check for local search intent alignment. What type of page is Google rewarding for this keyword? Local service page, homepage, location page, city page, product page, category page, article, directory, map pack / GBP result, etc.
- Check whether the page clearly targets the service + city / area.
- Check whether the city / area is naturally mentioned in the title, H1, intro, headings, body content, image alt-text, and internal anchors where appropriate.
- Check whether the service entity is clear.
- Check whether the page has local proof. Examples: local project examples, service area details, nearby areas served, local reviews / testimonials, local photos, business address, phone number, hours, license / certification, local case study, map, directions, or service process.
- Check whether NAP information is visible if this is a local business page. Name, address, phone.
- Check whether the phone number is visible and clickable if this is a local lead generation / service page.
- Check whether business hours are visible if relevant.
- Check whether the page clearly explains the service area if this is a service-area business.
- Check whether LocalBusiness schema or relevant local schema is present if appropriate.
- Check whether schema data matches the visible page content.
- Check whether the page supports the business category / service category.
- Check for keyword stuffing issues.
- Check for excessive entity over-usage when compared to competitors.
- Check whether the page is missing important entities with importance 9, 10, and Highly Related Words.
- Check whether the related_important entity score is lower than the competition.
- Check for proper sub-headline usage (H1, H2, H3) according to the report. Not too many H1s, at least one useful H2.
- Check whether sub-headlines support the local search intent.
- Check for excessively thin content (sub-450 words)
- Check word count versus competition.
- Check for outdated sections.
- Check the speed benchmark section of the report for TTFB and CLS issues. If the TTFB is too high, the page might struggle to rank. If CLS is materially above 0 or worse than competitors, this might also be associated with ranking issues.
- Check to see if the page has internal links pointing back to it and it's not an orphan page.
- Check internal link opportunities if available.
- Check whether important service pages, city pages, location pages, blog posts, or hub pages internally link to this local page.
- Verify that the Google category for our content aligns with the top 3 competitors on Google. If drastically different, there might be an issue.
- Check whether the top competitors are local business pages, directory pages, city/service pages, homepages, or informational pages.
- Check whether this looks like a website organic ranking issue, a GBP / map pack issue, a local prominence issue, or both.
- Check any obvious issue from the report that may be holding the page back.
6. If Google Business Profile information is available, check GBP / website alignment.
Additionally, check:
- Does the business name match the website?
- Does the phone number match the website?
- Does the address / service area match the website?
- Does the GBP primary category match the page topic?
- Do the GBP services match the services discussed on the page?
- Are important services in GBP missing from the page?
- Is the target page supporting the same service / category that GBP is targeting?
If GBP information is not available, note this as unknown. Do not invent GBP data.
7. Identify the top 1, 2 or 3 biggest issues preventing the local page from ranking to it's full potential. Not specified how many issues because it will vary.
8. Do not edit the page. Do not fix the page. Do not add entities. Do not add internal links. Do not change the title. This is diagnostic only.
#DIAGNOSTIC OUTPUT
9. For each major issue found, explain:
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
10. If the page has many small issues, group them together instead of listing every tiny issue. Focus on the top 1-3 issues that are most likely holding the page back.
11. If everything checks out on the page, say that clearly. If indexability, on-page, content, entity, speed, headings, internal links, local relevance, local proof, and category alignment all look fine, then explain that it's likely domain / link issues, GBP / map pack issues, local prominence issues, review / citation issues, distance / proximity issues, or outside-page factors.
#REPORT
Produce a simple local SEO diagnostic report.
The report should include:
- target URL
- keyword / topic used for the scan
- target city / area
- business name
- business type / service
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
- LocalBusiness schema issue, yes/no / not applicable
- NAP visibility issue, yes/no / not applicable
- GBP / website alignment issue, yes/no / unknown
- service area clarity issue, yes/no
- city / location relevance issue, yes/no
- local proof issue, yes/no
- duplicate / cannibalization issue, yes/no
- search intent alignment
- local intent alignment
- map pack vs organic split
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
- local internal link opportunities
- Google category alignment with top 3 competitors
- likely reason the page is not ranking to it's full potential
- recommended fixes
- whether the issue appears to be indexability, technical, local relevance, GBP-related, NAP-related, schema-related, on-page, internal linking, content, entity-related, category-related, cannibalization-related, speed-related, local prominence-related, or likely domain / link related
#SUCCESS
You will be successful when you have performed a deep local SEO diagnostic, checked technical / indexability issues, gone through the on-page-seo report sequentially, checked local relevance, service / city alignment, NAP, schema, local proof, GBP alignment if available, internal links and speed benchmarks, identified the top 1-3 biggest issues preventing the page from ranking to it's full potential, explained the likely fixes, and clearly stated whether the issue appears to be indexability, technical, local relevance, GBP-related, NAP-related, schema-related, on-page, internal linking, content, entity-related, category-related, cannibalization-related, speed-related, local prominence-related, or likely domain / link related.
