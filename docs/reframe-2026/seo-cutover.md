# SEO Cutover & Redirect Plan — extense.co relaunch

> The single biggest ranking lever of the relaunch. The new site is built
> and SEO-prepped; this runbook moves the **old site's ranking equity onto
> the new site** without losing it. Owner-triggered; nothing here fires
> automatically.

---

## The situation (two domains)

- **Old site (live, indexed):** `www.ex-tense.co` — Siteground, static `.html`
  URLs. This is what Google currently ranks.
- **New site (built, staged):** will serve at **`extense.co` / `www.extense.co`**
  on Vercel. Today `extense.co`/`www` **307-redirect to `ex-tense.co`** via two
  host rules in `vercel.json`.

Because the *domain changes* (`ex-tense.co` → `extense.co`) **and** many URLs
change (`.html` → clean paths, some slugs renamed), this is a **domain
migration**. The rule that makes or breaks it: **every old URL must `301` to
its specific new URL** — not a blanket redirect to the homepage (that throws
away page-level equity).

**Canonical host:** the site's `site`, canonicals, sitemap, and Organization
schema all use **`https://www.extense.co`**. So `www` is canonical; the apex
`extense.co` must `301` → `www`.

---

## Step 1 — Pre-cutover (DONE)

Already shipped (all invisible / no visible page change):
- Structured data (Organization, WebSite, BreadcrumbList, FAQPage, Service ×7,
  TechArticle ×3); OG image; staging `noindex`; junk + sitemap-config cleanup;
  titles ≤ ~60 and meta descriptions ≤ ~160, keyword-front-loaded; duplicate
  "insights" shells retired + 301'd.

---

## Step 2 — Flip the new site live (Vercel / extense.co)

1. In `vercel.json`, **delete the two host-redirect rules** (`has` host
   `extense.co` and `www.extense.co` → `ex-tense.co`). Domains are already
   attached, so the new site serves immediately.
2. **Set `www.extense.co` as the Primary Domain** in Vercel project settings
   so the apex `extense.co` auto-`301`s to `www` (or add an explicit apex→www
   redirect). Confirms one canonical host.
3. Leave the **staging `noindex`** header in place — it is host-scoped to
   `extense-website.vercel.app` and does **not** touch `www.extense.co`
   (production stays `index, follow`).
4. The existing path redirects in `vercel.json` (`/company/about-us`,
   `/resources/case-studies*`) and `astro.config.mjs`
   (`/capabilities*` → `/services`, `/company/faqs` → `/resources/faq`,
   retired insights slugs) stay.

---

## Step 3 — Old-domain 301 map (ex-tense.co → extense.co)  ⭐ equity transfer

Implement on the **old site (Siteground `.htaccess`)** so each indexed
`ex-tense.co` URL `301`s to its new `www.extense.co` equivalent. Keep
`ex-tense.co` alive (pointing here) for at least the GSC Change-of-Address
window (Google recommends ~180 days), ideally permanently.

| Old (`www.ex-tense.co/…`) | New (`https://www.extense.co/…`) |
|---|---|
| `/` | `/` |
| `/about.html` | `/company` |
| `/contact.html` | `/contact` |
| `/our-process.html` | `/company/our-process` |
| `/careers.html` | `/company/careers` |
| `/privacy-policy.html` | `/privacy` |
| `/terms.html` | `/terms` |
| `/solutions/` | `/solutions` |
| `/solutions/technical-documentation-publishing.html` | `/solutions/technical-docs-and-publishing` |
| `/solutions/content-migration-modernization.html` | `/solutions/content-migration` |
| `/solutions/xml-data-interoperability.html` | `/solutions/xml-data-interoperability` |
| `/services/` | `/services` |
| `/services/dita-engineering.html` | `/services/dita-engineering` |
| `/services/publishing-engineering.html` | `/services/publishing-engineering` |
| `/services/ccms-services.html` | `/services/ccms-services` |
| `/services/xml-engineering.html` | `/services/xml-engineering` |
| `/services/technical-writing-content-development.html` | `/services/technical-writing-content-development` |
| `/services/structured-content-strategy.html` | `/services/structured-content-strategy` |
| `/services/system-integration.html` | `/services/system-integration` |
| `/industries/` | `/industries` |
| `/industries/government.html` | `/industries/government-and-defense` |
| `/industries/financial-services.html` | `/industries/financial-services` |
| `/industries/insurance.html` | `/industries/insurance` |
| `/industries/automotive.html` | `/industries/transportation` |
| `/industries/life-sciences.html` | `/industries/life-sciences` |
| `/resources/` | `/resources` |
| `/resources/faqs.html` | `/resources/faq` |
| `/resources/ai-content-readiness-guide.html` | `/resources/ai-readiness` |
| `/resources/dita-migration-playbook.html` | `/resources/migration-playbook` |
| `/resources/publishing-automation-guide.html` | `/resources/automation-guide` |
| `/work/` | `/company/our-work-and-case-studies` |
| `/work/case-studies.html` | `/company/our-work-and-case-studies` |

**Net-new pages** (no old equivalent — they simply get indexed fresh):
`/solutions/ai-ready-content`, `/industries/technology`, the 3 case-study
detail pages under `/company/our-work-and-case-studies/*`.

### Siteground `.htaccess` (paste-ready, on ex-tense.co)
```apache
RewriteEngine On
# Per-URL 301s (old .html -> new clean URL on extense.co)
RewriteRule ^about\.html$ https://www.extense.co/company [R=301,L]
RewriteRule ^contact\.html$ https://www.extense.co/contact [R=301,L]
RewriteRule ^our-process\.html$ https://www.extense.co/company/our-process [R=301,L]
RewriteRule ^careers\.html$ https://www.extense.co/company/careers [R=301,L]
RewriteRule ^privacy-policy\.html$ https://www.extense.co/privacy [R=301,L]
RewriteRule ^terms\.html$ https://www.extense.co/terms [R=301,L]
RewriteRule ^solutions/technical-documentation-publishing\.html$ https://www.extense.co/solutions/technical-docs-and-publishing [R=301,L]
RewriteRule ^solutions/content-migration-modernization\.html$ https://www.extense.co/solutions/content-migration [R=301,L]
RewriteRule ^solutions/xml-data-interoperability\.html$ https://www.extense.co/solutions/xml-data-interoperability [R=301,L]
RewriteRule ^services/(dita-engineering|publishing-engineering|ccms-services|xml-engineering|technical-writing-content-development|structured-content-strategy|system-integration)\.html$ https://www.extense.co/services/$1 [R=301,L]
RewriteRule ^industries/government\.html$ https://www.extense.co/industries/government-and-defense [R=301,L]
RewriteRule ^industries/automotive\.html$ https://www.extense.co/industries/transportation [R=301,L]
RewriteRule ^industries/(financial-services|insurance|life-sciences)\.html$ https://www.extense.co/industries/$1 [R=301,L]
RewriteRule ^resources/faqs\.html$ https://www.extense.co/resources/faq [R=301,L]
RewriteRule ^resources/ai-content-readiness-guide\.html$ https://www.extense.co/resources/ai-readiness [R=301,L]
RewriteRule ^resources/dita-migration-playbook\.html$ https://www.extense.co/resources/migration-playbook [R=301,L]
RewriteRule ^resources/publishing-automation-guide\.html$ https://www.extense.co/resources/automation-guide [R=301,L]
RewriteRule ^work/case-studies\.html$ https://www.extense.co/company/our-work-and-case-studies [R=301,L]
# Section indexes + anything else -> matching path (then catch-all to homepage)
RewriteRule ^solutions/?$ https://www.extense.co/solutions [R=301,L]
RewriteRule ^services/?$ https://www.extense.co/services [R=301,L]
RewriteRule ^industries/?$ https://www.extense.co/industries [R=301,L]
RewriteRule ^resources/?$ https://www.extense.co/resources [R=301,L]
RewriteRule ^work/?$ https://www.extense.co/company/our-work-and-case-studies [R=301,L]
RewriteRule ^$ https://www.extense.co/ [R=301,L]
# Final safety net: any other old URL -> new homepage
RewriteRule ^(.*)$ https://www.extense.co/ [R=301,L]
```

---

## Step 4 — Defensive redirects on the NEW domain (optional, recommended)

In case anything links to old-style `.html` paths on `extense.co` directly,
mirror the map as Vercel `redirects` (source = old path on extense.co). Ask
me to add this block to `vercel.json` — it's the same map, `permanent: true`.
Low-risk; safe to add before cutover (extense.co serves no `.html` pages).

---

## Step 5 — Google Search Console

1. Verify **`https://www.extense.co`** (and the apex) as properties. Keep
   **`ex-tense.co`** verified too.
2. Submit `https://www.extense.co/sitemap-index.xml`.
3. After the Step-3 301s are confirmed working, use GSC **Change of Address**
   (from `ex-tense.co` → `extense.co`) to signal the migration.
4. Request indexing for the homepage + top pages; monitor Coverage + the
   "Page with redirect" / 404 reports for a few weeks.
5. (If used) move Bing Webmaster Tools the same way.

---

## Step 6 — Post-cutover verification checklist

- [ ] `https://extense.co/` (apex) `301`s → `https://www.extense.co/`.
- [ ] `www.extense.co` serves the new site `200` (no longer redirects to ex-tense.co).
- [ ] Production pages return `robots: index, follow` (NOT noindex); staging
      `extense-website.vercel.app` still returns `X-Robots-Tag: noindex`.
- [ ] Spot-check 8–10 rows of the Step-3 table: old URL → `301` → correct new URL (single hop, not a chain).
- [ ] `https://www.extense.co/sitemap-index.xml` lists the new URLs with `www` host.
- [ ] `og-default.png` loads; share-debuggers (LinkedIn Post Inspector, etc.) render the card.
- [ ] Rich Results Test passes for FAQPage (/resources/faq), a Service page, and a TechArticle guide.
- [ ] No leftover links to retired URLs (capabilities/*, /company/faqs, insights slugs) — they 301 cleanly.

---

## Notes / decisions captured
- `automotive` → `transportation` and `government` → `government-and-defense`
  are the only industry **slug renames**; the rest keep their slug.
- Old `/resources/*-guide.html` resource slugs were renamed to the shorter
  dedicated-page slugs (`ai-readiness`, `migration-playbook`, `automation-guide`).
- Old site had **5 industries**; new adds **Technology** (net-new).
- Old site had **3 solutions**; new adds **AI-Ready Content** (net-new).
