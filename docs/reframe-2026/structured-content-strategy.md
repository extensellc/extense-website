# Structured Content Strategy (service detail) — Reframe Plan

> Status: **implemented — pending staging sign-off.** Second of the 7 `/services/<slug>`
> detail sub-pages. Built **bespoke** (page-local CSS), reusing the shared atoms
> (`Hero`, `SectionSiblings`, `CTAModule`) and the proven card / related-card /
> `#fef3c7`-callout patterns from the Technical Writing page — **no new shared
> kit** (per-page tuning stays isolated; matches the Solutions-section
> precedent). Decisions locked: build = bespoke+atoms; hero subdeck = **A**
> (benefit-led, 40–60%); **text-only hero** (visual can be added later, as on
> TW). Tags: `[OLD]` (ex-tense.co/services/structured-content-strategy.html) /
> `[NEW]` (current components) / `[DRAFT]` (net-new, needs approval).
> Conventions in [README.md](README.md); model = the shipped
> [technical-writing-content-development.md](technical-writing-content-development.md).

---

## 1. Page job
- **URL:** `/services/structured-content-strategy`
- **Primary reader:** a content/IA lead or program owner deciding *whether to
  invest in strategy before tooling* — wants proof that taxonomy, governance,
  and reuse planning pay off (the 40–60% number) before buying a CCMS.
- **The one job:** make the case that **strategy precedes technology**, show the
  **reuse payoff** (40–60%), the **strategic pillars**, and the **roadmap**, then
  convert to an assessment.

---

## 2. Inventory — OLD page (ex-tense.co/.../structured-content-strategy.html)
1. **Hero** — H1 "Structured Content Strategy" + subdeck "Moving from
   'Documents' to 'Information Assets'. Future-proof your content lifecycle."
2. **Strategy Before Technology** — intro paragraph.
3. **The "Reuse" Paradigm** — explanation + **40–60% Content Reduction** stat
   (amber oval, left) + 3-item reuse list (Fragment / Topic / Map Reuse).
4. **Key Strategic Pillars** — **3 cards** w/ circular icon chips: Taxonomy &
   Metadata · Governance Models · Legacy Analysis.
5. **Strategic Roadmap** — **5-step strip** w/ arrows: Audit → Reuse Matrix →
   Model Design → Workflow Def → Pilot.
6. **Related Services** — **3 cards**: Technical Writing · DITA Engineering ·
   CCMS Services. (No mid-page assessment CTA.)
7. Footer.

## 3. Inventory — NEW site
Page doesn't exist (the `/services` card + sibling switcher link here, 404 until
built). Reusing: `Hero` (universal, text-only), `SectionSiblings`
(variant="services"), `CTAModule` (closer). Patterns to copy page-local from TW:
hairline card w/ bare amber line icon (no chip), `#fef3c7` callout fill, mono
`01–0N` index, related-card (mono "Service" label · title · body · "Explore →").

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page order, re-skinned; CTA added as closer (parity).
- **Hero subdeck = `[DRAFT]` A** (locked): old "documents → information assets"
  framing + the 40–60% number.
- **Cards = new-system idiom** (left-aligned, bare amber line icon, **no circular
  chip**) — consistent with the shipped TW + `/services` cards.
- **40–60% stat** → a `#fef3c7` washed stat panel (left) beside the reuse
  explanation + list (right), echoing the old left-stat/right-text split without
  the literal oval.
- **Roadmap** → 5-step strip with mono `01–05` index + amber connectors;
  stacks on mobile.
- **CTA-as-closer** (`CTAModule`, compact + accentLine) — `[DRAFT]` body.
- **Voice:** all `[OLD]` copy is clean (no banned verbs).

---

## 5. Wireframe
Order mirrors the old page; CTA added at the close.

### Section 1 — Hero · universal `Hero` (+ taxonomy-tree side visual)
- **Side visual** (added per owner): a **taxonomy / content-model tree** SVG —
  a `CONTENT MODEL` root branching to `PRODUCT · AUDIENCE · VERSION` facets with
  leaf values, document-grade chrome (`FIG. 02 / taxonomy.model`, `CLASSIFY ·
  GOVERN · REUSE`), amber connector draw + scroll-reveal (reduced-motion
  fallback). Chosen over the "faceted topic" option: shows the strategic
  deliverable (the IA/model), reads as IA depth, and is distinct from TW's
  fan-out.
- **H1** `[OLD]`: "Structured Content Strategy"
- **Subdeck** `[DRAFT]` (A, revised per owner): "Future-proof your content
  lifecycle by moving from documents to information assets — a reuse strategy
  that significantly cuts content volume and keeps every warning, procedure, and
  disclaimer consistent across the corpus." *(The concrete 40–60% number lives
  in the stat panel below, so the page keeps its specificity.)*

### Section 2 — Sibling switcher · `SectionSiblings` (variant="services")
- `← Services` + 7 dot-separated siblings; current = **Content Strategy**
  (amber + bold).

### Section 3 — Strategy Before Technology · `[OLD]`
- **Heading** `[OLD]`: "Strategy Before Technology"
- **Intro** `[OLD]`: "Buying a CCMS does not solve your content problems. A
  robust strategy defines how your content behaves, who it serves, and where it
  flows."

### Section 4 — The "Reuse" Paradigm · `[OLD]` (stat panel + text)
- **Heading** `[OLD]`: "The 'Reuse' Paradigm"
- **Left — stat panel** (`#fef3c7` washed, bordered): big amber **"40–60%"** +
  label "Content reduction".
- **Right — body** `[OLD]`: "Traditional authoring locks information inside
  linear documents. If a safety warning changes, you have to find and update it
  in 50 different user manuals. Our structured content strategy breaks these
  documents down into modular components (Topics) that are written once and
  referenced everywhere. We analyze your entire corpus to identify high-value
  reuse candidates:"
- **Reuse list** `[OLD]` (term + desc):
  - **Fragment Reuse** — Warnings, notes, and legal disclaimers.
  - **Topic Reuse** — Procedures common across product families.
  - **Map Reuse** — Entire deliverables constructed from shared chapters.

### Section 5 — Key Strategic Pillars · `[OLD]` (3 cards)
- **Heading** `[OLD]`: "Key Strategic Pillars"
- **3 cards** `[OLD]` (3-up; bare amber line icon + title + body):
  1. **Taxonomy & Metadata** — "We design the classification systems that make
     your content findable. This includes defining facet values for product,
     version, audience, and user role." *(icon: tag/hierarchy)*
  2. **Governance Models** — "Who owns the content? Who approves the reuse? We
     establish the Governance Committees and Style Guides ('The Rules of the
     Road') to prevent content chaos." *(icon: shield/check)*
  3. **Legacy Analysis** — "Not everything should be migrated. We perform ROT
     (Redundant, Obsolete, Trivial) analysis to ensure you only migrate valuable
     content to the new system." *(icon: funnel/filter)*

### Section 6 — Strategic Roadmap · `[OLD]` (5-step strip)
- **Heading** `[OLD]`: "Strategic Roadmap"
- **5 steps** `[OLD]` (bordered cards, mono `01–05`, amber connectors; stack on
  mobile):
  1. **Audit** — "Quantitative analysis of existing docs."
  2. **Reuse Matrix** — "Identifying commonalities across products."
  3. **Model Design** — "Mapping content to DITA structure."
  4. **Workflow Def** — "Authoring → Review → Translation → Publish."
  5. **Pilot** — "Testing the strategy with a small dataset."

### Section 7 — Related Services · `[OLD]` (3 cards)
- **Heading** `[OLD]`: "Related Services"
- **3 cards** `[OLD]` (mono "Service" · title · body · "Explore →"):
  - **Technical Writing** → `/services/technical-writing-content-development` —
    "Professional documentation development for complex technical products and
    systems."
  - **DITA Engineering** → `/services/dita-engineering` — "Topic modeling,
    specialization, and constraint modules for scalable content architectures."
  - **CCMS Services** → `/services/ccms-services` — "Platform selection,
    configuration, and ongoing support for enterprise content management."
- *DITA Engineering + CCMS Services are sibling pages built later — links live
  now, 404 until then.*

### Section 8 — CTA (closing) · `CTAModule` (compact + accentLine)
- **Heading** `[NEW, locked]`: "Sample Content Assessment"
- **Body** `[DRAFT]`: "Send us a sample of your content estate. We'll map reuse
  potential, run a ROT pass, and sketch a target information model — so you can
  see the volume you'd cut before committing to a platform. No commitment
  required."
- `audience="general"`.

### Removed
- Old text breadcrumb (→ sibling switcher), footer nav (site footer covers it).

---

## 6. Decision log
- **D-1 — Bespoke + shared atoms; no new kit.** *(Locked.)*
- **D-2 — Hero subdeck `[DRAFT]` A** (benefit-led, 40–60%). *(Locked.)*
- **D-3 — Hero visual = taxonomy / content-model tree** (added per owner after
  reviewing two mockups; chosen over "faceted topic"). *(Locked.)*
- **D-4 — Cards = new-system idiom** (no circular chip). *(Following TW.)*
- **D-5 — 40–60% as a `#fef3c7` stat panel** beside the reuse text. *(Proposed.)*
- **D-6 — Roadmap = 5-step strip, mono `01–05` + amber connectors.** *(Proposed.)*
- **D-7 — CTA-as-closer.** *(Following.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| 1 Hero | `Hero` (universal) | New copy — `[DRAFT]` A subdeck, text-only |
| 2 Sibling switcher | `SectionSiblings` (services) | Reuse — current="structured-content-strategy" |
| 3 Strategy Before Technology | inline section | **New build** — `[OLD]` heading + intro |
| 4 Reuse Paradigm | inline section + stat panel | **New build** — `#fef3c7` stat + `[OLD]` text/list |
| 5 Pillars | inline section + page-local cards | **New build** — 3 `[OLD]` cards |
| 6 Roadmap | inline section + 5-step strip | **New build** — `[OLD]` steps, `01–05` |
| 7 Related | inline 3-card row | **New build** — 3 `[OLD]` cards |
| 8 CTA | `CTAModule` | Reuse — `compact` + `accentLine`, `[DRAFT]` body |
| Page | `services/structured-content-strategy.astro` | **New file** |

**Cross-cutting (verify at build):**
- This page clears 1 more dead `/services/<slug>` link; 5 still 404 after
  (dita-engineering, publishing-engineering, ccms-services, system-integration,
  xml-engineering).
- Spacing-token trap: only `--space-{1,2,3,4,5,6,8,12,16,20,24,32}` exist.
- Verify on the local preview at 1280×900 / 375×812.

---

## 8. Open items for review
1. **Hero subdeck** — A locked; edit if you want different wording.
2. **40–60% stat panel** — `#fef3c7` washed panel beside the text (proposed) —
   OK, or a plainer treatment?
3. **Roadmap** — mono `01–05` + amber connectors (proposed) vs plain cards.
4. **CTA body** `[DRAFT]` — approve/edit.
5. **Pillar icons** — defaulting to tag / shield / funnel line icons; tune on
   staging.
