# Transportation (industry sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** Fourth of the 6 `/industries/<slug>`
> sub-pages ported as a faithful reframe. Bespoke build (page-local CSS,
> prefix `tr-`), reusing the shared atoms (`Hero`, `SectionSiblings`,
> `CTAModule`) and patterns proven on G&D / FS / LS (3-card grids with bare
> amber line icons, `#fef3c7` amber-tinted callout, 01–05 numbered roadmap
> strip, hero document-grade SVG visual, `section-band` rhythm). Replaces
> the current `IndustryPageLayout`-based page; the layout's stale
> `/capabilities/*` links go away with it.
>
> **The page was renamed Automotive → Transportation post-old-site.** The
> OLD page is automotive-only; the URL is now Transportation. Reconciliation
> choice (locked, Option (a)): pull the 6 OLD automotive sections forward
> verbatim; add ONE [DRAFT] cross-mode acknowledgment near the end naming
> aviation / rail / maritime under bounded-scope engagements. Minimum [DRAFT]
> departure while honoring the Transportation rename.
>
> **Locked this session (2026-06-03):** H1 = [DRAFT] "Automotive &
> Transportation Information Systems"; faithful — all 6 old-page sections
> kept [OLD] verbatim; one [DRAFT] cross-mode callout in S5; CTA stays [OLD]
> "Free Automotive Content Assessment".
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [life-sciences.md](life-sciences.md).

---

## 1. Page job
- **URL:** `/industries/transportation` (renamed from `/industries/automotive`).
- **Primary reader:** service-information / technical-publications /
  aftersales-ops lead at an automotive OEM, Tier-1 supplier, MRO, or
  transportation operator — someone whose maintenance procedures,
  service bulletins, owner's literature, or VIN-driven publications have
  to land accurately across dealer networks, in-vehicle channels, and
  regulatory audits.
- **The one job:** prove that automotive service-information engineering
  (single-source DITA, VIN-driven assembly, multi-channel delivery, AR-
  ready topics, safety-recall pipelines) is the firm's core capability —
  and that the same discipline extends to aviation / rail / maritime
  under bounded-scope engagements. Then convert.

---

## 2. Inventory — OLD page (ex-tense.co/industries/automotive)
Six sections, automotive-only:

1. **Hero** — dark navy banner. H1 "Automotive Information Systems" +
   subdeck.
2. **The Software-Defined Vehicle** — intro + **3-card grid**: Service
   Information (SI) · VIN-Specific Owner's Literature · Augmented Reality
   (AR) Delivery.
3. **Multi-Channel Automotive Publishing** — intro + **3-card grid**:
   Safety Recall Management · API-Driven Content Delivery · Multi-Language
   & Market Variants.
4. **VIN-Specific Publishing Workflow** — heading only + **5-step
   horizontal strip**: Build Data → Map Resolution → Topic Selection →
   Assembly → Publish.
5. **Free Automotive Content Assessment** — dark navy mid-page CTA banner.
6. **Explore Related Industries** — **2-card cross-link**: Government &
   Defense (industry) · Technical Documentation & Publishing (solution).

All body copy reads clean under the locked voice — no banned verbs needing
substitution.

## 3. Inventory — NEW site (current)
Built on shared `IndustryPageLayout`, **expanded post-rename to cover all
four transportation modes**:

- Hero (4-mode subdeck)
- Document Types (6, across modes)
- Standards (8, across modes including ATA Spec 2200 · AAR M-1003 · IMO
  MSC · USCG NVIC)
- **CrossModeComparison** (4-column matrix: Automotive · Aviation · Rail ·
  Maritime, 5 row categories)
- Failure-Mode callout (multi-mode)
- Signals (4 buyer-symptom lines, one per mode)
- **Capability Relevance** (4 cards) — **stale** `/capabilities/*` links.
- Case Studies (2)
- CTAModule (generic, `general` audience)

Reuse from the template: nothing structural; the bespoke rebuild replaces
the page. The new-site multi-mode scope is preserved at light weight via
the [DRAFT] cross-mode callout in S5 + the [DRAFT] subdeck augmentation.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order preserved. Six OLD
  automotive sections pulled forward. One [DRAFT] cross-mode acknowledgment
  added per owner-chosen scope (a).
- **D-1 — H1 = [DRAFT] "Automotive & Transportation Information
  Systems"** *(locked).* Carries the OLD page name forward and signals the
  Transportation rename in one phrase. Minimum [DRAFT] departure.
- **D-2 — Hero subdeck = [DRAFT-augmented]** — [OLD] automotive sentence
  verbatim + [DRAFT] cross-mode clause appended. Mirrors the G&D hero
  pattern (defense [OLD] + civilian [DRAFT]). Resolves the H1/subdeck
  scope mismatch with one short addition rather than a rewrite. See S1.
- **D-3 — Cross-mode callout in S5** *(locked, Option (a))*. Rendered as
  `#fef3c7` amber-tinted callout (same idiom as LS S4 "Regulatory Agility
  in Practice"), sitting below the VIN-Specific Publishing Workflow strip.
  Mono CROSS-MODE PATTERNS eyebrow + heading + paragraph body acknowledging
  aviation / rail / maritime under bounded-scope engagements.
- **D-4 — S6 "Explore Related" = 2 cards** [OLD] verbatim
  (Government & Defense + Technical Documentation & Publishing). NOT
  expanded to 3 cards like FS/LS — old page has 2, both fit cleanly, no
  visual-sparseness issue. Heading [DRAFT] "Explore Related" (drops
  "Industries" per the established G&D/FS/LS precedent — section carries
  Industry + Solution).
  - Card 2 target updates to `/solutions/technical-docs-and-publishing`
    (the new-site URL for the old "Technical Documentation & Publishing"
    content).
- **D-5 — CTA name = [OLD] "Free Automotive Content Assessment"** with
  [OLD] body verbatim. Despite the Transportation rename, the offer name
  is automotive-specific in the OLD copy and the body explicitly invites
  service-manual / owner's-guide samples — keeping verbatim preserves the
  conversion mechanism. Audience = `general`.
- **D-6 — Hero side-visual = transportation-themed document-grade SVG**
  (concepts to mock after wireframe sign-off, same workflow as G&D / FS /
  LS). Most promising directions:
  - **(a)** Multi-channel automotive publishing fan — central
    `<vehicle>` source chip with radial outputs to 5 delivery channels
    (Dealer DMS, In-Vehicle Infotainment, Mobile Service App, AR Overlay,
    Print PDF). Renders the page's S4 thesis directly.
  - **(b)** VIN-filtered content delivery — `<vin>` config (with build
    options) → DITA profiler → assembled topic stream → published output.
    Renders the page's S5 workflow thesis.
  - **(c)** Cross-mode pattern — one structured-content discipline (central
    chip) → 4 mode chips (auto · aviation · rail · maritime). Renders the
    [DRAFT] cross-mode acknowledgment thesis. Risks making the page feel
    cross-mode rather than automotive-led; flagged but probably not picked.
- **D-7 — Banded-section rhythm:** S3 plain · S4 band · S5 plain · S6
  band. Same alternating cadence as FS/LS.
- **D-8 — Retire `IndustryPageLayout` usage on this page.** Pattern set
  by G&D / FS / LS. Other 2 industry pages (insurance, technology) stay
  on the template for now.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + transportation-themed side visual
- **H1** `[DRAFT-locked]`: "Automotive & Transportation Information
  Systems"
- **Subdeck** `[DRAFT-augmented]`:
  > "Service information, diagnostics, and in-vehicle content delivery
  > for OEMs and Tier-1 suppliers — where documentation accuracy directly
  > affects repair quality and recall compliance. Plus aviation, rail,
  > and maritime service documentation under bounded-scope engagements
  > where the same engineering discipline applies."

  First sentence is **[OLD]** verbatim. Second sentence is **[DRAFT]** —
  mirrors the cross-mode callout in S5 in compressed form.
- `subdeckMaxWidth="520px"` (matches /industries hero treatment).
- **Side visual:** TBD post-sign-off; mock candidates per D-6.

### S2 — Siblings nav · `SectionSiblings` (variant="industries")
- current = **Transportation** (amber + bold).

### S3 — The Software-Defined Vehicle `[OLD]` · 3-card grid
- **Heading** `[OLD]`: "The Software-Defined Vehicle"
- **Intro** `[OLD]`: "Modern vehicles are software platforms. The Owner's
  Manual is no longer a printed booklet — it is an in-car app, a voice
  assistant response, an AR overlay for technicians, and a responsive web
  portal, all generated from the same structured source."
- **3 cards** `[OLD]` (bare amber line icons, hairline border):
  1. **Service Information (SI)** *(icon: monitor — reuse FS monitor)* —
     "We link Diagnostic Trouble Codes (DTCs) to specific repair
     procedures at the metadata level. A technician scans the OBD-II
     port, the diagnostic tool reads the fault code, and the system
     retrieves the exact DITA topic — complete with torque specs, wiring
     diagrams, and part numbers — for that specific fault on that
     specific model year."
  2. **VIN-Specific Owner's Literature** *(icon: doc — reuse G&D/FS doc)*
     — "Each vehicle's build configuration (VIN data) determines its
     documentation. If the build sheet includes 'Panoramic Sunroof,' the
     owner's manual includes the sunroof chapter. If not, it is excluded.
     This produces tailored, accurate documentation for every individual
     vehicle — not a generic manual padded with irrelevant content."
  3. **Augmented Reality (AR) Delivery** *(icon: play-circle — new icon,
     simple circle with play triangle)* — "Semantic tagging of repair
     procedures enables AR overlays. Structured metadata (bolt location,
     torque sequence, component ID) allows AR glasses or tablet cameras
     to project step-by-step instructions onto the physical engine bay,
     guiding the technician's hands to the exact component."

### S4 — Multi-Channel Automotive Publishing `[OLD]` · 3-card grid (banded)
- **Heading** `[OLD]`: "Multi-Channel Automotive Publishing"
- **Intro** `[OLD]`: "Automotive content must reach dealers, technicians,
  owners, and regulatory bodies through different channels — from dealer
  management systems to in-vehicle infotainment screens."
- **3 cards** `[OLD]`:
  1. **Safety Recall Management** *(icon: shield — reuse G&D/LS shield)*
     — "When a safety recall is issued, the affected repair procedure
     must be published to every dealer within hours — not weeks. Our
     publishing pipeline pushes recall-specific content to dealer
     portals, generates NHTSA-compliant notification letters, and
     updates the in-vehicle system simultaneously."
  2. **API-Driven Content Delivery** *(icon: code-brackets — new icon,
     `<>`)* — "Headless content APIs serve structured topics to dealer
     diagnostic tools, mobile service apps, and in-vehicle infotainment
     systems. Content is delivered as JSON-LD with semantic metadata —
     not as rendered pages — enabling each client application to present
     information in its native format."
  3. **Multi-Language & Market Variants** *(icon: globe — reuse FS/LS
     globe)* — "A single vehicle platform may be sold in 40+ markets
     with different regulatory requirements, measurement systems, and
     languages. DITA profiling manages market-specific variations (EU
     safety standards vs. US FMVSS), while component-level translation
     ensures consistency across all 40 localized publications."

### S5 — VIN-Specific Publishing Workflow `[OLD]` · 01-05 strip + cross-mode callout
- **Heading** `[OLD]`: "VIN-Specific Publishing Workflow"
- **5 steps** `[OLD]` (01–05 numbered roadmap strip, same idiom as G&D
  S6/S7):
  1. **01 — Build Data** — "Receive VIN configuration as XML from
     manufacturing"
  2. **02 — Map Resolution** — "Match VIN options to DITA map filter
     conditions"
  3. **03 — Topic Selection** — "Resolve applicable topics and exclude
     non-matching content"
  4. **04 — Assembly** — "Merge selected topics with shared boilerplate
     and legal text"
  5. **05 — Publish** — "Generate in-car HTML5, print PDF, and dealer
     portal output"
- **Should the strip's steps carry contextual body paragraphs?** (Per
  the LS precedent where the lifecycle steps got 1-2 sentence bodies for
  context.) The OLD page shows just title + 1-line desc per step; this
  matches the as-shipped feel. **Default: no body lines** to keep faithful;
  if she wants them, that's a [DRAFT] addition we'd sign off separately.
  Flag for owner.
- **Cross-Mode Patterns callout** `[DRAFT]` (amber `#fef3c7`, amber-pressed
  border-left, sits below the workflow strip, full-width container-prose
  like the LS callout):
  - **Eyebrow** `[DRAFT]`: "CROSS-MODE PATTERNS"
  - **Heading** `[DRAFT]`: "Beyond automotive."
  - **Body** `[DRAFT]`:
    > "The VIN-driven workflow above is automotive-specific, but the
    > engineering discipline carries across modes. We serve commercial
    > aviation (ATA Spec 2200, S1000D), rail (AAR M-1003, FRA Title 49
    > CFR), and maritime (IMO MSC, USCG NVIC) under bounded-scope
    > engagements when the program's documentation surface fits our
    > core capabilities."

### S6 — Explore Related `[OLD]` · 2-card cross-link (banded)
- **Heading** `[DRAFT]` (drops "Industries" per established precedent):
  "Explore Related"
- **Card 1** `[OLD]` — eyebrow "INDUSTRY", title "Government & Defense",
  body:
  > "S1000D data modules, IETM delivery, and MIL-STD compliance for
  > defense vehicle platforms."

  Link target: `/industries/government-and-defense`, CTA "EXPLORE →".
- **Card 2** `[OLD]` — eyebrow "SOLUTION", title "Technical Documentation
  & Publishing", body:
  > "Multi-channel publishing pipelines for HTML5, PDF, API, AR, and
  > in-vehicle delivery."

  Link target: `/solutions/technical-docs-and-publishing` (URL updated to
  the new-site path), CTA "EXPLORE →".

### S7 — CTA · `CTAModule` (audience="general")
- **Heading** `[OLD]`: "Free Automotive Content Assessment"
- **Body** `[OLD]`: "Share a sample service manual chapter or owner's
  guide section. We'll analyze VIN-filtering potential, identify reuse
  opportunities across model lines, and map the path from static PDFs to
  a structured, multi-channel content architecture. No commitment
  required."
- CTA button label: matches existing CTAModule convention ("Request Your
  Free Assessment").

---

## 6. Decision log
- **D-1** *(locked)* — H1 = [DRAFT] "Automotive & Transportation
  Information Systems".
- **D-2** *(locked)* — Hero subdeck = [DRAFT-augmented]: [OLD] verbatim
  + [DRAFT] cross-mode clause.
- **D-3** *(locked, Option (a))* — S5 carries a [DRAFT] cross-mode
  acknowledgment callout below the workflow strip.
- **D-4** *(locked)* — S6 = 2-card cross-link [OLD] verbatim (Industry +
  Solution); heading "Explore Related" [DRAFT-precedent].
- **D-5** *(locked)* — CTA name + body = [OLD] verbatim; audience =
  `general`.
- **D-6** *(pending owner)* — Hero side-visual concept: candidates A
  (multi-channel automotive publishing fan), B (VIN-filtered content
  delivery), C (cross-mode pattern). Mock 2–3 on a temp route after
  wireframe sign-off.
- **D-7** *(locked)* — Banded rhythm: S3 plain · S4 band · S5 plain ·
  S6 band.
- **D-8** *(locked)* — Retire `IndustryPageLayout` usage on this page;
  bespoke build with page-local CSS prefix `tr-`.
- **D-9** *(pending owner)* — S5 workflow steps: add 1-2 sentence
  [DRAFT] body lines per step (LS precedent), or keep terse title + desc
  only (faithful to OLD). My default: keep terse (faithful).

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)
| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[DRAFT-locked]` | H1 "Automotive & Transportation Information Systems" |
| S1  | `[DRAFT]` | Subdeck cross-mode clause (second sentence) |
| S5  | `[DRAFT]` | Cross-Mode Patterns callout — eyebrow + heading + body |
| S6  | `[DRAFT-precedent]` | Heading "Explore Related" (drops Industries) |

All other body copy + cards are `[OLD]` verbatim.
