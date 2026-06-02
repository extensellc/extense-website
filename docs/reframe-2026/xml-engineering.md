# XML & Schematron Engineering (service detail) — Reframe Plan

> Status: **implemented — pending staging sign-off.** **Last of the 7** `/services/<slug>`
> detail sub-pages. Built **bespoke** (page-local CSS, prefix `xe-`), reusing
> the shared atoms (`Hero`, `SectionSiblings`, `CTAModule`) and the patterns
> proven on DITA / Publishing / CCMS / SI (icon-card grids, 3-card row, 01-0N
> or un-numbered strip, `#fef3c7` sub-block, related cards, hero node-graph
> visual). Faithful rebuild of the old
> `ex-tense.co/services/xml-engineering.html` (7 sections + mid-page banner);
> the banner is folded into the end CTA per owner.
> **Locked this session:** H1 = "XML & Schematron Engineering";
> **faithful — all 6 content sections, no mid-page banner**; hero **visual D**
> (three engineering pillars feeding into governed XML).
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [system-integration.md](system-integration.md).

---

## 1. Page job
- **URL:** `/services/xml-engineering`
- **Primary reader:** an XML/content engineering lead, info architect, or
  technical buyer evaluating whether to outsource XML governance — schema
  design, XSLT transformation, Schematron rules — rather than build the
  expertise in-house.
- **The one job:** prove deep XML engineering capability — schema, transform,
  validate — and the modern toolchain around it (Java/Python/Node/GraphQL/CSS
  Paged Media/XML databases/AI-Ready) — then convert.

> **Note (overlap, accepted — faithful):** "AI-Ready Content Engineering"
> section overlaps `/services/dita-engineering`'s AI-Ready section heavily;
> "CSS Paged Media → PDF" overlaps `/services/publishing-engineering`. Per
> owner: keep all, cross-link via the Related cards.

---

## 2. Inventory — OLD page
Hero → Beyond Well-Formedness (3 icon cards) → The Validation Stack (5-step
strip + 3 cards below) → **[mid-page Free Schema Health Check banner —
DROPPED, folded into end CTA]** → Modern XML Processing (6 cards) → AI-Ready
Content Engineering (6 cards + "Why Structured XML Is an AI Advantage"
sub-block) → Related Services (3 cards). No end-of-page CTA on the old page —
added as closer for parity, carrying the banner's offer name.

## 3. Inventory — NEW site
Page doesn't exist (last unbuilt `/services/<slug>`, 404 until built). Reuse:
`Hero` (with visual D), `SectionSiblings` (services), `CTAModule` (closer).
Page-local patterns from DITA / Publishing / CCMS / SI: hero node-graph SVG
with scroll-reveal + reduced-motion fallback, icon-card grid (bare amber line
icons), 3-card row with amber top accent, un-numbered roadmap strip (SI
Architecture pattern), `#fef3c7` sub-block (DITA Data Asset pattern), related-
card.

---

## 4. Mapping decisions
- **Faithful rebuild**, old-page section order; **mid-page banner dropped**
  (owner decision); end-of-page `CTAModule` with the "Free Schema Health
  Check" name carried forward.
- **D-1 — H1 = "XML & Schematron Engineering"** *(locked).* Foregrounds the
  Schematron differentiator.
- **D-2 — Hero visual = D** *(locked):* three amber pillar chips at top
  (`schema` / `transform` / `validate`) — the three engineering layers the
  page's hero subdeck names — with convergent connectors dropping into a
  central amber `extense.engineering` chip; that chip sits between a soft-
  dashed `<chapter>` (well-formed, raw) on the left and a custom-amber
  `<chapter>` (governed) on the right. Full scroll-reveal (`.fx` + draw),
  reduced-motion fallback. `FIG. 01 / engineering.layers / RAW → GOVERNED`.
- **3-card sections** (Beyond Well-Formedness, the 3 cards under Validation
  Stack, Related) = grid-3.
  - Beyond Well-Formedness = with **bare amber line icons** (XSLT / Schematron
    / Schema icons; old page had icons).
  - 3 cards under Validation Stack = amber top accent line, no eyebrows
    (they're distinct topics, not engagement modes).
- **6-card sections** (Modern XML Processing, AI-Ready Content Engineering) =
  grid-6 (4+2) with **bare amber line icons** for visual consistency with the
  other detail-page 6-card grids.
- **5-step Validation Stack strip** = the SI Integration Architecture pattern
  (**un-numbered** technical components, not chronological phases). Each step
  uses the `--meta` modifier: mono caption sub-label + body explanation.
  - **D-3 — Step body lines** are `[OLD]` verbatim sub-labels carried forward
    (e.g., "DTD / XSD / RelaxNG — Parent-child rules"). *(Locked.)*
- **AI-Ready sub-block "Why Structured XML Is an AI Advantage"** = DITA Data
  Asset sub-block pattern (`#fef3c7`-tinted centered or `dita-subblock`-style).
- **Voice cleanup (D-4):** JSON-LD card body uses the banned verb "enabling".
  Swap "— enabling rich search results..." → "— for rich search results..."
  (minimal, faithful edit). *(Proposed.)*
- **D-5 — Banded-section rhythm:** S2 plain · S3 band · S4 plain · S5 band ·
  S6 plain · S7 band (Related). *(Locked.)*

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal) + visual D (animated)
- **H1** `[LOCKED]`: "XML & Schematron Engineering"
- **Subdeck** `[OLD]`: "Schema design, transformation pipelines, and
  validation frameworks that enforce quality at the structural level — before
  content ever reaches a reviewer."

### S2 — Sibling switcher · `SectionSiblings` (variant="services")
- current = **XML Engineering** (amber + bold).

### S3 — Beyond Well-Formedness · `[OLD]` (3 icon cards, amber top accent)
- **Intro** `[OLD]`: "XML is just text until you enforce the rules. We design
  and implement the schema layers, transformation pipelines, and business-
  rule validation that turn raw markup into governed, publishable content."
- **3 cards** `[OLD]`:
  1. **XSLT 3.0 Development** *(icon: code brackets)* — "Complex multi-source
     transformations — merging XML streams, generating JSON, SQL, or EPUB
     output, and handling million-node datasets with XSLT 3.0 streaming. We
     write production-grade stylesheets with full unit test coverage using
     Saxon."
  2. **Schematron Business Rules** *(icon: check-in-square)* — "DTD and XSD
     check structure. Schematron checks business logic: 'If classification is
     'Internal', then distribution must be 'Restricted'.' We author ISO
     Schematron rule sets that catch semantic violations before they reach
     production."
  3. **Schema Design & Specialization** *(icon: layers)* — "Custom XSD,
     RelaxNG, and DITA specializations that model your product data without
     breaking standards compliance. We extend element models, add domain-
     specific attributes, and maintain backward compatibility with existing
     toolchains."

### S4 — The Validation Stack · `[OLD]` (5-step un-numbered strip + 3 cards, band)
- **Intro** `[OLD]`: "Production-grade content governance requires multiple
  validation layers — each catching a different class of defect."
- **5 stages** `[OLD]` (un-numbered, `--meta` style: tag-line caption + body):
  1. **Structure** — "DTD / XSD / RelaxNG — Parent-child rules"
  2. **Business Logic** — "Schematron — Semantic constraints"
  3. **Style & Naming** — "Checkstyles — Conventions & terminology"
  4. **Link Integrity** — "Cross-reference & conref validation"
  5. **Clean Output** — "Validated, build-ready XML"
- **3 cards below** `[OLD]` (amber top accent, no eyebrows):
  - **XQuery & XPath** — "Full-text queries, content audits, and cross-
    collection analytics in BaseX, MarkLogic, or eXist-db. We build reporting
    dashboards that surface reuse metrics, orphaned topics, and metadata
    gaps."
  - **CI-Integrated Validation** — "We embed validation into Jenkins, GitHub
    Actions, and Azure DevOps pipelines. Every commit triggers schema
    validation, Schematron checks, and broken-link detection — blocking bad
    content before it merges."
  - **Migration Schema Mapping** — "Mapping legacy schemas (DocBook, custom
    DTDs, FrameMaker EDD) to DITA or S1000D. We document every mapping
    decision and produce automated XSLT converters for repeatable batch
    migration."

### S5 — Modern XML Processing · `[OLD]` (6 icon cards, band)
- **Intro** `[OLD]`: "XSLT is powerful, but it's not always the right tool. We
  build with the full spectrum of modern technologies for XML transformation
  and delivery."
- **6 cards** `[OLD]` (each with bare amber line icon):
  1. **Programmatic Transforms (Java & C#)** *(icon: layers)*
  2. **Python & Node.js Pipelines** *(icon: code)*
  3. **JSON & YAML Interoperability** *(icon: braces)*
  4. **GraphQL Content Layers** *(icon: graph)*
  5. **CSS Paged Media → PDF** *(icon: pagefold)*
  6. **XML Databases & Search** *(icon: database)*
  *(Full body copy carried verbatim.)*

### S6 — AI-Ready Content Engineering · `[OLD]` (6 icon cards + sub-block)
- **Intro** `[OLD]`: "Structured XML is the ideal input for AI systems. We
  engineer the additional layers that make your content retrievable,
  embeddable, and citable by machines."
- **6 cards** `[OLD]` (each with bare amber line icon):
  1. **RAG Chunking & Embedding Prep** *(icon: grid)*
  2. **Semantic Labeling for LLMs** *(icon: tag)*
  3. **JSON-LD & Schema.org Mapping** *(icon: graph)* — *(D-4 voice cleanup:
     "— enabling rich search results..." → "— for rich search results...")*
  4. **Knowledge Graph Generation** *(icon: network)*
  5. **Embedding-Friendly Transforms** *(icon: cube)*
  6. **Content API for AI Pipelines** *(icon: plug)*
- **Sub-block — Why Structured XML Is an AI Advantage** `[OLD]` (DITA
  sub-block pattern):
  - **Heading**: "Why Structured XML Is an AI Advantage"
  - **Body**: "Organizations trying to feed unstructured Word and PDF content
    to AI systems spend most of their effort on parsing, chunking, and
    metadata extraction. If your content is already in structured XML, you've
    solved the hardest part. We build the transform layer that bridges XML
    governance with AI consumption — so your existing content investment
    compounds into AI readiness."

### S7 — Related Services · `[OLD]` (3 cards, band)
- **DITA Engineering** → `/services/dita-engineering` — "Topic modeling,
  specialization, and constraint modules for scalable content architectures."
- **System Integration** → `/services/system-integration` — "Connecting CCMS,
  CMS, and enterprise platforms via APIs and middleware."
- **Publishing Engineering** → `/services/publishing-engineering` — "Custom
  multi-channel publishing pipelines for PDF, HTML5, EPUB, and API
  documentation."

### S8 — CTA (closing) · `CTAModule` (compact + accentLine)
- **Heading** `[OLD, carried from mid-page banner]`: "Free Schema Health
  Check"
- **Body** `[OLD, from mid-page banner]`: "Send us your DTD, XSD, or
  Schematron rules. We'll audit for completeness, identify unvalidated
  business rules, and recommend the validation layers you're missing. No
  commitment required."

### Removed
- Mid-page "Free Schema Health Check" dark banner (owner: single CTA at the
  bottom). The offer name carried forward as the CTA heading.
- Old text breadcrumb (→ sibling switcher), footer nav.

---

## 6. Decision log
- **D-1 — H1 "XML & Schematron Engineering".** *(Locked.)*
- **D-2 — Hero visual D (three pillars feeding governed XML).** *(Locked.)*
- **D-3 — Validation Stack un-numbered, `--meta` style** (same as SI
  Architecture). *(Locked.)*
- **D-4 — Voice cleanup on JSON-LD card** ("— enabling" → "— for").
  *(Proposed.)*
- **D-5 — Faithful, mid-page banner dropped, end-CTA carries the "Free Schema
  Health Check" name.** *(Locked.)*
- **D-6 — Bespoke + shared atoms, `xe-` prefix.** *(Locked.)*

---

## 7. Build inventory
| Section | Component | Action |
|---|---|---|
| S1 Hero | `Hero` + visual D (animated) | New — `[OLD]` subdeck, three-pillar SVG |
| S2 Switcher | `SectionSiblings` (services) | Reuse — current="xml-engineering" |
| S3 Beyond Well-Formedness | section + 3 icon cards (accent line) | **New** |
| S4 Validation Stack | section + 5-step un-numbered strip + 3 cards (band) | **New** |
| S5 Modern XML Processing | section + 6 icon cards (band) | **New** |
| S6 AI-Ready Content Engineering | section + 6 icon cards + sub-block | **New** |
| S7 Related | section + 3 related cards (band) | **New** |
| S8 CTA | `CTAModule` | Reuse — `compact` + `accentLine`, `[OLD]` body |
| Page | `services/xml-engineering.astro` | **New file** |

**Cross-cutting:**
- Clears the **last** dead `/services/<slug>` link — all 7 detail pages live
  after this ships.
- Delete the temp mock `xml-engineering-mock.astro` at build time.
- Spacing-token trap: only `--space-{1,2,3,4,5,6,8,12,16,20,24,32}` exist.
- Verify on the local preview at 1280×900 / 375×812.

---

## 8. Open items for review
1. **Hero subdeck** — confirm `[OLD verbatim]` (no edit).
2. **CTA** — confirm `[OLD]` heading "Free Schema Health Check" + body
   carried from the dropped mid-page banner.
3. **D-4 Voice cleanup on JSON-LD card** — confirm "— enabling rich search
   results..." → "— for rich search results...". Alt: a fuller rewrite.
4. **Validation Stack 5-step strip** — confirm **un-numbered** (matches SI
   Architecture; faithful to old page). Alt: numbered `01–05`.
5. **3 cards under Validation Stack** (XQuery / CI / Migration Schema) —
   confirm **no eyebrows** (amber top accent only). Alt: add eyebrows like
   "Query / CI / Migration".
