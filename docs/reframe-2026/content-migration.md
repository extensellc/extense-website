# Content Migration (sub-page) — Reframe Plan

> Status: **implemented** on `redesign-2026` — build clean, preview-verified
> (desktop + mobile). Not yet committed; awaiting your review of the built page.
> Tags: `[OLD]` (ex-tense.co) / `[NEW]` (current extense.co, live) / `[DRAFT]`
> (net-new, needs approval). Conventions in [README.md](README.md).
>
> **Direction (locked this session):** same recipe as Technical Docs — rebuild
> the body to the **old-site sections** in the new design; cut the
> problem-education section; keep Hero/Siblings/CTA as chrome; amber card
> treatment (index + draw-in accent + hover lift); CTA-as-closer.
>
> **Metrics ruling (locked):** the old Content Migration & Modernization page's
> prose, text, and metrics are **authoritative** (Extense's typical results) —
> use them verbatim as `[OLD]`. Feature the old page's **15–30% deduplication**
> figure. Drop the current page's unverified **45% reuse** claim, and don't
> introduce **10×** (it wasn't on the old sub-page).

---

## 1. Page job

- **URL:** `/solutions/content-migration`
- **Primary reader:** a buyer with a stuck or scary legacy estate (FrameMaker,
  Word, RoboHelp, InDesign, SGML, scanned PDF) who needs it in clean DITA and
  doesn't trust a hand-rekey to finish or to find the redundancy.
- **The one job:** show **what we convert from** (breadth), **what the
  conversion produces** (source → DITA → AI-ready), the **deduplication payoff**,
  and the **process**, then route + convert.

---

## 2. Inventory — OLD site (ex-tense.co/solutions/content-migration-modernization.html)

1. **Hero** — "Content Migration & Modernization" / "Unlock the value of your
   legacy data." *("unlock" is a banned verb.)*
2. **Source Formats We Convert From** — chip band: Microsoft Word, FrameMaker,
   InDesign, RoboHelp, MadCap Flare, DocBook, HTML, Markdown, AuthorIT,
   Confluence, SGML, Excel, PDF (OCR).
3. **How Conversion Works** — intro + 3 columns (Source Document / DITA Output /
   AI-Ready Content), each a 5-item checklist.
4. **Automatic Topic Deduplication** — prose; *"Typical result: 15–30% of topics
   identified as duplicates and consolidated in the first pass."*
5. Free Content Health Check CTA.
6. **The Modernization Journey** — intro + 5-step strip (Analyze → Model →
   Transform → Enrich → Go Live) + 3 cards (Legacy Conversion / Metadata
   Strategy / Quality Assurance).
7. **Explore Related Solutions** — CCMS Implementation & Integration · Technical
   Documentation & Publishing · XML Data Interoperability.
8. Newsletter *(prohibited)* · Footer.

## 3. Inventory — NEW site (current, live, pre-reframe build)

Hero (`ContentMigrationHero`, "The conversion that finishes." + funnel SVG) →
Siblings → **Problem** ("Why manual conversion never finishes" — *problem-ed*) →
Pipeline (Audit→Model→Convert→Deduplicate→Validate) → Sources (5 editorial
blocks) → ROI ("Recovery rate… **45% reuse**") → generic `/services` link → CTA.

**Disposition:** keep Hero + Siblings + CTA. Cut Problem. Replace Pipeline →
Modernization Journey, Sources → Source Formats + How Conversion Works, ROI →
Automatic Topic Deduplication. Add Explore Related (3-up). Delete the four
orphaned `ContentMigration*` components (Problem/Pipeline/Sources/ROI).

---

## 4. Mapping decisions

### Keep from NEW `[NEW]`
- **ContentMigrationHero** — solution-led, on-pattern. Keep (D-3; hero-body
  rewrite proposed as an open item).
- **SolutionsSiblings**, **CTAModule** — keep. CTA gains `accentLine` for parity.

### Rebuild to OLD-site sections `[OLD]` (new design)
- **Source Formats We Convert From** — chip band, the 13 `[OLD]` formats.
- **How Conversion Works** — 3-column source→DITA→AI-ready, `[OLD]` checklists.
- **Automatic Topic Deduplication** — `[OLD]` prose, 15–30% featured.
- **The Modernization Journey** — `[OLD]` 5-step strip + 3 capability cards.
- **Explore Related Solutions** — `[OLD]` 3-up, remapped to real pages (D-5).

### Cut
- **ContentMigrationProblem** (problem-education). Delete.
- **ContentMigrationPipeline / Sources / ROI** — superseded by the rebuilt
  sections; delete.

### Voice swaps (D-4)
- Modernization Journey intro: "we **transform** information architecture" →
  "we **re-engineer** information architecture" (banned verb).
- Metadata Strategy card: "taxonomy tags…**to enable** future faceted search" →
  "…**for** future faceted search."
- Step-name **"Transform"** kept — it's the literal XML-transformation step, not
  the marketing verb (same call as TDP D-8).

---

## 5. Wireframe

Order mirrors the old-site body: **orient → breadth → what you get → payoff →
process → cross-sell → convert.**

### Section 1 — Hero · `ContentMigrationHero` (keep) · `[NEW]`
- Kicker `AUDIT · CONVERT · DEDUPE · VALIDATE`; H1 "The conversion that
  *finishes.*"; funnel SVG (many inputs → one deduplicated warehouse).
- **Open item (D-3):** the body is a bit mechanism-led (the apparatus:
  "audited… parsed… deduplicated… validated"). Proposed benefit-led `[DRAFT]`
  rewrite: *"Hand a twenty-year estate of FrameMaker, Word, RoboHelp, InDesign,
  and scanned PDF to a pipeline that actually finishes — clean DITA, the
  duplicates already collapsed, every topic traceable to the source it came
  from. The migration that used to stall in a typing pool ships on a schedule."*
  Keep current vs swap in?

### Section 2 — Sibling nav · `SolutionsSiblings` (keep)

### Section 3 — Source Formats We Convert From · NEW `ContentMigrationFormats` · `[OLD]`
- **Heading** `[OLD]`: "Source Formats We Convert From"
- **Chips** `[OLD]`: Microsoft Word · FrameMaker · InDesign · RoboHelp · MadCap
  Flare · DocBook · HTML · Markdown · AuthorIT · Confluence · SGML · Excel ·
  PDF (OCR). Hairline/mono chips, viewport reveal.
- *Rationale:* breadth/relevance first — "yes, we handle what you have."

### Section 4 — How Conversion Works · NEW `ContentMigrationConversion` · `[OLD]`
- **Intro** `[OLD]`: "Our conversion methodology combines proven migration tools
  with deep DITA expertise to handle the heavy lifting. You focus on quality."
- **3 columns** `[OLD]`, amber-indexed, with amber arrows between (Source → DITA
  → AI-Ready):
  - **Source Document** — Inconsistent heading styles · Manual numbered lists ·
    Embedded images at random DPI · No metadata or taxonomy · Duplicate content
    across files.
  - **DITA Output** — Clean topic types (concept, task, reference) · Semantic
    `<ol>`/`<steps>` markup · Normalized images, consistent DPI · Rich metadata +
    SubjectScheme keys · Deduplicated with conref/conkeyref reuse.
  - **AI-Ready Content** — Chunked topics optimized for RAG retrieval ·
    Schema.org + JSON-LD metadata mapping · Semantic labels for LLM grounding +
    citation · Embedding-friendly short descriptions per topic · Knowledge-graph
    nodes from the subject-scheme taxonomy.
- *Rationale:* the offer — what the conversion produces, end state forward.

### Section 5 — Automatic Topic Deduplication · NEW `ContentMigrationDeduplication` · `[OLD]`
- **Heading** `[OLD]`: "Automatic Topic Deduplication"
- **Body** `[OLD]`: "During conversion, we analyze every paragraph and span
  across your entire document collection using industry-proven migration tools
  and structured content analysis. Exact-match duplicates are identified and
  consolidated into reusable warehouse topics with conref pointers — saving you
  from discovering redundancy months later."
- **Punch** `[OLD]`: "Typical result: **15–30% of topics identified as duplicates
  and consolidated in the first pass.**" (primary-color emphasis, not an amber
  stat block — single-accent rule.)
- *Rationale:* the compounding payoff; the headline metric (D-2).

### Section 6 — The Modernization Journey · NEW `ContentMigrationJourney` · `[OLD]` + voice swaps
- **Intro** `[OLD · "transform"→"re-engineer"]`: "We don't just move files; we
  re-engineer information architecture. From unstructured chaos to intelligent,
  reusable XML."
- **5-step strip** `[OLD]` (same vocabulary as the retired Pipeline):
  Analyze *(Dedup & Audit Legacy Source)* → Model *(Define Information
  Architecture)* → Transform *(Automated XML Conversion)* → Enrich *(Add Semantic
  Metadata)* → Go Live *(Validate, Baseline & Hand Off)*.
- **3 cards** `[OLD]`, amber card treatment:
  - **Legacy Conversion** — "We build custom parsers for FrameMaker, InDesign,
    Word, and RoboHelp to extract maximum structure."
  - **Metadata Strategy** `[OLD · "enable"→"for"]` — "Applying taxonomy tags
    during migration for future faceted search and dynamic filtering."
  - **Quality Assurance** — "Automated schematron validation ensures every
    migrated topic adheres to your new content model."
- *Rationale:* the method + capability proof, after the offer.

### Section 7 — Explore Related Solutions · NEW `ContentMigrationRelated` · `[OLD]` (remapped)
- **Heading** `[OLD]`: "Explore Related Solutions" — 3-card grid, amber treatment.
  - **Technical Documentation & Publishing** `[OLD]` (SOLUTION) →
    `/solutions/technical-docs-and-publishing`; "End-to-end documentation and
    multi-channel publishing with DITA-OT."
  - **XML Data Interoperability** `[OLD]` (SOLUTION) →
    `/solutions/xml-data-interoperability`; "XML integration, transformation, and
    API-driven content delivery."
  - **CCMS Implementation & Integration** `[OLD]` (**SERVICE** → `/services`
    placeholder; CCMS is a service in the new IA); "Platform selection,
    configuration, and integration for content management."
- **Open item:** label the CCMS card "CCMS Implementation & Integration" (old
  title) or "CCMS Services" (new IA name)?

### Section 8 — CTA (closing) · `CTAModule` (keep, + `accentLine`) · `[NEW]`
- Compact "Sample Content Assessment" + the animated amber line. CTA-as-closer
  (D-6).

### Removed
- Problem, Pipeline, Sources, ROI sections.

---

## 6. Decision log
- **D-1 — Rebuild body to old-site sections; cut Problem.** *(Agreed.)*
- **D-2 — Old-site copy/metrics authoritative;** feature 15–30% dedup; drop the
  current 45% reuse; no 10×. *(Agreed.)*
- **D-3 — Keep `[NEW]` hero + funnel** (old "Unlock…" has a banned verb).
  *Hero-body benefit-led rewrite proposed — confirm.*
- **D-4 — Voice swaps:** intro "transform"→"re-engineer"; card "enable"→"for";
  step name "Transform" kept (technical). *(Proposed.)*
- **D-5 — Explore Related remap:** 2 Solutions (TDP, XML Interop) + 1 Service
  (CCMS → `/services`). *(Proposed.)*
- **D-6 — CTA-as-closer + `accentLine`** (per TDP D-10 + parity). *(Following.)*
- **D-7 — Amber card treatment** (index + draw-in accent + hover lift) on the
  How-Conversion columns, the 3 Journey cards, and the Related cards (per TDP
  D-13). *(Following.)*
- **D-8 — Delete** ContentMigrationProblem/Pipeline/Sources/ROI. *(Agreed.)*

---

## 7. Build inventory

| Section | Component | Action |
|---|---|---|
| 1 Hero | `ContentMigrationHero` | Keep (optional benefit-led body rewrite — D-3) |
| 2 Siblings | `SolutionsSiblings` | Keep |
| 3 Source Formats | `ContentMigrationFormats` (new) | **New build** — `[OLD]` chip band |
| 4 How Conversion Works | `ContentMigrationConversion` (new) | **New build** — 3-col source→DITA→AI-ready, amber + arrows |
| 5 Auto Dedup | `ContentMigrationDeduplication` (new) | **New build** — `[OLD]` prose + 15–30% punch |
| 6 Modernization Journey | `ContentMigrationJourney` (new) | **New build** — 5-step strip + 3 cards (amber) |
| 7 Explore Related | `ContentMigrationRelated` (new) | **New build** — 3-up, remapped |
| 8 CTA | `CTAModule` | Keep + `accentLine` |
| — | `ContentMigrationProblem/Pipeline/Sources/ROI` | **Delete** (orphaned) |
| Page | `content-migration.astro` | **Edit** — new imports + order; drop `CrossPillarLink` usage (component kept) |

New builds: 5. Deletes: 4 components + removed `CrossPillarLink` usage. Keeps: 3.

**Border-stitch note:** Siblings carries `border-bottom`; the section below
(Source Formats) must not double it with a `border-top`. Re-verify dividers.

---

## 8. Open items for review
1. **Hero body** — keep current (mechanism-led) or swap in the benefit-led
   `[DRAFT]` rewrite (§5 Section 1)?
2. **CCMS related card** — "CCMS Implementation & Integration" (old title) vs
   "CCMS Services" (new IA name)?
3. Confirm the **voice swaps** (D-4).
