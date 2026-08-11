# Original Recipe Reference

Source: On-Page.ai guide, recipe: 6. Light Page Refresh, Single Page

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF
You are performing SEO work.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, edit the target page, create reports, etc.
#TASK
Perform a light SEO refresh on the URL "
https://www.yoursite.com/url/
" for the keyword: "
keyword
"
#PROCESS
1. First, verify and read the target URL page.
2. Start by performing an on-page Lite scan using the on-page-seo tool on the target URL.
3. When the on-page-seo Lite scan completes, go through the entity data and identify:
- entities with importance 9
- entities with importance 10
- Highly Related Words
- content length / word count compared to the competition
- image alt-text issues if available
- any obvious outdated sections that conflict with user intent
4. Add an appropriate quantity of entities with importance 9, 10 and 'Highly Related Words' naturally into the text. Light edits, preserve as much human text as possible. (Do not touch title). Prefer sentence level edits over full rewrites.
5. If an important term was considered but cannot be added naturally without hurting readability, list it in the final report as “not added” with the reason.
6. This is a light content refresh. Preserve the human writing as much as possible. Preserve the title. Preserve the slug. Preserve the structure unless there is an obvious issue.
7. If the content is thin when compared to the average, add a maximum of one new short paragraph of text.
8. If applicable, the new short paragraph should:
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
14. In the event that the page is too thin, broken, irrelevant, or cannot be refreshed naturally, note it in the final report.
#VERIFICATION
You may re-scan after editing to evaluate the before & after score. If the user is low in credits, skip this step. (The initial Lite scan before editing is the only scan required for this light refresh process.)
15. Once the light refresh edits have been made, verify:
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
16. If any task cannot be completed due to access, environment, permissions, missing tools, unavailable data, failed scan, image generation not being available, or the page not being a good fit for light refresh. Note it in the final report.
17. Produce a simple HTML report file of the changes. Provide an audit trail within the report of the changes you made.
#REPORT
The final HTML report should include:
- target URL
- keyword / topic used for the scan
- Lite scan status
- entities with importance 9 / 10 added
- Highly Related Words added
- important terms considered but not added
- short paragraph added, yes/no
- image added, yes/no
- image alt-text updated, yes/no
- outdated sections updated or flagged
- access issues
- audit trail
#SUCCESS
You will be successful when the target page has been processed, all possible light refresh improvements have been added naturally, all skipped items have been explained, and you have produced a simple HTML report outlining the changes, entities added, Highly Related Words added, image / alt-text updates, short paragraph added and have provided an audit trail.
