# Publishing Engineering (service detail) — Reframe Plan

> Status: **implemented — pending staging sign-off.** Fourth of the 7 `/services/<slug>` detail
> sub-pages. Built **bespoke** (page-local CSS, prefix `pub-`), reusing the shared
> atoms (`Hero`, `SectionSiblings`, `CTAModule`) and the patterns proven on
> DITA Engineering (icon-card grids, 3-card row, `01–0N` strip, `#fef3c7` callout,
> related cards, hero node-graph visual). Faithful rebuild of the old
> `ex-tense.co/services/publishing-engineering.html` (7 sections).
> **Locked this session:** H1 = "Publishing Engineering & Automation"; **faithful —
> all 7 sections**; hero **visual = B** (one-source → many-outputs fan).
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [dita-engineering.md](dita-engineering.md).

---

## 1. Page job
- **URL:** `/services/publishing-engineering`
- **Primary reader:** a docs-platform owner / publishing lead evaluating whether
  Extense can render one structured source into many pixel-perfect outputs
  (PDF, HTML5, WebHelp, portals, EPUB, eLearning) and automate the build.
- **The one job:** prove deep multi-output publishing capability — modern stacks,
  the transformation engine, the rendering pipeline, localization, and the long
  tail of advanced formats — then convert.

> **Note (overlap, accepted — faithful):** the Core Transformation Engine and
> Containerized Build / DITA-OT topics overlap `/services/dita-engineering`
> (DITA-OT Services); the headless/JSON topics overlap the DITA Delivery & AI-Ready
> sections; Static Site Generators overlap DITA Delivery. Per owner: keep all,
> cross-link via the Related cards.

---

## 2. Inventory — OLD page (7 sections)
Hero ("Publishing Automation") → Modern Publishing Technologies (6 cards, 4+2) →
The Core Transformation Engine (3 cards) → The Rendering Pipeline (5-step strip) →
Automated Localization Publishing (callout) → Advanced Output Formats (6 cards,
4+2) → Related Services (3 cards). No closing CTA on the old page.

## 3. Inventory — NEW site
Page doesn't exist (sibling switcher + `/services` card link here, 404 until built).
Reuse: `Hero` (with visual B), `SectionSiblings` (services), `CTAModule` (closer).
Page-local patterns from DITA: hero node-graph SVG, icon-card grid (bare amber line
icons), 3-card row, `01–0N` roadmap strip, `#fef3c7` callout, inline `<code>`,
related-card.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page order; CTA added as closer (parity with DITA).
- **D-1 — H1 = "Publishing Engineering & Automation"** *(locked).* Names the
  service (matches nav/card label) and keeps the old "automation" framing.
- **D-2 — Hero visual = B** *(locked):* one amber `<map>` source fanning to output
  chips (PDF / HTML5 / EPUB / JSON). Differentiated from the TW reuse fan by using
  **output-format** leaves + distinct layout. Full scroll-reveal (`.fx` + draw),
  reduced-motion fallback. `FIG. 01 / single.source / ONE → MANY`.
- **6-card sections** (Modern Publishing Technologies, Advanced Output Formats) =
  the DITA icon-card 4+2 grid with **bare amber line icons**.
- **3-card section** (Core Transformation Engine) = the DITA 3-card row, amber top
  accent line.
- **5-step Rendering Pipeline** = the `01–05` roadmap strip (amber connectors).
- **Localization** = `#fef3c7` callout (old page's green → our amber), inline
  `<code>` for `xml:lang`.
- **Section-band rhythm:** alternate `.section-band` tint as on DITA.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + visual B
- **H1** `[LOCKED]`: "Publishing Engineering & Automation"
- **Subdeck** `[DRAFT]`: "Pixel-perfect outputs from a single structured source —
  PDF, HTML5, WebHelp, EPUB, and custom portals. We engineer the transforms and
  automate the build, so every output rebuilds itself on each commit."
  - *(Alt, closer to `[OLD]`: "Pixel-perfect outputs from structured source. PDF,
    HTML5, WebHelp, and custom portals.")*

### S2 — Sibling switcher · `SectionSiblings` (variant="services")
- current = **Publishing Engineering** (amber + bold).

### S3 — Modern Publishing Technologies · `[OLD]` (6 cards, 4+2, icons)
- **Intro** `[OLD]`: "Beyond traditional XSLT pipelines — we implement the latest
  tools and approaches that are reshaping how structured content reaches its
  audience."
- **6 cards** `[OLD]`:
  1. **CSS Paged Media → PDF** — "Replace complex XSL-FO stylesheets with CSS you
     already know. Using Prince XML, Antenna House CSS, or WeasyPrint, we generate
     print-quality PDFs with CSS Paged Media — the same styling language your web
     team uses. Designers can own the PDF layout without learning FO."
  2. **GraphQL Content APIs** — "Serve published content through GraphQL endpoints
     where consumers request exactly the fields and fragments they need. We build
     the schema, resolvers, and caching layer — so front-end teams, mobile apps,
     and chatbots can query your content like a database." *(voice cleanup:
     `[OLD]` "— enabling front-end teams…" → "— so front-end teams… can"; "enable"
     is a banned verb.)*
  3. **Headless & Decoupled Delivery** — "Publish structured content as JSON to
     headless CMS platforms (Contentful, Strapi) or custom REST APIs. The content
     is authored once in DITA and delivered to any front-end — React portals,
     mobile apps, kiosk displays, VR/AR interfaces — without format lock-in."
  4. **Static Site Generators** — "Build DITA output into Jamstack-ready sites
     using Gatsby, Astro, Hugo, or Eleventy. Combined with CDN deployment
     (CloudFront, Netlify, Vercel), your documentation loads in milliseconds with
     zero server infrastructure to maintain." *(voice cleanup: `[OLD]` opened
     "Transform DITA output into…" → "Build…"; reads less marketing-led. Keep
     "transform" only where it's the literal XSLT term.)*
  5. **Docs-as-Code Pipelines** — "Git-based authoring workflows with pull requests,
     branch previews, and automated quality checks. Every commit triggers
     validation, build, and deploy — the same CI/CD discipline your engineering
     team applies to code, now applied to content."
  6. **Containerized Build Environments** — "DITA-OT packaged in Docker containers
     for reproducible builds across developer machines, CI servers, and cloud
     platforms. No more 'works on my machine' — every build runs in an identical,
     version-locked environment."

### S4 — The Core Transformation Engine · `[OLD]` (3 cards)
- *Heading keeps "Transformation" — the literal XSLT/transform term (allowed by the
  voice rule). Flagged for confirmation.*
- **Intro** `[OLD]`: "Your content is XML data. To the user, it needs to be a
  beautiful PDF or a responsive website. We build the engines that make that
  conversion happen automatically."
- **3 cards** `[OLD]`:
  1. **DITA-OT Customization** — "The DITA Open Toolkit is the industry standard
     engine. We write custom plugins (XSLT/Java) to override default behaviors,
     ensuring your fonts, colors, and layouts match your corporate branding
     exactly."
  2. **XSL-FO & PDF Formatting** — "Print is not dead. We master XSL-FO (Formatting
     Objects) to handle complex pagination, float handling, change bars, and
     multi-column layouts for regulatory PDF deliverables."
  3. **Responsive HTML5** — "We build modern, Bootstrap-based or custom HTML5
     outputs that integrate with your corporate website. We handle search indexing,
     TOC generation, and context-sensitive linking."

### S5 — The Rendering Pipeline · `[OLD]` (5-step strip)
- **5 steps** `[OLD]` (`01–05`, amber connectors):
  1. **Source** — "Verified DITA Map"
  2. **Pre-Process** — "Link resolution & keyref expansion"
  3. **Transformation** — "XSLT application"
  4. **Post-Process** — "CSS / JS injection"
  5. **Artifact** — "Final PDF / ZIP"
- *Open: old strip is label + sub-label only (no `01–05`). Proposing the numbered
  roadmap pattern for consistency with DITA's workflow strip; alt = un-numbered.*

### S6 — Automated Localization Publishing · `[OLD]` (callout)
- **Heading** `[OLD]`: "Automated Localization Publishing"
- **Body** `[OLD]`: "One of the biggest bottlenecks in publishing is handling
  languages. Our pipelines automatically detect the `xml:lang` attribute of the
  root map and switch the generated static text (like 'Table of Contents' becoming
  'Table des matières') automatically. We configure font-mappings to ensure CJK
  (Chinese, Japanese, Korean) characters render correctly without tofu boxes."
- *Treatment: `#fef3c7` callout (old page used a green left-border box → our amber),
  inline `<code>` for `xml:lang`.*

### S7 — Advanced Output Formats · `[OLD]` (6 cards, 4+2, icons)
- **Intro** `[OLD]`: "Not every deliverable is a PDF or a website. We build custom
  transforms for specialized output targets." *(transform = literal XSLT term.)*
- **6 cards** `[OLD]`:
  1. **EPUB 3 & Digital Publishing** — "Accessible, reflowable eBooks with embedded
     media, MathML equations, and semantic navigation. We build EPUB3 outputs that
     pass validation and render consistently across Kindle, Apple Books, and Kobo."
  2. **Markdown & Developer Docs** — "Convert DITA to GitHub-flavored Markdown for
     developer portals, README files, and wikis. API reference content authored in
     DITA publishes alongside code in the same repository and rendering pipeline
     developers already use." *(voice cleanup: `[OLD]` opened "Transform DITA to…"
     → "Convert…")*
  3. **Embedded Help & Microcontent** — "Deliver topic fragments — tooltips, inline
     hints, contextual panels — directly into application UIs. We build the API
     layer and JavaScript widgets that pull DITA-sourced microcontent into your
     product in real time."
  4. **SCORM & eLearning Packages** — "Package DITA Learning & Training content as
     SCORM 1.2 or 2004 modules. We build the transform layer that adds interactive
     assessments, completion tracking, and LMS API integration — from the same
     structured source as your documentation."
  5. **JSON & YAML Data Feeds** — "Structured content as machine-readable data. We
     build DITA-OT plugins that output JSON or YAML — feeding product catalogs,
     configuration portals, knowledge bases, and AI/RAG pipelines from your single
     source."
  6. **Multi-Brand & White-Label** — "One source, multiple brand identities. We
     configure parameterized publishing pipelines where logos, color schemes, legal
     text, and terminology switch automatically based on build profiles —
     supporting OEM and partner documentation programs."

### S8 — Related Services · `[OLD]` (3 cards)
- **DITA Engineering** → `/services/dita-engineering` — "Topic modeling,
  specialization, and constraint modules for scalable content architectures."
- **XML Engineering** → `/services/xml-engineering` — "Custom schema design, XSLT
  transformation, and validation pipelines." *(404 until built.)*
- **CCMS Services** → `/services/ccms-services` — "Platform selection,
  configuration, and ongoing support for enterprise content management."
  *(404 until built.)*

### S9 — CTA (closing) · `CTAModule` (compact + accentLine)
- **Heading** `[DRAFT]`: "Sample Output Build"
- **Body** `[DRAFT]`: "Send us a sample DITA map and the output you need — PDF,
  HTML5, EPUB, or a data feed. We'll build a proof-of-concept render and return the
  pipeline plan: transforms, plugins, and the automation to keep it current. No
  commitment required."

### Removed
- Old text breadcrumb (→ sibling switcher), footer nav.

---

## 6. Decision log
- **D-1 — H1 "Publishing Engineering & Automation".** *(Locked.)*
- **D-2 — Hero visual B** (one source → many outputs fan; output-format leaves to
  differentiate from the TW reuse fan). *(Locked.)*
- **D-3 — Faithful, all 7 sections; CTA-as-closer added.** *(Locked.)*
- **D-4 — Bespoke + shared atoms, `pub-` prefix.** *(Locked.)*
- **D-5 — Voice cleanups on `[OLD]` copy:** drop "enabling" (GraphQL card); swap
  sentence-leading "Transform…" → "Build…/Convert…" on the Static-Site and Markdown
  cards (keep "transform" only as the literal XSLT term). *(Proposed.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| S1 Hero | `Hero` + visual B | New copy — `[DRAFT]` subdeck, node-graph SVG |
| S2 Switcher | `SectionSiblings` (services) | Reuse — current="publishing-engineering" |
| S3 Modern Pub Tech | section + 6 icon cards (4+2) | **New** |
| S4 Core Engine | section + 3 cards | **New** |
| S5 Rendering Pipeline | inline 5-step strip | **New** — `01–05` |
| S6 Localization | `#fef3c7` callout + inline `<code>` | **New** |
| S7 Advanced Formats | section + 6 icon cards (4+2) | **New** |
| S8 Related | inline 3-card row | **New** |
| S9 CTA | `CTAModule` | Reuse — `compact` + `accentLine`, `[DRAFT]` body |
| Page | `services/publishing-engineering.astro` | **New file** |

**Cross-cutting:**
- Clears 1 more dead `/services/<slug>` link; 3 still 404 after (ccms-services,
  system-integration, xml-engineering).
- Spacing-token trap: only `--space-{1,2,3,4,5,6,8,12,16,20,24,32}` exist.
- Delete the temp mock page `publishing-engineering-mock.astro` at build time.
- Verify on the local preview at 1280×900 / 375×812.

---

## 8. Open items for review
1. **Hero subdeck** `[DRAFT]` (S1) — approve / edit / use the closer-to-`[OLD]` alt.
2. **CTA** `[DRAFT]` heading + body (S9) — approve / edit.
3. **Voice cleanups (D-5)** — OK to drop "enabling" and swap the two leading
   "Transform…" verbs?
4. **"The Core Transformation Engine"** heading — keep faithful (transformation =
   literal XSLT term) or rename?
5. **Rendering Pipeline** — numbered `01–05` (like DITA) or un-numbered labels?
