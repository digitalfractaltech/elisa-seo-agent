# Original Recipe Reference

Source: On-Page.ai guide, recipe: 13. Image and Alt Text Optimization, Single Page

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF
You are performing SEO work.
- You have access to the on-page-seo MCP connector
- You have access to the target site
- You may upload, download, browse, edit the target page, create reports, etc.
#TASK
Perform image + alt-text optimization on the URL: "
https://www.yoursite.com/url/
" for the keyword: "
keyword
"
#PROCESS
1. First, verify and read the target URL page.
2. Start by performing an on-page Standard scan using the on-page-seo tool on the target URL.
3. When the on-page-seo Standard scan completes, review the image / alt-text sections of the report.
Additionally, check:
- image alt-text issues if available
- whether all images have appropriate alt-text with entities inside them where natural
- whether images are relevant to the topic / search intent
- whether the page is low on images compared to the competition
- whether competitors are using more useful visual content
- whether any image is missing alt-text
- whether any image has weak, generic, duplicated, or irrelevant alt-text
- whether adding a generated image would improve the page
4. Verify that all the images have appropriate alt-text with entities inside them where natural.
5. If an image has missing or weak alt-text, update the alt-text so that it is descriptive and relevant to the page topic. Use entities where natural.
6. Preserve the human writing as much as possible. Preserve the title. Preserve the slug. Preserve the structure unless there is an obvious issue.
7. If appropriate, use your built-in image generator (Codex has a built in image generator) to add one or more new generated images where appropriate within the content if the environment supports it. This helps if the page is low on images compared to the competition and it helps to break up long blocks of text.
The images should:
- fit naturally into the existing page
- support the topic / search intent
- include appropriate alt-text with entities where natural
- improve the page instead of feeling randomly added
- they should be spaced out and not immediately follow another image
8. Do not add images just to add images. Only add generated images if the page is very low in images compared to the competitors, or if the page has long blocks of text that would clearly benefit from a useful visual.
9. If image generation is not available, create the exact image prompts, recommended placement, filename and alt-text, and list it in the final report.
10. In the event that the page has no images, determine whether adding one or more images would improve the page. If yes, add generated images where appropriate if the environment supports it. If no, explain why in the final report.
#VERIFICATION
11. Once the image / alt-text edits have been made, verify:
- The original title was preserved.
- The original slug was preserved.
- The structure was preserved unless there was an obvious issue.
- The page still reads naturally.
- The human writing was preserved as much as possible.
- Image alt-text was checked and updated if necessary.
- Alt-text uses relevant entities where natural.
- Images are relevant to the topic / search intent.
- Generated images were added if appropriate, or the reason they were not added is explained.
- The page was not broken during editing.
12. If any task cannot be completed due to access, environment, permissions, missing tools, unavailable data, image generation not being available, or the page not being a good fit for image / alt-text optimization. Note it in the final report.
13. Produce a simple HTML report file of the changes. Provide an audit trail within the report of the changes you made.
#REPORT
The final HTML report should include:
- target URL
- keyword / topic used for the scan
- Standard scan status
- image / alt-text issues found
- original image alt-text
- updated image alt-text
- entities used in alt-text
- images added, yes/no
- generated image prompts, if image generation was not available
- image placement
- filenames
- whether the page was low on images compared to competitors
- images left unchanged and why
- access issues
- audit trail
#SUCCESS
You will be successful when the target page has been processed, all image / alt-text issues have been reviewed, missing or weak alt-text has been improved where appropriate, generated images have been added if the page is low on images compared to competitors and the environment supports it, the title and human writing have been preserved, and you have produced a simple HTML report outlining the changes, justifications, images added, alt-text updated and have provided an audit trail.
