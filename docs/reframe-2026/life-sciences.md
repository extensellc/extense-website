# Life Sciences (industry sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** Third of the 6 `/industries/<slug>`
> sub-pages ported as a faithful reframe (old-site content, new-site design).
> Bespoke build (page-local CSS, prefix `ls-`), reusing the shared atoms
> (`Hero`, `SectionSiblings`, `CTAModule`) and the patterns proven on
> G&D and FS (3-card grids with bare amber line icons, `#fef3c7` amber-tinted
> callout, multi-card cross-link, hero document-grade SVG visual,
> `section-band` rhythm). Replaces the current `IndustryPageLayout`-based
> page; the layout's stale `/capabilities/*` links go away with it.
>
> **Locked this session (2026-06-03):** H1 = [OLD] verbatim "Life Sciences
> & Pharma"; faithful — all 5 old-page sections kept; S4 carries an inline
> proof-point callout (Regulatory Agility in Practice); S5 = 3-card mix
> (1 [OLD] industry + 1 [DRAFT] solution + 1 [DRAFT] service); CTA name
> "Free Regulatory Content Assessment" preserved.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [financial-services.md](financial-services.md).

---

## 1. Page job
- **URL:** `/industries/life-sciences` (unchanged)
- **Primary reader:** regulatory affairs, technical publications, or quality
  documentation lead at a medical device manufacturer, pharma, or biotech —
  someone whose IFU, SPL, CSR, or submission content has to survive FDA /
  EMA / PMDA / TGA review without triggering a 483, recall, or submission
  delay.
- **The one job:** prove that documentation in life sciences is a regulated
  asset (validated CCMS, multi-market profiling, audit-traceable change,
  paragraph-level compliance) — and convert.

---

## 2. Inventory — OLD page (ex-tense.co)
Five sections, single register:

1. **Hero** — dark navy banner. H1 "Life Sciences & Pharma" + subdeck.
2. **Labeling & Clinical Documentation** — heading + intro + **3-card grid**:
   Structured Product Labeling (SPL) · Instructions for Use (IFU) · Clinical
   Study Reports (CSR).
3. **Regulatory Compliance Infrastructure** — heading + intro + **3-card
   grid**: 21 CFR Part 11 Compliance · UDI & Symbol Management · Multi-Market
   Submissions, plus a green-outlined **"Regulatory Agility in Practice"
   callout** below the cards (proof-point: EU MDR symbol change → 4,500 IFUs
   republished overnight across 30+ languages).
4. **Free Regulatory Content Assessment** — dark navy mid-page CTA banner.
5. **Explore Related Industries** — **1-card cross-link**: Government &
   Defense (only).

All body copy reads clean under the locked voice — no banned verbs needing
substitution. Section 5's single-card sparseness flagged in mapping
decisions.

## 3. Inventory — NEW site (current)
Built on shared `IndustryPageLayout`:

- Hero (FDA-Class-I-recall-framed subdeck)
- Document Types (5)
- Standards (7 — including EU MDR + ISO 14971 added per page)
- **AuditCycle** (3-lane timeline: Submissions / Surveillance / Safety
  events — content-rich)
- Failure-Mode callout (FDA Class I recall)
- Signals (4 buyer-symptom lines)
- **Capability Relevance** (4 cards) — **stale** `/capabilities/*` links.
- Case Studies (2)
- CTAModule (generic, `general` audience)

Reuse from the template: nothing structural; bespoke rebuild replaces the
page. Atoms (`Hero`, `SectionSiblings`, `CTAModule`) carry over.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order preserved. All 5 old sections
  pulled forward. Single register (no civilian/defense pairing).
- **D-1 — H1 = [OLD] verbatim "Life Sciences & Pharma"** *(locked).*
  Owner-chosen. Already specific (names the two sub-domains the page covers)
  — no [DRAFT] substitution needed.
- **D-2 — Hero subdeck = [OLD] verbatim** — "Structured content management
  for FDA, EMA, and MDR compliance — where content errors affect patient
  safety and can delay market authorization by months."
- **D-3 — S4 "Regulatory Agility in Practice" callout** rendered as
  `#fef3c7` amber-tinted callout (established idiom from /industries
  adjacent-industries section) — body [OLD] verbatim. Sits inside section
  4 below the 3-card grid; full-width container-prose width; amber
  border-left + small mono "PROOF POINT" eyebrow above the heading.
- **D-4 — S5 "Explore Related" = 3-card mix** *(locked — Option B).*
  Old page has 1 card (Government & Defense); expanded to 3 to match the
  FS Related pattern and avoid a visually sparse single-card row.
  - Card 1: **[OLD]** INDUSTRY · Government & Defense (verbatim body).
  - Card 2: **[DRAFT]** SOLUTION · XML Data Interoperability — fit: SPL
    XML, eCTD submissions, and HL7 vocabulary are the page's named XML
    artifacts.
  - Card 3: **[DRAFT]** SERVICE · CCMS Services — fit: S3 intro literally
    names "component content management systems (CCMS)" as the engineering
    discipline the page argues for.
- **D-5 — CTA name = [OLD] "Free Regulatory Content Assessment"** with
  [OLD] body verbatim. Audience = `general` (life sciences is private
  sector).
- **D-6 — Hero side-visual = life-sciences-themed document-grade SVG**
  (concepts to mock after wireframe sign-off, same workflow as G&D / FS).
  Most promising directions:
  - **(a)** Multi-market submission fan — central `<content>` source chip
    with radial outputs to FDA · EMA · PMDA · TGA regulator chips
    (parallels the page's Multi-Market Submissions card thesis).
  - **(b)** IFU translation propagation — central `<ifu>` source with a
    "safety warning · v3.2" change marker, and 30+ language outputs
    receiving the propagated change (literal rendering of the IFU card's
    example: "change a safety warning once, system flags all 30 language
    versions").
  - **(c)** Component content reuse + audit (similar to FS Option E
    pattern, specialized for life sciences) — `<component>` source →
    21 CFR Part 11 audit metadata band → deliverables (IFU · SPL · CSR ·
    Submission Module).
- **D-7 — Banded-section rhythm:** S3 plain · S4 band · S5 plain. Three
  body sections; alternating with one banded middle. Same rhythm as FS.
- **D-8 — Retire `IndustryPageLayout` usage on this page.** Pattern set
  by G&D / FS. Other 3 industry pages stay on the template for now.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + life-sciences-themed side visual
- **H1** `[OLD]`: "Life Sciences & Pharma"
- **Subdeck** `[OLD]`: "Structured content management for FDA, EMA, and
  MDR compliance — where content errors affect patient safety and can
  delay market authorization by months."
- `subdeckMaxWidth="520px"` (matches /industries hero treatment).
- **Side visual:** TBD post-sign-off; mock candidates per D-6.

### S2 — Siblings nav · `SectionSiblings` (variant="industries")
- current = **Life Sciences** (amber + bold).

### S3 — Labeling & Clinical Documentation `[OLD]` · 3-card grid
- **Heading** `[OLD]`: "Labeling & Clinical Documentation"
- **Intro** `[OLD]`: "In Life Sciences, content is a regulated asset. We
  implement component content management systems (CCMS) that enforce data
  integrity, traceability, and multi-market compliance at the paragraph
  level."
- **3 cards** `[OLD]` (bare amber line icons, hairline border):
  1. **Structured Product Labeling (SPL)** *(icon: doc)* — "We convert
     unstructured design files into FDA-compliant SPL XML. Drug listing
     data, package inserts, and medication guides are structured once and
     published to DailyMed, the FDA Electronic Submissions Gateway, and
     print simultaneously. Every element carries HL7 SPL vocabulary
     codes."
  2. **Instructions for Use (IFU)** *(icon: globe)* — "IFUs for medical
     devices must be published in 30+ languages and comply with EU MDR,
     FDA 21 CFR Part 820, and ISO 13485. We manage translations at the
     component level — change a safety warning once, and the system flags
     all 30 language versions for translation update with full
     traceability."
  3. **Clinical Study Reports (CSR)** *(icon: activity-pulse — reuse FS
     pulse)* — "CSRs are the backbone of regulatory submissions. We
     structure them so data tables auto-populate from SAS/R datasets,
     narrative sections follow ICH E3 guidelines, and cross-references
     resolve automatically. This accelerates the submission-ready
     timeline from months to weeks."

### S4 — Regulatory Compliance Infrastructure `[OLD]` · 3-card grid + amber callout (banded)
- **Heading** `[OLD]`: "Regulatory Compliance Infrastructure"
- **Intro** `[OLD]`: "Regulatory requirements differ by market (FDA, EMA,
  PMDA, TGA) and product class. Your content system must enforce
  compliance rules, not rely on authors to remember them."
- **3 cards** `[OLD]`:
  1. **21 CFR Part 11 Compliance** *(icon: shield — reuse G&D shield)* —
     "Electronic signatures, audit trails, and access controls that
     satisfy FDA Part 11 requirements. Every content change is
     timestamped, attributed to a named individual, and locked into a
     tamper-evident baseline. No content leaves the system without
     validated sign-off."
  2. **UDI & Symbol Management** *(icon: grid-of-squares — 2×2 grid icon)*
     — "Unique Device Identification (UDI) data and ISO 15223 symbols are
     managed as structured metadata — not embedded images. When the EU
     MDR changes a symbol requirement, update the central library once
     and republish thousands of IFUs with the correct symbols overnight."
  3. **Multi-Market Submissions** *(icon: users — reuse FS users)* — "A
     single content repository serves FDA (eCTD Module 3), EMA
     (NeeS/eCTD), and regional agencies. Market-specific profiling
     generates the correct document set for each authority — same source
     content, different regulatory packaging."
- **"Regulatory Agility in Practice" callout** `[OLD]` (amber `#fef3c7`,
  amber-pressed border-left, mono PROOF POINT eyebrow, sits below the
  card grid, full-width container-prose):
  - **Eyebrow** `[DRAFT — locked]`: "PROOF POINT" (mono caps, new in this
    context; established label style from /industries adjacent-callout).
  - **Heading** `[OLD]`: "Regulatory Agility in Practice"
  - **Body** `[OLD]`: "When the EU MDR regulations changed requirements
    for standard symbols on medical device IFUs, our clients updated
    their central symbol library once. The system automatically
    republished 4,500 IFUs with the correct symbols overnight — across
    30+ languages, with full audit trail documentation for notified
    body review."

### S5 — Explore Related `[OLD + DRAFT]` · 3-card cross-link
- **Heading** `[DRAFT]` (per established G&D/FS precedent — drops the
  "Industries" qualifier since the section carries Industry + Solution +
  Service): "Explore Related"
- **Card 1** `[OLD]` — eyebrow "INDUSTRY", title "Government & Defense",
  body:
  > "S1000D, MIL-STD, and ITAR-compliant documentation with air-gapped
  > publishing pipelines."

  Link target: `/industries/government-and-defense`, CTA "EXPLORE →".
- **Card 2** `[DRAFT]` — eyebrow "SOLUTION", title "XML Data
  Interoperability", body:
  > "FDA SPL XML generation, eCTD submission assembly, and HL7 vocabulary
  > integration from structured content."

  Link target: `/solutions/xml-data-interoperability`, CTA "EXPLORE →".
- **Card 3** `[DRAFT]` — eyebrow "SERVICE", title "CCMS Services", body:
  > "Validated CCMS implementation for regulated content — 21 CFR Part 11
  > authoring workflows, audit trails, and multi-market publishing."

  Link target: `/services/ccms-services`, CTA "EXPLORE →".

### S6 — CTA · `CTAModule` (audience="general")
- **Heading** `[OLD]`: "Free Regulatory Content Assessment"
- **Body** `[OLD]`: "Share a sample IFU, SPL, or submission component.
  We'll analyze structure, identify multi-market profiling opportunities,
  and map the path to a component-based regulatory content architecture.
  No commitment required."

  (Body partially visible in screenshot 5 — the visible fragment ends
  with "component-based regulatory content architecture. No commitment
  required." This proposed copy reconstructs the full body consistent
  with the visible fragment and the FS / G&D CTA patterns. **Flag for
  sign-off** — only spot where reconstructed copy is needed.)
- CTA button label: matches existing CTAModule convention ("Request Your
  Free Assessment").

---

## 6. Decision log
- **D-1** *(locked)* — H1 = [OLD] "Life Sciences & Pharma".
- **D-2** *(locked)* — Hero subdeck = [OLD] verbatim.
- **D-3** *(locked)* — S4 "Regulatory Agility in Practice" callout
  rendered as `#fef3c7` amber-tinted block below the cards.
- **D-4** *(locked — Option B)* — S5 = 3-card mix: [OLD] Industry +
  [DRAFT] Solution + [DRAFT] Service.
- **D-5** *(locked)* — CTA name = [OLD] "Free Regulatory Content
  Assessment"; body partially [DRAFT-reconstructed] — flag for sign-off.
- **D-6** *(pending owner)* — Hero side-visual concept: candidates A
  (multi-market submission fan), B (IFU translation propagation), C
  (component-content reuse + audit). Mock 2–3 on a temp route after
  wireframe sign-off.
- **D-7** *(locked)* — Banded rhythm: S3 plain · S4 band · S5 plain.
- **D-8** *(locked)* — Retire `IndustryPageLayout` usage on this page;
  bespoke build with page-local CSS prefix `ls-`.

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)
| Loc | Tag | Item |
|-----|-----|------|
| S4  | `[DRAFT-locked]` | "PROOF POINT" eyebrow (D-3) |
| S5  | `[DRAFT-locked]` | Heading "Explore Related" (drops Industries) |
| S5  | `[DRAFT]` | Card 2 — SOLUTION · XML Data Interoperability body |
| S5  | `[DRAFT]` | Card 3 — SERVICE · CCMS Services body |
| S6  | `[DRAFT-reconstructed]` | CTA body (full text — only partial visible in screenshot; reconstructed to match visible fragment) |

All section bodies + cards in S3, S4 are `[OLD]` verbatim. S5 card 1
+ S4 callout are `[OLD]` verbatim.
