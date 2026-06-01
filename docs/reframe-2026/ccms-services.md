# CCMS Managed Services (service detail) — Reframe Plan

> Status: **implemented — pending staging sign-off.** Fifth of the 7 `/services/<slug>` detail
> sub-pages. Built **bespoke** (page-local CSS, prefix `ccms-`), reusing the
> shared atoms (`Hero`, `SectionSiblings`, `CTAModule`) and the patterns proven
> on DITA / Publishing (icon-card grids, 3-card row, `#fef3c7` callout, related
> cards, hero node-graph visual). Faithful rebuild of the old
> `ex-tense.co/services/ccms-services.html` (10 sections, mid-page banner
> folded into the end CTA per owner).
> **Locked this session:** H1 = "CCMS Managed Services & Administration"; **faithful —
> all 10 sections, no mid-page banner**; hero **visual E** (continuous-operations
> timeline); **Engagement Models** = uniform amber top + mono tier eyebrow.
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [publishing-engineering.md](publishing-engineering.md).

---

## 1. Page job
- **URL:** `/services/ccms-services`
- **Primary reader:** a docs-platform owner / CCMS admin lead / content-ops
  manager evaluating whether to outsource ongoing CCMS administration to a
  specialist team rather than load it onto generic IT or in-house admins.
- **The one job:** prove deep operational expertise across the major CCMS
  platforms, **as an ongoing service** (not a one-shot engineering build) —
  then convert.

> **Note (overlap, accepted — faithful):** Publishing Triggers (S6) overlaps
> `/services/publishing-engineering`; JIRA/Git/CI-CD integration (S7) overlaps
> the System Integration page; Platform Migration (S4) overlaps
> `/solutions/content-migration`. Per owner: keep all, cross-link via the
> Related cards.

---

## 2. Inventory — OLD page (10 sections)
Hero ("CCMS Managed Services") → Expert Administration (3 cards) → Operational
Services (6 cards) → **[mid-page Free CCMS Health Check banner — DROPPED, folded
into end CTA]** → Platforms We Support (6 cards) → Workflow & Configuration
Services (3 cards) → Upgrades & Integration Management (3 cards) → Engagement
Models (3 cards w/ colored top borders + checklists) → Knowledge Transfer &
Enablement (3 cards) → Related Services (2 cards). No end-of-page CTA on the
old page — added as closer for parity.

## 3. Inventory — NEW site
Page doesn't exist (sibling switcher + `/services` card link here, 404 until
built). Reuse: `Hero` (with visual E), `SectionSiblings` (services), `CTAModule`
(closer). Page-local patterns from DITA/Publishing: hero node-graph SVG with
scroll-reveal + reduced-motion fallback, icon-card grid (bare amber line icons),
3-card row with amber top accent, mono eyebrow on Engagement Models cards,
checklist (✓), related-card.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order; **mid-page Free CCMS Health
  Check banner dropped** (owner decision); end-of-page `CTAModule` added with
  the "Free CCMS Health Check" name carried forward (keeps the recognisable
  offer hook).
- **D-1 — H1 = "CCMS Managed Services & Administration"** *(locked).* Names
  the service + keeps the solution-led "managed" framing.
- **D-2 — Hero visual = E** *(locked):* continuous-operations timeline. Five
  cadenced events (monitor / patch / audit / DR drill / upgrade) plotted on a
  horizontal time axis (DAILY → ANNUAL) with a chevron at the right end
  indicating continuation, and an amber `extense.ops · continuous` chip. Full
  scroll-reveal (`.fx` + draw), reduced-motion fallback. `FIG. 01 / ops.timeline
  / CONTINUOUS`. Most directly captures the *ongoing* nature of managed
  services and is visually distinct from every other detail-page hero (all of
  which are snapshot/topology diagrams).
- **6-card sections** (Operational Services, Platforms We Support) = the
  DITA/Publishing icon-card 4+2 grid. Operational Services = **with bare amber
  line icons**; Platforms We Support = **text-only** (the platform names
  themselves carry recognition).
- **3-card sections** (Expert Administration, Workflow & Configuration,
  Upgrades & Integration Management, Knowledge Transfer & Handoff) = the
  DITA 3-card row with amber top accent.
- **Engagement Models** = grid-3, uniform amber top accent, **mono tier eyebrow**
  above each title, plus ✓ checklist inside each card. *(D-5; see eyebrow
  copy below.)*
- **D-3 — Section rename: "Knowledge Transfer & Enablement" → "Knowledge
  Transfer & Handoff".** *(Voice rule: the noun "enablement" derives from the
  banned verb "enable." The section is literally about gradual handoff —
  runbooks / admin training / gradual handoff — so the rename is more accurate
  too.)*
- **D-4 — Related Services: 3 cards** (old page had 2). Adding **DITA
  Engineering** as the 3rd, since CCMS work naturally cross-links to DITA
  (DITA's own related cards already list CCMS Services). Final 3: DITA
  Engineering · System Integration · Publishing Engineering.
- **D-5 — Engagement Models tier eyebrow** = **`FOR 20+ WRITERS` / `FOR 5–20
  WRITERS` / `ONE-TIME · ANNUAL`** (team-size descriptors, mono uppercase
  pressed amber). Reads more informatively than "TIER 1/2/3" (these aren't
  tiers — they're different engagement models for different team shapes).
- **D-6 — Banded-section rhythm:** alternate `.section-band` tint as on
  DITA/Publishing. Plan: S3 plain · S4 band · S5 plain · S6 band · S7 plain · S8
  band · S9 plain · Related band.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + visual E (animated)
- **H1** `[LOCKED]`: "CCMS Managed Services & Administration"
- **Subdeck** `[OLD]`: "DBA-level administration, ongoing optimization, and
  Tier 2/3 support for your Component Content Management System — so your
  writers focus on writing."
  - *(Alt `[DRAFT]` if you want the timeline visual reinforced: "DBA-level
    administration, ongoing optimization, and Tier 2/3 support for your
    Component Content Management System. We run the platform on a continuous
    cadence — so your writers stay focused on writing.")*

### S2 — Sibling switcher · `SectionSiblings` (variant="services")
- current = **CCMS Services** (amber + bold).

### S3 — Expert Administration · `[OLD]` (3 icon cards, amber top accent)
- **Intro** `[OLD]`: "A CCMS is a database application with XML-aware
  workflows, access controls, and publishing integrations. It requires
  dedicated operational expertise — not just an IT generalist."
- **3 cards** `[OLD]`:
  1. **User Support (Tier 2/3)** *(icon: lifering)* — "When a writer says 'I
     can't check in this file,' it's usually a locked resource, a validation
     error, or a merge conflict. We are the helpdesk that speaks DITA —
     resolving content-specific issues that generic IT support cannot
     diagnose."
  2. **Performance Tuning** *(icon: gauge)* — "Optimizing XML database
     indexing, search configurations, and query performance for large
     repositories (1M+ objects). We profile slow operations, restructure
     indexes, and implement caching strategies that keep response times under
     2 seconds."
  3. **Schema & DTD Updates** *(icon: layers)* — "Deploying new DTDs,
     specializations, and constraint modules without breaking legacy content.
     We test schema changes against the full repository, produce migration
     scripts, and validate backward compatibility before going live."

### S4 — Operational Services · `[OLD]` (6 icon cards, band)
- **Intro** `[OLD]`: "Ongoing administration tasks that keep your CCMS healthy
  and your content team productive."
- **6 cards** `[OLD]` (each with a bare amber line icon):
  1. **User Onboarding** *(icon: user-plus)* — workspace setup, role-based
     permissions, authoring environment.
  2. **Platform Migration** *(icon: swap)* — CCMS A→B (IXIASOFT→Heretto,
     Vasont→Paligo), data export, schema mapping, link integrity.
  3. **Repository Cleanup** *(icon: broom/trash)* — orphans, broken conrefs,
     stale branches, ROT report with remediation scripts.
  4. **Access Control & Auditing** *(icon: shield)* — role-based access,
     branch policies, audit trail for regulated environments.
  5. **Backup & Disaster Recovery** *(icon: database)* — scheduled backups,
     restore testing, DR runbooks; RTO/RPO at production-DB parity.
  6. **Health Monitoring** *(icon: heartbeat)* — system health, storage,
     indexing, queue backlogs; alert and remediate before writers notice.
  *(Full `[OLD]` body copy carried verbatim at build.)*

### S5 — Platforms We Support · `[OLD]` (6 text cards)
- **Intro** `[OLD]`: "We provide managed services across the major CCMS
  platforms — not just one vendor. If your team uses it, we administer it."
- **6 cards** `[OLD]` (text-only, no icons): IXIASOFT CCMS · Tridion Docs
  (SDL) · Heretto (easyDITA) · Paligo · Vasont / Astoria · Git-Based & Open
  Source. *(Full body copy carried verbatim.)*

### S6 — Workflow & Configuration Services · `[OLD]` (3 cards, amber top accent, band)
- **Intro** `[OLD]`: "A CCMS is only as effective as its workflows. We design
  and implement the operational logic that governs how content moves from
  draft to published."
- **3 cards** `[OLD]`: Review & Approval Workflows · Branching & Release
  Management · Publishing Triggers & Automation. *(Full body copy carried
  verbatim.)*

### S7 — Upgrades & Integration Management · `[OLD]` (3 cards, amber top accent)
- **Intro** `[OLD]`: "Keeping your CCMS current and connected to the tools
  your teams depend on."
- **3 cards** `[OLD]`: Platform Version Upgrades · TMS & Localization
  Connectors · JIRA, Git & CI/CD Integration.

### S8 — Engagement Models · `[OLD]` (3 cards w/ amber top + mono eyebrow + ✓ list, band)
- **Intro** `[OLD]`: "Flexible service models that fit your team size, budget,
  and operational maturity."
- **3 cards** `[OLD]`:
  1. **`[FOR 20+ WRITERS]` Dedicated Admin** — "A named Extense CCMS
     administrator embedded in your team — full-time or part-time. They
     attend your standups, know your content architecture, and respond
     within your SLA. Ideal for large teams (20+ writers) with complex
     configurations."
     - ✓ Named resource, consistent context
     - ✓ 2-hour response SLA (business hours)
     - ✓ Monthly reporting & roadmap reviews
  2. **`[FOR 5–20 WRITERS]` Shared Pool** — "Access to our CCMS engineering
     team on a monthly retainer with a block of hours. Tickets are triaged by
     priority and handled by the specialist with the right platform
     expertise. Ideal for mid-size teams (5–20 writers) with periodic needs."
     - ✓ Platform-certified specialists
     - ✓ 4-hour response SLA (business hours)
     - ✓ Rollover unused hours (up to 20%)
  3. **`[ONE-TIME · ANNUAL]` Project-Based** — "Fixed-scope engagements for
     upgrades, migrations, workflow redesigns, or performance overhauls.
     Defined deliverables, timeline, and budget. Ideal for one-time
     initiatives or annual maintenance windows."
     - ✓ Fixed price, defined scope
     - ✓ Knowledge transfer included
     - ✓ Post-project support period

### S9 — Knowledge Transfer & Handoff · `[OLD]` (3 cards, amber top accent)
- *Section heading renamed from "Knowledge Transfer & **Enablement**" — voice
  rule (D-3).*
- **Intro** `[OLD]`: "We don't create dependencies. Every engagement includes
  documentation and training so your internal team grows more capable, not
  more reliant on us."
- **3 cards** `[OLD]`: Admin Runbooks · CCMS Admin Training · Gradual Handoff.

### S10 — Related Services · 3 cards (band)
- **DITA Engineering** → `/services/dita-engineering` — "Topic modeling,
  specialization, and constraint modules for scalable content architectures."
- **System Integration** → `/services/system-integration` — `[OLD]`
  "Connecting CCMS, CMS, and enterprise platforms via APIs and middleware."
  *(404 until built.)*
- **Publishing Engineering** → `/services/publishing-engineering` — `[OLD]`
  "Custom multi-channel publishing pipelines for PDF, HTML5, EPUB, and API
  documentation."

### S11 — CTA (closing) · `CTAModule` (compact + accentLine)
- **Heading** `[DRAFT]`: "Free CCMS Health Check"
- **Body** `[DRAFT]`: "We'll audit your CCMS configuration — permissions
  model, indexing strategy, workflow bottlenecks, and orphan content ratio.
  You'll receive a prioritized remediation plan and the ops cadence we'd
  recommend. No commitment required."

### Removed
- Mid-page "Free CCMS Health Check" dark banner (owner: single CTA at the
  bottom). The offer name carried forward as the CTA heading.
- Old text breadcrumb (→ sibling switcher), footer nav.

---

## 6. Decision log
- **D-1 — H1 "CCMS Managed Services & Administration".** *(Locked.)*
- **D-2 — Hero visual E (continuous-operations timeline).** *(Locked.)*
- **D-3 — Section rename: "Enablement" → "Handoff".** *(Proposed.)*
- **D-4 — Related Services: add DITA Engineering as 3rd card** (final list:
  DITA · System Integration · Publishing). *(Proposed.)*
- **D-5 — Engagement Models eyebrows = team-size descriptors** ("FOR 20+
  WRITERS" / "FOR 5–20 WRITERS" / "ONE-TIME · ANNUAL"). *(Proposed.)*
- **D-6 — Faithful, mid-page banner dropped, end-CTA carries the "Free CCMS
  Health Check" name.** *(Locked.)*
- **D-7 — Bespoke + shared atoms, `ccms-` prefix.** *(Locked.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| S1 Hero | `Hero` + visual E (animated) | New — `[OLD]` subdeck, timeline SVG |
| S2 Switcher | `SectionSiblings` (services) | Reuse — current="ccms-services" |
| S3 Expert Admin | section + 3 icon cards (accent line) | **New** |
| S4 Operational Services | section + 6 icon cards (band) | **New** |
| S5 Platforms | section + 6 text cards | **New** |
| S6 Workflow & Config | section + 3 cards (accent, band) | **New** |
| S7 Upgrades & Integration | section + 3 cards (accent) | **New** |
| S8 Engagement Models | section + 3 cards (eyebrow + checklist, band) | **New** |
| S9 Knowledge Transfer & Handoff | section + 3 cards (accent) | **New** |
| S10 Related | section + 3 related cards (band) | **New** |
| S11 CTA | `CTAModule` | Reuse — `compact` + `accentLine`, `[DRAFT]` body |
| Page | `services/ccms-services.astro` | **New file** |

**Cross-cutting:**
- Clears 1 more dead `/services/<slug>` link; 2 still 404 after
  (system-integration, xml-engineering).
- Delete the temp mock `ccms-services-mock.astro` at build time.
- Spacing-token trap: only `--space-{1,2,3,4,5,6,8,12,16,20,24,32}` exist.
- Verify on the local preview at 1280×900 / 375×812.

---

## 8. Open items for review
1. **Hero subdeck** — confirm `[OLD verbatim]` (or use the alt `[DRAFT]`
   that adds the "continuous cadence" line to reinforce visual E).
2. **CTA `[DRAFT]`** (S11) heading + body — approve / edit.
3. **D-3 Section rename** "Enablement" → "Handoff" — confirm.
4. **D-4 Related Services** — add DITA Engineering as 3rd? Confirm or keep
   the old page's 2 cards (System Integration + Publishing only).
5. **D-5 Engagement Models eyebrows** — confirm "FOR 20+ WRITERS / FOR 5–20
   WRITERS / ONE-TIME · ANNUAL", or pick an alternative
   (e.g. literal "TIER 1 / 2 / 3", or "01 EMBEDDED / 02 RETAINER / 03 PROJECT").
