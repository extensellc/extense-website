# DITA Engineering (service detail) — Reframe Plan

> Status: **implemented — pending staging sign-off.** Third of the 7 `/services/<slug>` detail
> sub-pages, and the **largest** (11 content sections). Built **bespoke**
> (page-local CSS), reusing the shared atoms (`Hero`, `SectionSiblings`,
> `CTAModule`) and the proven patterns from TW/SCS (card grid, `#fef3c7`
> callout, 5-step `01–0N` roadmap strip, related-card). Decisions locked:
> **faithful — all 11 sections**; hero subdeck = **A**; **text-only hero**.
> Tags: `[OLD]` (ex-tense.co/services/dita-engineering.html) / `[NEW]` / `[DRAFT]`.
> Conventions in [README.md](README.md); model = the shipped
> [technical-writing-content-development.md](technical-writing-content-development.md)
> and [structured-content-strategy.md](structured-content-strategy.md).

---

## 1. Page job
- **URL:** `/services/dita-engineering`
- **Primary reader:** an information architect / docs-platform owner / technical
  evaluator judging whether Extense can engineer DITA *at depth* — specialization,
  constraints, SubjectScheme, conversion, IA, DITA-OT — not just author in it.
- **The one job:** prove deep DITA engineering capability across the full
  lifecycle (model → convert → architect → deliver → operate), then convert.

> **Note (overlap, accepted):** §6 Legacy Conversion overlaps
> `/solutions/content-migration`; §8 AI-Ready overlaps
> `/solutions/ai-ready-content`; §9–10 (Delivery & Hosting, DITA-OT Services)
> overlap the *Publishing Engineering* service page. Per owner: keep all
> (faithful). Related cards + cross-links can point readers to the owning pages.

---

## 2. Inventory — OLD page (11 sections)
Hero → Backbone (Why Engineering Matters + Core Competencies callout) →
Engineering Workflow (5-step) → Specialization/Constraints/SubjectScheme (3
cards) → Case Study (Semiconductor) → Legacy Conversion (3 cards + dedup) → IA
for DITA (6-item checklist + Governance callout) → AI-Ready (3 cards + Data
Asset) → Delivery & Hosting (6 cards) → DITA-OT Services (6 cards) → Related (3
cards). No closing CTA on the old page.

## 3. Inventory — NEW site
Page doesn't exist (sibling switcher + `/services` card link here, 404 until
built). Reuse: `Hero` (text-only), `SectionSiblings` (services), `CTAModule`
(closer). Page-local patterns from TW/SCS: hairline card + bare amber line icon,
`#fef3c7` callout, `01–0N` strip, related-card. **New page-local bits:** inline
`<code>` styling, a 6-item ✓ checklist, the case-study box (Scenario/Solution/
Result), side callouts (Core Competencies, Governance Deliverables), and
"sub-block" highlights (Dedup, Data Asset).

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page order; CTA added as closer (parity).
- **Hero subdeck = `[DRAFT]` A** (locked).
- **Cards = new-system idiom** (left-aligned, bare amber line icon, no chip).
- **5-step Workflow** = the SCS roadmap strip pattern (`01–05`, amber connectors).
- **6-card sections** (Delivery & Hosting, DITA-OT Services) = 4+2 grid (echoing
  the TW doc-types grid).
- **Inline code** (`<api-operation>`, `@audience`, etc.) = a mono `code` style
  (subtle tint) so the technical specificity reads as document-grade, not raw.
- **Voice:** all `[OLD]` copy clean (technical terms allowed).

---

## 5. Wireframe

### S1 — Hero · universal `Hero` (text-only)
- **H1** `[OLD]`: "DITA Engineering & Architecture"
- **Subdeck** `[DRAFT, A]`: "Out-of-the-box DITA is rarely enough. We engineer
  the semantic model — specialization, constraints, and SubjectScheme — that
  enforces consistency across teams of 50+ writers and feeds automation, search,
  and AI."

### S2 — Sibling switcher · `SectionSiblings` (variant="services")
- current = **DITA Engineering** (amber + bold).

### S3 — The Backbone of Intelligent Content · `[OLD]`
- **Heading** `[OLD]`: "The Backbone of Intelligent Content"
- **Intro** `[OLD]`: "Standard DITA is powerful, but 'out-of-the-box' is rarely
  enough for enterprise requirements. We engineer the standard to work for you."
- **Two-column:** left = **Why Engineering Matters** `[OLD]`: "Implementing DITA
  without engineering the semantic model is like building a house without a
  blueprint. You might have walls and a roof, but the plumbing won't connect.
  Effective DITA engineering bridges the gap between raw XML standards and your
  specific business logic. It ensures that your content is not just 'structured'
  but **semantically meaningful**, enabling automation, faceted search, and
  dynamic delivery. At Extense, our information architects don't just know the
  tags; we know how to constrain and specialize them to enforce consistency
  across teams of 50+ writers."
  - right = **Core Competencies** callout `[OLD]` (4 ✓): DITA 1.3 & 2.0
    Standards · RNG & DTD Constraints · Schematron Validation · SubjectScheme
    Taxonomy.

### S4 — Our Engineering Workflow · `[OLD]` (5-step strip)
- **Heading** `[OLD]`: "Our Engineering Workflow"
- **5 steps** `[OLD]` (`01–05`, amber connectors; SCS roadmap pattern):
  1. **Analysis** — "Audit existing content for semantic patterns."
  2. **Modeling** — "Define topic types and domain requirements."
  3. **Development** — "Code the DTD/RNG schemas and plugins."
  4. **Validation** — "Implement Schematron rules for QA."
  5. **Deployment** — "Package into CCMS-ready frameworks."

### S5 — Specialization · Constraints · SubjectScheme · `[OLD]` (3 cards)
- *Open item: the old page has these as 3 heading-less cards. Proposing a light
  umbrella heading `[DRAFT]`: "Engineering the Standard" + one-line intro, so the
  section has a header like the others. (Alt: keep heading-less, faithful.)*
- **3 cards** `[OLD]` (with inline `<code>`):
  1. **Specialization** — "We create custom DITA specializations. If you are
     documenting APIs, we build an `<api-operation>` topic type. If you are in
     pharma, we build a `<clinical-protocol>` shell."
  2. **Constraints** — "Too many choices confuse writers. We use DITA constraints
     to remove unused elements (like `<longquoteref>`), simplifying the authoring
     interface and reducing training time."
  3. **SubjectScheme Maps** — "We implement robust metadata taxonomies using
     SubjectScheme. This allows you to control the values allowed in attributes
     like `@audience` or `@platform`, ensuring consistent filtering."

### S6 — Case Study: Semiconductor Fabrication · `[OLD]` (case-study box)
- **Heading** `[OLD]`: "Case Study: Semiconductor Fabrication"
- **Scenario** `[OLD]`: "A client needed to document register maps for 500+
  chips. Manual entry was error-prone."
- **Our Solution** `[OLD]`: "We developed a custom DITA specialization for
  register data and wrote an XSLT transformation to auto-generate the DITA topics
  directly from the engineering IP-XACT files."
- **Result** `[OLD]`: "100% accuracy and zero manual authoring time for reference
  data."
- *Treatment: a bordered/`#fef3c7` box with mono labels (Scenario / Solution /
  Result).*

### S7 — Legacy Content Conversion to DITA · `[OLD]`
- **Heading** `[OLD]`: "Legacy Content Conversion to DITA"
- **Intro** `[OLD]`: "Migrate your existing documentation — Word, FrameMaker,
  HTML, InDesign, or proprietary XML — into clean, structured DITA topics."
- **3 cards** `[OLD]`:
  1. **Source Analysis & Mapping** — "We audit your legacy corpus to identify
     structural patterns, implicit topic boundaries, and reuse candidates. Every
     paragraph style, heading level, and inline convention is mapped to the
     appropriate DITA element before a single file is converted."
  2. **Automated Conversion Pipelines** — "Using industry-proven migration tools
     — Stilo Migrate, custom XSLT/Python scripts, and pandoc-based workflows — we
     automate the bulk conversion. Manual intervention is reserved for edge cases,
     not the rule. Typical throughput: thousands of pages per sprint."
  3. **Post-Conversion QA** — "Automated Schematron validation, side-by-side
     visual diff against the original, and metadata completeness checks. We don't
     hand off until every topic passes structural and content-fidelity gates."
- **Sub-block — Deduplication at Conversion Time** `[OLD]`: "During conversion,
  we analyze every paragraph and span across your entire document collection
  using structured content analysis. Exact-match and near-match duplicates are
  identified, consolidated into reusable warehouse topics with conref pointers,
  and tracked in a deduplication report — saving you from discovering redundancy
  months later. **Typical result:** 15–30% of content identified as duplicate and
  consolidated in the first pass."

### S8 — Information Architecture for DITA · `[OLD]`
- **Heading** `[OLD]`: "Information Architecture for DITA"
- **Subdeck** `[OLD]`: "Structure that scales. We design the IA layer that turns
  a collection of topics into a navigable, filterable, reusable content system."
- **Two-column:** left = **What We Define** 6-item ✓ checklist `[OLD]`:
  - **Topic typing rules** — when to use concept vs. task vs. reference vs.
    troubleshooting
  - **Map hierarchy design** — bookmap, submap, and relationship table structures
    for your deliverables
  - **Key architecture** — keydef maps, key scopes, and variable resolution
    strategies for multi-product content
  - **Reuse strategy** — conref, conkeyref, and content-reference library patterns
    that scale without fragility
  - **Metadata & filtering model** — `@audience`, `@platform`, `@product`, `@rev`
    attributes plus SubjectScheme-controlled values
  - **Naming & folder conventions** — file naming, directory structure, and ID
    strategies that work across CCMS, Git, and CI pipelines
  - right = **Governance Deliverables** callout `[OLD]`: "Every IA engagement
    produces a **DITA Style Guide** — a living document that codifies topic
    templates, element usage rules, metadata requirements, and writing patterns.
    This becomes your team's single source of truth for content standards."

### S9 — AI-Ready Content Engineering · `[OLD]`
- **Heading** `[OLD]`: "AI-Ready Content Engineering"
- **Subdeck** `[OLD]`: "Your DITA content is already structured. We make it
  machine-intelligent — optimized for retrieval, embedding, and LLM grounding."
- **3 cards** `[OLD]`:
  1. **RAG-Optimized Chunking** — "We size and structure topics for optimal
     vector embedding — right-sized for token limits, self-contained for retrieval
     accuracy. Short descriptions become embedding-friendly summaries. Metadata
     becomes filter context."
  2. **Semantic Labeling** — "Every topic carries machine-readable labels — topic
     type, product version, audience, and domain context. When an LLM retrieves a
     chunk, it knows what kind of content it's citing and can attribute the source
     precisely."
  3. **JSON-LD & Knowledge Graph Mapping** — "We map DITA metadata and
     SubjectScheme taxonomies to Schema.org types and RDF triples. Your
     documentation becomes a queryable knowledge graph — not just a file system of
     XML documents."
- **Sub-block — From Documentation to Data Asset** `[OLD]`: "Well-engineered DITA
  is 70% of what you need for an AI content pipeline. The topic architecture
  provides natural chunk boundaries, metadata provides filter dimensions, and
  short descriptions provide ready-made summaries. We close the remaining 30% with
  transform plugins, embedding pipelines, and delivery API integration."

### S10 — Delivery & Hosting · `[OLD]` (6 cards, 4+2)
- **Heading** `[OLD]`: "Delivery & Hosting"
- **Subdeck** `[OLD]`: "Content that's structured but not delivered is content
  that doesn't exist. We build the last mile — from DITA source to live,
  accessible output."
- **6 cards** `[OLD]`: Static Site Publishing · Headless Content APIs · PDF &
  Print · Portal & CMS Integration · Context-Sensitive Help · Hosted
  Documentation Portals. *(Full copy carried verbatim at build.)*

### S11 — DITA-OT Services · `[OLD]` (6 cards, 4+2)
- **Heading** `[OLD]`: "DITA-OT Services"
- **Subdeck** `[OLD]`: "The DITA Open Toolkit is the engine behind every output.
  We keep it running, extend it, and upgrade it."
- **6 cards** `[OLD]`: DITA-OT Upgrades · Custom Plugin Development · CI/CD
  Pipeline Integration · Performance Optimization · Troubleshooting & Support ·
  DITA-OT Managed Service. *(Full copy carried verbatim at build.)*

### S12 — Related Services · `[OLD]` (3 cards)
- **Publishing Engineering** → `/services/publishing-engineering` — "Custom
  multi-channel publishing pipelines for PDF, HTML5, EPUB, and API documentation."
- **XML Engineering** → `/services/xml-engineering` — "Custom schema design, XSLT
  transformation, and validation pipelines."
- **Structured Content Strategy** → `/services/structured-content-strategy` —
  "Information architecture, taxonomy design, and content governance frameworks."

### S13 — CTA (closing) · `CTAModule` (compact + accentLine)
- **Heading** `[NEW, locked]`: "Sample Content Assessment"
- **Body** `[DRAFT]`: "Send us a sample of your DITA source — or your current docs
  if you're pre-DITA. We'll assess your information model, specialization
  opportunities, and DITA-OT pipeline, and return a concrete engineering plan. No
  commitment required."

### Removed
- Old text breadcrumb (→ sibling switcher), footer nav.

---

## 6. Decision log
- **D-1 — Faithful, all 11 sections.** *(Locked.)*
- **D-2 — Hero subdeck `[DRAFT]` A.** *(Locked.)*
- **D-3 — Hero visual = DITA specialization model** (added per owner; chosen
  over "engineer the standard" + "DITA-OT build"). `<topic>` deriving into
  `<concept>`/`<task>`/`<reference>` + a custom amber `<api-operation>`, code-
  style tags, scroll-reveal. *(Locked.)*
- **D-4 — Bespoke + shared atoms.** *(Locked.)*
- **D-5 — CTA-as-closer added** (old page had none). *(Following.)*
- **D-6 — Umbrella heading for the Specialization/Constraints/SubjectScheme
  trio** — proposing `[DRAFT]` "Engineering the Standard"; alt = heading-less.
  *(Open.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| S1 Hero | `Hero` (universal) | New copy — `[DRAFT]` A subdeck, text-only |
| S2 Switcher | `SectionSiblings` (services) | Reuse — current="dita-engineering" |
| S3 Backbone | inline section + side callout | **New** — prose + Core Competencies (4 ✓) |
| S4 Workflow | inline 5-step strip | **New** — SCS roadmap pattern, `01–05` |
| S5 Techniques | inline 3-card row (inline `<code>`) | **New** — 3 `[OLD]` cards |
| S6 Case Study | inline case-study box | **New** — Scenario/Solution/Result |
| S7 Legacy Conversion | section + 3 cards + sub-block | **New** |
| S8 IA for DITA | section + 6-item checklist + callout | **New** |
| S9 AI-Ready | section + 3 cards + sub-block | **New** |
| S10 Delivery & Hosting | section + 6 cards (4+2) | **New** |
| S11 DITA-OT Services | section + 6 cards (4+2) | **New** |
| S12 Related | inline 3-card row | **New** |
| S13 CTA | `CTAModule` | Reuse — `compact` + `accentLine`, `[DRAFT]` body |
| Page | `services/dita-engineering.astro` | **New file** (large) |

**Cross-cutting (verify at build):**
- Clears 1 more dead `/services/<slug>` link; 4 still 404 after
  (publishing-engineering, ccms-services, system-integration, xml-engineering).
- Spacing-token trap: only `--space-{1,2,3,4,5,6,8,12,16,20,24,32}` exist.
- Verify on the local preview at 1280×900 / 375×812 (long page).

---

## 8. Open items for review
1. **Hero subdeck** A (locked) + **CTA body** `[DRAFT]` — approve/edit.
2. **D-6** — umbrella heading "Engineering the Standard" for the 3-card trio, or
   keep heading-less?
3. **Case-study box** treatment — `#fef3c7` washed box vs plain hairline box.
4. **Inline `<code>`** styling — subtle tint vs amber.
5. Section background rhythm — old page alternates white / light-gray section
   fills; I'll alternate to keep 11 sections legible (confirm at staging).
