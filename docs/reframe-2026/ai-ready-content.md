# AI-Ready Content (sub-page) — Reframe Plan

> Status: **implemented + shipped (round 2).** Last of the four
> `/solutions/*` sub-pages. Tags: `[OLD]` (ex-tense.co/ai-ready.html) /
> `[NEW]` (current extense.co, live, pre-reframe) / `[DRAFT]` (net-new,
> needs approval). Conventions in [README.md](README.md).
>
> **Round 2 (post-review, owner direction):** the original reframe leaned
> too far from the old page. Reverted toward the old structure: (1) **hero
> back to the problem-framed `[OLD]`** headline + body + the 4-metric band
> (25–35% / 85%+ / 3× / 15 yrs); the precision-gauge moved **down to the
> offer section**; a new **content-grounds-answer** flow SVG is the hero
> visual. (2) **ROI block re-added** ("What 'Good Enough' Content Is
> Actually Costing," ~$540K) after the use-case table — light-amber panel,
> not navy. (3) Two-pipeline section uses the **old heading/subdeck**,
> **Without Structured, Enriched Content** (✗) / **With Extense Structured
> Content** (✓) captions, and **no transformation / Extense migration**
> connector labels. (4) Offer cards now a **single left column** (5 equal)
> with the **gauge pinned (sticky) on the right** through the cards.
> (5) **Go Deeper** replaces Explore Related (Guide → `/resources/ai-readiness`,
> DITA Engineering → `/services` placeholder, Content Migration). These
> reverse several round-1 decisions below; the round-1 record is kept for
> history.
>
> Old-page **screenshots reviewed** — they confirm the crawl and the
> section set, and pin down the old visual treatment (red/green semantic
> color throughout; the use-case section was a real 4-column table; the
> 5-phase strip has a Week 1 → 4–8 wks timeline bar; offers carry
> light-amber `Deliverable:` pills). Render-fidelity notes are inline in
> §5; none of it changed a decision.
>
> **The wrinkle that makes this page different:** on Tech Docs, Migration,
> and XML Interop the old pages were already solution-led, so "rebuild to
> the old-site sections" and "lead with solutions / cut problem-ed + ROI"
> pointed the same way. **The old AI-Ready page is the opposite — a
> problem/cost-led landing page.** Its signature sections ("What
> Unstructured Content Is Costing You," the ~$540K ROI block, the problem
> hero) are exactly what the locked thesis bans. So we can't mirror it
> faithfully.
>
> **Resolution (this session):** pull forward only the old page's
> **solution-led** sections; drop its problem-education and ROI blocks.
> That's the reframe applied to a page that needs more judgment than its
> siblings. The upside: the *current* new-build body already lines up with
> those solution sections, so AI-Ready needs **lighter demolition** — the
> only clearly invented section to cut is `AiReadyClosing`.

---

## 1. Page job

- **URL:** `/solutions/ai-ready-content` (old source lived at the root:
  `ex-tense.co/ai-ready.html`).
- **Primary reader:** a problem-aware buyer who has already deployed (or
  is deploying) an LLM/chatbot/RAG pipeline and is getting bad answers —
  a content-ops or AI/platform lead who suspects the content, not the
  model, is the bottleneck.
- **The one job:** show that **retrieval precision is a content-engineering
  property** — prove it with the before/after pipeline, show the breadth
  (one engineered corpus → seven AI use cases), name the method (5 phases)
  and the deliverables (what Extense hands over), then route + convert. The
  "why structure" is settled; the buyer wants the fix.

---

## 2. Inventory — OLD site (ex-tense.co/ai-ready.html)

1. **Hero** — "Your AI Is Only As Good As Your Content" (problem-led) +
   problem sub-deck + "Get Your Free AI-Readiness Assessment."
2. **Key metrics band** — 25–35% (chatbot precision, unstructured) · 85%+
   (after structured engineering) · 3× (avg accuracy improvement) · 15 yrs
   (experience).
3. **"What Unstructured and Unenriched Content Is Costing You Right Now"**
   — intro + **6 problem subsections** (Hallucinations · Support tickets ·
   Localization costs · Fine-tuning · Personalization · Search relevance).
   *Pure problem-education.*
4. **"Two Content Pipelines. One Outcome Difference."** — before/after
   pipeline (Without → 25–35% · With Extense → 85%+).
5. **"Every AI Use Case Needs the Same Foundation"** — intro + **7-row
   table** (Use Case | What It Needs | Without Structure | With Extense
   Structure). *Solution-led.*
6. **"What 'Good Enough' Content Is Actually Costing"** — ROI block:
   $180K + $240K + $120K = **~$540K** annual drag. *Pure cost/ROI.*
7. **"From Unstructured or Unenriched to AI-Ready in 5 Phases"** — Audit &
   Score → Structure & Type → Enrich Metadata → Build Pipeline → Integrate
   & Validate, with a Week 1 → 4–8 weeks timeline.
8. **"We Engineer — We Don't Just Advise"** — intro + **5 deliverable
   offerings** (Free Assessment · Structured Migration · Taxonomy &
   Metadata · AI-Native Pipeline · Integration & Validation) + a
   before/after bar chart (30% → 87%, **+57pts**).
9. **"Start With a Free Assessment"** — CTA + 20-topic assessment form.
10. **"Go Deeper"** — 3 cards: Guide (resource) · DITA Engineering
    (Service) · Content Migration (Solution).
11. **Newsletter** — *(prohibited.)* · Footer.

## 3. Inventory — NEW site (current, live, pre-reframe build)

Hero (`AiReadyHero`, "Retrievable, by design." + animated precision-gauge
SVG) → Siblings → **`AiReadyComparison`** (Two pipelines, before/after —
this *replaces* the standard 3-up problem section; it is not a separate
problem-ed block) → **`AiReadyPipeline`** (5-stage AUDIT → STRUCTURE →
ENRICH → BUILD → VALIDATE, manifesto intro) → **`AiReadyUseCases`** (5
editorial chapter-blocks) → **`AiReadyClosing`** ("The measurement is the
deliverable," 85% — *new-invented prose*) → generic `CrossPillarLink`
(`/services`) → `CTAModule` (no `accentLine`).

**Disposition:** keep Hero + Siblings + CTA. Keep Comparison and Pipeline
(they *are* old-page sections). Rebuild UseCases → the old 7-use-case
comparison table. **Add** a "We Engineer" offer section (not on the new
page). **Cut** `AiReadyClosing` (invented) and the generic `CrossPillarLink`
→ replace with a 3-up Related. **Do not pull forward** the old problem-ed
and ROI blocks or the newsletter.

---

## 4. Mapping decisions

### Keep from NEW `[NEW]`
- **AiReadyHero** — solution-led, on-thesis; keep the gauge. **Body
  rewritten benefit-led `[DRAFT]`** (Q3 — see §5 Section 1).
- **AiReadyComparison** (Two pipelines) — the old "Two Content Pipelines"
  section, already ≈ verbatim. Keep; refine to design parity.
- **AiReadyPipeline** (5 phases) — the old "5 Phases" section; identical
  phase names. Keep; swap the invented manifesto for the `[OLD]` intro
  (D-4).
- **SolutionsSiblings**, **CTAModule** — keep. CTA gains `accentLine` for
  parity with the three siblings.

### Rebuild / Add to OLD-site sections `[OLD]`
- **Every AI Use Case Needs the Same Foundation** — rebuild
  `AiReadyUseCases` (5 editorial blocks) → the old **7-row comparison
  table** (Q1). `[OLD]` copy verbatim.
- **We Engineer — We Don't Just Advise** — **new section** (Q2): 5
  deliverable cards, `[OLD]` copy. The old bar chart is **dropped** — the
  hero gauge already carries 30 → 87 / +57pts (D-6).
- **Explore Related Solutions** — replace the generic `CrossPillarLink`
  with a 3-up (2 Solutions + 1 Service), remapped from the old "Go Deeper"
  (D-7).

### Cut
- **AiReadyClosing** (invented "The measurement is the deliverable" prose;
  85% already lands in the hero gauge and the structured-pipeline outcome).
  Delete.
- **Old problem-ed block** ("What Unstructured Content Is Costing You," 6
  subsections) — not pulled forward (banned).
- **Old ROI block** (~$540K) — not pulled forward (recipe cuts ROI).
- **Newsletter** — prohibited.
- **`CrossPillarLink` usage** — replaced by the 3-up (component kept; other
  pages may still use it).

### Voice swaps
- Minimal here — unlike the siblings, the old AI-Ready solution copy is
  largely clean of banned verbs (`transform`/`enable`/`unlock`/`harness`).
  One to watch: the current `AiReadyUseCases` block #5 body uses "the same
  metadata **enables** compliance auditing" — that copy is being replaced
  by the `[OLD]` table, whose Compliance row reads "AI detects missing
  `<prereq>`, untagged warnings, coverage gaps" (no banned verb), so the
  issue retires with the rebuild. Re-scan the final `[OLD]` cells at build.

---

## 5. Wireframe

Order (solution-led, escalating): **claim → proof → reach → method → offer
→ cross-sell → convert.** This matches the old-page body order (Two
Pipelines → 7-use-case table → 5 Phases → We Engineer) with the problem-ed
and ROI blocks removed.

### Section 1 — Hero · `AiReadyHero` (keep; body rewritten) · `[NEW]` H1 + `[DRAFT]` body
- **Kicker** `[NEW]`: `TYPE · CHUNK · FILTER · MEASURE`
- **H1** `[NEW]`: "Retrievable, by *design.*"
- **Body** `[DRAFT — needs approval]`, benefit-led 4-sentence deck
  (replaces the current mechanism-flavored body, esp. "the translation
  layer between your documentation and the LLMs that consume it"):
  > "Ask the chatbot a question your docs already answer, and get the right
  > answer back — cited to the exact section it came from, not a confident
  > guess stitched from averaged context. The corpus that gets RAG to 85%
  > precision is the same one that feeds semantic search, AI translation,
  > fine-tuning, and compliance auditing, so the content is engineered once
  > and every AI system reads from it. Typed DITA topics, controlled
  > metadata, and stable section IDs are what make retrieval precise —
  > precision becomes a measurable property of the content, scored against
  > your real user queries rather than tuned on the model. Start from Word,
  > PDF, or DITA that was never enriched; the work that closes the gap is
  > the same."
- **Visual** `[NEW]`: animated precision-gauge SVG (BASELINE 30% → AFTER
  87%, +57pts, calibration readout) — unchanged.

### Section 2 — Sibling nav · `SolutionsSiblings` (keep) · n/a

### Section 3 — Two Content Pipelines (the proof) · `AiReadyComparison` (keep) · `[NEW ≈ OLD]`
- **Heading** `[NEW]`: "Two pipelines. *One measurement.*" *(old page:
  "Two Content Pipelines. One Outcome Difference." — keep the new wording,
  it's tighter; open to reverting to `[OLD]`.)*
- **Sub-deck** `[NEW]`: "Same query, same LLM, same vector store. What the
  model retrieves is determined entirely by whether the content was
  engineered for retrieval."
- **Two columns** (`[NEW]`, ≈ the old stage labels verbatim):
  - **UNSTRUCTURED** — Content sources → Flat ingestion → Arbitrary
    chunking → Vector store → LLM context window → **Outcome: 25–35%
    precision** (wrong answers · hallucinations · escalated tickets).
  - **STRUCTURED** — Content sources → Typed DITA topics → Metadata +
    section IDs → Semantic chunking → Vector store + metadata filters →
    **Outcome: 85%+ precision** (correct answers · cited sources · reduced
    support load). Single amber accent on the structured outcome.
- *Rationale:* the before/after frame **is** the argument; leads the body
  as the proof. (The "without" column reads as contrast, not standalone
  problem-ed — same justification as keeping the 7-table's "without"
  column.)
- *Render fidelity (screenshots):* the old page renders this as two
  **red-tinted / green-tinted** side-by-side flow cards (✗/✓), with a dark
  red 25–35% box vs. a dark green 85%+ box. We deliberately **do not**
  replicate the red/green — the current `AiReadyComparison` already makes
  the correct single-amber translation (subdued "without," amber on the
  structured outcome only). Keep that.

### Section 4 — Every AI Use Case Needs the Same Foundation (the reach) · rebuild `AiReadyUseCases` → table · `[OLD]`
- **Heading** `[OLD]`: "Every AI Use Case Needs the Same Foundation"
- **Intro** `[OLD]`: "It's not just chatbots. Every AI initiative your
  organization runs draws from the same content well. Structure it once —
  every system benefits."
- **7-row comparison table** `[OLD]` (Use Case | What It Needs from Content
  | Without Structure | With Extense Structure):
  1. **Chatbot / RAG** — Typed chunks, metadata filters, section IDs for
     citation | 25–35% precision. Hallucinations fill gaps. | 85%+
     precision. Cited, traceable answers.
  2. **Semantic Search** — audience, difficulty, domain metadata per topic
     | Relevance improves slightly. Filtering impossible. | Role-scoped
     results. Right level, right domain.
  3. **AI-Assisted Translation** — Semantic elements (`<step>`,
     `<warning>`, `<shortdesc>`) | NMT treats everything as prose. Quality
     inconsistent. | Element-aware NMT. Safety phrasing rules fire on
     `<note type="warning">`.
  4. **LLM Fine-Tuning** — Clean, typed, deduplicated training examples |
     Noisy training data. Model learns contradictions. | High-signal
     corpus. Model learns your voice, not an average.
  5. **Personalization** — audience + difficulty metadata on every topic |
     Same content for everyone. Personalization is theoretical. | Dynamic
     delivery by role, level, product line.
  6. **Compliance Auditing** — Schema-enforced structure to audit against |
     AI can flag keywords but not structural gaps. | AI detects missing
     `<prereq>`, untagged warnings, coverage gaps.
  7. **AI-Assisted Authoring** — Typed templates + controlled vocabulary
     constraints | AI generates off-topic, inconsistent drafts. | AI fills
     typed templates. Output is consistently on-structure.
- **Render** — hairline comparison table on desktop (mono use-case names,
  amber accent on the "With Extense" column header); **stacks to per-use-
  case cards on mobile** (a 4-column table is unreadable < 768px). See
  Open item 2.
- *Render fidelity (screenshots):* the old page already rendered this as a
  real 4-column table — dark navy header row, lavender use-case-name pills,
  **red** "Without Structure" text vs. **green** "With Extense Structure"
  text. So Q1 (table) is faithful, not a reinterpretation. We swap the
  red/green/navy for the locked palette: hairline rows, mono header, single
  amber accent on the "With Extense" column; "without" cells in muted text.
- *Rationale:* breadth of value — "structure once, every system benefits."
  The strongest solution-led section on the old page.

### Section 5 — From Unstructured to AI-Ready in 5 Phases (the method) · `AiReadyPipeline` (keep) · `[OLD]` intro + `[NEW]` stages
- **Intro** `[OLD]` (replaces the invented manifesto "Precision is a
  content engineering problem."): "A deterministic engineering process —
  not a consulting engagement with open-ended deliverables. Whether you're
  starting from Word documents or from DITA that was never properly
  enriched, each phase has a concrete output and a measurable improvement."
  *(D-4 — confirm we drop the manifesto framing for the `[OLD]` intro.)*
- **5-stage strip** `[NEW]` (phase names identical to `[OLD]`):
  - **01 Audit & Score** — 7-dimension AI-readiness scorecard → gap
    analysis / AI-readiness score.
  - **02 Structure & Type** — DITA migration, stable section IDs.
  - **03 Enrich Metadata** — subject scheme + controlled vocabulary, 100%
    coverage gate.
  - **04 Build Pipeline** — DITA-OT emits `chunks.jsonl`,
    `glossary-index.json` alongside HTML / PDF.
  - **05 Integrate & Validate** — vector store live, precision measured
    against real queries.
- *Rationale:* the method — deterministic, output per phase. Sits after the
  reach so "how" follows "what."
- *Optional add (screenshots):* the old page pairs the 5-phase strip with a
  **timeline bar** beneath it — Week 1 → 4–8 weeks (small corpus) →
  AI-Ready ✓. Our current `AiReadyPipeline` omits it. A restrained hairline
  timeline rule would reinforce "deterministic process / weeks, not
  quarters." See Open item 6.

### Section 6 — We Engineer — We Don't Just Advise (the offer) · NEW `AiReadyOffer` · `[OLD]`
- **Heading** `[OLD]`: "We Engineer — We Don't Just Advise"
- **Intro** `[OLD]`: "Every engagement ends with working, measurable
  infrastructure — not a report with recommendations you have to implement
  yourself."
- **5 deliverable cards** `[OLD]` (amber card treatment; each card leads
  with the offering and ends with an emphasized **Deliverable:** line):
  1. **Free AI-Readiness Assessment** — "Send us 20 topics. We score them
     on 7 dimensions — content typing, metadata coverage, section
     addressability, vocabulary control, semantic markup, reuse
     architecture, and pipeline maturity — and return a gap analysis with
     specific next steps." **Deliverable:** Scored gap analysis · No
     obligation.
  2. **Structured Migration** — "We convert your Word, PDF, FrameMaker, or
     wiki content to typed DITA XML with section IDs. Automation tooling
     handles scale — 1,000 topics is not 1,000 hours of manual work."
     **Deliverable:** Typed DITA corpus with full section addressability.
  3. **Taxonomy & Metadata Engineering** — "We design a controlled
     vocabulary — audience, difficulty, domain, intent — and apply it at
     scale. Validation rules prevent vocabulary drift from day one."
     **Deliverable:** Subject scheme + 100% metadata coverage.
  4. **AI-Native Publishing Pipeline** — "We configure your DITA-OT
     toolchain to produce `chunks.jsonl`, `glossary-index.json`, and
     `content-manifest.json` alongside HTML and PDF — all from a single
     source, on every build." **Deliverable:** Automated multi-format
     pipeline including JSONL.
  5. **Integration & Precision Validation** — "We connect your output to
     your vector store, configure metadata filters for intent routing and
     audience scoping, run retrieval tests against real user queries, and
     deliver a measured precision baseline." **Deliverable:** Live AI
     retrieval with measured 85%+ precision target.
- **Bar chart — dropped** (D-6): the old "30% → 87% / +57pts" chart is
  already the hero gauge; reproducing it here would double the figure.
  *Screenshots confirm the old layout is 2-column (numbered offerings left,
  the bar chart right). Dropping the chart leaves the cards needing a
  layout: propose an amber-card grid (sibling treatment) or keep the old
  numbered-list editorial style. The light-amber `Deliverable:` pills are
  on the old page — keep them. See Open item 5.*
- *Differentiation from §5 (the overlap you flagged is real):* §5 is the
  **process** (horizontal sequence strip — how the work flows); §6 is the
  **deliverables** (cards — what you walk away holding). Different framing,
  different layout, so the adjacency reads as "method, then outputs," not
  repetition. The list ends on the measured-85% deliverable → a clean
  bridge into Related + CTA. See Open item 3.

### Section 7 — Explore Related Solutions · NEW `AiReadyRelated` · `[OLD]` (remapped)
- **Heading** `[OLD]`: "Explore Related Solutions" (old page: "Go Deeper")
  — 3-up, amber card treatment:
  - **Content Migration & Modernization** (SOLUTION) →
    `/solutions/content-migration`; `[OLD]` "Proven methodology for
    converting unstructured content to structured, enriched DITA XML at
    scale." *(the prerequisite to AI-readiness.)*
  - **XML Data Interoperability** (SOLUTION) →
    `/solutions/xml-data-interoperability`; "Structured XML as the
    canonical source for AI pipelines — semantic labels, JSON-LD, and
    retrieval-ready topics." *(its old page already carries an AI-Ready
    Interoperability callout.)*
  - **DITA Engineering** (SERVICE → `/services` placeholder); `[OLD]`
    "Topic modeling, metadata enrichment, AI-ready content architecture,
    and controlled vocabulary design."
- **Dropped from the old "Go Deeper":** the **Guide** card (the
  `resources/ai-content-readiness-guide` page doesn't exist yet). See Open
  item 4 (Tech Docs as an alternative second Solution).

### Section 8 — CTA (closing) · `CTAModule` (keep, + `accentLine`) · `[NEW]`
- Compact "Sample Content Assessment" + the animated amber line.
  CTA-as-closer, parity with the three siblings. Current body kept:
  > "Send us 20 topics from your current documentation. We'll score them on
  > 7 AI-readiness dimensions and return a gap analysis with the next
  > concrete steps — within two business days."

### Removed
- `AiReadyClosing`; old problem-ed block; old ROI ($540K) block;
  newsletter; generic `CrossPillarLink` usage.

---

## 6. Decision log

- **D-1 — The old AI-Ready page is problem/cost-led; pull forward only its
  solution sections** (Two Pipelines, 7-use-case table, 5 Phases, We
  Engineer), drop problem-ed + ROI. *(Resolved this session.)*
- **D-2 — Use-case section = the old 7-row comparison table** (not the 5
  editorial blocks). *(Q1 — chosen.)*
- **D-3 — Add "We Engineer" as a distinct offer section** (5 deliverable
  cards). *(Q2 — chosen.)*
- **D-4 — 5-phase intro swapped to the `[OLD]` "deterministic engineering
  process" copy**, dropping the invented "Precision is a content
  engineering problem." manifesto. *(Proposed — confirm.)*
- **D-5 — Hero body rewritten benefit-led `[DRAFT]`** (Q3 — chosen;
  net-new copy needs explicit approval before ship). Gauge unchanged.
- **D-6 — Drop the "We Engineer" bar chart** (30 → 87 / +57pts already in
  the hero gauge). *(Proposed.)*
- **D-7 — Related 3-up:** Content Migration + XML Data Interoperability
  (Solutions) + DITA Engineering (Service → `/services`). Drop the old
  Guide card. *(Proposed.)*
- **D-8 — CTA-as-closer + `accentLine`** (parity). *(Following.)*
- **D-9 — Cut `AiReadyClosing`;** delete it + drop `CrossPillarLink` usage.
  *(Proposed.)*
- **D-10 — Order:** proof (pipelines) → reach (use-case table) → method (5
  phases) → offer (We Engineer). Matches the old-page body order minus the
  cut blocks. *(Proposed — alternative was table-first; chose
  pipeline-first as it sets up "structure → precision," then "and it serves
  7 use cases.")*

---

## 7. Build inventory

| Section | Component | Action |
|---|---|---|
| 1 Hero | `AiReadyHero` | Keep gauge; **rewrite body** `[DRAFT]` (D-5) |
| 2 Siblings | `SolutionsSiblings` | Keep |
| 3 Two Pipelines | `AiReadyComparison` | Keep; design-parity refine |
| 4 Use-case foundation | `AiReadyUseCases` → **rebuild to 7-row table** | **Rebuild** — `[OLD]` 7-use-case comparison table; responsive stack on mobile |
| 5 Five Phases | `AiReadyPipeline` | Keep; **swap intro to `[OLD]`** (D-4) |
| 6 We Engineer | `AiReadyOffer` (new) | **New build** — 5 deliverable cards, amber treatment; no bar chart |
| 7 Explore Related | `AiReadyRelated` (new) | **New build** — 3-up, remapped (D-7) |
| 8 CTA | `CTAModule` | Keep + `accentLine` |
| — | `AiReadyClosing` | **Delete** (orphaned) |
| Page | `ai-ready-content.astro` | **Edit** — new imports + order; drop `CrossPillarLink` usage |

New builds: 2 (`AiReadyOffer`, `AiReadyRelated`). Rebuild: 1
(`AiReadyUseCases` → table). Keeps (refine): 3 (Hero, Comparison,
Pipeline). Deletes: 1 (`AiReadyClosing`) + removed `CrossPillarLink` usage.

**Border-stitch note:** Siblings carries a `border-bottom`; the section
directly below (Comparison) must not double it with a `border-top` —
already handled in the current `AiReadyComparison`. Re-verify dividers
top-to-bottom after the rebuild, especially around the new §6/§7.

---

## 8. Open items for review

1. **Hero body `[DRAFT]`** (§5 Section 1) — approve / edit the benefit-led
   rewrite, or keep the current body?
2. **7-use-case table rendering** — desktop hairline table + mobile card
   stack (proposed), or a different treatment (e.g. 7 amber cards with the
   "with Extense" framing only)?
3. **§5 / §6 adjacency** — confirm the process-strip vs deliverable-cards
   differentiation reads as distinct, not repetitive. (Fallback if it feels
   redundant at build: fold the `Deliverable:` lines into the §5 phase
   cards and drop §6 — but that reverses Q2.)
4. **Related second Solution** — XML Data Interoperability (proposed) or
   Technical Documentation & Publishing?
5. **Confirm D-4** (drop the 5-phase manifesto for the `[OLD]` intro) and
   **D-6** (drop the offer bar chart). If we drop the chart, pick the §6
   layout: amber-card grid (sibling treatment) vs. the old numbered-list
   editorial style. Keep the light-amber `Deliverable:` pills either way.
6. **5-phase timeline bar** — add the old page's Week 1 → 4–8 wks →
   AI-Ready ✓ rule beneath the strip (restrained, hairline), or leave the
   current strip as-is?
