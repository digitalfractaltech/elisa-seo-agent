# Original Recipe Reference

Source: On-Page.ai guide, recipe: 3. Single Page Internal Links, Detailed Version

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF You are performing SEO internal linking work.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, edit the target pages, create reports, etc.
#TASK
Build internal links pointing to this target page:
"https://yoursite.com/yourtargetURL/"
#PROCESS
1. First, verify and read the target URL page.
2. Determine the best keyword / topic to use for the on-page standard scan. If a keyword was provided, use that. If not, infer it from the page title, H1, URL slug, and content.
3. Run an on-page standard scan using the on-page-seo tool for the target URL and keyword / topic.
4. When the on-page-seo scan completes, within the report, you'll have the 3 pages with most relevance for internal links.
5. For each of the 3 suggested internal link source pages, check them to see if they are already present and/or linking from the main content.
#INTERNAL LINKING PROCESS
##When you receive an on-page standard scan report:
- Verify that the suggested source page has main content. ie: it's not a category page, tag page, search page, author page, archive page, etc. If that type of page is suggested, then we just skip/ignore that internal link recommendation.
- Verify that the source page does not already link to the target page from the main content.
(If the source page already links to the target page from the main content, mark it as already done and move to the next one.)
- If the source page does not have useful main content, skip it and note the reason in the report.
- If the source page is relevant, has main content, and is not already linking to the target page, then perform a minor edit the text to seamlessly add a natural anchor text link within the main content. (The anchor text should be chosen naturally based on the sentence and surrounding paragraph.)
- Prefer links inside the actual article / page content, not menus, sidebars, footers, related post boxes, etc.
- In the event that you cannot add a natural link because the content is completely irrelevant, then note it in the final report.
6. For this target page, you'll want to create up to 3 seamless contextual internal links.
7. If there are fewer than 3 good internal link opportunities, only add the valid ones and explain why the others were skipped.
8. If the target page has no good internal link opportunities (nothing was returned in the standard on-page scan or no good / valid links were in the scan), note it in the report.
#VERIFICATION
9. Once internal links have been added, verify each edited source page and confirm that the internal link exists in the main content.
10. Verify that the target URL received the correct number of internal links, up to 3 where possible.
11. If any task cannot be completed due to access, environment, permissions, missing tools, no main content, already existing links, unavailable data or failed scans. Note it in the final report.
12. Produce a full HTML report file of the changes. Provide an audit trail within the report of the changes you made.
#REPORT
The final HTML report should include:
- target URL
- keyword / topic used for the scan
- suggested source pages from the on-page-seo scan
- source pages checked
- total source pages checked
- total internal links added
- anchor text used
- final source URL
- final target URL
- whether the source page already linked to the target
- whether the source page had main content
- complete audit trail
#SUCCESS
You will be successful when the target page has been processed, all possible seamless contextual internal links have been added from relevant source pages, all skipped items have been explained, and you have produced a complete HTML report outlining the changes, justifications, source URLs, target URL, anchor text used and have provided an audit trail."
