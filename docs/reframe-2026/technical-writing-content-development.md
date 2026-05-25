# Technical Writing & Content Development (service detail) — Reframe Plan

> Status: **implemented — pending staging sign-off.** First of the 7
> `/services/<slug>` detail sub-pages. Built **bespoke**, reusing the universal
> atoms (`Hero`, `CTAModule`, `SiblingsBreadcrumb`). The
> shared-kit-vs-fully-bespoke call is **deferred to page 2** — for this first
> page both paths are identical, so we build it bespoke now and decide what (if
> anything) to extract once the pattern is proven against review. Decisions
> locked: hero subdeck **B**; **both** cross-nav elements (top switcher +
> bottom Related); Quality Standard **four-gate `01–04` strip**; doc-type grid
> **3+3**; **new-system** cards (left-aligned, no chip). Tags: `[OLD]`
> (ex-tense.co/services/technical-writing-content-development.html) / `[NEW]`
> (current extense.co components) / `[DRAFT]` (net-new, needs approval).
> Conventions in [README.md](README.md); built on the just-shipped main
> [services.md](services.md) shape.

---

## 1. Page job
- **URL:** `/services/technical-writing-content-development`
- **Primary reader:** a documentation/content-ops lead evaluating *whether
  Extense can author their content* — wants to see method (how we write),
  range (what we deliver), and a quality bar before requesting an assessment.
- **The one job:** prove technical writing here is an **engineering
  discipline** with measurable output (STE, four-gate QA, 30–40% translation
  savings), show the **breadth of deliverables**, and convert to a sample
  assessment.

---

## 2. Inventory — OLD page (ex-tense.co/.../technical-writing-content-development.html)
1. **Hero** — H1 "Technical Writing & Content Development" + subdeck
   "Information engineering, not just writing. We build structured content
   that scales across products, languages, and channels."
2. **Precision in Every Sentence** — intro + **3 feature cards**
   (Topic-Based Authoring · Simplified Technical English · Minimalist Design).
   The STE card carries "30–40% reduction in translation cost."
3. **Documentation Types We Deliver** — intro ("From 10-page quick-start
   guides to 50,000-page technical data packages…") + **6 type cards** in a
   4+2 grid.
4. **Our Quality Standard** — light-fill callout box (the four-gate review).
5. **Free Content Assessment** — dark CTA band, "Request Your Free Assessment".
6. **Related Services** — 2 cards (Structured Content Strategy · DITA
   Engineering).
7. Footer.

## 3. Inventory — NEW site
Page does not exist (the `/services` card + TopNav dropdown link here and
currently 404). Reusable atoms already shipped:
- `Hero` (universal): H1 + subdeck, optional side slot.
- `CTAModule`: **heading locked to "Sample Content Assessment"**, body
  adaptable, `compact` + `accentLine` props (the solution/services closer).
- `SiblingsBreadcrumb`: `services` variant is **stale** (still lists the
  deleted `project-based` / `staff-augmentation` / `managed-services`), used
  nowhere — repoint to the 7 services.
- Card vocabulary from `/services`: hairline border + fill, bare amber line
  icon top-left (no circular chip — AI-Ready deliberately dropped chips),
  hover lift. Tokens: amber `--color-accent-primary-hover` icons, mono labels.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page order, re-skinned to the new design system —
  the owner iterates finely on the staged page, so build close to the old one.
- **Hero subdeck = blended `[DRAFT]`** (your call): keep the old "Information
  engineering, not just writing" opener, append a benefit/number. Options in
  §5. All other copy is pulled forward `[OLD]` (clean — no banned verbs).
- **CTA as closer** (your call): the old mid-page "Free Content Assessment"
  band becomes the page-closing `CTAModule`. Its heading is locked to "Sample
  Content Assessment" (the old "20-page sample" maps onto it cleanly); the old
  body is adapted as `[DRAFT]`. `compact` + `accentLine`, parity with the
  solution pages.
- **Sibling switcher:** repoint `SiblingsBreadcrumb` `services` → the 7
  services and place it under the hero (mirrors the industries pattern; the
  only live use of the component). Short labels so 7 fit one line.
- **Keep** the bottom "Related Services" curated 2-card section `[OLD]`.
- **Card style:** new-system idiom (left-aligned, bare line icon, no circular
  chip) for consistency with the shipped `/services` cards — not the old
  centered/chipped cards. Flag for staging review.
- **Icons:** small inline-SVG line icons echoing the old page, drawn in the
  same style as the `/services` card icons.

---

## 5. Wireframe
Order mirrors the old page; CTA moved to the close per your call.

### Section 1 — Hero · universal `Hero`
- **H1** `[OLD]`: "Technical Writing & Content Development"
- **Subdeck** — pick one blended `[DRAFT]` (old opener + a number):
  - **A:** "Information engineering, not just writing. We build structured
    content that cuts translation cost 30–40% and reads identically across
    every language and channel."
  - **B:** "Information engineering, not just writing. Structured content that
    scales from a 10-page quick-start to a 50,000-page data package — and cuts
    translation cost 30–40%."
  - **C:** "Information engineering, not just writing. We build structured
    content that's clear, translatable, and reusable — and cuts translation
    cost 30–40% across products, languages, and channels."
- **Side visual** (added per owner): a **single-source reuse map** SVG in the
  hero side slot — a pool of 6 reusable topic modules fanning out via amber
  connectors to 4 outputs (User Guide · API Reference · In-App Help · PDF /
  HTML5). Document-grade idiom matching the `/services` hero flow (corner
  registration marks, mono `FIG. 01 / single-source.reuse` chrome, scroll-reveal
  with reduced-motion fallback). Visualizes the subdeck's "authored once →
  scales across products, languages, and channels."

### Section 2 — Sibling switcher · `SiblingsBreadcrumb` (services, repointed)
- 7 short labels: Technical Writing · Content Strategy · DITA Engineering ·
  Publishing Engineering · CCMS Services · System Integration · XML
  Engineering, current = Technical Writing.

### Section 3 — Precision in Every Sentence · `[OLD]`
- **Heading** `[OLD]`: "Precision in Every Sentence"
- **Intro** `[OLD]`: "Technical writing is an engineering discipline. We
  employ Simplified Technical English (STE), minimalist principles, and
  information typing to ensure every topic is clear, translatable, and
  reusable."
- **3 feature cards** `[OLD]` (3-up grid; icon + title + body, no CTA link):
  1. **Topic-Based Authoring** — "Every concept, task, and reference is a
     standalone, reusable unit. We design topic hierarchies that support
     mix-and-match assembly for different audiences — operator guides, admin
     manuals, and API references — from the same source pool."
  2. **Simplified Technical English** — "We write to ASD-STE100 — limiting
     vocabulary to ~900 approved words, enforcing sentence-length constraints,
     and eliminating ambiguity. The result: 30–40% reduction in translation
     cost and content that reads identically across cultures."
  3. **Minimalist Design** — "We focus on the instructional core. If the user
     doesn't need theory to complete the task, we move the theory to a
     separate concept topic. Every sentence must earn its place — reducing
     cognitive load and support ticket volume."

### Section 4 — Documentation Types We Deliver · `[OLD]`
- **Heading** `[OLD]`: "Documentation Types We Deliver"
- **Intro** `[OLD]`: "From 10-page quick-start guides to 50,000-page technical
  data packages — we match the deliverable to the audience and regulatory
  context."
- **6 type cards** `[OLD]` (3+3 grid — cleaner than the old 4+2):
  1. **User & Admin Guides** — "Task-oriented documentation with conditional
     profiling for different user roles — operators, administrators, and
     developers — from the same DITA source."
  2. **API & Developer Docs** — "OpenAPI/Swagger integration, code samples,
     endpoint reference, and getting-started tutorials. We merge
     auto-generated API specs with human-authored conceptual content."
  3. **Regulatory Submissions** — "FDA eSTAR packages, S1000D data modules,
     SPL drug labels, and compliance documentation that meets the exact
     structural requirements of the target authority."
  4. **Installation & Maintenance** — "Step-by-step procedures with safety
     admonitions, illustrated parts catalogs, and troubleshooting decision
     trees for field service teams."
  5. **Release Notes & Changelogs** — "Automated release note generation from
     JIRA/Azure DevOps tickets, merged with editorial summaries. Versioned,
     searchable, and linked to the affected documentation."
  6. **UX Microcopy & In-App Help** — "Tooltips, error messages, onboarding
     flows, and context-sensitive help strings authored in DITA and delivered
     as JSON snippets directly into your application UI."

### Section 5 — Our Quality Standard · `[OLD]` (+ optional gate strip `[DRAFT]`)
- **Heading** `[OLD]`: "Our Quality Standard"
- **Body** `[OLD]`: "Every deliverable passes a four-gate review: structural
  validation (Schematron), terminology compliance (STE word list), editorial
  review (peer + SME), and output QA (visual + accessibility). We don't ship
  content that hasn't cleared all four."
- *Treatment: hairline/elevated callout band. Optional enhancement — render
  the four gates as a mono-labelled inline strip (01 Structural · 02
  Terminology · 03 Editorial · 04 Output QA) above/below the sentence, for a
  document-grade visual. `[DRAFT]` labels derived from `[OLD]`. Default to the
  strip; fall back to a plain callout if it reads heavy on staging.*

### Section 6 — Related Services · `[OLD]`
- **Heading** `[OLD]`: "Related Services"
- **2 cards** `[OLD]` (mono "Service" label · title · body · "Explore →"):
  - **Structured Content Strategy** → `/services/structured-content-strategy`
    — "Information architecture, taxonomy design, and content governance
    frameworks."
  - **DITA Engineering** → `/services/dita-engineering` — "Topic modeling,
    specialization, and constraint modules for scalable content
    architectures."
- *Both targets are sibling service pages, built later — links live now, 404
  until then (same pattern as the `/services` cards).*

### Section 7 — CTA (closing) · `CTAModule` (compact + accentLine)
- **Heading** `[NEW, locked]`: "Sample Content Assessment"
- **Body** `[DRAFT, from OLD]`: "Send us a 20-page sample of your existing
  documentation. We'll analyze readability grade, reuse potential, STE
  compliance, and translation-cost impact — no commitment required."
- `audience="general"`, default button "Submit a sample →".

### Removed
- Old text breadcrumb (replaced by the sibling switcher), the standalone dark
  CTA band (folded into the closing `CTAModule`), the global footer nav (the
  site footer already covers it).

---

## 6. Decision log
- **D-1 — Bespoke build, defer the kit:** build TW bespoke; decide
  shared-kit-vs-fully-bespoke at page 2. *(Agreed — both identical for page 1.)*
- **D-2 — CTA as closer:** old "Free Content Assessment" band → closing
  `CTAModule` (locked "Sample Content Assessment" heading). *(Your call.)*
- **D-3 — Hero subdeck blended `[DRAFT]`:** old opener + a number.
  *(Locked: **Option B**, then extended per owner — "…scales from a 10-page
  quick-start to a 50,000-page data package — including scaling across
  products, languages, and channels — and cuts translation cost 30–40%."
  Chosen for the proof-of-depth signal across both Fortune 500 and federal
  evaluators; the products/languages/channels clause folds the old multi-axis
  benefit back in.)*
- **D-4 — Repoint `SiblingsBreadcrumb` services → 7**, use as top sibling
  switcher. *(Following the repoint task you flagged.)*
- **D-5 — Card idiom = new system** (left-aligned, no circular chip), not the
  old centered/chipped cards. *(Proposed — iterate on staging.)*
- **D-6 — 6 doc-type cards in 3+3** (vs old 4+2). *(Proposed.)*
- **D-7 — Quality Standard as a 4-gate strip** by default. *(Proposed.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| 1 Hero | `Hero` (universal) | New copy — blended `[DRAFT]` subdeck |
| 2 Sibling switcher | `SiblingsBreadcrumb` (services) | **Repoint** variant → 7 services; render under hero |
| 3 Precision | inline section + page-local feature cards | **New build** — 3 `[OLD]` cards |
| 4 Doc Types | inline section + page-local type cards | **New build** — 6 `[OLD]` cards (3+3) |
| 5 Quality Standard | inline callout (+ optional gate strip) | **New build** — `[OLD]` + `[DRAFT]` gate labels |
| 6 Related | inline 2-card row | **New build** — 2 `[OLD]` cards |
| 7 CTA | `CTAModule` | Reuse — `compact` + `accentLine`, `[DRAFT]` body |
| Page | `services/technical-writing-content-development.astro` | **New file** |

**Cross-cutting (verify at build):**
- Repointing `SiblingsBreadcrumb` `services` changes the variant globally —
  confirm nothing else renders it (grep already shows only
  `IndustryPageLayout` uses the component, and only the industries variant).
- This page clears 1 of the 7 dead `/services/<slug>` links (TopNav dropdown +
  the `/services` Expert Services cards). The other 6 still 404 until built.
- Spacing-token trap: only `--space-{1,2,3,4,5,6,8,12,16,20,24,32}` exist.
- Verify on the local preview at an explicit viewport (1280×900 / 375×812);
  reveal animations don't fire headless.

---

## 8. Open items — RESOLVED (locked before build)
1. **Hero subdeck** — **Option B.**
2. **Sibling switcher + Related** — **both.**
3. **Quality Standard** — **four-gate `01–04` strip.**
4. **Doc-type grid** — **3+3.**
5. **Card idiom** — **new-system** (left-aligned, no chip).

Remaining for staging review: px-level spacing, the quality-callout fill
(currently `--color-surface-elevated`/white), gate-strip weight, and the usual
line-break/alignment finesse.
