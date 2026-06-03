# Insurance (industry sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** Fifth of the 6 `/industries/<slug>`
> sub-pages ported as a faithful reframe. Bespoke build (page-local CSS,
> prefix `ins-`), reusing the shared atoms (`Hero`, `SectionSiblings`,
> `CTAModule`) and patterns proven on G&D / FS / LS / Transportation
> (3-card grids with bare amber line icons, 01–05 numbered roadmap strip,
> 3-card cross-link, hero document-grade SVG visual, `section-band` rhythm).
> Replaces the current `IndustryPageLayout`-based page; the layout's stale
> `/capabilities/*` links go away with it.
>
> **Locked this session (2026-06-03):** H1 = [OLD] verbatim "Insurance
> Policy Construction"; faithful — all 6 old-page sections kept [OLD]
> verbatim; CTA stays [OLD] "Free Policy Content Assessment".
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [transportation.md](transportation.md).

---

## 1. Page job
- **URL:** `/industries/insurance` (unchanged)
- **Primary reader:** policy-form / regulatory / claims-ops lead at a
  multi-state insurance carrier, MGA, or insurance-platform provider —
  someone whose policy forms, endorsements, and claims-handling content
  has to clear state DOI review, SERFF filing, and multi-stakeholder
  approval without drift across 50 jurisdictions.
- **The one job:** prove that an insurance policy is a *modular assembly*
  (reusable clauses × state-variant profiling × audit-grade versioning),
  not a document — and that the engineering for SERFF-ready filing,
  redline diffs, and multi-stakeholder review is core capability. Then
  convert.

---

## 2. Inventory — OLD page (ex-tense.co)
Six sections, single register:

1. **Hero** — dark navy banner. H1 "Insurance Policy Construction" +
   subdeck.
2. **Modular Policy Architectures** — heading + intro + **3-card grid**:
   Component Content Management · 50-State Conditional Filtering ·
   Endorsement Assembly.
3. **Regulatory Filing & Compliance** — heading + intro + **3-card
   grid**: SERFF-Ready Output · Redline & Comparison · Multi-Stakeholder
   Review.
4. **Policy Assembly Pipeline** — heading only + **5-step horizontal
   strip**: Base Form → Profiling → Endorsement Stack → Review & Approve
   → Publish & File.
5. **Free Policy Content Assessment** — dark navy mid-page CTA banner.
6. **Explore Related Industries** — **3-card cross-link**: Financial
   Services (industry) · Content Migration (solution) · DITA Engineering
   (service).

All body copy reads clean under the locked voice — no banned verbs needing
substitution.

## 3. Inventory — NEW site (current)
Built on shared `IndustryPageLayout`:

- Hero (policy-form-as-product subdeck)
- Document Types (5)
- Standards (4, including ACORD + NAIC ORSA)
- **`variantPolicyForm`** — bespoke render of a sample homeowners policy
  form with per-section state cardinality (NY/FL/CA/TX/etc. + overflow
  counts). The most distinctive piece of new-site content for this
  vertical; informed Concept C in the hero-visual brainstorm.
- Failure-Mode callout (DOI filing rejection)
- Signals (4 buyer-symptom lines)
- **Capability Relevance** (4 cards) — **stale** `/capabilities/*` links.
- Case Studies (2)
- CTAModule (generic)

Reuse from the template: nothing structural; bespoke rebuild replaces
the page. Atoms (`Hero`, `SectionSiblings`, `CTAModule`) carry over.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order preserved. All 6 OLD
  sections pulled forward.
- **D-1 — H1 = [OLD] verbatim "Insurance Policy Construction"**
  *(locked).* Already specific; no [DRAFT] substitution.
- **D-2 — Hero subdeck = [OLD] verbatim** — "Modular content
  architectures for multi-state, multi-product policy assembly — where
  a single misplaced clause can void coverage or trigger regulatory
  penalties."
- **D-3 — S5 Policy Assembly Pipeline = 01–05 numbered roadmap strip**
  (same idiom as G&D lifecycle / Transportation workflow). Should it
  carry contextual body paragraphs per step (LS precedent)? Default:
  no — keep terse title + 1-line desc per OLD. Flag for owner.
- **D-4 — S6 "Explore Related" = 3-card cross-link** [OLD] verbatim
  (Financial Services + Content Migration + DITA Engineering). Same
  3-card mix as FS/LS. Heading drops "Industries" per the established
  precedent.
- **D-5 — CTA name = [OLD] "Free Policy Content Assessment"** with
  [OLD] body verbatim. Audience = `general` (insurance is private
  sector).
- **D-6 — Hero side-visual = insurance-themed document-grade SVG.**
  Candidates A (50-state fan), B (component assembly), C (policy-record
  card) brainstormed; A judged repetitive vs LS/FS multi-jurisdiction
  patterns, C judged too body-like. Better synthesis proposed and locked
  as the candidate set to mock: **B + D** where
  - **B** — Component assembly: 5 clause components → 1 filing-package.
  - **D** — Component × jurisdiction assembly: 5 components → profiler
    (state filter) → assembled policy-form, with M×N multiplier
    footer. Combines the modular-component thesis (S3 lead-off card)
    with the 50-state-variant thesis (S3 second card).
- **D-7 — Banded-section rhythm:** S3 plain · S4 band · S5 plain · S6
  band. Same as Transportation/FS/LS.
- **D-8 — Retire `IndustryPageLayout` usage on this page.** Pattern
  set by G&D / FS / LS / Transportation. Only `/industries/technology`
  stays on the template afterward.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + insurance-themed side visual
- **H1** `[OLD]`: "Insurance Policy Construction"
- **Subdeck** `[OLD]`: "Modular content architectures for multi-state,
  multi-product policy assembly — where a single misplaced clause can
  void coverage or trigger regulatory penalties."
- `subdeckMaxWidth="520px"`.
- **Side visual:** TBD post-sign-off; mock candidates per D-6 (B + D).

### S2 — Siblings nav · `SectionSiblings` (variant="industries")
- current = **Insurance** (amber + bold).

### S3 — Modular Policy Architectures `[OLD]` · 3-card grid
- **Heading** `[OLD]`: "Modular Policy Architectures"
- **Intro** `[OLD]`: "An insurance policy is not a document — it is a
  modular assembly of declarations, insuring agreements, conditions,
  exclusions, and endorsements. Each component must be independently
  versioned, jurisdictionally filtered, and audit-trailed."
- **3 cards** `[OLD]` (bare amber line icons, hairline border):
  1. **Component Content Management** *(icon: grid)* — "Every clause,
     endorsement, and declaration page is stored as an independent,
     reusable content component. A 'Flood Exclusion' clause exists once
     and is assembled into every policy that requires it — Personal
     Auto, Commercial Property, Umbrella. Update the source, and every
     policy form that references it inherits the change."
  2. **50-State Conditional Filtering** *(icon: globe)* — "A single
     Auto Policy master contains every state-specific variation. DITA
     profiling attributes (state=\"CA NY TX\", product=\"auto\") control
     which paragraphs appear in which output. One source, 50 compliant
     publications — no manual copy-paste, no version drift."
  3. **Endorsement Assembly** *(icon: doc)* — "Endorsements modify base
     policy language. We build endorsement libraries where each
     endorsement is a standalone module with metadata linking it to
     applicable base forms, effective dates, and jurisdiction. The
     publishing engine assembles the correct endorsement stack per
     policy issuance."

### S4 — Regulatory Filing & Compliance `[OLD]` · 3-card grid (banded)
- **Heading** `[OLD]`: "Regulatory Filing & Compliance"
- **Intro** `[OLD]`: "Insurance content must satisfy state Departments
  of Insurance (DOI), SERFF filing requirements, and internal actuarial
  review — simultaneously."
- **3 cards** `[OLD]`:
  1. **SERFF-Ready Output** *(icon: shield)* — "Generate filing-ready
     PDF/A packages that meet SERFF submission requirements. Each filing
     includes the base form, applicable endorsements, rate pages, and a
     machine-readable change log showing exactly what differs from the
     previously approved version."
  2. **Redline & Comparison** *(icon: pulse — reuse FS/LS pulse)* —
     "Automated redline generation between policy versions. When an
     underwriter modifies terms, the system produces a word-level diff
     showing additions, deletions, and moved content — the exact artifact
     regulators and legal teams require for approval workflows."
  3. **Multi-Stakeholder Review** *(icon: users — reuse FS/LS users)* —
     "Actuarial, Legal, Compliance, and Product teams review the same
     structured source — not disconnected Word copies. Role-based review
     workflows ensure each stakeholder approves only their domain (rates,
     legal language, regulatory compliance) before the form advances to
     filing."

### S5 — Policy Assembly Pipeline `[OLD]` · 01–05 strip
- **Heading** `[OLD]`: "Policy Assembly Pipeline"
- **5 steps** `[OLD]` (01–05 numbered roadmap):
  1. **01 — Base Form** — "Base policy with all clauses and state
     variants"
  2. **02 — Profiling** — "Apply state, product, and coverage filters"
  3. **03 — Endorsement Stack** — "Attach applicable endorsements by
     metadata"
  4. **04 — Review & Approve** — "Multi-stakeholder sign-off workflow"
  5. **05 — Publish & File** — "Generate customer PDF + SERFF filing
     package"
- **D-3 — Step bodies:** default off (faithful to OLD). Flag for owner.

### S6 — Explore Related `[OLD]` · 3-card cross-link (banded)
- **Heading** `[DRAFT-precedent]`: "Explore Related"
- **Card 1** `[OLD]` — eyebrow "INDUSTRY", title "Financial Services",
  body:
  > "Policy management, regulatory filing, and audit trail solutions for
  > banking and capital markets."

  Link target: `/industries/financial-services`, CTA "EXPLORE →".
- **Card 2** `[OLD]` — eyebrow "SOLUTION", title "Content Migration",
  body:
  > "Migrate legacy Word-based policy forms to structured XML with
  > automated conversion pipelines."

  Link target: `/solutions/content-migration`, CTA "EXPLORE →".
- **Card 3** `[OLD]` — eyebrow "SERVICE", title "DITA Engineering",
  body:
  > "Specialization, profiling, and conditional publishing architectures
  > for complex document assembly."

  Link target: `/services/dita-engineering`, CTA "EXPLORE →".

### S7 — CTA · `CTAModule` (audience="general")
- **Heading** `[OLD]`: "Free Policy Content Assessment"
- **Body** `[OLD]`: "Share a sample policy form or endorsement library.
  We'll analyze your clause reuse potential, identify state-variation
  gaps, and map the path from Word-based forms to a modular content
  architecture. No commitment required."

---

## 6. Decision log
- **D-1** *(locked)* — H1 = [OLD] verbatim "Insurance Policy
  Construction".
- **D-2** *(locked)* — Hero subdeck = [OLD] verbatim.
- **D-3** *(pending owner)* — S5 workflow steps: terse (default, faithful
  to OLD) or add 1-2 sentence [DRAFT] bodies per step (LS precedent).
- **D-4** *(locked)* — S6 = 3-card cross-link [OLD] verbatim (Industry +
  Solution + Service). Heading "Explore Related" [DRAFT-precedent].
- **D-5** *(locked)* — CTA name + body = [OLD] verbatim; audience =
  `general`.
- **D-6** *(pending owner pick)* — Hero side-visual = B (component
  assembly) or D (component × jurisdiction). Mocked on
  `/insurance-mock`.
- **D-7** *(locked)* — Banded rhythm: S3 plain · S4 band · S5 plain ·
  S6 band.
- **D-8** *(locked)* — Retire `IndustryPageLayout` usage on this page;
  bespoke build with page-local CSS prefix `ins-`.

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)
| Loc | Tag | Item |
|-----|-----|------|
| S6  | `[DRAFT-precedent]` | Heading "Explore Related" (drops Industries) |

All body copy + cards in S3, S4, S5, S6, S7 are `[OLD]` verbatim. No
other `[DRAFT]` items.
