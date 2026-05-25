# Services (main page) — Reframe Plan

> Status: **implemented + shipped to staging** (`main`). Hero benefit-led
> `[DRAFT]` approved; CCMS card titled "CCMS Services"; 7-card colorized
> line icons; engagement cards (definition + instrument + "best when") +
> lifecycle thesis + timeline. 3 engagement sub-pages + `ServicePageLayout`
> deleted; TopNav Services dropdown repointed to the 7 services. The 7
> service detail sub-pages are the next task. Tags: `[OLD]`
> (ex-tense.co/services/index.html) / `[NEW]` (current extense.co, live) /
> `[DRAFT]` (net-new, needs approval). Conventions in [README.md](README.md).
>
> **The mismatch:** the current new `/services` page is built *backwards*
> from the old site. The old main Services page leads with **7 service
> offerings** ("Expert Services Across the Content Lifecycle") and keeps
> **Engagement Models** as a tiny 3-blurb tail; the 7 services were the
> *sub-pages*. The new site inverted this — it made the **3 engagement
> models** the entire page (a bespoke "Three ways to engage" build) plus 3
> deep sub-pages, and **never built the 7 services** at all.
>
> **This task** flips it back to the old-site shape: rebuild `/services` to
> **Hero → Expert Services (7 cards) → Engagement Models (compact) → CTA**,
> delete the 3 engagement-model sub-pages, and (in a *later* task) build the
> 7 service detail sub-pages modeled on the old site's.

---

## 1. Page job
- **URL:** `/services`
- **Primary reader:** a buyer scoping *who does the work* — a
  documentation/content-ops lead or procurement owner deciding what to
  outsource and how to contract for it.
- **The one job:** show the **breadth of services** (the 7 offerings across
  the content lifecycle), each routing to a detail page, then explain **how
  to engage** (the 3 commercial models), then convert.

---

## 2. Inventory — OLD site (ex-tense.co/services/index.html)
1. **Hero** — "Our Services" / "From authoring to automation, we provide the
   expertise to optimize your content operations."
2. **Expert Services Across the Content Lifecycle** — intro + **7 service
   cards** (icon + name + description + DETAILS link), laid out 4 + 3:
   Technical Writing & Content Development · Structured Content Strategy ·
   DITA Engineering · Publishing Engineering · CCMS Managed Services ·
   System Integration · XML & Schematron Engineering.
3. **Engagement Models** — 3 one-line blurbs: Project-Based · Staff
   Augmentation · Managed Services.
4. **Logo band** ("Trusted by engineering leaders worldwide") — *(prohibited
   off the homepage.)*
5. **Newsletter** — *(prohibited.)* · Footer.

## 3. Inventory — NEW site (current, live)
**`/services/index.astro`** — bespoke "Three ways to engage" page, entirely
engagement-model-focused: thesis pull-quote → **3 SOW/Order-Form/SLA
document-fragment cards** → **lifecycle narrative + animated timeline** →
**"when you'd pick each" signals (3×3)** → CTA. *No Expert Services section.*

**3 sub-pages** (`project-based`, `staff-augmentation`, `managed-services`)
— each a deep `ServicePageLayout` page: narrative (4 ¶) · a paginated
SOW/Order-Form/SLA "document book" (5 pages, incl. fee ranges) · 5 phases ·
in/out-of-scope table · 4 signals · 3 anti-patterns · 2 vignettes ·
related · CTA.

**Disposition:** the 7 services don't exist on the new site → **build new**
(from `[OLD]`). The engagement-model material is over-built → **distill** a
compact section onto the main page. **Delete** the 3 sub-pages + the orphaned
`ServicePageLayout`. Retire the fragment cards, the signals, and the
lifecycle narrative; **keep the timeline visual.**

---

## 4. Mapping decisions
- **Lead with the 7 services** (`[OLD]` "Expert Services"), 4+3 card grid,
  each card → its future `/services/<slug>` detail page (links live now, will
  404 until the sub-pages are built next — your call, D-6).
- **Engagement Models = compact section** (richer than the old 3 one-liners,
  per your call): a one-line **lifecycle thesis** + the **timeline visual** +
  **3 cards** (name · one-line definition · contract instrument · "best when"
  cue). Distilled `[DRAFT]` from the current `[NEW]` sub-page content.
- **Keep** Hero (old "Our Services" copy) + add `CTAModule` as closer
  (+ `accentLine`).
- **Cut** the logo band (no client logos off the homepage), the newsletter,
  and the bespoke fragments / signals / lifecycle-narrative.
- **Delete** `project-based.astro`, `staff-augmentation.astro`,
  `managed-services.astro`, and `ServicePageLayout.astro` (orphaned after).
- **Voice:** the 7 `[OLD]` descriptions are clean (no banned verbs;
  "transformations" in XML & Schematron is the technical term, allowed).

---

## 5. Wireframe
Order mirrors the old-site body: **orient → services (breadth) → engagement
(how to buy) → convert.**

### Section 1 — Hero · `[OLD]`
- **H1** `[OLD]`: "Our Services"
- **Subdeck** `[OLD]`: "From authoring to automation, we provide the
  expertise to optimize your content operations."
- *Open item: keep `[OLD]` (clean) or a benefit-led `[DRAFT]` rewrite like
  the solution heroes? Default: keep `[OLD]`.*

### Section 2 — Expert Services Across the Content Lifecycle · NEW build · `[OLD]`
- **Heading** `[OLD]`: "Expert Services Across the Content Lifecycle"
- **Intro** `[OLD]`: "From the first word written to the last pixel
  published, our team of information architects, XML engineers, and
  publishing specialists provide hands-on expertise at every stage."
- **7 cards** (4 + 3 grid; card vocabulary = hairline card, amber accent,
  hover lift, "Details →"), `[OLD]` copy verbatim, each linking to its detail
  page:
  1. **Technical Writing & Content Development** → `/services/technical-writing-content-development` — "Professional authoring using Simplified Technical English (ASD-STE100), topic-based methodology, and minimalist principles. We write API references, user guides, install guides, release notes, and UX copy."
  2. **Structured Content Strategy** → `/services/structured-content-strategy` — "Information Architecture (IA), taxonomy design, reuse models (conref, conkeyref, warehouse topics), and content governance frameworks that reduce redundancy by 40–60%."
  3. **DITA Engineering** → `/services/dita-engineering` — "Specialization, constraints, SubjectScheme maps, and custom DITA-OT plugin development. We build the information model that fits your product, not the other way around."
  4. **Publishing Engineering** → `/services/publishing-engineering` — "Custom DITA-OT PDF plugins (XSL-FO), responsive HTML5 themes, EPUB generation, and batch publishing automation via Jenkins, GitHub Actions, or Azure DevOps pipelines."
  5. **CCMS Managed Services** → `/services/ccms-services` — "Post-implementation administration, Tier 2/3 helpdesk, schema updates, performance tuning for XML databases with 1M+ objects, onboarding, and orphan topic cleanup." *(Open item D-5: title "CCMS Managed Services" (old) vs "CCMS Services" (matches slug; avoids collision with the Managed Services engagement model below).)*
  6. **System Integration** → `/services/system-integration` — "Connecting your CCMS to JIRA, Git, Salesforce, Zendesk, PLM, and PIM systems. We build REST API middleware, webhooks, and event-driven connectors."
  7. **XML & Schematron Engineering** → `/services/xml-engineering` — "XSLT 2.0/3.0 transformations, Schematron business-rule validation, DTD/XSD specialization, and custom checkstyle rules for naming conventions and metadata enforcement."
- *Icon treatment: TBD at build — either small colorized line icons (like
  the AI-Ready problem cards) or an amber mono index (01–07). Default: line
  icons, to echo the old page.*

### Section 3 — Engagement Models · NEW build (reuses timeline) · `[DRAFT, from NEW]`
- **Heading** `[OLD]`: "Engagement Models"
- **Thesis intro** `[NEW]`: "The right engagement model isn't a property of
  the client — it's a property of where the work is in its own lifecycle."
- **Timeline visual** `[NEW]`: reuse the existing `.svc-timeline` (Project-Based
  → Staff Augmentation → Managed Services across Month 0 → 24+, with the
  "ongoing" arrow). Markup/CSS/JS lifted from the current `/services` page.
- **3 cards** `[DRAFT, distilled from NEW sub-pages]` — name · definition ·
  instrument · "best when":
  - **Project-Based** — *Instrument: Statement of Work.* "Fixed scope, fixed
    fee, defined endpoint. The default for IA refactors, migration programs,
    and CCMS implementations." **Best when** you have a clear deliverable and
    procurement wants a fixed price.
  - **Staff Augmentation** — *Instrument: Order Form (under your MSA).*
    "Embedded senior specialists working to your plan, on your timelines —
    time-and-materials, 3–12 month engagements." **Best when** you have the
    strategy and need execution capacity, or hiring is frozen but contracting
    isn't.
  - **Managed Services** — *Instrument: Service Level Agreement.* "Your CCMS
    and publishing pipelines operated for you — administration, governance,
    Tier 2/3 support. SLA-bounded and recurring." **Best when** the
    architecture is stable and the work has shifted from building to
    operating.
- *All card copy is `[DRAFT]` distilled from the current `[NEW]` content —
  needs your sign-off before ship.*

### Section 4 — CTA (closing) · `CTAModule` (+ `accentLine`) · `[NEW]`
- Compact "Sample Content Assessment" + animated amber line. CTA-as-closer,
  parity with the solution pages.

### Removed
- Logo band, newsletter, the bespoke document-fragment cards, the
  "when you'd pick each" signals, the standalone lifecycle narrative.

---

## 6. Decision log
- **D-1 — Flip to old-site shape:** lead with the 7 services; demote
  engagement models to a compact section. *(Agreed.)*
- **D-2 — Engagement Models richer than old site:** thesis intro + timeline
  visual + 3 cards (definition + instrument + "best when"). *(Q1/Q2 — chosen;
  card copy `[DRAFT]` pending sign-off.)*
- **D-3 — Keep the timeline; retire fragments + signals + lifecycle prose.**
  *(Q2 — chosen.)*
- **D-4 — Delete the 3 engagement-model sub-pages + `ServicePageLayout`.**
  *(Agreed.)*
- **D-5 — CCMS service card title** — "CCMS Managed Services" (old) vs "CCMS
  Services" (slug match, avoids collision with the Managed Services *model*).
  *(Open — proposing "CCMS Services".)*
- **D-6 — 7 cards link to future `/services/<slug>` URLs now** (will 404
  until the sub-pages are built next). *(Q — chosen.)*
- **D-7 — CTA-as-closer + `accentLine`** (parity). *(Following.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| 1 Hero | `Hero` (universal) | Rebuild copy → "Our Services" |
| 2 Expert Services | inline section / `ServicesExpert` (new) | **New build** — 7 `[OLD]` cards (4+3), link to `/services/<slug>` |
| 3 Engagement Models | inline section (reuses `.svc-timeline`) | **New build** — thesis + timeline + 3 distilled cards |
| 4 CTA | `CTAModule` | Keep + `accentLine` |
| Page | `services/index.astro` | **Rebuild** — drop fragments/signals/narrative |
| — | `services/project-based.astro`, `staff-augmentation.astro`, `managed-services.astro` | **Delete** |
| — | `layouts/ServicePageLayout.astro` | **Delete** (orphaned) |

**Cross-cutting (verify at build):**
- **TopNav** — if the Services dropdown links to `/services/project-based`
  etc., update it (point to `/services`, or list the 7 services). Don't leave
  dead nav links.
- **SiblingsBreadcrumb `variant="services"`** — currently the 3 engagement
  models are its siblings; update or retire for the new IA.
- **Orphan check before deleting shared components** — `ServicePageLayout`
  imports `CompactList`, `DocumentRow`, `LifecycleNav`, `SiblingsBreadcrumb`.
  Confirm whether other pages use them; delete only what's truly orphaned.
- Solution-page "Related" Service cards already point at `/services`
  (index) — unaffected.

---

## 8. Open items for review
1. **Engagement-model card copy** (§5 Section 3) — approve/edit the `[DRAFT]`
   definitions + "best when" cues.
2. **Hero** — keep `[OLD]` "Our Services" or a benefit-led rewrite?
3. **CCMS service card title** (D-5) — "CCMS Services" vs "CCMS Managed
   Services"?
4. **7-card icons** — colorized line icons (old-site echo) vs amber mono
   index (01–07)?
5. Confirm the **deletes** (3 sub-pages + `ServicePageLayout`) and the
   **TopNav / breadcrumb** updates.
