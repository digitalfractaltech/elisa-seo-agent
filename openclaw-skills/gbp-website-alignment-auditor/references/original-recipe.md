# Original Recipe Reference

Source: On-Page.ai guide, recipe: 16. Local Website and GBP Alignment Verification

This is the authoritative recipe text for this skill. SKILL.md is the concise navigation layer. When running this skill in production, follow this reference if it is more specific.

---

#SELF
You are performing local SEO audit work.
- You have access to the target site
- You have access to the Chrome connector which you can use to browse the GBP.
- You may upload, download, browse, read the target website, create reports, etc.
- If available, you may use the on-page-seo MCP connector to help understand the website category / topical alignment.
#TASK
Perform a GBP-to-Website Alignment Audit for the website: "
https://www.yoursite.com
"
Business name: "
[OPTIONAL - LEAVE BLANK IF UNKNOWN]
"
Target city / area: "
[OPTIONAL - LEAVE BLANK IF UNKNOWN]
"
Google Business Profile URL: "
[OPTIONAL - LEAVE BLANK IF UNKNOWN]
"
The goal is to compare the Google
 Business Profile information against the website content and identify mismatches, missing information, weak local relevance, NAP issues, service/category gaps, and anything that may be holding back local SEO performance.
Do as much checking as possible without requiring the user to enter a bunch of information.
If the Google Business Profile URL is provided, use it.
If the Google Business Profile URL is not provided, try to find the correct public Google Business Profile / Google Maps listing using the business name, website, phone number, address, brand name, city / area, and other public information you can find.
Do not invent GBP information. If something cannot be verified, mark it as unknown.
#PROCESS
1. First, verify and read the target website homepage.
2. Determine what type of local business this appears to be:
- local service business
- service-area business
- storefront / physical location
- multi-location business
- ecommerce + local showroom
- local professional service
- medical / dental / clinic
- restaurant / hospitality
- other
3. Try to identify the business information from the website.
Check:
- business name
- phone number
- address
- service area
- city / area
- business hours
- contact page
- location page
- footer NAP
- homepage NAP
- visible services
- main service pages
- location / service area pages
- schema / structured data if available
- LocalBusiness schema if available
- Organization schema if available
- sameAs links if available
- social profile links if available
4. Try to find the Google Business Profile / Google Maps listing.
Use as much public information as possible:
- business name
- website domain
- phone number
- address
- city / area
- brand name
- contact page information
- footer NAP
- Google search / Google Maps result if available
If multiple GBP listings are found, choose the most likely match and explain why. If there is uncertainty, note the confidence level.
5. Extract as much GBP information as possible.
Check:
- GBP business name
- primary category
- secondary categories if visible
- services listed if visible
- products listed if visible
- address
- service area
- phone number
- website URL
- hours
- business description if visible
- appointment / booking links if visible
- photos if visible
- review themes if visible
- attributes if visible
If a field is not visible or cannot be verified, mark it as unknown.
6. Compare GBP information against the website.
Additionally, check:
- Does the GBP business name match the website business name?
- Does the GBP phone number match the website phone number?
- Does the GBP address match the website address?
- Does the GBP service area match the website service area?
- Does the GBP website URL point to the correct website?
- Do the GBP hours match the website hours?
- Does the GBP primary category match what the website is actually about?
- Do the GBP secondary categories match the services shown on the website?
- Do the GBP services match the services discussed on the website?
- Are important services listed in GBP missing from the website?
- Are important services on the website missing from GBP?
- Does the homepage clearly support the GBP primary category?
- Do service pages clearly support the GBP services?
- Does the website clearly explain the target city / area?
- Does the website have location / service area pages if appropriate?
- Does the website have LocalBusiness schema or Organization schema?
- Does the schema match the visible website information?
- Does the schema match the GBP information?
- Are there NAP inconsistencies between homepage, footer, contact page, schema and GBP?
- Is the phone number visible and clickable?
- Is the address visible if this is a physical location?
- Is the service area visible if this is a service-area business?
- Are business hours visible if relevant?
- Is the business category / service category clear on the website?
- Does the website look locally relevant or does it look generic?
7. If useful, perform an on-page Standard scan using the on-page-seo tool on the homepage or the most important local landing page.
Use this only to help understand:
- Google category alignment
- topical alignment
- missing important entities
- Highly Related Words
- service/category relevance
- whether the page supports the business category / service category
If there is no clear keyword, infer the best keyword from the homepage title, H1, URL slug, business type, services and city / area.
8. Identify the biggest GBP-to-website alignment issues.
Not specified how many issues because it will vary.
Focus on the issues most likely to hurt local SEO performance:
- NAP mismatch
- GBP category does not match website focus
- GBP services missing from website
- website services missing from GBP
- service area unclear
- address / phone / hours mismatch
- missing LocalBusiness schema
- schema conflicts with visible content
- weak local relevance
- weak service/category support
- missing service pages
- missing location / service-area pages
- duplicate or confusing location information
- GBP listing may not be the correct listing
- GBP data could not be verified
9. Do not edit the website. Do not fix the website. Do not change GBP. This is an audit only.
#AUDIT OUTPUT
10. For each major issue found, explain:
- what the issue is
- what was found on the website
- what was found in the GBP / Google Maps listing
- why this issue may matter for local SEO
- how serious the issue is
- what should be done to fix it
Use priority levels:
- Critical
- High
- Medium
- Low
- No issue found
- Unknown / could not verify
11. If everything checks out, say that clearly. If GBP, website NAP, services, categories, service area, schema, and local relevance all look aligned, explain that the issue may be outside of GBP-to-website alignment, such as reviews, citations, links, proximity / distance, local prominence, or competition strength.
#REPORT
Produce a simple GBP-to-Website Alignment Audit report.
The report should include:
- website URL
- business name
- target city / area
- GBP URL found, if found
- GBP match confidence
- business type
- website NAP found
- GBP NAP found
- NAP alignment status
- GBP primary category
- GBP secondary categories if visible
- website category / service focus
- category alignment status
- GBP services found
- website services found
- services missing from website
- services missing from GBP
- address alignment
- phone alignment
- hours alignment
- website URL alignment
- service area alignment
- LocalBusiness / Organization schema status
- schema alignment with website and GBP
- local relevance issues
- service / city clarity issues
- location page / service area page issues
- on-page-seo category / entity observations if a Standard scan was used
- top issues found
- recommended fixes
- unknown / unverifiable items
- audit trail
#RECOMMENDED FIXES
For the recommended fixes, include:
- Critical fixes
- High priority fixes
- Medium priority fixes
- Low priority fixes
- quick wins
- what to do first
For recommendations, be specific. Do not say "improve GBP" or "improve website" without explaining what should be improved.
Examples:
- Add missing service pages for services listed in GBP.
- Update website footer NAP to match GBP.
- Add LocalBusiness schema that matches visible NAP.
- Add service area details to the homepage or service page.
- Add city / area language naturally where appropriate.
- Align GBP services with actual website service pages.
- Remove or clarify conflicting addresses / phone numbers.
- Make the phone number clickable.
- Add business hours to the contact page if relevant.
#SUCCESS
You will be successful when you have checked the website, attempted to find and verify the Google Business Profile, compared GBP categories / services / NAP against the website content, identified the biggest alignment issues, explained the likely fixes, and produced a simple report showing what matches, what does not match, what could not be verified, and what should be fixed first.
```
