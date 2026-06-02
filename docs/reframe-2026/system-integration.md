# System Integration & API Connectors (service detail) — Reframe Plan

> Status: **implemented — pending staging sign-off.** Sixth of the 7 `/services/<slug>` detail
> sub-pages. Built **bespoke** (page-local CSS, prefix `si-`), reusing the
> shared atoms (`Hero`, `SectionSiblings`, `CTAModule`) and the patterns proven
> on DITA / Publishing / CCMS (icon-card grids, 3-card row, 01–0N strip,
> `#fef3c7` callout, related cards, hero node-graph visual). Faithful rebuild
> of the old `ex-tense.co/services/system-integration.html` (10 sections); the
> old mid-page "Free Integration Assessment" banner is folded into the end CTA
> per owner.
> **Locked this session:** H1 = "System Integration & API Connectors";
> **faithful — all 10 sections, no mid-page banner**; hero **visual D**
> (before / after — manual handoff eliminated); **How We Deliver** 3 cards
> use uniform amber accent + mono eyebrow.
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [ccms-services.md](ccms-services.md).

---

## 1. Page job
- **URL:** `/services/system-integration`
- **Primary reader:** a docs / content-ops lead, integration architect, or IT
  leader at a company where content lives in multiple systems (CCMS,
  engineering ticketing, CRM/support, PLM/ERP, TMS) and currently moves via
  manual handoffs.
- **The one job:** prove that we can eliminate the "swivel-chair" between
  content systems — design, build, secure, and operate the connectors — then
  convert.

> **Note (overlap, accepted — faithful):** Publishing Triggers, CI/CD, and
> TMS connector topics overlap `/services/ccms-services` and
> `/services/publishing-engineering`. Per owner: keep all, cross-link via the
> Related cards.

---

## 2. Inventory — OLD page (10 sections)
Hero → The Cost of Disconnected Systems (3 problem cards) → The Connected
Content Ecosystem (6 icon cards) → Integration Architecture (5-step strip
+ No Vendor Lock-In sub-block) → **[mid-page Free Integration Assessment
banner — DROPPED, folded into end CTA]** → Technology Stack (6 cards) →
Security & Compliance (3 cards) → Ongoing Support & Monitoring (3 cards) →
How We Deliver (5-step strip + 3 cards w/ colored top borders) → Related
Services (3 cards). No end-of-page CTA on the old page — added as closer for
parity.

## 3. Inventory — NEW site
Page doesn't exist (sibling switcher + `/services` card link here, 404 until
built). Reuse: `Hero` (with visual D), `SectionSiblings` (services),
`CTAModule` (closer). Page-local patterns from DITA / Publishing / CCMS:
hero node-graph SVG with scroll-reveal + reduced-motion fallback, icon-card
grids (bare amber line icons), 3-card row with amber top accent,
`#fef3c7` callout, mono eyebrow on the engagement-style cards, related-card.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order; **mid-page banner dropped**
  (owner decision); end-of-page `CTAModule` with the "Free Integration
  Assessment" name carried forward.
- **D-1 — H1 = "System Integration & API Connectors"** *(locked).*
- **D-2 — Hero visual = D** *(locked):* before / after — manual handoff
  eliminated. Two stacked rows separated by an amber `extense.connectors`
  rule. Top row (BEFORE / MANUAL, soft dashed): JIRA → swivel-chair → CCMS.
  Bottom row (AFTER / AUTOMATED): JIRA → direct amber arrow → custom-amber
  `<ccms>`. Full scroll-reveal (`.fx` + draw), reduced-motion fallback.
  `FIG. 01 / handoff.eliminated / MANUAL → AUTOMATED`. Most directly carries
  the page's headline value ("so content flows without manual handoffs").
- **6-card sections** (Connected Ecosystem, Technology Stack) = the
  DITA/Publishing/CCMS icon-card 4+2 grid, **both with bare amber line
  icons**.
- **3-card sections** (Cost of Disconnected Systems, Security & Compliance,
  Ongoing Support & Monitoring) = grid-3 with amber top accent.
- **5-step strips** (Integration Architecture, How We Deliver delivery
  phases) = two roadmap strips on the same page.
  - **D-3 — Differentiate the two strips:** Integration Architecture =
    **unnumbered** technical pipeline (Event Source · Middleware · CCMS API ·
    Validate · Notify — components, not phases); How We Deliver = **numbered
    `01–05`** chronological process (Discovery → Operate, matches DITA
    workflow / Publishing rendering pipeline). *(Proposed.)*
- **No Vendor Lock-In** sub-block under Integration Architecture = the
  centered `#fef3c7` sub-block pattern (DITA "Deduplication" precedent).
- **How We Deliver** 3 cards (Pre-Built Accelerators / Custom Connectors /
  Knowledge Transfer) = uniform amber top accent + **mono eyebrow** + body.
  - **D-4 — Eyebrow copy:** **`TEMPLATED` / `BESPOKE` / `HANDOFF`**
    (delivery-mode descriptors, mono uppercase pressed amber). *(Proposed.)*
- **D-5 — Banded-section rhythm:** S2 plain · S3 band · S4 plain · S6 band ·
  S7 plain · S8 band · S9 plain · S10 band. *(Locked.)*

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + visual D (animated)
- **H1** `[LOCKED]`: "System Integration & API Connectors"
- **Subdeck** `[OLD]`: "Connecting your CCMS to engineering, support, PLM,
  and translation systems — so content flows without manual handoffs."

### S2 — Sibling switcher · `SectionSiblings` (variant="services")
- current = **System Integration** (amber + bold).

### S3 — The Cost of Disconnected Systems · `[OLD]` (3 cards, amber top accent)
- *Problem-led section, kept per owner (AI-Ready precedent).*
- **Intro** `[OLD]`: "When your content systems don't talk to each other,
  your team pays the price every day."
- **3 cards** `[OLD]`:
  1. **Manual Handoffs** — "Writers check JIRA for updates, copy ticket
     details into the CCMS, email translators with file packages, and
     manually upload finished content to the portal. Every handoff is a
     delay — and a place where information gets lost or garbled."
  2. **Version Drift** — "Engineering ships v2.4 but the knowledge base still
     reflects v2.3. Support agents answer tickets with outdated procedures.
     Customers find contradictions between the help portal and the PDF they
     downloaded last month. Disconnected systems make version mismatch
     inevitable."
  3. **Compliance Exposure** — "In regulated industries, you must prove that
     the published document matches the approved source, that translations
     are current, and that every change is auditable. Manual processes leave
     gaps that auditors find — and that cost you."

### S4 — The Connected Content Ecosystem · `[OLD]` (6 icon cards, band)
- **Intro** `[OLD]`: "Documentation lives between Engineering and the end
  user. We build the middleware, webhooks, and API connectors that eliminate
  the 'swivel-chair' copy-paste between systems."
- **6 cards** `[OLD]` (each with a bare amber line icon):
  1. **JIRA / Azure DevOps → CCMS** *(icon: clipboard / ticket)* — "When an
     engineering story moves to 'Done,' our connector automatically creates a
     content task in the CCMS, pre-populates metadata (product, version,
     component), and assigns it to the mapped writer. Zero lag between
     code-complete and doc-start."
  2. **Git → DITA Sync** *(icon: branch)* — "Developer-authored Markdown or
     MDITA in Git repositories is bidirectionally synced with the official
     DITA CCMS. Our pipelines convert, validate, and merge — preserving
     authoring freedom without sacrificing structural governance."
  3. **Salesforce / Zendesk / ServiceNow** *(icon: bubble)* — "Push
     troubleshooting guides and knowledge articles directly to the support
     agent's console. When a ticket is filed for a known issue, the connector
     surfaces the exact DITA topic — significantly reducing average handle
     time."
  4. **Translation Management (TMS)** *(icon: globe)* — "XLIFF round-trip
     integration with Trados, memoQ, Memsource, and XTM. We export only
     changed segments, route to the right TMS workflow, and auto-import
     translated content back into the CCMS — fully validated."
  5. **PLM / ERP Systems** *(icon: gear)* — "Link DITA content to part
     numbers, BOMs, and engineering change orders in Windchill, Teamcenter,
     or SAP. When a part revision changes, the content link flags affected
     documentation for review automatically."
  6. **CI/CD Publishing Pipelines** *(icon: cycle)* — "GitHub Actions,
     Jenkins, and Azure DevOps pipelines that build, validate, and deploy
     documentation on every commit. We treat docs as code — with the same
     rigor as your software release process."

### S5 — Integration Architecture · `[OLD]` (5-step un-numbered strip + sub-block)
- **Intro** `[OLD]`: "Every connector follows our event-driven architecture
  pattern — loosely coupled, fault-tolerant, and auditable."
- **5 stages** `[OLD]` (technical pipeline, un-numbered; amber connectors):
  1. **Event Source** — "JIRA · Git · PLM · TMS"
  2. **Middleware** — "Webhook / REST · Mapping Logic"
  3. **CCMS API** — "Create · Update · Link Topics"
  4. **Validate** — "Schema Check · Business Rules"
  5. **Notify** — "Email · Slack · Dashboard"
- **Sub-block — No Vendor Lock-In** `[OLD]` (`#fef3c7` callout, centered):
  - **Heading**: "No Vendor Lock-In"
  - **Body**: "We build to open standards — REST APIs, XLIFF 2.1, CMIS, and
    OAuth 2.0. If you switch your CCMS, TMS, or issue tracker, the
    integration layer adapts — not your entire workflow."

### S6 — Technology Stack · `[OLD]` (6 icon cards, band)
- **Intro** `[OLD]`: "What we build with — open, maintainable, and chosen to
  fit your existing infrastructure."
- **6 cards** `[OLD]` (each with a bare amber line icon):
  1. **Node.js & Python** *(icon: code brackets)*
  2. **Java & .NET** *(icon: layers)*
  3. **Apache Kafka & MQ** *(icon: queue / chain)*
  4. **REST & GraphQL APIs** *(icon: graph)*
  5. **iPaaS & Low-Code** *(icon: puzzle / plug)*
  6. **Docker & Kubernetes** *(icon: cube)*
  *(Full `[OLD]` body copy carried verbatim at build.)*

### S7 — Security & Compliance · `[OLD]` (3 cards, amber top accent)
- **Intro** `[OLD]`: "Integrations move data between systems. We ensure every
  connection is secure, auditable, and compliant with your regulatory
  requirements."
- **3 cards** `[OLD]`: Authentication & Authorization · Data in Transit &
  at Rest · Audit Trails & Compliance. *(Full body copy carried verbatim.)*

### S8 — Ongoing Support & Monitoring · `[OLD]` (3 cards, amber top accent, band)
- **Intro** `[OLD]`: "Integrations aren't 'set and forget.' APIs change,
  tokens expire, schemas evolve. We keep your connectors healthy after
  deployment."
- **3 cards** `[OLD]`: Proactive Monitoring · API Change Management ·
  Incident Response.

### S9 — How We Deliver · `[OLD]` (5-step numbered strip + 3 eyebrow cards)
- **Intro** `[OLD]`: "Every integration engagement follows a structured
  process — from discovery to production, with your team involved at every
  stage."
- **5 phases** `[OLD]` (`01–05`, amber connectors):
  1. **Discovery** — "Map your toolchain, data flows, and automation goals."
  2. **Design** — "Architecture blueprint with API contracts and error
     handling."
  3. **Build** — "Iterative development with staging environment testing."
  4. **Deploy** — "Production rollout with rollback procedures."
  5. **Operate** — "Monitoring, maintenance, and continuous improvement."
- **3 cards below the strip** `[OLD]` (amber top accent + mono eyebrow):
  1. **`[TEMPLATED]` Pre-Built Accelerators** — "For common integrations
     (JIRA → CCMS, CCMS → TMS, Git → DITA), we start from proven connector
     templates — not a blank slate. This cuts implementation time
     significantly and reduces risk with battle-tested patterns."
  2. **`[BESPOKE]` Custom Connectors** — "For unique workflows (PLM → DITA,
     proprietary ERP, legacy systems), we design and build bespoke
     connectors. Every custom integration comes with API documentation,
     admin runbooks, and automated tests."
  3. **`[HANDOFF]` Knowledge Transfer** — "We document every connector,
     train your team to troubleshoot common issues, and provide the source
     code. You're never locked into our services — your team can maintain
     and extend the integrations independently."

### S10 — Related Services · `[OLD]` (3 cards, band)
- **CCMS Services** → `/services/ccms-services` — "Platform selection,
  configuration, and ongoing support for enterprise content management."
- **XML Engineering** → `/services/xml-engineering` — "Custom schema design,
  XSLT transformation, and validation pipelines." *(404 until built.)*
- **Publishing Engineering** → `/services/publishing-engineering` — "Custom
  multi-channel publishing pipelines for PDF, HTML5, EPUB, and API
  documentation."

### S11 — CTA (closing) · `CTAModule` (compact + accentLine)
- **Heading** `[OLD, carried from mid-page banner]`: "Free Integration
  Assessment"
- **Body** `[OLD, from mid-page banner]`: "Tell us your current toolchain —
  CCMS, issue tracker, TMS, PLM — and we'll map the integration architecture,
  identify automation opportunities, and estimate implementation effort. No
  strings attached."

### Removed
- Mid-page "Free Integration Assessment" dark banner (owner: single CTA at
  the bottom). The offer name carried forward as the CTA heading.
- Old text breadcrumb (→ sibling switcher), footer nav.

---

## 6. Decision log
- **D-1 — H1 "System Integration & API Connectors".** *(Locked.)*
- **D-2 — Hero visual D (before/after — manual handoff eliminated).**
  *(Locked.)*
- **D-3 — Two roadmap strips differentiated:** Integration Architecture =
  un-numbered components; How We Deliver = numbered `01–05` phases.
  *(Proposed.)*
- **D-4 — How We Deliver eyebrows** = `TEMPLATED` / `BESPOKE` / `HANDOFF`.
  *(Proposed.)*
- **D-5 — Faithful, mid-page banner dropped, end-CTA carries the "Free
  Integration Assessment" name.** *(Locked.)*
- **D-6 — Bespoke + shared atoms, `si-` prefix.** *(Locked.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| S1 Hero | `Hero` + visual D (animated) | New — `[OLD]` subdeck, before/after SVG |
| S2 Switcher | `SectionSiblings` (services) | Reuse — current="system-integration" |
| S3 Cost of Disconnected | section + 3 cards (accent line) | **New** |
| S4 Connected Ecosystem | section + 6 icon cards (band) | **New** |
| S5 Integration Architecture | section + 5-step un-numbered strip + `#fef3c7` sub-block | **New** |
| S6 Technology Stack | section + 6 icon cards (band) | **New** |
| S7 Security & Compliance | section + 3 cards (accent line) | **New** |
| S8 Ongoing Support & Monitoring | section + 3 cards (accent line, band) | **New** |
| S9 How We Deliver | section + 5-step numbered strip + 3 eyebrow cards | **New** |
| S10 Related | section + 3 related cards (band) | **New** |
| S11 CTA | `CTAModule` | Reuse — `compact` + `accentLine`, `[OLD]` body |
| Page | `services/system-integration.astro` | **New file** |

**Cross-cutting:**
- Clears 1 more dead `/services/<slug>` link; 1 still 404 after
  (xml-engineering).
- Delete the temp mock `system-integration-mock.astro` at build time.
- Spacing-token trap: only `--space-{1,2,3,4,5,6,8,12,16,20,24,32}` exist.
- Verify on the local preview at 1280×900 / 375×812.

---

## 8. Open items for review
1. **Hero subdeck** — confirm `[OLD verbatim]` (no edit needed).
2. **CTA** — confirm `[OLD verbatim]` carried from the dropped mid-page
   banner ("Free Integration Assessment" + body + "No strings attached.").
3. **D-3 Two roadmap strips** — confirm Integration Architecture = un-numbered
   (technical components), How We Deliver = numbered `01–05` (phases). Alt =
   number both for visual consistency.
4. **D-4 How We Deliver eyebrows** — confirm `TEMPLATED` / `BESPOKE` /
   `HANDOFF`, or pick an alt:
   - `FAST START` / `CUSTOM BUILD` / `OWNED BY YOU`
   - `01 ACCELERATE` / `02 BUILD` / `03 HANDOFF` (numbered)
   - `FOR COMMON FLOWS` / `FOR UNIQUE FLOWS` / `FOR YOUR TEAM`
