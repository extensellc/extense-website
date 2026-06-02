# Government Agencies & Defense (industry sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** First of the 6 `/industries/<slug>`
> sub-pages to be ported as a faithful reframe (old-site content, new-site
> design). Will be built **bespoke** (page-local CSS, prefix `gd-`), reusing
> the shared atoms (`Hero`, `nav/SiblingsBreadcrumb`, `CTAModule`) and the
> patterns proven on the service detail pages (icon-card grids, 01-0N numbered
> roadmap strip, `#fef3c7` callout, related-card two-up, hero document-grade
> SVG visual). Replaces the current `IndustryPageLayout`-based page entirely;
> the layout's stale `/capabilities/*` links go away with it.
>
> **Locked this session (2026-06-02):** H1 = "Government Agencies & Defense";
> faithful — all 6 old-page sections kept verbatim where possible; **equal
> weight** for civilian and defense via paired sections; old's "Free S1000D
> Readiness Assessment" CTA name preserved.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [xml-engineering.md](xml-engineering.md).

---

## 1. Page job
- **URL:** `/industries/government-and-defense` (unchanged)
- **Primary reader:** federal procurement / program lead at a defense prime
  or systems integrator (S1000D / IETM / ITAR-aware), OR a documentation /
  records-management lead at a civilian federal agency (Section 508 / FOIA /
  rulemaking-aware). Two registers, same page.
- **The one job:** demonstrate that the same engineering discipline handles
  both defense documentation (S1000D / MIL-STD / ITAR / IETMs) and civilian
  agency content (Section 508 / agency publishing standards / records
  management) — with equal depth, paired section-by-section.

---

## 2. Inventory — OLD page (ex-tense.co)
Six sections, defense-only, S1000D-centric:

1. **Hero** — dark navy banner. H1 "Defense & Aerospace Documentation" +
   subdeck.
2. **S1000D Implementation** — heading + intro + 3-card grid (Data Modules ·
   Applicability & Filtering · BREX Rules & Validation).
3. **Security & Compliance** — heading + intro + 3-card grid (ITAR &
   Classified Handling · Air-Gapped Publishing · Audit & Traceability).
4. **The S1000D Lifecycle** — 5-step horizontal flow (DM Authoring → CSDB
   Check-in → QA & Review → Despatch → IETP Build).
5. **Free S1000D Readiness Assessment** — dark navy mid-page CTA banner with
   named offer.
6. **Explore Related Industries** — 2-card cross-link (Automotive industry +
   XML Data Interoperability solution).

No civilian-agency content on the old page; civilian appears to live
elsewhere on ex-tense.co (out of scope for this port — the directive is
"faithful to this page" + "equal weight" via additive civilian sections).

## 3. Inventory — NEW site (current)
Built on a shared `IndustryPageLayout` template:

- Hero (joint civilian + defense)
- Document Types list (mixed civilian + defense)
- Standards list (mixed)
- Federal Program Lifecycle (two-track timeline: Defense Program · Civilian
  Agency) — closest existing structural parallel to what we'd want
- Failure-Mode callout (S1000D-focused)
- Signals block (4 buyer-symptom lines, mixed)
- **Capability Relevance** (4 cards) — **stale**: all four link to
  `/capabilities/*`, which were **retired** in the Solutions reframe. These
  links 404 once shipped to public domains.
- Case Studies (2)
- CTAModule (generic Sample Content Assessment, public-sector audience)

Reuse from the template: nothing structural; the bespoke rebuild replaces
the whole page. Atoms (`Hero`, `nav/SiblingsBreadcrumb`, `CTAModule`) carry
over from the broader site.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order preserved. All 6 old sections
  pulled forward. Add **civilian-parallel sections** to satisfy equal-weight
  directive — paired with the corresponding defense sections.
- **D-1 — H1 = "Government Agencies & Defense"** *(locked).* Owner-chosen.
  Carries the URL's promise (both registers) and signals civilian +
  defense equal weight from the H1 itself.
- **D-2 — Hero subdeck = [DRAFT] paired civilian/defense.** Old subdeck is
  defense-only and won't carry the H1. Proposed two-sentence parallel: old
  defense sentence verbatim + a parallel civilian sentence with matching
  weight. See S1.
- **D-3 — Paired-section structure:**
  - S3 (S1000D Implementation, defense) ↔ S4 (Agency Publishing & Section
    508, civilian) — both 3-card grids, mirroring layout.
  - S5 (Security & Compliance) — kept joint, [OLD] intro with micro-tweak
    to acknowledge civilian; 3 cards stay [OLD] verbatim (ITAR defense-
    specific; Air-Gapped / Audit & Traceability span both registers).
  - S6 (The S1000D Lifecycle, defense, 5-step) ↔ S7 (The Agency Publishing
    Lifecycle, civilian, 5-step) — both 01–05 numbered roadmap strips.
- **D-4 — Related Industries card 1 swap:** Old page → Automotive (the
  closest sibling vertical to defense aerospace). The current `/industries`
  matrix folds Automotive + Aviation + Rail into **Transportation**. Card 1
  swaps to Transportation with a body that names all three modes. Card 2
  (XML Data Interoperability) stays [OLD] verbatim.
- **D-5 — CTA name "Free S1000D Readiness Assessment" kept [OLD] solo.**
  Defense-named because S1000D is the most concrete named offer in the old
  page and named offers convert better than generic ones (per established
  service-detail pattern: DITA = "Sample Content Assessment", Publishing =
  "Sample Output Build", CCMS = "Free CCMS Health Check"). Civilian doesn't
  have a clean analog named offer in the old material. **Alternative for
  owner review:** pair with a [DRAFT] civilian offer (e.g., "Free Section
  508 Documentation Audit") — doubles CTA surface but preserves equal-
  weight thesis to the close.
- **D-6 — Hero side-visual = S1000D-themed document-grade SVG** (DM
  hierarchy → CSDB → IETP). Old page had no side visual; new-site
  convention has one. The visual leans defense because that's where the
  domain language has named primitives; civilian equal weight is carried
  by body sections, not the hero visual. Mock candidates after wireframe
  sign-off, same workflow as Publishing / CCMS / SI / XML.
- **D-7 — Banded-section rhythm:** S3 plain · S4 band · S5 plain · S6
  band · S7 plain · S8 band (Related). Paired sections alternate bg so
  they read as siblings, not duplicates.
- **D-8 — Retire `IndustryPageLayout` usage on this page.** Other 5
  `/industries/<slug>` pages stay on the template for now; ported case-by-
  case in future sessions. The stale `/capabilities/*` links in this
  page's data go away once the file is rewritten.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + S1000D side visual
- **H1** `[LOCKED]`: "Government Agencies & Defense"
- **Subdeck** `[DRAFT]` — paired construction, defense first verbatim, then
  civilian parallel:
  > "Mission-critical S1000D, MIL-STD, and ITAR-compliant technical
  > documentation — engineered for interoperability between OEMs, suppliers,
  > and the armed forces. Federal civilian agency content modernization —
  > Section 508-conformant, records-management compliant, and engineered to
  > agency publishing standards."

  Defense sentence is **[OLD]** verbatim. Civilian sentence is **[DRAFT]**
  written to mirror weight (~25 words each, parallel structure: domain +
  conformance markers).
- **Side visual:** S1000D-themed document-grade SVG (concept TBD post-
  sign-off). Likely candidates: DM hierarchy fan-out → CSDB → IETP build;
  or three-pillar (`<dmodule>` / `<csdb>` / `<ietp>`) convergence in the
  XML-engineering idiom.

### S2 — Siblings nav · `nav/SiblingsBreadcrumb`
- Back-link "← Industries" + dot-separated row of the other 5 industries
  with **Government & Defense** as current (amber + bold).

### S3 — S1000D Implementation (defense register) `[OLD]` · 3-card grid
- **Heading** `[OLD]`: "S1000D Implementation"
- **Intro** `[OLD]`: "S1000D is not just a schema — it is a complex
  business logic engine governing data module creation, applicability
  filtering, and cross-organizational data exchange. We implement every
  layer."
- **3 cards** `[OLD]` (bare amber line icons, hairline border, no shadow):
  1. **Data Modules (DMs)** *(icon: document)* — "Granular content chunks
     authored as XML data modules and managed in a Common Source Data Base
     (CSDB). We design DM coding schemes, implement SNS structures, and
     enforce naming conventions across multi-vendor programs."
  2. **Applicability & Filtering** *(icon: check-in-circle)* —
     "ACT/CCT/PCT configuration management — filtering content by tail
     number, block number, or variant. We implement applicability cross-
     reference tables that ensure technicians see only the procedures
     relevant to their specific aircraft configuration."
  3. **BREX Rules & Validation** *(icon: shield)* — "Business Rule
     Exchange implementation that enforces project-specific constraints —
     required metadata, allowed illustration formats, and mandatory cross-
     references. Our BREX validation runs in CI pipelines, catching
     violations before data despatch."

### S4 — Agency Publishing & Section 508 (civilian register) `[DRAFT]` · 3-card grid (banded)
Paired with S3. Same 3-card grid pattern, civilian register.
- **Heading** `[DRAFT]`: "Agency Publishing & Section 508"
- **Intro** `[DRAFT]` (mirrors S3 intro's "X is not just Y — it is Z"
  structure, ~50 words):
  > "Federal civilian agency content isn't just published — it's authored
  > to standards that govern accessibility, retention, and public
  > consumption. Section 508 conformance, agency-specific publishing
  > conventions, and records-management compliance are built into the
  > content architecture, not bolted on at review time."
- **3 cards** `[DRAFT]`:
  1. **Section 508 Conformance** *(icon: accessibility — universal access
     symbol or doc-with-wave)* — "Accessible content engineered at the
     source — semantic structure, alt-text discipline, screen-reader-
     conformant PDF generation, and authoring-tool integration. We
     implement accessibility constraints in the content model so violations
     are caught at authoring time, not at the OIG review."
  2. **Agency Publishing Standards** *(icon: stamp/seal)* — "Each federal
     agency has its own content and publishing conventions — IRS publication
     guides, FAA directive formats, GSA documentation standards. We adapt
     the authoring environment, the schema layer, and the publishing
     pipeline to the agency's actual conventions rather than a generic
     federal template."
  3. **Records Management & FOIA** *(icon: archive/folder)* — "Title 5 USC
     and Title 44 records-management compliance built into the content
     lifecycle — retention metadata at the data module level, FOIA-readiness
     for every published artifact, and audit trails that satisfy NARA and
     OIG retention reviews."

### S5 — Security & Compliance (joint) `[OLD + DRAFT micro-tweak]` · 3-card grid
- **Heading** `[OLD]`: "Security & Compliance"
- **Intro** `[DRAFT]` micro-tweak — adds "and federal civilian agencies"
  to the end of the [OLD] intro so the section reads joint, not defense-
  only:
  > "We build documentation workflows for classified, ITAR-controlled, and
  > CUI environments — with the access controls and audit trails that
  > defense programs **and federal civilian agencies** require."

  (Underline marks the inserted phrase; remove underline at ship.)
- **3 cards** `[OLD]` verbatim (apply to both registers as-is):
  1. **ITAR & Classified Handling** *(icon: lock)* — "Release sanitization
     workflows that redact controlled data for foreign national
     distribution. We implement marking automation, paragraph-level
     classification, and derivative classification guides integrated into
     the authoring environment."
  2. **Air-Gapped Publishing** *(icon: server-stack)* — "Isolated build
     environments with no network connectivity for SECRET and above
     content. We configure offline DITA-OT toolchains, local schema
     catalogs, and removable-media delivery workflows for SCIF
     environments."
  3. **Audit & Traceability** *(icon: document)* — "Complete audit logs
     for every view, edit, export, and distribution event. We build
     traceability matrices linking requirements → procedures → test
     results to satisfy DCMA and DCAA audit requirements."

### S6 — The S1000D Lifecycle (defense) `[OLD]` · 01–05 numbered roadmap strip (banded)
- **Heading** `[OLD]`: "The S1000D Lifecycle"
- **Optional eyebrow** `[DRAFT]`: "DEFENSE REGISTER" — mono caps, signals
  the pairing with S7.
- **5 steps** `[OLD]` (SI "How We Deliver" 01–05 pattern):
  1. **01 — DM Authoring** — "Create data modules in XML"
  2. **02 — CSDB Check-in** — "Validate against BREX & Schema"
  3. **03 — QA & Review** — "SME sign-off & release marking"
  4. **04 — Despatch** — "DMRL distribution to partners"
  5. **05 — IETP Build** — "Interactive Electronic Technical Pubs"

### S7 — The Agency Publishing Lifecycle (civilian) `[DRAFT]` · 01–05 numbered roadmap strip
Paired with S6. Same 01–05 idiom, civilian register.
- **Heading** `[DRAFT]`: "The Agency Publishing Lifecycle"
- **Optional eyebrow** `[DRAFT]`: "CIVILIAN REGISTER" — mirrors S6.
- **5 steps** `[DRAFT]` (parallel to S6's 5-step S1000D lifecycle):
  1. **01 — Authoring** — "Draft against agency publishing standards"
  2. **02 — Section 508 Review** — "Accessibility conformance"
  3. **03 — Approval & Sign-off** — "Internal & inter-agency review"
  4. **04 — Publication** — "Release via agency channel or Federal Register"
  5. **05 — Records Retention** — "NARA archival & FOIA-readiness"

### S8 — Explore Related Industries `[OLD-structure + DRAFT card 1 swap]` · 2-card cross-link (banded)
- **Heading** `[OLD]`: "Explore Related Industries"
- **Card 1** `[OLD-structure + DRAFT swap]` — eyebrow "INDUSTRY",
  title swapped from old's "Automotive" to **"Transportation"** (the
  current new-site sibling that subsumes Automotive + Aviation + Rail).
  Body `[DRAFT]` condensed from the /industries Transportation card:
  > "Service information operations across modes — automotive VIN-specific
  > guides, aviation ATA Spec 2200 maintenance manuals, and rail AAR
  > M-1003 procedures."

  Link target: `/industries/transportation`, CTA text "EXPLORE →".
- **Card 2** `[OLD]` — eyebrow "SOLUTION", title "XML Data
  Interoperability", body `[OLD]`:
  > "S1000D-to-DITA bridges, XSLT transformation pipelines, and API-driven
  > content delivery."

  Link target: `/solutions/xml-data-interoperability`, CTA "EXPLORE →".

### S9 — CTA · `CTAModule` (audience="public-sector")
- **Heading** `[OLD]`: "Free S1000D Readiness Assessment"
- **Body** `[OLD]`: "Share your current TDP structure and we'll evaluate
  S1000D migration feasibility, estimate CSDB architecture, and identify
  BREX rule requirements — at no cost."
- **CTA button:** "Request Your Free Assessment" (matching existing
  `CTAModule` button conventions).
- **Open question (D-5):** keep [OLD] solo as drafted above, OR pair with a
  [DRAFT] civilian named offer — candidate: "Free Section 508 Documentation
  Audit" with body roughly "Share a representative civilian-agency
  publication and we'll return a Section 508 conformance assessment,
  remediation effort estimate, and a records-management readiness review —
  at no cost." Side-by-side double-CTA preserves equal-weight thesis to the
  close; solo keeps the page tighter and matches the convert-best named-
  offer convention.

---

## 6. Decision log
- **D-1** *(locked)* — H1 = "Government Agencies & Defense".
- **D-2** *(locked)* — Pull all 6 old-page sections forward [OLD] verbatim
  where possible; add civilian-parallel sections [DRAFT] for equal weight.
- **D-3** *(locked)* — Paired-section structure: S3↔S4 (Implementation),
  S5 joint, S6↔S7 (Lifecycle), S8 cross-link, S9 CTA.
- **D-4** *(locked)* — Related Industries card 1 swap Automotive →
  Transportation (the current new-site sibling).
- **D-5** *(pending owner)* — CTA: solo [OLD] "Free S1000D Readiness
  Assessment" vs paired with [DRAFT] civilian "Free Section 508
  Documentation Audit".
- **D-6** *(pending owner)* — Hero side-visual concept (S1000D-themed
  SVG candidates to mock after wireframe sign-off).
- **D-7** *(proposed)* — Banded-section rhythm: S3 plain · S4 band · S5
  plain · S6 band · S7 plain · S8 band.
- **D-8** *(locked)* — Retire `IndustryPageLayout` usage on this page;
  bespoke build with page-local CSS (prefix `gd-`). Other 5 industry
  pages stay on template for now.

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)
Net-new copy that doesn't have an old-site source — all needs explicit
sign-off per the verbatim-default rule:

| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[DRAFT]` | Hero subdeck civilian sentence |
| S4  | `[DRAFT]` | "Agency Publishing & Section 508" heading |
| S4  | `[DRAFT]` | Section intro paragraph |
| S4  | `[DRAFT]` | 3 card titles + bodies (Section 508 Conformance · Agency Publishing Standards · Records Management & FOIA) |
| S5  | `[DRAFT]` | Intro micro-tweak (adds "and federal civilian agencies") |
| S6  | `[DRAFT]` | Optional eyebrow "DEFENSE REGISTER" |
| S7  | `[DRAFT]` | "The Agency Publishing Lifecycle" heading |
| S7  | `[DRAFT]` | Optional eyebrow "CIVILIAN REGISTER" |
| S7  | `[DRAFT]` | 5 step labels + captions (Authoring · Section 508 Review · Approval & Sign-off · Publication · Records Retention) |
| S8  | `[DRAFT]` | Card 1 swap (label + condensed body for Transportation) |
| S9  | `[DRAFT-conditional]` | Civilian "Free Section 508 Documentation Audit" CTA (only if D-5 lands on paired) |
