# Technology & Semiconductors (industry sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** Last of the 6 `/industries/<slug>`
> sub-pages. **Unique among industries: no OLD page exists** — the
> ex-tense.co site didn't carry a Technology vertical, so this page is
> built fresh from the new-site source content and from the cross-industry
> thesis (Extense as content-engineering firm for technology /
> semiconductor companies across hardware, software, and security
> compliance documentation). Bespoke build (page-local CSS, prefix
> `tech-`), reusing the shared atoms (`Hero`, `SectionSiblings`,
> `CTAModule`) and patterns proven on G&D / FS / LS / Transportation /
> Insurance. Replaces the current `IndustryPageLayout`-based page; the
> layout's stale `/capabilities/*` links go away with it.
>
> **Locked this session (2026-06-03):** H1 = [DRAFT] "Technology &
> Semiconductors"; **the entire page is [DRAFT]** (no OLD verbatim source);
> three-product-surface organizing thesis: hardware/silicon ·
> software/API · security/compliance.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [insurance.md](insurance.md).

---

## 1. Page job
- **URL:** `/industries/technology` (unchanged; H1 features the
  "Semiconductors" peer per owner decision — same model as G&D where the
  H1 calls out both registers but the URL stays simple).
- **Primary reader:** documentation / developer-experience / security-
  compliance lead at a semiconductor company, hardware vendor (consumer
  electronics, networking gear, IoT), SaaS platform provider, or
  defense-tech vendor — someone whose datasheets, API references, or
  SOC 2 control narratives have to ship on the same cadence as their
  silicon respins, code releases, or annual audit cycles.
- **The one job:** prove that three distinct documentation surfaces
  (hardware/silicon, software/API, security/compliance) live in one
  content-engineering practice — and that the CI/CD-driven publishing
  cadence keeps each surface aligned with its underlying release cycle.
  Then convert.

---

## 2. Inventory — OLD page
**None.** The old ex-tense.co site did not carry a Technology vertical.
This page is wholly [DRAFT] (excluding atoms and shared CSS idioms
inherited from the other industry pages). Every section needs sign-off.

## 3. Inventory — NEW site (current)
Built on shared `IndustryPageLayout`, with substantial original content
that the bespoke rebuild draws from:

- Hero (3-product-surface subdeck — the page's organizing thesis line)
- Document Types (6 types across the three surfaces)
- Standards (8: IEEE · IPC · JEDEC · SOC 2 · ISO 27001 · NIST · ITAR/EAR · FCC)
- **`productSurfacePanels`** — bespoke render of three sample documentation
  artifacts (CMOS-1234A SRAM datasheet · Payments API reference · SOC 2
  CC6.1 Logical Access Controls narrative), each showing the
  typographic register of its surface. The most distinctive piece of
  source material; informed the hero-visual brainstorm.
- Failure-Mode callout ("When the documentation is wrong, the product
  is functionally wrong — for that audience")
- Signals (4 buyer-symptom lines, one per surface + one cross-segment)
- **Capability Relevance** (4 cards) — **stale** `/capabilities/*` links.
- Case Studies (2: semiconductor portfolio + SaaS+SOC 2 modernization)
- CTAModule (generic)

The new-site page's most load-bearing content asset is the three-product-
surface framing in the subdeck and the `productSurfacePanels`. The
bespoke rebuild keeps that organizing thesis as the page's spine.

---

## 4. Mapping decisions
- **Fresh build** — no faithful-port discipline applies. Every section
  is [DRAFT].
- **D-1 — H1 = [DRAFT] "Technology & Semiconductors"** *(locked, owner
  decision).* Same dual-name pattern as G&D; signals depth in chip-vendor
  documentation specifically while keeping the broader Technology scope.
  URL stays `/industries/technology`.
- **D-2 — Hero subdeck = [DRAFT]** compressed version of the new-site
  subdeck — captures the three-surface thesis in ~25 words rather than
  ~50. See S1 for proposed copy.
- **D-3 — S3 organizing thesis: three product surfaces.** The most
  load-bearing structural decision. Three cards in a grid, one per
  surface: Hardware & Silicon Documentation · Software & API
  Documentation · Security & Compliance Documentation. Each names its
  audience, the relevant standards, and the typographic register.
- **D-4 — S4 = Continuous Publishing Cadence** — 01-05 numbered roadmap
  strip with body paragraphs (LS/Insurance precedent), banded. Argues
  the CI/CD-driven publishing thesis that ties all three surfaces under
  one cadence (silicon respin · semantic-version release · audit cycle).
- **D-5 — Drop the `productSurfacePanels` document-fragment rendering.**
  The new-site page renders three full document artifacts side-by-side
  showing typographic registers. Beautiful but heavy — the bespoke page
  keeps the three-surface thesis in the S3 cards and the hero side-visual,
  not in a full-section document-fragment block. Recoverable later if
  needed.
- **D-6 — S5 "Explore Related" = 3-card cross-link** [DRAFT] (Industry:
  G&D for defense-tech / ITAR overlap · Solution: AI-Ready Content ·
  Service: DITA Engineering). Heading "Explore Related" per established
  precedent.
- **D-7 — CTA name = [DRAFT]** "Free Technical Content Assessment" —
  matches the established Free [Domain] Content Assessment pattern
  (G&D=S1000D Readiness, FS=Compliance, LS=Regulatory, Transportation=
  Automotive, Insurance=Policy). Audience = `general`.
- **D-8 — Hero side-visual = three-product-surface themed SVG**
  (concepts to mock after wireframe sign-off). Candidates:
  - **(a)** Three product surfaces in parallel — 3 small artifact cards
    side-by-side (DATASHEET · API REFERENCE · SOC 2 NARRATIVE), each
    showing 2-3 lines of sample fields in its own typographic register.
    Literal rendering of the page thesis.
  - **(b)** One discipline → three outputs fan — central
    `<source>` chip with radial outputs to the three surface chips.
  - **(c)** Three sources converging into one practice — 3 source chips
    at top (hardware/software/security) → central `extense.tech-docs`
    chip below. Inverse of (b).
- **D-9 — Banded-section rhythm:** S3 plain · S4 band · S5 band. Same as
  Transportation/Insurance.
- **D-10 — Retire `IndustryPageLayout` usage on this page.** With this
  port, **all 6 industry sub-pages are bespoke**; the layout becomes
  unused after the merge and is a candidate for deletion (separate
  cleanup commit). Same disposition as the `IndustryPageLayout`-driven
  stale `/capabilities/*` link debt — gone with the last user.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + three-surface side visual
- **H1** `[DRAFT-locked]`: "Technology & Semiconductors"
- **Subdeck** `[DRAFT]`:
  > "Datasheets for system integrators, API docs for developers, security
  > attestations for buyer security teams — three product surfaces, three
  > audiences, one engineering discipline."
- `subdeckMaxWidth="520px"`.
- **Side visual:** TBD post-sign-off; mock candidates per D-8.

### S2 — Siblings nav · `SectionSiblings` (variant="industries")
- current = **Technology** (amber + bold).

### S3 — Three Product Surfaces `[DRAFT]` · 3-card grid
- **Heading** `[DRAFT]`: "Three Product Surfaces"
- **Intro** `[DRAFT]`:
  > "Technology and semiconductor companies ship three distinct
  > documentation surfaces — one for system integrators reading datasheets,
  > one for developers reading API reference, one for buyer security teams
  > reading SOC 2 narratives. Each carries its own typographic register,
  > structural conventions, and audit-trail obligations. Engineering
  > documentation discipline is what makes the three live in the same
  > content system without losing their distinct shapes."
- **3 cards** `[DRAFT]`:
  1. **Hardware & Silicon Documentation** *(icon: chip)* — "Datasheets,
     application notes, and reference designs for semiconductor vendors —
     JEDEC-conformant, EDA-toolchain-integrated, version-aligned with
     silicon respins. PCB design files, IPC-conformant assembly docs,
     and FCC certification packages for consumer electronics, networking
     equipment, and IoT devices."
  2. **Software & API Documentation** *(icon: code-brackets — reuse
     Transportation code icon)* — "Developer-facing reference docs,
     integration guides, and code samples. Auto-generated from OpenAPI
     specs where possible; hand-authored where developer experience
     requires editorial care. Versioned release notes and changelogs
     tied to semantic-version tags; aggregated views for buyers tracking
     platform adoption."
  3. **Security & Compliance Documentation** *(icon: shield — reuse
     G&D/LS/Insurance shield)* — "SOC 2 reports, ISO 27001 statement of
     applicability and control narratives, penetration test reports,
     NIST 800-series mappings. The documentation buyer security teams
     review before signing — and the audit-trail evidence the next year's
     auditor walks through. ITAR/EAR handling where defense-tech and
     dual-use export controls apply."

### S4 — Continuous Publishing Cadence `[DRAFT]` · 01-05 strip (banded)
- **Heading** `[DRAFT]`: "Continuous Publishing Cadence"
- **Intro** `[DRAFT]` (operational-arc construction matching G&D /
  Transportation / Insurance):
  > "The operational arc from source to released documentation — five
  > gated stages tying the publishing cadence to each surface's release
  > cycle (silicon respin, semantic-version release, audit cycle)."
- **5 steps** `[DRAFT]` (with bodies, LS/Insurance precedent):
  1. **01 — Source-of-Truth Authoring**
     - desc: "Author against the single content source"
     - body: "Hardware specs, API references, and control narratives
       written into a structured CCMS with metadata that survives the
       publishing pipeline. EDA toolchain integration syncs silicon
       revisions; source-control hooks keep API specs aligned with code."
  2. **02 — Validation Pass**
     - desc: "Validate against schemas and business rules"
     - body: "Schema validation catches structural drift; business-rule
       validation catches semantic violations (datasheet-vs-silicon
       drift, API-vs-implementation drift, control-narrative-vs-evidence
       drift). Failures return to the author before publishing runs."
  3. **03 — Auto-Generation**
     - desc: "Generate machine-readable docs from source"
     - body: "Where source is structured (OpenAPI specs, EDA output,
       IdP provisioning logs), the publishing pipeline auto-generates
       the relevant documentation surfaces. Hand-authored content layers
       on top where editorial care is required."
  4. **04 — Pre-Release Build**
     - desc: "Build outputs for every target surface"
     - body: "PDF datasheets for distribution. Web-ready API reference
       for developer portal. SOC 2 control narrative for the auditor.
       Output formats generated in parallel from one source, each in
       its target typographic register."
  5. **05 — Release-Tied Publication**
     - desc: "Publish on the release cadence"
     - body: "Hardware: tied to silicon respin or product launch.
       Software: tied to semantic-version release. Security: tied to
       annual audit cycle plus continuous evidence collection. The
       publishing cadence matches the release cadence — no doc lag."

### S5 — Explore Related `[DRAFT]` · 3-card cross-link (banded)
- **Heading** `[DRAFT-precedent]`: "Explore Related"
- **Card 1** `[DRAFT]` — eyebrow "INDUSTRY", title "Government & Defense",
  body:
  > "S1000D data modules, IETM delivery, and MIL-STD compliance for
  > defense-tech vendors — where ITAR-controlled silicon and dual-use
  > export documentation overlap with technology product programs."

  Link target: `/industries/government-and-defense`, CTA "EXPLORE →".
- **Card 2** `[DRAFT]` — eyebrow "SOLUTION", title "AI-Ready Content",
  body:
  > "Retrieval over technical documentation estates — datasheets, API
  > references, security policies — engineered so developer-facing AI
  > assistants cite the right page, the right version, the right product
  > line."

  Link target: `/solutions/ai-ready-content`, CTA "EXPLORE →".
- **Card 3** `[DRAFT]` — eyebrow "SERVICE", title "DITA Engineering",
  body:
  > "The engineering discipline that makes hardware, software, and
  > security documentation live in one content system — specialization,
  > profiling, and publishing automation across distinct typographic
  > registers."

  Link target: `/services/dita-engineering`, CTA "EXPLORE →".

### S6 — CTA · `CTAModule` (audience="general")
- **Heading** `[DRAFT]`: "Free Technical Content Assessment"
- **Body** `[DRAFT]`:
  > "Share a 20-page sample — datasheet, API reference, or security
  > attestation. We'll return a content-readiness assessment focused on
  > the publishing-cadence and retrieval-readiness questions specific
  > to technology and semiconductor documentation. No commitment
  > required."

---

## 6. Decision log
- **D-1** *(locked)* — H1 = [DRAFT] "Technology & Semiconductors".
- **D-2** *(locked)* — Hero subdeck = [DRAFT] compressed three-surface
  thesis.
- **D-3** *(locked)* — S3 = Three Product Surfaces, 3-card grid
  (Hardware & Silicon · Software & API · Security & Compliance).
- **D-4** *(locked)* — S4 = Continuous Publishing Cadence, 01–05 strip
  with body paragraphs, banded.
- **D-5** *(locked)* — Drop `productSurfacePanels` document-fragment
  rendering from the bespoke build.
- **D-6** *(locked)* — S5 = 3-card cross-link [DRAFT] (G&D + AI-Ready
  Content + DITA Engineering); heading "Explore Related".
- **D-7** *(locked)* — CTA name = [DRAFT] "Free Technical Content
  Assessment"; audience = `general`.
- **D-8** *(pending owner pick)* — Hero side-visual: candidates A
  (three surfaces in parallel), B (source → 3 outputs fan), C
  (3 sources → 1 practice). Mock 2–3 on a temp route after wireframe
  sign-off.
- **D-9** *(locked)* — Banded rhythm: S3 plain · S4 band · S5 band.
- **D-10** *(locked)* — Retire `IndustryPageLayout` on this page;
  bespoke build with page-local CSS prefix `tech-`. Layout becomes
  unused after this port (candidate for deletion in a follow-up
  cleanup commit).

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)
**Entire page is [DRAFT]** — no OLD verbatim source. Every line below
needs explicit sign-off.

| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[DRAFT-locked]` | H1 (D-1) |
| S1  | `[DRAFT]` | Subdeck (compressed three-surface thesis) |
| S3  | `[DRAFT]` | Heading "Three Product Surfaces" |
| S3  | `[DRAFT]` | Intro paragraph (~70 words) |
| S3  | `[DRAFT]` | Card 1 — Hardware & Silicon Documentation title + body |
| S3  | `[DRAFT]` | Card 2 — Software & API Documentation title + body |
| S3  | `[DRAFT]` | Card 3 — Security & Compliance Documentation title + body |
| S4  | `[DRAFT]` | Heading "Continuous Publishing Cadence" |
| S4  | `[DRAFT]` | Intro (operational-arc line) |
| S4  | `[DRAFT]` | 5 step titles + 5 desc lines + 5 body paragraphs |
| S5  | `[DRAFT-precedent]` | Heading "Explore Related" |
| S5  | `[DRAFT]` | 3 related cards (Industry / Solution / Service bodies) |
| S6  | `[DRAFT]` | CTA heading "Free Technical Content Assessment" |
| S6  | `[DRAFT]` | CTA body |
