# Original Recipe Reference

Source: On-Page.ai guide, recipe: 17. Local Website Cannibalization Checker, City or Region Audit

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF
You are performing local SEO cannibalization diagnostic work. You will need to build a detailed task list of the steps in order to complete your local SEO cannibalization work. Continue until the task list is complete.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, read the target pages, create reports, write scripts, execute scripts, etc.
#TASK
Find whether multiple pages on this site are targeting the same local service + city intent.
Website / sitemap: "
https://www.yoursite.com/sitemap.xml
"
Target service: "
plumber
"
Target city / area: "
miami
"
Target keyword: "
plumber miami
"
The goal is to determine whether the site has cannibalization issues where multiple internal pages are targeting the same service + city / area, same keyword, or same local search intent.
## Examples of pages that may be competing in a local site:
- /plumber-miami/
- /miami-plumber/
- /emergency-plumber-miami/
- /services/plumbing-miami/
- /locations/miami/
#PROCESS
1. First, pull the sitemap and create a lightweight manifest of URLs that may be relevant to the target service + city / area.
Do not fetch, read, scan, or extract content from all sitemap URLs while building the manifest. Start by using sitemap URLs and obvious URL patterns.
Look for URLs that include:
- the target service
- service variations
- the target city / area
- city variations
- service + city combinations
- location folder patterns
- service folder patterns
- nearby service / city variations if relevant
2. Build a candidate list of possible cannibalizing pages.
The candidate list should include:
- exact service + city matches
- reversed service + city matches
- pages with the same service but different local modifier
- pages with the same city but similar service
- emergency / near me / local / service-area variations
- location pages that may overlap with service pages
- service pages that may overlap with location pages
- blog posts or articles that may accidentally target the same local intent
3. If too many candidate pages are found, narrow the initial investigation to the strongest candidates first.
Prioritize:
- URLs with the target service and city / area in the slug
- URLs close to the top level of the site
- service pages
- location pages
- pages that look like money pages
- pages likely to be internally linked
- pages with title / H1 patterns that appear to match the same keyword
4. For each candidate page, verify and read the page.
For each candidate page, check:
- URL
- title tag
- H1
- main H2s
- canonical tag
- meta robots
- HTTP status
- whether the page is indexable
- whether the page canonical points to itself or to another URL
- whether the page appears to target the same service + city / area
- whether the page appears to target the same keyword / search intent
- whether the page has overlapping service entities
- whether the page has overlapping location entities
- whether the page has duplicate or near-duplicate content
- whether the page is a service page, city page, location page, article, category page, homepage, or other
5. If a primary target URL is provided, compare every candidate page against the primary target URL.
If a primary target URL is not provided, determine which URL should be the primary page based on:
- best match to the target service + city / area
- strongest local search intent alignment
- strongest page type for the keyword
- cleanest URL
- best title / H1 alignment
- best content depth
- best internal linking
- best entity coverage
- best canonical/indexability setup
- closest match to what Google appears to reward for the keyword
6. Use the on-page-seo MCP connector where useful.
For the primary target URL, run an on-page Standard scan using the target keyword.
If there are 1-3 strong competing internal pages, you may also run Standard scans on those pages if needed to compare:
- related_important entity score
- missing entities
- Highly Related Words
- Google category alignment
- content length / word count compared to competition
- internal link opportunities
- title / H1 / content relevance
Do not waste scans on weak candidates that clearly do not target the same intent.
7. Check for duplicate title / H1 patterns.
Additionally, check:
- pages using the same or near-same title tag
- pages using the same or near-same H1
- pages using the same city + service phrase in the title / H1
- pages using the same heading structure with only small location changes
- pages that look like doorway / duplicate service-city variations
8. Check for overlapping entities and content.
Additionally, check:
- whether the same service entities are repeated across competing pages
- whether the same local entities are repeated across competing pages
- whether the pages have the same main entity focus
- whether the pages are too similar to deserve separate URLs
- whether one page is clearly broader and another page is more specific
- whether pages can be differentiated by service, emergency intent, neighborhood, location, audience, or use case
9. Check internal links and internal anchors.
Additionally, check:
- which page is being internally linked the most
- whether internal links point to the wrong page
- whether anchors for the target keyword point to multiple competing pages
- whether the primary page has enough internal links pointing back to it
- whether competing pages are stealing internal link relevance
- whether the site is sending mixed signals about which page should rank
10. Check canonicalization and indexability.
Additionally, check:
- whether competing pages canonicalize to themselves
- whether competing pages canonicalize to each other
- whether any page should be canonicalized but is not
- whether any page is noindex
- whether any page is blocked
- whether any page redirects
- whether any page is thin, broken, or not useful
11. Check if the wrong page may be ranking.
If you can verify ranking / SERP / search result information, check:
- which internal URL appears to be ranking for the target keyword
- whether Google is ranking the wrong page
- whether the ranking page is weaker than the intended primary page
- whether the intended primary page is being underlinked or diluted
If ranking data is not available, infer the risk from content, titles, H1s, internal links, and canonical setup.
12. Identify the primary page and competing internal pages.
For each competing page, decide whether it should be:
- merged
- redirected
- canonicalized
- differentiated by intent
- internally linked to the primary page
- kept separate
- left alone
13. Do not edit the site. Do not redirect pages. Do not canonicalize pages. Do not add internal links. This is diagnostic only.
#CANNIBALIZATION OUTPUT
14. For each cannibalization issue found, explain:
- what the issue is
- which pages are competing
- why they may be competing
- what each page appears to target
- which page should be the primary page
- whether the issue is severe, moderate, or minor
- what should be done to fix it
Use priority levels:
- Critical
- High
- Medium
- Low
- No issue found
15. If there are many competing pages, group them by intent.
Example groups:
- main service + city intent
- emergency service + city intent
- location page intent
- nearby city intent
- article / informational intent
- category / archive intent
16. If pages are similar but not actually competing, say that clearly.
For example:
- one page targets emergency intent
- one page targets general service intent
- one page targets a nearby city
- one page is informational and should support the money page
- one page is a location hub and should internally link to the service page
#REPORT
Produce a simple local cannibalization report.
The report should include:
- website / sitemap used
- target service
- target city / area
- target keyword
- primary target URL, if provided
- primary page selected
- reason this should be the primary page
- candidate pages found
- competing internal pages
- page type for each candidate
- title / H1 for each candidate
- canonical status for each candidate
- indexability status for each candidate
- whether each page targets the same service + city / area
- overlapping entities / content notes
- internal link / anchor overlap issues
- wrong page being internally linked, yes/no
- wrong page possibly ranking, yes/no / unknown
- severity of cannibalization
- recommended action for each URL
- pages to merge
- pages to redirect
- pages to canonicalize
- pages to differentiate by intent
- pages that should internally link to the primary page
- pages to leave alone
- unknown / unverifiable items
- audit trail
#RECOMMENDED ACTIONS
For recommendations, be specific.
Use one of these actions for each competing page:
## Merge
Use when two pages are targeting the same service + city / area and both are trying to satisfy the same intent.
## Redirect
Use when one page is clearly weaker, duplicate, outdated, thin, or should no longer exist as a separate URL.
## Canonicalize
Use when pages must remain accessible but one should clearly be treated as the primary version.
## Differentiate by intent
Use when both pages can exist, but they need clearer separation.
### Examples:
- one page becomes emergency plumber Miami
- one page becomes general plumbing services Miami
- one page becomes drain cleaning Miami
- one page becomes Miami location page
- one page becomes an informational article supporting the service page
## Add internal links to primary page
Use when a supporting page should point relevance toward the primary money page.
## Leave alone
Use when the pages are not actually competing or already have distinct intent.
#SUCCESS
You will be successful when you have found the pages that may be targeting the same local service + city intent, identified the primary page, listed the competing internal pages, checked title / H1 patterns, overlapping entities, internal anchors, canonicals, indexability and possible wrong-page ranking, and produced a simple HTML report with recommended actions: merge, redirect, canonicalize, differentiate by intent, add internal links to primary page, or leave alone.
