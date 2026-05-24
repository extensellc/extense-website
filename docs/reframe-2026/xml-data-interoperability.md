# XML Data Interoperability (sub-page) — Reframe Plan

> Status: **implemented** on `redesign-2026` — build clean, preview-verified
> (desktop + mobile). Spec table uses the full `[OLD]` descriptions; hero
> rewritten benefit-led. Tags: `[OLD]` (ex-tense.co) / `[NEW]` (current
> extense.co, live) / `[DRAFT]` (net-new, needs approval). Conventions in
> [README.md](README.md).
>
> **Direction (locked this session):** same recipe as the other three — rebuild
> the body to the **old-site sections** in the new design; cut the
> problem-education section; keep Hero/Siblings/CTA as chrome; amber treatment;
> CTA-as-closer. The 10 Transformation Technologies render as a **two-column
> spec table** (name | one-line description), not cards. The new-invented
> "When the schema is the contract" closing is **cut**.
>
> Old-page copy is authoritative (typical Extense work, same ruling as CM) —
> reused `[OLD]` verbatim, with banned-verb swaps.

---

## 1. Page job
- **URL:** `/solutions/xml-data-interoperability`
- **Primary reader:** an architect/integration lead whose systems (CCMS, PIM,
  ERP, CMS, LMS, legacy) disagree on the same fact, who needs one canonical
  source feeding every consumer and standard.
- **The one job:** show the **standards we bridge**, the **toolset**, and the
  **5-stage interoperability architecture**, then route + convert.

## 2. Inventory — OLD site (ex-tense.co/solutions/xml-data-interoperability.html)
1. **Hero** — "XML Data Interoperability" / "Transform siloed data into…" *("Transform" banned)*
2. **Enterprise Integration Standards** — intro + 6 cards (S1000D & Defense · IIoT & Industry 4.0 · Healthcare & Life Sciences · Semantic Web & Knowledge Graphs · Financial & Regulatory XBRL · API Documentation & Code Sync)
3. **Transformation Technologies** — intro + 10 tools (XSLT 3.0 · XQuery & XPath 3.1 · Schema Validation · JSON⟷XML Bridge · Event-Driven Pipelines · XML Databases · GraphQL Content APIs · Custom Java & C# · CSS-to-PDF · Python & Node.js)
4. **The Interoperability Layer** — 5-stage strip (Ingest → Normalize → Validate → Enrich → Deliver) + **AI-Ready Interoperability** callout
5. Free Assessment CTA
6. **Explore Related Solutions** — Content Migration · Tech Docs & Publishing · XML Engineering (Service)
7. Newsletter · Footer

## 3. Inventory — NEW site (current, live, pre-reframe)
Hero ("One fact. Every system." + fabric SVG) → Siblings → **Problem** ("Why
systems disagree on the facts" — *problem-ed*) → Pipeline → Patterns (5 editorial
blocks) → **Closing** ("When the schema is the contract" — new-invented) → generic
`/services` link → CTA.

**Disposition:** keep Hero + Siblings + CTA. Cut Problem + Closing. Replace
Patterns → Standards (6 cards) + Technologies (spec table). Replace Pipeline →
The Interoperability Layer (old 5-stage + AI-Ready callout). Add Related 3-up.
Delete the four orphaned `XmlDataInterop*` components (Problem/Pipeline/Patterns/Closing).

---

## 4. Mapping decisions
- **Keep `[NEW]`:** `XmlDataInteropHero` (fabric SVG; old "Transform…" hero has a
  banned verb), `SolutionsSiblings`, `CTAModule` (+`accentLine`).
- **Rebuild to OLD sections `[OLD]`:** Enterprise Integration Standards (6 cards),
  Transformation Technologies (spec table, 10 rows), The Interoperability Layer
  (5-stage + AI-Ready callout), Explore Related Solutions (3-up).
- **Cut:** `XmlDataInteropProblem` (problem-ed), `XmlDataInteropPipeline`,
  `XmlDataInteropPatterns`, `XmlDataInteropClosing` (new-invented). Delete.
- **Voice swaps (D-3):** S1000D card "…**enabling** commercial and military
  documentation to share…" → "…**so** commercial and military documentation
  share…"; Semantic Web card "**enabling** knowledge graphs…" → "**for**
  knowledge graphs…". (Old hero "Transform…" not used — new hero kept.)

---

## 5. Wireframe
Order mirrors the old-site body: **orient → standards → toolset → architecture →
cross-sell → convert.**

### Section 1 — Hero · `XmlDataInteropHero` (keep) · `[NEW]`
- Kicker `NORMALIZE · VALIDATE · BRIDGE · QUERY`; H1 "One fact. *Every system.*";
  body; animated fabric SVG (systems → canonical XML → systems). No change.
- *Optional:* the body is partly mechanism-led; a benefit-led tweak is available
  if you want parity with the TDP/CM heroes. Default: leave as-is.

### Section 2 — Sibling nav · `SolutionsSiblings` (keep)

### Section 3 — Enterprise Integration Standards · NEW `XmlDataInteropStandards` · `[OLD]` (2 swaps)
- **Heading** `[OLD]`: "Enterprise Integration Standards"
- **Intro** `[OLD]`: "XML is the lingua franca of complex data. We build bridges
  between proprietary silos and open standards — so your content can flow across
  systems without manual rekeying."
- **6 cards** (3×2 grid, amber index/accent/hover), `[OLD]`:
  - **S1000D & Defense Specs** `[OLD · "enabling"→"so"]`
  - **IIoT & Industry 4.0** `[OLD]`
  - **Healthcare & Life Sciences** `[OLD]`
  - **Semantic Web & Knowledge Graphs** `[OLD · "enabling"→"for"]`
  - **Financial & Regulatory (XBRL)** `[OLD]`
  - **API Documentation & Code Sync** `[OLD]` *(retains the "100% API accuracy" claim)*
- *Rationale:* relevance first — "we speak your industry's standard."

### Section 4 — Transformation Technologies · NEW `XmlDataInteropTechnologies` · `[OLD, condensed]`
- **Heading** `[OLD]`: "Transformation Technologies"
- **Intro** `[OLD]`: "The engine room behind every interoperability pipeline. We
  select the right tool for each transformation stage."
- **Spec table** — two columns (tool name | one-line description), hairline rows,
  amber tool names; all 10 (descriptions condensed from the old card copy to one
  line each):
  1. **XSLT 3.0** — Streaming transforms for million-node documents; schema-to-schema and multi-format output.
  2. **XQuery & XPath 3.1** — Complex querying across BaseX, MarkLogic, and eXist-db.
  3. **Schema Validation** — XSD, RelaxNG, and Schematron quality gates, CI-integrated.
  4. **JSON ⟷ XML Bridge** — Bidirectional conversion that preserves semantic structure, not just syntax.
  5. **Event-Driven Pipelines** — Kafka, EventBridge, and webhook-triggered transforms — near real-time, no batch lag.
  6. **XML Databases** — Native storage in MarkLogic, BaseX, or eXist-db with XQuery access at scale.
  7. **GraphQL Content APIs** — Federated content graphs; clients query exactly the fields they need.
  8. **Custom Java & C#** — Saxon, JAXB, or LINQ to XML for logic beyond XSLT — testable, CI/CD-ready.
  9. **CSS-to-PDF Publishing** — Print-quality PDF via CSS Paged Media (Prince, Antenna House, WeasyPrint).
  10. **Python & Node.js Pipelines** — lxml, Beautiful Soup, fast-xml-parser for migration, enrichment, and AI/ML glue.
- *Rationale:* all 10 tools, descriptions kept, compact + document-grade (the
  spec table you picked). *Open: confirm the condensed one-liners (trimmed from
  the full old copy) — or use the full descriptions.*

### Section 5 — The Interoperability Layer · NEW `XmlDataInteropLayer` · `[OLD]`
- **Heading** `[OLD]`: "The Interoperability Layer"
- **Intro** `[OLD]`: "Every pipeline we build follows this five-stage
  architecture — from raw ingest to intelligent delivery."
- **5-stage strip** `[OLD]` (Ingest/Normalize/Validate/Enrich/Deliver vocabulary,
  amber arrows): Ingest *(Sensors · APIs · Legacy Files · Code Repos)* → Normalize
  *(XSLT / XQuery transform to canonical schema)* → Validate *(XSD + Schematron
  quality gates)* → Enrich *(Metadata · Taxonomy · RDF mapping)* → Deliver
  *(Portals · Chatbots · APIs · VR/AR)*.
- **AI-Ready Interoperability callout** `[OLD]` (highlighted box): "Structured XML
  is the ideal source for AI pipelines. We add semantic labels, embedding-friendly
  short descriptions, and JSON-LD mappings to every topic — making your content
  retrievable by RAG systems, citation-ready for LLMs, and indexable as
  knowledge-graph nodes."
- *Rationale:* the method — the 5-stage architecture + the AI-ready angle.

### Section 6 — Explore Related Solutions · NEW `XmlDataInteropRelated` · `[OLD]`
- 3-up (amber card treatment):
  - **Content Migration & Modernization** (SOLUTION) → `/solutions/content-migration`; "Migrate legacy content to structured DITA XML with automated pipelines."
  - **Technical Documentation & Publishing** (SOLUTION) → `/solutions/technical-docs-and-publishing`; "End-to-end documentation and multi-channel publishing with DITA-OT."
  - **XML Engineering** (SERVICE → `/services` placeholder) → "Custom schema design, XSLT transformation, and validation."

### Section 7 — CTA (closing) · `CTAModule` (keep, + `accentLine`) · `[NEW]`
- Compact "Sample Content Assessment" + the animated amber line.

### Removed
- Problem, Pipeline, Patterns, Closing sections.

---

## 6. Decision log
- **D-1 — Rebuild body to old-site sections; cut Problem + Closing.** *(Agreed.)*
- **D-2 — Transformation Technologies → two-column spec table** (all 10, condensed
  one-line descriptions). *(Agreed.)*
- **D-3 — Voice swaps** ("enabling"→"so"/"for"); old hero's "Transform" avoided by
  keeping the new hero. *(Proposed.)*
- **D-4 — Standards as 6 cards** (amber treatment); Layer as 5-stage + AI-Ready
  callout; Related as 3-up (2 Solutions + XML Engineering Service). *(Agreed.)*
- **D-5 — CTA-as-closer + `accentLine`** (parity). *(Following.)*
- **D-6 — Old-page copy authoritative** (incl. the specific standards/tool claims
  and "100% API accuracy"). *(Per CM ruling.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| 1 Hero | `XmlDataInteropHero` | Keep (optional benefit-led body tweak) |
| 2 Siblings | `SolutionsSiblings` | Keep |
| 3 Standards | `XmlDataInteropStandards` (new) | **New build** — 6-card 3×2 grid, amber |
| 4 Technologies | `XmlDataInteropTechnologies` (new) | **New build** — 2-col spec table, 10 rows |
| 5 Interoperability Layer | `XmlDataInteropLayer` (new) | **New build** — 5-stage strip + AI-Ready callout |
| 6 Related | `XmlDataInteropRelated` (new) | **New build** — 3-up |
| 7 CTA | `CTAModule` | Keep + `accentLine` |
| — | `XmlDataInteropProblem/Pipeline/Patterns/Closing` | **Delete** (orphaned) |
| Page | `xml-data-interoperability.astro` | **Edit** — new imports + order; drop `CrossPillarLink` usage |

New builds: 4. Deletes: 4 components + removed `CrossPillarLink` usage. Keeps: 3.

**Border-stitch note:** Siblings carries `border-bottom`; Standards (the section
below) must not double it with a `border-top`.

---

## 8. Open items for review
1. **Spec-table descriptions** — confirm the condensed one-liners (§5 Section 4),
   or use the full old card descriptions.
2. **Hero body** — keep as-is (default), or apply a benefit-led tweak like TDP/CM?
3. Confirm the **voice swaps** (D-3).
