# Home — Reframe Plan

> Status: inventory **done**, mapping **done**, wireframe **done** — awaiting
> review before implementation. Tags: `[OLD]` (from ex-tense.co) / `[NEW]` (kept
> from current extense.co) / `[DRAFT]` (net-new, approved where noted).
> Conventions in [README.md](README.md).
>
> Direction (locked this session): preserve the old site's *content*, render it
> in the new site's *design*, sequence it to the **prospective client's
> cognitive flow** (old order not strictly preserved — see Decision log).

---

## 1. Page job

- **URL:** `/`
- **Primary reader:** problem-aware, actively-shopping buyer — a prime
  contractor's capture/technical lead, or a Fortune 500 documentation /
  content-ops / compliance decision-maker.
- **The one job:** state **what Extense delivers and what they get**, then walk
  the buyer through offer → proof → method → why-us → their sector → action.
  Assume the "why structured content matters" is already settled.

---

## 2. Inventory — OLD site (ex-tense.co/)

1. Hero — H1 "Harnessing the Power of XML to Transform Your Organization"; sub
   "Strategic Consulting | Content Engineering | CCMS & Publishing Solutions |
   IETM Development"; "Minority-Owned • Woman-Owned Small Business"; CTA "Get
   Free Assessment".
2. The Extense Content Ops Stack — Strategy / Engineering / Automation /
   Delivery (4 layers).
3. Stats — 13+ / 11+ / WSOB / 3 Sectors / 508.
4. Logo marquee — "Trusted by Government, Commercial & Non-Profit Organizations."
5. The Content Engineering Lifecycle — "We don't just write words. We engineer
   information systems." Model / Author / Manage / Publish / Analyze.
5b. Two solution cards — Technical Documentation, Data Interoperability.
6. CTA band — Free Content Health Check / "Request Your Free Assessment".
7. Why Organizations Choose Extense — Standards-First Engineering /
   End-to-End Ownership / Enterprise Partner; Author→Manage→Publish flow;
   tech badges (DITA-OT, XSLT 3.0, Schematron, IXIASOFT, Paligo, S1000D,
   Oxygen XML, XQuery, CI/CD).
8. Tailored for High-Stakes Industries — Gov & Defense / Life Sciences /
   Automotive / Financial Services / Insurance.
9. Newsletter — "Stay Connected with Extense." (PROHIBITED.)
10. Footer.

## 3. Inventory — NEW site (current extense.co/)

1. `HomeHero` — kicker "DITA · DocBook · S1000D · NIEM"; H1 "Content engineering
   for organizations whose documentation needs to be right."; sub on
   auditable/multilingual/version-correct; clients line; animated DITA tree.
   No CTA.
2. Failure modes ×5 — "What happens when documentation is wrong." (Problem-ed.)
3. Pillars ×4 — "Four capabilities. One lifecycle." IA / Migration / CCMS /
   AI-Ready.
4. `ContentOpsStack` — 5 layers (Strategy / Engineering / Automation / Delivery
   / Analyze).
5. `StatBlock.three` — 60 / 72 / 85.
6. `TrustBadges` — 13+ / 11+ / DITA·S1000D / 508.
7. `LogoBench.full` — 12 logos.
8. `AudiencePivotCard` ×2 — public / private.
9. `CTAModule` — Sample Content Assessment.

---

## 4. Mapping decisions (final)

### Pull forward from OLD `[OLD]`
- Content Ops Stack content (already in new site).
- Stats (already in new `TrustBadges`, WSOB/3-sectors dropped).
- Logo marquee (already in new `LogoBench`).
- **Content Engineering Lifecycle** (Model→Analyze) — *not* in new site; rebuild
  in new design.
- **The 7 services** + scope copy — sourced from the old `/services/*` pages.
- **Why Choose Extense** (Standards-First, End-to-End Ownership) + the
  Author→Manage→Publish flow + the tech-badge row — rebuild in new design.
- **5 industry cards** + copy.
- Hero solution-list intent (expressed in the new H1/sub, not verbatim).

### Keep from NEW `[NEW]`
- `HomeHero` shell + animated DITA tree, kicker, clients line.
- `ContentOpsStack` (5 layers, unchanged — D-7).
- `TrustBadges`, `LogoBench`, `CTAModule`, `Footer`.
- Document-grade voice + design system throughout.

### Cut
- **Failure-modes** section (problem-education — buyer is problem-aware). D-6.
- **New 4-pillar** section → replaced by the 7-service section. D-4 / D-6.
- **Old 2 solution cards** → absorbed into the 7-service section. D-4.
- **Public/private audience pivot** → replaced by the 5 industry cards. D-5.
- **60/72/85 `StatBlock`** as a standalone section → numbers relocate into the
  hero sub-deck (their substantiated home). D-1.
- **Newsletter** (prohibited). **WSOB / minority-owned markers** (prohibited).

---

## 5. Wireframe

Order follows the shopping buyer's cognitive flow:
**orient → offer → proof → method → convert → why-us → your-sector → act.**

### Section 1 — Hero  · component: `HomeHero` (modify) · `[NEW]` shell
- **Kicker** `[NEW]`: `DITA · DocBook · S1000D · NIEM`
- **H1** `[DRAFT]`: "DITA migration, CCMS implementation, and AI-ready content
  engineering."
- **Sub-deck** `[DRAFT]`: "For documentation teams past the diagnosis — Extense
  delivers the structured-content systems behind 60% faster publishing, 72%
  lower translation cost, and 85% retrieval precision."
- **No in-hero CTA.** Conversion handled by the persistent nav "Free Assessment"
  button (see Section 0) + the mid-page CTA band (Section 7).
- **Clients line** `[NEW]`: IRS · U.S. House · Toyota · FedEx · Morgan Stanley · AMD
- **Visual** `[NEW]`: animated DITA tree (kept).
- *Rationale:* solution-forward H1 answers "do you do what I need?" instantly
  (relevance-first for a shopping buyer); the sub-deck carries the outcome proof
  (60/72/85) so the hero sells both capability and result. H1 stays in
  recognizable buyer vocabulary (DITA/CCMS/AI-ready), not the internal service
  taxonomy — the 7-pillar section below is the menu; the H1 is the hook.

### Section 0 — TopNav  · component: `TopNav` (modify, sitewide) · `[NEW]`
- Add a persistent primary CTA button, top-right: **"Free Assessment"** `[DRAFT label]`
  → `/contact`.
- *Rationale:* an actively-shopping buyer should always have a one-click action.
  Sitewide (not just home). Distinct from the mid-page band's "Sample Content
  Assessment" label — the nav button is shorter chrome; the band is the full
  conversion offer.

### Section 2 — Service Pillars (7)  · component: NEW (PillarIndexRow-style) · `[DRAFT]` copy
- **Heading** `[DRAFT]`: "Seven services. End to end."
- **Sub-deck** `[DRAFT]`: "From strategy and authoring through engineering,
  publishing, and integration — engaged individually or as one operation."
- **Rows (01–07), numbered index-row layout, each with icon + scroll-draw-in:**
  Scope copy condensed from the old `/services/*` pages (`[DRAFT]`, verbatim
  phrases preserved). Placeholder hrefs `/services/[slug]` pending the Services
  rework.
  - **01 Technical Writing** — "Topic-based authoring, Simplified Technical
    English, and regulatory submissions — structured content built to scale
    across products, languages, and channels." · icon: pen-nib over lined doc
  - **02 Content Strategy** — "Taxonomy, governance, and reuse architecture
    defined before tooling: legacy audit, reuse matrix, content model." · icon:
    connected taxonomy nodes
  - **03 DITA Engineering** — "Semantic content models that drive automation —
    DITA 1.3/2.0, Schematron validation, SubjectScheme taxonomies, custom
    specializations." · icon: nested topic tree
  - **04 Publishing Engineering** — "Pixel-perfect output from structured source
    — PDF via CSS Paged Media, responsive HTML5, portals, docs-as-code
    pipelines." · icon: source → fan-out outputs
  - **05 CCMS Services** — "DBA-level administration and Tier 2/3 support for
    IXIASOFT, Tridion Docs, Heretto, and Paligo — so writers focus on writing."
    · icon: stacked repository + branch
  - **06 System Integration** — "Connecting the CCMS to engineering, support,
    PLM, and translation systems, so content flows without manual handoffs." ·
    icon: hub with connectors
  - **07 XML Engineering** — "Schema design, transformation pipelines, and
    validation frameworks that enforce quality at the structural level — before
    content reaches a reviewer." · icon: `</>` with validation check
- **Animation** `[NEW pattern]`: scroll-triggered stroke-draw-in
  (`stroke-dasharray`), staggered down the rows; optional hover re-draw;
  `prefers-reduced-motion` off. Same motion language as Content Ops Stack + hero.
- *Rationale:* the offer is the buyer's first real question ("do you do my
  thing?"), so it sits at #2, right under the hero. Replaces both the old 2
  solution cards and the new 4 pillars (D-4). Index-row (not a grid) handles 7
  cleanly and matches the document-grade list aesthetic.

### Section 3 — Trust badges  · component: `TrustBadges` (reuse) · `[NEW]`
- 13+ Years in Business · 11+ Major Clients Served · DITA · S1000D Content
  Standards · 508 Section Compliant.
- *Rationale:* credentials open the proof cluster.

### Section 4 — Logo marquee  · component: `LogoBench.full` (reuse) · `[NEW]`
- Eyebrow: "Trusted by Government Agencies, Fortune 500 Companies, & Non-Profit
  Organizations." 12 logos.
- *Rationale:* "and these organizations trust us" — brand credibility right
  after the offer. Badges + logos = one proof cluster (#3–4).

### Section 5 — Content Ops Stack  · component: `ContentOpsStack` (reuse) · `[NEW]`
- "The content ops stack." / "Five integrated layers. One seamless content
  operation." Strategy / Engineering / Automation / Delivery / Analyze.
- *Rationale:* first "how we work" lens — the capability **layers**. Unchanged
  per D-7.

### Section 6 — Content Engineering Lifecycle  · component: NEW · `[OLD]` copy
- **Heading** `[OLD]`: "The Content Engineering Lifecycle"
- **Sub-deck** `[OLD]`: "We don't just write words. We engineer information
  systems."
- **Stages** `[OLD]` (horizontal, arrow-connected): Model (Define Schema &
  Taxonomy) → Author (Structured XML Writing) → Manage (CCMS Version Control) →
  Publish (Automated PDF/HTML5) → Analyze (Usage Metrics).
- *Rationale:* second "how we work" lens — the workflow **stages over time**
  (distinct from the Ops Stack's layers, per D-3). Built **visually distinct**:
  horizontal arrow-connected sequence vs. the Ops Stack's 5-column grid, so the
  two don't read as repetition.

### Section 7 — CTA band (mid-page)  · component: `CTAModule` (reuse) · `[NEW]`
- Label `[NEW]`: "Sample Content Assessment". Body `[NEW]`: "Submit a 20-page
  sample. We'll return conversion feasibility, content recovery rate, and
  engineering effort within two business days…"
- *Rationale:* mid-page conversion for the buyer already convinced by offer +
  proof + method. Late-scroll conversion is covered by the persistent nav CTA.

### Section 8 — Why Choose Extense  · component: NEW · `[OLD]` + 1 `[DRAFT]`
- **Heading** `[OLD]`: "Why Organizations Choose Extense"
- **Sub-deck** `[OLD]`: "We bring deep domain expertise where precision and
  compliance are non-negotiable."
- **Three differentiators:**
  - **Standards-First Engineering** `[OLD]`: "Every engagement starts with proper
    information architecture — DITA specializations, Schematron rules, and
    content models designed for long-term maintainability."
  - **End-to-End Ownership** `[OLD]`: "From content strategy through publishing
    automation — a single team that understands the full stack. No hand-offs, no
    knowledge gaps."
  - **Regulated-Industry Track Record** `[DRAFT, approved]`: "Thirteen-plus years
    engineering documentation for federal agencies, Fortune 500 manufacturers,
    life sciences, and financial institutions — sectors where a content error
    carries real downstream cost." *(Replaces the prohibited "Enterprise
    Partner" / woman-/minority-owned card; reworded to avoid echoing the
    sub-deck's "precision and compliance are non-negotiable.")*
- **Tooling flow** `[OLD]`: Author (DITA XML & Structured Content) → Manage (CCMS
  Version Control & Review) → Publish (PDF · HTML5 · API · Mobile · IETM).
- **Tech badges** `[OLD]`, restyled to the new design (hairline / mono, not the
  old dark-blue pills): DITA-OT · XSLT 3.0 · Schematron · IXIASOFT · Paligo ·
  S1000D · Oxygen XML · XQuery · CI/CD.
- *Rationale:* differentiation + technical depth = "why us." The tech badges are
  the practitioner-credibility signal (proof of tooling fluency) that this
  audience scans for.

### Section 9 — Industries (5)  · component: `IndustryCard` (reuse) · `[OLD]` copy
- **Heading** `[OLD]`: "Tailored for High-Stakes Industries"
- **Sub-deck** `[OLD]`: "We understand the compliance and precision required in
  regulated sectors."
- **Cards** `[OLD]`:
  - Government & Defense — "S1000D compliance and mission-critical documentation
    support."
  - Life Sciences — "Labeling, regulatory submission content, and FDA validation."
  - Transportation — "VIN-specific customization and after-sales service portal data." *(label changed from "Automotive" per decision; links to `/industries/transportation`.)*
  - Financial Services — "Secure, audit-ready policy and procedure management
    systems."
  - Insurance — "Product Disclosure Statements (PDS) and claims processing flows."
- *Rationale:* "do they know my sector?" — self-relevance, just before the
  footer. Replaces the public/private audience pivot (D-5).

### Section 10 — Footer  · component: `Footer` (reuse) · `[NEW]`

---

## 6. Decision log

- **D-1 — Hero H1 + sub-deck.** Chose **A (solution-forward)** H1 over B
  (outcome-forward) — relevance-first for a shopping buyer; B's numbers would be
  orphaned (no standalone outcomes section in this order); lower vendor-pitch
  risk with the federal/F500 audience. Folded B's strength into a **drafted
  sub-deck** carrying 60/72/85. H1 kept in recognizable buyer vocabulary, not
  re-tuned to the 7-service names. *(Confirmed.)*
- **D-2 — CTAs.** Sitewide nav button "Free Assessment"; one mid-page band
  "Sample Content Assessment"; no in-hero CTA. *(Confirmed.)*
- **D-3 — Lifecycle kept.** It's a distinct lens (workflow stages) from the Ops
  Stack (capability layers) and the Why-Choose flow (tooling pipeline). Built
  visually distinct to avoid repetition. *(Confirmed.)*
- **D-4 — 7 service pillars.** Replace old 2 solution cards + new 4 pillars.
  Numbered index-row, icons + scroll-draw animation, scope copy from old
  `/services/*` pages, placeholder hrefs pending Services rework. *(Confirmed.)*
- **D-5 — 5 industry cards** restored; replace the audience pivot. *(Confirmed.)*
- **D-6 — Failure-modes dropped;** "Enterprise Partner" → "Regulated-Industry
  Track Record." *(Confirmed.)*
- **D-7 — Content Ops Stack** stays 5 layers, unchanged. *(Confirmed.)*
- **Order.** Old order *not* strictly preserved — resequenced to cognitive flow
  (offer pulled up to #2; proof clustered behind it). *(Confirmed.)*

---

## 7. Build inventory

| Section | Component | Action |
|---|---|---|
| 0 TopNav CTA | `TopNav` | **Modify** (add sitewide "Free Assessment" button) |
| 1 Hero | `HomeHero` | **Modify** (new H1 + sub-deck) |
| 2 Service pillars | new (PillarIndexRow-style) | **New build** + 7 icons + scroll-draw |
| 3 Trust badges | `TrustBadges` | Reuse |
| 4 Logo marquee | `LogoBench` | Reuse |
| 5 Content Ops Stack | `ContentOpsStack` | Reuse |
| 6 Lifecycle | new | **New build** (distinct from Ops Stack) |
| 7 CTA band | `CTAModule` | Reuse |
| 8 Why Choose | new | **New build** (3 cards + flow + tech badges) |
| 9 Industries | `IndustryCard` | Reuse (new section wrapper) |
| 10 Footer | `Footer` | Reuse |

New builds: 3 components (Service pillars, Lifecycle, Why Choose). Modifies: 2
(TopNav, HomeHero). Reuses: 5.

---

## 8. Open items (minor — resolve at build)

- **Industries naming:** RESOLVED — label is **Transportation**, links to
  `/industries/transportation`. (Old "Automotive" copy retained.)
- **Service hrefs:** placeholder `/services/[slug]` until the Services rework
  finalizes routes.
- **"Free Assessment" nav label** is `[DRAFT]` — confirmed verbally; lock at
  build.
- **Outcomes reinforcement:** 60/72/85 live only in the hero sub-deck in this
  order. Optional later: a small outcomes section if we want them repeated.
