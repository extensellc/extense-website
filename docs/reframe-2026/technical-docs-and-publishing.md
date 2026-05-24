# Technical Docs & Publishing (sub-page) — Reframe Plan

> Status: **implemented** on `redesign-2026` — build clean, preview-verified
> (desktop + mobile). Not yet committed; awaiting your review of the built page.
> Tags: `[OLD]` (ex-tense.co) / `[NEW]` (current
> extense.co, live) / `[DRAFT]` (net-new, needs approval). Conventions in
> [README.md](README.md).
>
> **Direction (locked this session):** rebuild the page **body** to mirror the
> old site's section set — **Modern Publishing Architecture · Multi-Channel
> Output Formats · Headless Content Delivery · Explore Related Solutions** — in
> the new design system. Drop the new-site-invented sections (Problem, Pipeline
> "build artifact," standalone Localization, AI-Assisted Authoring) and the
> old-site DITA-OT Customization section. Keep the hero, sub-page nav, and CTA
> as structural chrome.
>
> **Why the pivot is low-risk on claims:** the surviving sections use **`[OLD]`
> copy already published on ex-tense.co** rather than the pre-reframe `[NEW]`
> invented claims (DITA-OT 4.x / vendor list / 85% / 21 CFR Part 11), which lived
> in the now-dropped Pipeline, editorial Outputs, and Localization sections.

---

## 1. Page job

- **URL:** `/solutions/technical-docs-and-publishing`
- **Primary reader:** a problem-aware buyer who entered by this *specific*
  problem — "we can't ship to every channel from one source," "our docs are
  authored five times in five tools." A documentation/content-ops lead or a
  publishing engineer evaluating whether Extense can run the pipeline.
- **The one job:** show the **publishing architecture** (one DITA source →
  every channel), enumerate **what it produces** (the output formats + headless
  delivery), and route to a related solution/service — then convert. The "why
  structured content" is already settled.

---

## 2. Inventory — OLD site (ex-tense.co/solutions/technical-documentation-publishing.html)

1. **Hero** — "Technical Documentation & Publishing" / "Automate your delivery
   pipeline and produce world-class documentation."
2. **Modern Publishing Architecture** — intro ("We move beyond static Word
   documents. Our solution leverages structured content (DITA/XML) to enable:")
   + 3 bullets (Single-Source Publishing · Content Reuse · Automated Formatting)
   + DITA Source → Transformation → PDF/HTML5 diagram + **Key Benefits** sidebar
   (40% translation cut · faster time-to-market · consistent branding · error
   reduction via reuse).
3. **DITA-OT Customization** — *(dropped — not requested.)*
4. **Multi-Channel Output Formats** — "From the same DITA source, we generate
   pixel-perfect output for every channel your audience needs." 6 cards.
5. **Headless Content Delivery** — "Modern documentation goes beyond static
   files…" 3 cards (API/REST · Chatbot & AI · Embedded Help).
6. **AI-Assisted Authoring** — *(dropped — not requested.)*
7. **Free Content Health Check** CTA.
8. **Explore Related Solutions** — Content Migration & Modernization (SOLUTION) +
   DITA Engineering (SERVICE).
9. **Newsletter** — *(prohibited.)*

## 3. Inventory — NEW site (current, live, pre-reframe build)

Hero (`TechDocsHero`, "One source. Every output channel." + starburst) →
Siblings nav → **Problem** ("What unstructured publishing costs") → **Pipeline**
("output is a build artifact," 5 stages) → **Outputs** ("Five outputs, one
source," 5 editorial blocks) → **Localization** (72%) → single `/services`
cross-link → CTA.

**Disposition:** keep Hero + Siblings + CTA. Cut Problem, Pipeline, Localization
(72% folds into §Architecture). Rebuild Outputs → Multi-Channel cards. Build new
Architecture + Headless + two-up Related.

---

## 4. Mapping decisions

### Keep from NEW `[NEW]`
- **TechDocsHero** — solution-led, on-thesis. Keep. *(Visual still lists a 6-item
  output set incl. RAG; left illustrative — see Open items.)*
- **SolutionsSiblings**, **CTAModule** — keep unchanged.

### Rebuild to OLD-site sections `[OLD]` (in new design)
- **Modern Publishing Architecture** — `[OLD]` intro + 3 bullets + architecture
  diagram + benefits, with the locked **72%** folded into the benefits (replacing
  the old 40%). New build; may borrow the hero/pipeline diagram vocabulary.
- **Multi-Channel Output Formats** — `[OLD]` card grid, **7 cards** (old 6 +
  IETM as a 7th). Rebuild `TechDocsOutputs` from editorial blocks → card grid.
- **Headless Content Delivery** — `[OLD]` intro + 3 cards. New build. The locked
  **85% retrieval precision** lands in the Chatbot & AI card.
- **Explore Related Solutions** — `[OLD]` two-up: Content Migration (Solution,
  real link) + DITA Engineering (Service → `/services` placeholder). Replaces the
  single generic cross-link.

### Cut
- **TechDocsProblem** (problem-education), **TechDocsPipeline** (build-artifact
  framing; its architecture story folds into §Architecture), **TechDocsLocalization**
  (72% folds into §Architecture), **AI-Assisted Authoring** (not requested),
  **DITA-OT Customization** (not requested). Delete the three bespoke `TechDocs*`
  components that no longer have a home.

### Voice swaps
- §Architecture intro: "…to **enable**:" → "…to **deliver**:" (banned verb).
- §Architecture benefit: "Error reduction **via** reuse" → "…**through** reuse."

---

## 5. Wireframe

Order mirrors the old-site body (solution-led, no problem-education):
**orient → architecture → formats → headless delivery → cross-sell → convert.**
*(Related sits before the CTA so the CTA closes the page — see D-10.)*

### Section 1 — Hero · `TechDocsHero` (kept; body rewritten) · `[NEW]` H1 + `[DRAFT, approved]` body
- Kicker `[NEW]`: `AUTHOR · VALIDATE · BUILD · PUBLISH`
- H1 `[NEW]`: "*One source.* Every output channel."
- Body `[DRAFT, approved]` — rewritten from the original mechanism-led copy
  ("One repository… One DITA-OT build pipeline… emitted from the same source…")
  to a **benefit-led** four-sentence deck (D-11): "Author a topic once, and the
  same DITA source ships as print PDF, responsive HTML5, EPUB3, IETM, SCORM,
  developer portals, and AI-ready retrieval. One correction updates every
  channel and every locale — the manual, the portal, and the chatbot never fall
  out of sync. Nobody reformats a release by hand and nobody re-exports to PDF;
  the formatting cycle that used to gate every ship date is gone. And because
  each translated paragraph is reused everywhere it appears, a new format or a
  new market only pays for the segments that actually changed."
- Visual `[NEW]`: animated starburst — unchanged, left illustrative (its boxes
  still read PDF/HTML5/EPUB3/IETM/SCORM/RAG; see Open item 4).

### Section 2 — Sibling nav · `SolutionsSiblings` (keep) · n/a

### Section 3 — Modern Publishing Architecture · NEW build · `[OLD]` + locked 72%
- **Heading** `[OLD]`: "Modern Publishing Architecture"
- **Intro** `[OLD · "enable"→"deliver"]`: "We move beyond static Word documents.
  The publishing architecture is built on structured content — DITA/XML — to
  deliver:"
- **Three bullets** `[OLD]`:
  - **Single-Source Publishing** — "Write once, publish to PDF, HTML5, WebHelp,
    and Mobile formats seamlessly."
  - **Content Reuse** — "Eliminate redundancy by reusing topics across different
    manuals and versions."
  - **Automated Formatting** — "Let the styling engines handle the layout,
    ensuring consistency and brand compliance."
- **Diagram** `[OLD concept, new render]`: DITA Source *(Authoring in XML)* →
  Transformation *(DITA-OT Engine)* → PDF / HTML5. Rendered in the new hairline
  vocabulary (can reuse the hero starburst's node styling).
- **Benefits** `[locked metric + DRAFT sharpened]` — sharpened from the old
  generic checkmark list toward operational specificity (per your call):
  - **72% lower translation cost** `[locked 60/72/85; replaces old "40%"]`
  - **Same-day publish** `[DRAFT]` — no formatting cycle between content
    approval and release.
  - **One stylesheet, every locale** `[DRAFT]` — brand and layout can't drift
    between a manual and its translation.
  - **Fix once, propagate everywhere** `[DRAFT]` — a correction resolves in every
    manual that references the topic; no stale copy survives in a parallel doc.
- *Rationale:* the old-site "light" architecture section is the solution
  statement — it leads the body and carries the headline number (72%). The three
  non-numeric benefits are sharpened from the old generic phrasing ("faster
  time-to-market," "consistent branding worldwide," "error reduction via reuse")
  to concrete, mechanism-anchored claims, with no fabricated numbers.

### Section 4 — Multi-Channel Output Formats · `TechDocsFormats` (rebuilt → 9-card grid) · `[OLD]` ×6 + 3 `[DRAFT]`
- **Heading** `[OLD]`: "Multi-Channel Output Formats"
- **Sub-deck** `[OLD]`: "From the same DITA source, we generate pixel-perfect
  output for every channel your audience needs."
- **Cards (9) — balanced 3×3 grid**, grouped *print · web · specialized*. Page
  order: PDF/Print · Accessible PDF/508 · Word/DOCX · Responsive HTML5 ·
  Mobile/Offline · Markdown/Portals · EPUB/eBook · SCORM/eLearning · IETM. Six
  `[OLD]` formats plus three `[DRAFT, approved]` (Accessible PDF, Word/DOCX, IETM):
  1. **PDF / Print** `[OLD]` — "XSL-FO rendering via Antenna House or Apache FOP.
     Pixel-perfect branded manuals, data sheets, and regulatory submissions with
     TOC, index, cross-references, and change bars — ready for print or
     compliance archives."
  2. **Responsive HTML5** `[OLD]` — "SEO-optimized, searchable web portals with
     custom branded themes. Full-text search, breadcrumb navigation, version
     selectors, and responsive layouts — deployed to any static host, CDN, or
     documentation platform."
  3. **Mobile / Offline** `[OLD]` — "Progressive Web App packages for field
     technicians, service engineers, and remote teams. Cached locally for offline
     access with automatic sync when connectivity returns — no app store
     required."
  4. **EPUB / eBook** `[OLD]` — "Reflowable EPUB3 output for training guides,
     onboarding handbooks, and reference manuals. Distribute through enterprise
     LMS platforms, intranets, or standard eBook readers with full accessibility
     support."
  5. **Markdown / Developer Portals** `[OLD]` — "Export DITA to clean Markdown
     for GitHub wikis, ReadMe.io, Docusaurus, and developer portals. Maintain a
     single DITA source of truth while publishing natively to platforms your
     developers already use."
  6. **SCORM / eLearning** `[OLD]` — "Package DITA learning content as SCORM 1.2
     or 2004 modules for your LMS. Quizzes, assessments, and completion tracking
     built from the same structured source — no duplicate authoring in a separate
     courseware tool."
  7. **IETM** `[DRAFT — approved]` — "S1000D-adjacent interactive
     electronic technical manuals for field service and maintenance. Procedural
     maps drive step-by-step workflows; the same DITA topics that produce the PDF
     and the portal drive the interactive manual — no re-authoring." *(not on the
     old page; net-new copy, kept per your call.)*
  8. **Accessible PDF / Section 508** `[DRAFT — approved]` — "Tagged, accessible
     PDF that meets Section 508 and PDF/UA — logical reading order, alt text, and
     tagged tables emitted by the build, not retrofitted. The same accessibility
     metadata carries into the HTML5 output." *(added to balance the grid; 508 is
     an existing trust badge.)*
  9. **Microsoft Word / DOCX** `[DRAFT — approved]` — "Microsoft Word and DOCX
     from the same DITA source — for stakeholders who review and redline in Word.
     Edits round-trip back into structured content; the review copy and the
     published manual never diverge." *(added to balance the grid.)*
- *Rationale:* the offer detail — the channels produced from the one source. Card
  grid matches the old-site treatment, restyled to new design. Nine cards make a
  balanced 3×3 (the seventh, IETM, otherwise orphaned a row). Each card carries an
  amber mono index, a short amber accent rule that draws in on scroll, and a hover
  lift (D-12, D-13).

### Section 5 — Headless Content Delivery · NEW build · `[OLD]` + locked 85%
- **Heading** `[OLD]`: "Headless Content Delivery"
- **Sub-deck** `[OLD]`: "Modern documentation goes beyond static files. We build
  headless delivery pipelines using Deploy APIs that push structured content to
  customer portals, mobile apps, chatbots, and embedded help — all from the same
  DITA source."
- **Cards (3):**
  1. **API / REST Endpoints** `[OLD]` — "Expose your DITA content as JSON/REST
     APIs. Embed documentation directly into products, self-service portals, and
     knowledge bases without duplicating a single paragraph."
  2. **Chatbot & AI Integration** `[OLD]` + `[DRAFT clause — approved]` —
     "Feed structured content into conversational AI and chatbots. DITA's
     semantic markup makes your docs retrieval-ready for RAG pipelines and LLM
     grounding — measured at 85% retrieval precision." *(85% is the locked
     60/72/85 figure; the appended clause is the only `[DRAFT]` wording here.)*
  3. **Embedded Help & Microcontent** `[OLD]` — "Deliver context-sensitive help
     directly inside your application UI. DITA short descriptions and microcontent
     map naturally to tooltips, walkthroughs, and in-app guidance."
- *Rationale:* the advanced-delivery tier — where RAG/85% naturally lives (old
  copy already frames it here). Catches the "docs as a service" buyer. Cards share
  the Multi-Channel treatment: amber index, draw-in accent rule, hover lift (D-13).

### Section 6 — Explore Related Solutions · NEW two-up (replaces `CrossPillarLink`) · `[OLD]`
- **Heading** `[OLD]`: "Explore Related Solutions"
- **Solution** `[OLD]` — eyebrow "SOLUTION"; "Content Migration & Modernization"
  → `/solutions/content-migration`; "Migrate legacy content to structured DITA
  XML with automated pipelines."
- **Service** `[OLD]` — eyebrow "SERVICE"; "DITA Engineering" → `/services`
  *(placeholder — the 7 `/services/*` detail pages don't exist yet)*; "Topic
  modeling, specialization, and content architecture."

### Section 7 — CTA (closing) · `CTAModule` (keep) · `[NEW]`
- Compact "Sample Content Assessment." Closes the page, consistent with the
  homepage and the other three solution sub-pages (CTA-as-closer). See D-10.

### Removed
- Problem, Pipeline, standalone Localization, AI-Assisted Authoring sections.

---

## 6. Decision log

- **D-1 — Body = the four old-site sections.** Architecture · Multi-Channel ·
  Headless · Explore Related. Hero/Siblings/CTA kept as chrome. *(Agreed.)*
- **D-2 — 72% folds into §Architecture benefits**, replacing the old 40%.
  *(Agreed.)*
- **D-3 — IETM kept as a 7th Multi-Channel format** (defense/S1000D value),
  though absent from the old page → its copy is `[DRAFT]`. *(Agreed.)*
- **D-4 — §Architecture built "light"** per the old site (intro + 3 bullets +
  diagram + benefits); the new Pipeline's 5-stage / "build artifact" depth is
  dropped. *(Agreed.)*
- **D-5 — 85% lands in Headless → Chatbot & AI** (locked metric; appended
  clause). *(Approved.)*
- **D-9 — Sharpen the §Architecture benefits** from the old generic list to
  mechanism-anchored claims (72% kept as the locked lead). *(Agreed; sharpened
  copy `[DRAFT]` pending final nod.)*
- **D-6 — Cut** Problem, Pipeline, Localization, AI-Authoring, DITA-OT
  Customization; delete the orphaned `TechDocs*` components. *(Agreed / proposed.)*
- **D-7 — Two-up Related** (Solution + Service), per the old site. *(Agreed.)*
- **D-8 — "Transform" label** — moot; the Pipeline section that carried it is
  dropped. *(Resolved by D-6.)*
- **D-10 — Related before CTA (deviation from the approved §5).** The approved
  doc had CTA → Related (old-site order). At build, switched to **Related → CTA**
  so the CTA closes the page: (a) matches the homepage CTA-as-closer pattern and
  all three sibling solution sub-pages; (b) avoids sandwiching a page-bg Related
  band between the elevated CTA and the elevated Footer. *Flagged for your veto.*
- **D-11 — Hero body rewritten benefit-led.** The original sub-deck was
  mechanism-led (described the apparatus: one repo, one pipeline, "emitted from
  the same source…"). Rewritten to a four-sentence outcome-led deck (author once
  → ships everywhere; one edit → every channel current; formatting cycle gone;
  translate only what changed). Also corrects the stale "six outputs … RAG" list.
  *(Approved.)*
- **D-12 — Multi-Channel grid → 9 cards (3×3).** 7 cards orphaned the IETM card
  (3+3+1). Added two real DITA-OT outputs — **Accessible PDF / Section 508** and
  **Microsoft Word / DOCX** (`[DRAFT, approved]`) — for a balanced 3×3. *(Approved.)*
- **D-13 — Card color + motion.** Both card sections (Multi-Channel + Headless)
  get an amber mono index, a short amber accent rule that draws in on scroll, and
  a hover lift. Hover uses the independent `translate` property so it composes
  with the reveal's `transform` instead of fighting it. *(Approved.)*

---

## 7. Build inventory

| Section | Component | Action |
|---|---|---|
| 1 Hero | `TechDocsHero` | Keep |
| 2 Siblings | `SolutionsSiblings` | Keep |
| 3 Architecture | `TechDocsArchitecture` (new) | **New build** — intro + 3 bullets + diagram + 4 benefits (72%) |
| 4 Multi-Channel | `TechDocsFormats` (new; replaced `TechDocsOutputs`) | **Rebuild** — 9-card 3×3 grid, `[OLD]`×6 + 3 `[DRAFT]`; amber index/accent/hover |
| 5 Headless | `TechDocsHeadless` (new) | **New build** — intro + 3 cards (85% in card 2); amber index/accent/hover |
| 6 CTA | `CTAModule` | Keep |
| 7 Related | `TechDocsRelated` (new) | **New build / replaced `CrossPillarLink` usage** — two-up Solution + Service |
| — | `TechDocsProblem`, `TechDocsPipeline`, `TechDocsLocalization`, `TechDocsOutputs` | **Deleted** (orphaned) |
| Page | `technical-docs-and-publishing.astro` | **Edit** — Hero → Siblings → Architecture → Formats → Headless → Related → CTA |

New builds: 4 (Architecture, Formats, Headless, Related). Deletes: 4 components
(incl. `TechDocsOutputs`) + removed `CrossPillarLink` usage (component kept; the
other three sub-pages still use it). Keeps: 3 (Hero, Siblings, CTA).

**Border-stitch note:** Siblings carries a `border-bottom`; the section directly
below (Architecture) must not double it with a `border-top`. Re-verify dividers
top-to-bottom after the rebuild.

---

## 8. Open items for review
1. ~~IETM card copy~~ — **approved.**
2. ~~85% clause on Chatbot & AI~~ — **approved.**
3. ~~Soft benefits~~ — **sharpen** (D-9); sharpened `[DRAFT]` copy in §5 Section 3
   pending a final nod before implement.
4. ~~Hero visual~~ — **leave illustrative** (no SVG change).

All resolved bar the final nod on the sharpened benefit lines (item 3).
