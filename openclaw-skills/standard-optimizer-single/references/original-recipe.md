# Original Recipe Reference

Source: On-Page.ai guide, recipe: 7. Standard Optimization, Single Page

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF
You are performing SEO work.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, edit the target page, create reports, etc.
#TASK
Perform a standard SEO optimization refresh on the URL "
https://yoursite.com/url/
" for the keyword: "
keyword
"
#PROCESS
1. First, verify and read the target URL page.
2. Start by performing an on-page Standard scan using the on-page-seo tool on the target URL.
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
15. In the event that the page is too thin, broken, irrelevant, or cannot be optimized naturally, note it in the final report.
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
19. If any task cannot be completed due to access, environment, permissions, missing tools, unavailable data, failed scan, image generation not being available, not enough credits for re-scan, or the page not being a good fit for standard optimization. Note it in the final report.
20. Produce a full HTML report file of the changes. Provide an audit trail within the report of the changes you made.
#REPORT
The final HTML report should include:
- target URL
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
- access issues
- audit trail
#SUCCESS
You will be successful when the target page has been processed, the biggest issues from the Standard scan have been identified and resolved where possible, all possible standard optimization improvements have been added naturally, the related_important entity score is higher than the competition or the remaining blocker is explained, all skipped items have been explained, and you have produced a full HTML report outlining the changes, justifications, entities added, Highly Related Words added, image / alt-text updates, before and after related_important score and have provided an audit trail.
