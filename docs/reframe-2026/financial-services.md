# Financial Services (industry sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** Second of the 6 `/industries/<slug>`
> sub-pages ported as a faithful reframe (old-site content, new-site design).
> Bespoke build (page-local CSS, prefix `fs-`), reusing the shared atoms
> (`Hero`, `SectionSiblings`, `CTAModule`) and the patterns proven on
> G&D and the service detail pages (3-card grids with bare amber line icons,
> sub-block heading+paragraph above a card row, 3-card cross-link, hero
> document-grade SVG visual, `section-band` rhythm). Replaces the current
> `IndustryPageLayout`-based page; the layout's stale `/capabilities/*`
> links go away with it.
>
> **Locked this session (2026-06-03):** H1 = "Financial Services
> Documentation & Compliance"; faithful — all 5 old-page sections kept
> verbatim; single-register page (no civilian/defense parallel like G&D);
> old's "Free Compliance Content Assessment" CTA name preserved.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [government-and-defense.md](government-and-defense.md).

---

## 1. Page job
- **URL:** `/industries/financial-services` (unchanged)
- **Primary reader:** documentation / records / control lead at a bank,
  brokerage, asset manager, fintech, or insurer with a SOX 404 exposure —
  someone whose policy, disclosure, and audit-trail content has to survive
  examiner review (SOX / SEC / OCC / FRB / FINRA / ESMA / FCA).
- **The one job:** prove that documentation in financial services is part
  of the control surface (single-source policy reuse, XBRL filing,
  multi-jurisdiction profiling, audit-traceable diffs) — and convert.

---

## 2. Inventory — OLD page (ex-tense.co)
Five sections, single register:

1. **Hero** — dark navy banner. H1 "Financial Documentation Strategy" +
   subdeck.
2. **Regulatory Velocity** — heading + intro + **3-card grid**:
   Policy & Procedure Management · Dynamic Reporting · Audit Trails &
   Compliance.
3. **The Single Source of Truth for Financial Institutions** — heading +
   intro + **"Unified Content Strategy" sub-block** (own micro-heading +
   paragraph) + **3-card grid**: XBRL & Regulatory Filing · Multi-Jurisdiction
   Delivery · Client Onboarding Docs.
4. **Free Compliance Content Assessment** — dark navy mid-page CTA banner
   with named offer.
5. **Explore Related Industries** — **3-card cross-link**: Insurance
   (industry) · XML Data Interoperability (solution) · Structured Content
   Strategy (service).

All body copy reads clean under the locked voice — no banned verbs needing
substitution.

## 3. Inventory — NEW site (current)
Built on shared `IndustryPageLayout`:

- Hero (SOX-framed subdeck)
- Document Types (5)
- Standards (5)
- **Control Chain** (5-stage timeline, content-rich)
- Failure-Mode callout (SOX 10-K material weakness)
- Signals (4 buyer-symptom lines)
- **Capability Relevance** (4 cards) — **stale**: all four link to
  `/capabilities/*`, retired in the Solutions reframe. Dead links.
- Case Studies (2)
- CTAModule (generic, `general` audience)

Reuse from the template: nothing structural; the bespoke rebuild replaces
the page. Atoms carry over (`Hero`, `SectionSiblings`, `CTAModule`).

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order preserved. All 5 old
  sections pulled forward. No civilian/defense pairing (single-register
  page, unlike G&D).
- **D-1 — H1 = "Financial Services Documentation & Compliance"** *(locked).*
  Owner-chosen `[DRAFT]` substitution. Carries domain (financial services),
  content scope (documentation), and the audit lens (compliance) in one
  line. Old verbatim "Financial Documentation Strategy" was too generic.
- **D-2 — Hero subdeck = `[OLD]` verbatim** — "Precision, compliance, and
  auditability for banking, fintech, and capital markets — where a single
  content error can trigger regulatory action." Lands the audience + the
  stakes without rewriting.
- **D-3 — S4 "Unified Content Strategy" sub-block layout:** full-width
  micro-heading + paragraph between the section intro and the 3-card grid
  (matches old's vertical layout). New page-local pattern
  `.fs-subblock` — hairline border-top, generous internal padding, body
  copy at text-body-lg to read as a callout. No amber tint (it's not a
  warning callout); subtle structural separation only.
- **D-4 — S5 "Explore Related" = 3-card grid** (not 2-card like G&D).
  Old page carries Industry + Solution + Service. Heading drops the
  "Industries" qualifier per the precedent set on G&D.
- **D-5 — CTA name = `[OLD]` "Free Compliance Content Assessment"** with
  `[OLD]` body verbatim. Audience = `general` (financial services is
  private sector, not `public-sector`).
- **D-6 — Hero side-visual = financial-themed document-grade SVG**
  (concepts to mock after wireframe sign-off, same workflow as G&D /
  Publishing / CCMS / SI / XML). Most promising directions:
  - **(a)** Single-source reuse fan — central `<policy>` chip with radial
    output chips (Employee Handbook · Compliance Manual · Training Deck ·
    Client Disclosure · XBRL filing) — argues the Unified Content Strategy
    thesis that the page's S4 sub-block names.
  - **(b)** SOX control chain pipeline — Authorship → Approval → Version
    Control → Audit → External Disclosure (5-stage horizontal) — argues
    the audit-traceability thesis.
  - **(c)** Multi-jurisdiction profiling fan — one `<master>` doc + radial
    state/country/entity outputs.
- **D-7 — Banded-section rhythm:** S3 plain · S4 band · S5 plain. Three
  body sections; alternating reads cleanest with one banded middle.
- **D-8 — Retire `IndustryPageLayout` usage on this page.** Pattern set
  by G&D port. Other 4 industry pages stay on the template for now.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + financial-themed side visual
- **H1** `[LOCKED]`: "Financial Services Documentation & Compliance"
- **Subdeck** `[OLD]`: "Precision, compliance, and auditability for
  banking, fintech, and capital markets — where a single content error
  can trigger regulatory action."
- `subdeckMaxWidth="520px"` (matches /industries hero treatment).
- **Side visual:** TBD post-sign-off; mock candidates per D-6.

### S2 — Siblings nav · `SectionSiblings` (variant="industries")
- current = **Financial Services** (amber + bold).

### S3 — Regulatory Velocity `[OLD]` · 3-card grid
- **Heading** `[OLD]`: "Regulatory Velocity"
- **Intro** `[OLD]`: "Financial regulations change daily. Your documentation
  — policies, procedures, prospectuses, and disclosures — must keep pace
  without error, without duplication, and with a complete audit trail."
- **3 cards** `[OLD]` (bare amber line icons, hairline border):
  1. **Policy & Procedure Management** *(icon: doc)* — "We decouple policy
     logic from formatting. A 'KYC Procedure' is authored once and
     transcluded (conref) into the Employee Handbook, the Compliance
     Manual, and the Online Help portal. When Compliance updates the
     source, all downstream deliverables update automatically."
  2. **Dynamic Reporting** *(icon: monitor / chart)* — "Generate
     client-specific investment reports, prospectuses, and disclosure
     documents by assembling XML data with pre-approved narrative blocks.
     Zero copy-paste errors. Full version history for every assembled
     output."
  3. **Audit Trails & Compliance** *(icon: shield)* — "Who changed the
     interest rate disclosure? When? Why? We provide Git-level diffs for
     every word change, reviewer sign-off tracking, and timestamped
     baselines that satisfy SOX, SEC, OCC, and FINRA auditors."

### S4 — The Single Source of Truth for Financial Institutions `[OLD]` · sub-block + 3-card grid (banded)
- **Heading** `[OLD]`: "The Single Source of Truth for Financial
  Institutions"
- **Intro** `[OLD]`: "Banks and financial firms share a common problem:
  the same policy content is rewritten independently by Risk, Operations,
  Training, and Legal — creating inconsistencies that auditors flag."
- **Unified Content Strategy sub-block** `[OLD]` (full-width, between intro
  and cards):
  - Sub-heading: "Unified Content Strategy"
  - Body: "The Risk team authors the core regulatory requirement once.
    That specific paragraph is technically transcluded (conref) into the
    Operations Manual, the Training Deck, and the Client-Facing
    Disclosure. If Risk updates the policy, every downstream deliverable
    reflects the change automatically — with a full audit trail of who
    changed what, when, and why."
- **3 cards** `[OLD]`:
  1. **XBRL & Regulatory Filing** *(icon: activity-pulse)* — "Automated
     generation of XBRL-tagged financial data from structured content.
     SEC 10-K/10-Q filings, ESMA ESEF reports, and iXBRL inline tagging
     — generated from the same XML source as the human-readable
     documents."
  2. **Multi-Jurisdiction Delivery** *(icon: globe)* — "DITA profiling
     (conditional text) manages jurisdiction-specific variations. One
     master disclosure document produces state-specific, country-specific,
     or entity-specific updates — with an automatic audit trail to each
     regulatory authority."
  3. **Client Onboarding Docs** *(icon: users)* — "Account opening
     packages, terms of service, and fee schedules assembled dynamically
     based on product type, account tier, and jurisdiction. Reduce
     onboarding document preparation from days to minutes."

### S5 — Explore Related `[OLD]` · 3-card cross-link
- **Heading** `[DRAFT]` (per G&D precedent — drops "Industries" since
  the section carries Industry + Solution + Service): "Explore Related"
- **Card 1** `[OLD]` — eyebrow "INDUSTRY", title "Insurance", body:
  > "Modular policy architectures with 50-state conditional filtering
  > and automated assembly."

  Link target: `/industries/insurance`, CTA "EXPLORE →".
- **Card 2** `[OLD]` — eyebrow "SOLUTION", title "XML Data
  Interoperability", body:
  > "XBRL integration, schema validation, and API-driven content delivery
  > for regulatory systems."

  Link target: `/solutions/xml-data-interoperability`, CTA "EXPLORE →".
- **Card 3** `[OLD]` — eyebrow "SERVICE", title "Structured Content
  Strategy", body:
  > "Taxonomy design, governance frameworks, and reuse architecture for
  > enterprise content."

  Link target: `/services/structured-content-strategy`, CTA "EXPLORE →".

### S6 — CTA · `CTAModule` (audience="general")
- **Heading** `[OLD]`: "Free Compliance Content Assessment"
- **Body** `[OLD]`: "Share a sample policy or disclosure document. We'll
  analyze reuse potential, identify duplication risk across departments,
  and map the path to a single-source content architecture. No commitment
  required."
- CTA button label: matches existing CTAModule convention ("Request Your
  Free Assessment").

---

## 6. Decision log
- **D-1** *(locked)* — H1 = "Financial Services Documentation &
  Compliance".
- **D-2** *(locked)* — Hero subdeck = `[OLD]` verbatim.
- **D-3** *(locked)* — S4 sub-block = full-width sub-heading + paragraph
  between section intro and the 3-card grid (matches old layout).
- **D-4** *(locked)* — S5 = 3-card cross-link, heading "Explore Related"
  (G&D precedent).
- **D-5** *(locked)* — CTA name + body = `[OLD]` verbatim; audience =
  `general`.
- **D-6** *(pending owner)* — Hero side-visual concept: candidates A
  (single-source reuse fan), B (SOX control chain), C (multi-jurisdiction
  profiling). Mock 2–3 on a temp route after wireframe sign-off.
- **D-7** *(locked)* — Banded-section rhythm: S3 plain · S4 band · S5
  plain.
- **D-8** *(locked)* — Retire `IndustryPageLayout` usage on this page;
  bespoke build with page-local CSS prefix `fs-`.

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)
| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[DRAFT-locked]` | H1 "Financial Services Documentation & Compliance" (D-1) |
| S5  | `[DRAFT-locked]` | Heading "Explore Related" (D-4, follows G&D precedent) |

All body copy is `[OLD]` verbatim — no other `[DRAFT]` items needing
sign-off.
