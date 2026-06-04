# Our Process (Company sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** Net-new page (current
> `/company/our-process` is a stub). Built to *deepen* the 5-phase
> methodology that `/company` only summarizes — each phase gets a deep
> section with deliverables, typical duration, exit criteria, and client
> touchpoints. Carries forward the old page's continuous-improvement loop
> ("Full Circle") and the 4-stat outcomes band; cuts the bits that are
> redundant with `/company`.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = the case-study detail pages for layout density (mono rail labels +
> structured-data right column).

---

## 1. Page job
- **URL:** `/company/our-process`
- **Primary reader:** procurement / evaluator / engineering champion who
  has read `/company` (firm identity) and now wants to understand exactly
  how a typical engagement unfolds — what they'd see week by week, what
  they'd receive at each gate, when each phase ends.
- **The one job:** answer *"what does each phase of working with Extense
  actually look like in practice?"* with enough specificity that a
  potential client can plan a procurement timeline and a contracting
  officer can scope an RFP against it.

---

## 2. Inventory — OLD page (extense.co/our-process)

1. **Hero** — H1 "Our Process" + subdeck "Methodology that Delivers Results."
2. **Our Methodology** — 5-step horizontal strip with amber connector arrows:
   - 01 Discovery — Stakeholder Interviews & Content Audit
   - 02 Architecture — Taxonomy & DITA Model Design
   - 03 Migration — Batch Conversion & Cleanup
   - 04 Implementation — CCMS Config & Stylesheet Dev
   - 05 Enablement — Training & Handover
   - Intro: *"A proven path to content maturity. We guide you through every step of the transformation."*
3. **3 Phase-group cards** (Discovery / Design / Deployment) — coarse
   groupings of the 5 phases, ~30-word body each.
4. **The Full Circle Approach** — 6-cell continuous loop:
   - Top row: 01 Discover → 02 Architect → 03 Migrate
   - Bottom row (reversed): 06 Optimize ← 05 Enable ← 04 Build
   - `↻ CONTINUOUS IMPROVEMENT` label in the middle
   - Intro: *"Inspired by decades of experience: every phase feeds the next. There is no hand-off gap."*
5. **What Makes Our Process Different** — 3-col (Agile Delivery / Prototype-First / Built-In Enablement)
6. **Typical Client Outcomes** — 4-stat band:
   - 60% — FASTER PUBLISHING
   - 72% — TRANSLATION SAVINGS
   - 45% — CONTENT REUSE RATE
   - 90% — FEWER SUPPORT TICKETS
7. **Free Content Health Check** — dark navy CTA banner
8. Stay Connected newsletter (banned — locked rule)

## 3. Inventory — NEW site (current state)
- **`/company/our-process`** — stub page (Hero only, "Coming soon" subdeck).
- **`/company` (main)** — already carries the 5-phase methodology as
  "How we work" (Discovery / Architecture / Migration / Implementation /
  Enablement, one paragraph each) AND the 3 principles (Agile delivery /
  Prototype-first / Built-in enablement). These two sections on `/company`
  cover old §2 and old §5 directly.

---

## 4. Mapping decisions

- **D-1 — H1 = [OLD] "Our Process".** Verbatim. Procurement-search-friendly.
- **D-2 — Hero subdeck = [DRAFT]** "Five phases. Continuous improvement.
  Inspectable artifacts at every step." Signals the page's three
  load-bearing claims (linear methodology + continuous loop + evidence).
- **D-3 — Drop "What Makes Our Process Different"** (old §5). The same
  three principles already appear on `/company` as "Principles in
  practice." Duplicating them here adds nothing and dilutes the page's
  process-depth focus.
- **D-4 — Drop the 3 Phase-group cards** (old §3, Discovery/Design/
  Deployment Phase). Coarse groupings of the 5 phases; redundant with the
  per-phase deep dive in this page's S3 and with `/company`'s methodology
  section. Cutting clears space for the deep-dive without losing content.
- **D-5 — Keep the 5-phase overview strip as a visual anchor before the
  deep-dive.** Familiar shape from the old page; orients the reader
  before the long-form sections.
- **D-6 — Per-phase deep-dive (S3) is the page's load-bearing net-new
  content.** Each phase gets a section with: body paragraph (extended
  from `/company`'s one-paragraph summary), Deliverables, Typical duration,
  Exit criteria, Client touchpoints. 4 facets per phase, 5 phases = 20
  data points the reader can take to a procurement conversation.
- **D-7 — The Full Circle (S4) is the second load-bearing reuse.**
  Genuinely distinct from the linear 5-phase strip — it adds Build and
  Optimize as continuous steps and frames post-handover engagement as a
  loop, not a hand-off. Rebuilt as a document-grade SVG (6-cell flow with
  amber connectors, corner reg-marks, mono FIG. chrome) in the established
  Extense visual idiom — same family as the case-study heroes.
- **D-8 — Typical Client Outcomes (S5) lifted [OLD] verbatim** — concrete
  numbers anchor the page after the methodology depth.
- **D-9 — Drop the custom "Free Content Health Check" CTA banner** in
  favor of the shared CTAModule (already does this exact offer site-wide).
- **D-10 — Drop the newsletter section** (locked rule).
- **D-11 — Section order:** Hero → 5-phase strip → 5 deep-dive sections
  → Full Circle → Outcomes → CTA. Reads as: overview → depth → continuity
  → proof → conversion.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal, no side visual)
- **H1** `[OLD]`: "Our Process"
- **Subdeck** `[DRAFT]`: "Five phases. Continuous improvement. Inspectable
  artifacts at every step."
- `subdeckMaxWidth="540px"`.
- No side visual — the 5-phase strip in S2 is the page's first visual
  anchor; a hero visual would compete.

### S2 — The five phases (overview strip) `[OLD]`
- **Heading** `[OLD]`: "The five phases"
- **Intro** `[DRAFT, lightly-edited from OLD]`: "A proven sequence from
  raw content to a published, operational, AI-ready program. Every
  phase produces inspectable artifacts you can review before the next
  begins."
- **5-cell strip** (mono numbered cards, amber connector between):
  - 01 · Discovery — Stakeholder interviews & content audit
  - 02 · Architecture — Taxonomy & DITA model design
  - 03 · Migration — Batch conversion & cleanup
  - 04 · Implementation — CCMS config & stylesheet dev
  - 05 · Enablement — Training & handover

### S3 — Phase by phase (deep-dive) `[DRAFT, extended from OLD + /company]`

Five sub-sections, one per phase. Each follows the same rail-grid
pattern: phase number in the left rail (mono), phase content in the
right column. Right column contains: heading, body paragraph, then a
4-facet panel (Deliverables · Typical duration · Exit criteria · Client
touchpoints).

#### S3.1 — Discovery
- **Body** `[lightly extended from /company OLD]`: "We don't move past
  Discovery until the constraints that would otherwise sink a content
  model have surfaced. That includes interviewing the people who will
  produce, edit, and consume the content, auditing what exists today,
  and mapping the use cases the system has to support. The goal isn't
  to gather requirements; it's to find the constraints the architecture
  has to obey."
- **Deliverables** `[DRAFT]`: Stakeholder interview synthesis · Content
  inventory and audit · Use-case map · Constraints register
- **Typical duration** `[DRAFT]`: 2–4 weeks, depending on content
  corpus size and number of stakeholder groups
- **Exit criteria** `[DRAFT]`: Constraints register signed off; use
  cases mapped to capabilities; no surfaced blocker remains unresolved
- **Client touchpoints** `[DRAFT]`: Weekly working session with content
  owners; one full readout at end of phase with stakeholder review

#### S3.2 — Architecture
- **Body** `[from /company OLD]`: "The architecture is the leverage
  point. Schema design, taxonomy, metadata strategy, and reuse decisions
  made here determine what's possible in every downstream phase. We
  design against the use cases Discovery surfaced, not against generic
  structured-content principles. The architecture has to work for this
  client's content, not for a textbook example of DITA."
- **Deliverables** `[DRAFT]`: Information model (DITA specialization,
  schema, subject scheme) · Taxonomy and metadata strategy · Reuse
  model · Publishing target spec
- **Typical duration** `[DRAFT]`: 3–6 weeks
- **Exit criteria** `[DRAFT]`: Schema validates against a representative
  content sample; metadata fields enumerated; reuse boundaries explicit;
  client team can author a topic in the model and have it validate
- **Client touchpoints** `[DRAFT]`: Weekly schema review with editorial
  leads; one mid-phase prototyping checkpoint with sample topic walkthrough

#### S3.3 — Migration
- **Body** `[from /company OLD]`: "Migration is recovery, not
  transcription. The conversion engine identifies reusable assets in
  legacy content and lifts them into the target schema; what isn't
  recoverable gets retired or rewritten with intent. We design the QA
  harness before the first batch runs — failing migrations fail because
  the validation strategy was an afterthought."
- **Deliverables** `[DRAFT]`: QA harness · Conversion pipeline ·
  Migration batches (typically iterative) · Per-batch recovery report
- **Typical duration** `[DRAFT]`: 4–12 weeks, proportional to corpus
  size; the first batch often spans 2–3 weeks alone
- **Exit criteria** `[DRAFT]`: QA harness passes on representative
  sample; recovery rate target met; rejected content categorized for
  retirement or rewrite
- **Client touchpoints** `[DRAFT]`: Weekly migration status reports
  with batch metrics; per-batch review of QA failures

#### S3.4 — Implementation
- **Body** `[from /company OLD]`: "Implementation makes the architecture
  operational across the toolchain — CCMS configuration, publishing
  pipelines, integration points. The discipline at this phase is to
  resist scope expansion: every feature added during implementation is
  a feature the team has to maintain afterward. We deliver the smallest
  implementation that runs."
- **Deliverables** `[DRAFT]`: CCMS configuration · Publishing pipeline
  (containerized DITA-OT or equivalent) · Integration points (API
  connectors, webhooks) · CI/CD wiring · System documentation
- **Typical duration** `[DRAFT]`: 6–10 weeks
- **Exit criteria** `[DRAFT]`: End-to-end publish from CCMS to all
  target outputs; production push tested; rollback procedure validated
- **Client touchpoints** `[DRAFT]`: Biweekly sprint reviews with
  engineering and content stakeholders; UAT with author cohort before
  go-live

#### S3.5 — Enablement
- **Body** `[from /company OLD]`: "Enablement runs through every phase,
  not at the end. Discovery teaches the practitioner how the program
  works. Architecture documentation becomes the team's runbook. Migration
  training transitions authors. CCMS rollout becomes the operating
  manual. The handover isn't a phase — it's a discipline applied
  throughout."
- **Deliverables** `[DRAFT]`: Author training materials · Schema runbook
  · Troubleshooting guide · Ongoing-support playbook (escalation paths,
  common issues)
- **Typical duration** `[DRAFT]`: Runs through every prior phase;
  concentrated 3–4 weeks at the close of Implementation for formal training
- **Exit criteria** `[DRAFT]`: Authors produce valid topics
  independently; CCMS operations team resolves 80%+ of operational tasks
  without Extense; runbook captures known issues
- **Client touchpoints** `[DRAFT]`: Continuous from Phase 1; formal
  training events at end of Implementation; 30/60/90-day check-ins
  post-handover

### S4 — The Full Circle `[OLD intro + redesigned visual]`
- **Heading** `[OLD]`: "The Full Circle"
- **Intro** `[OLD]`: "Inspired by decades of experience: every phase
  feeds the next. There is no hand-off gap."
- **6-cell continuous-loop SVG**, document-grade idiom (corner
  reg-marks, mono FIG. chrome, amber connectors, IntersectionObserver
  `.drawn` scroll-reveal):
  - Top row L→R: 01 Discover · 02 Architect · 03 Migrate
  - Bottom row R→L (loop reverses): 04 Build · 05 Enable · 06 Optimize
  - Amber connectors forming a complete loop (right edge of top row →
    down to right edge of bottom row → bottom row back leftward → left
    edge of bottom row → up to left edge of top row)
  - Central `↻ extense.continuous` chip on the connector spine
  - FIG. label at bottom

### S5 — Typical client outcomes `[OLD]`
- **Heading** `[OLD]`: "Typical client outcomes"
- **Intro** `[DRAFT]`: "Aggregate improvements measured across recent
  engagements. Numbers reflect the methodology applied — not
  best-case projections."
- **4-stat band** `[OLD]`:
  - 60% — Faster publishing
  - 72% — Translation savings
  - 45% — Content reuse rate
  - 90% — Fewer support tickets

### S6 — CTA · `CTAModule` (audience="general")
- Use the shared CTAModule. Replaces the custom "Free Content Health
  Check" navy banner from the old page (same offer site-wide; consistent
  treatment).
- **Heading** `[OLD-derived]`: "Free Content Health Check"
- **Body** `[OLD-derived]`: "Upload a 20-page sample document. We'll
  return conversion feasibility, reuse potential, and ROI projection
  within two business days — at no cost."

---

## 6. Decision log
- **D-1** *(locked)* — H1 = [OLD] "Our Process".
- **D-2** *(pending)* — Subdeck = [DRAFT] "Five phases. Continuous
  improvement. Inspectable artifacts at every step."
- **D-3** *(locked)* — Drop "What Makes Our Process Different"
  (redundant with /company Principles in practice).
- **D-4** *(locked)* — Drop the 3 Phase-group cards (redundant with
  per-phase deep-dive and /company methodology).
- **D-5** *(locked)* — Keep the 5-phase overview strip as visual
  anchor before deep-dive.
- **D-6** *(locked)* — Per-phase deep-dive structure: body + 4 facets
  (Deliverables · Duration · Exit criteria · Touchpoints).
- **D-7** *(locked)* — Full Circle = redesigned 6-cell SVG loop in
  document-grade idiom.
- **D-8** *(locked)* — Outcomes 4-stat band lifted [OLD] verbatim.
- **D-9** *(locked)* — CTA = shared CTAModule, drop custom banner.
- **D-10** *(locked)* — Drop newsletter.
- **D-11** *(locked)* — Section order: Hero → strip → deep-dive →
  Full Circle → outcomes → CTA.

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)

| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[DRAFT]` | Subdeck "Five phases. Continuous improvement. Inspectable artifacts at every step." |
| S2  | `[DRAFT, lightly edited]` | Intro paragraph |
| S3  | `[DRAFT]` | All 4 facet entries (Deliverables / Duration / Exit criteria / Touchpoints) × 5 phases = 20 net-new items |
| S5  | `[DRAFT]` | Intro paragraph |

Everything else (H1, the 5-phase strip body lines, the Full Circle heading + intro, the outcomes stat band) is `[OLD]` verbatim.
