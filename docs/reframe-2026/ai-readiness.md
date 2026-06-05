# AI-Readiness (Resources sub-page) — Redesign Plan

> Status: **wireframe pending sign-off.** The current
> `/resources/ai-readiness` is already a substantial page (hero with
> ScorecardDimensionCard side panel, 3-paragraph framing prose,
> horizontal-row 7-dim scorecard, interpretation rubric, vertical
> 5-phase roadmap, worked examples, output schema, CTA). The redesign
> tightens the layout into the document-grade rail-grid aesthetic
> established on `/company/our-process` and brings back the old page's
> punchier 3-card opener.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md).

---

## 1. Page job
- **URL:** `/resources/ai-readiness`
- **Primary reader:** content engineering lead, RAG/chatbot owner, or
  documentation manager evaluating whether their corpus is ready for
  AI retrieval. Often arrived here from search ("how to make content
  AI-ready") or from the Solutions page.
- **The one job:** give a self-serve diagnostic (the 7-dimension
  scorecard) plus a roadmap and worked examples so the reader can
  honestly assess their own corpus and understand what production-grade
  AI-readiness actually requires. Convert to a sample assessment at the
  end.

---

## 2. Inventory — OLD page (extense.co/ai-readiness)

1. **Hero** — H1 "How to Make Your Content AI-Ready" + subdeck "A
   practical guide to preparing structured content for chatbots, RAG
   pipelines, and intelligent retrieval."
2. **Why AI-Readiness Matters Now** — Intro + 3-card grid:
   - The Problem (unstructured content → AI can't distinguish)
   - The Cost of Inaction (25–35% retrieval precision, hallucinations)
   - The Opportunity (85%+ retrieval with semantic typing + metadata)
3. **AI-Readiness Scorecard** — Intro "Rate your content on these 7
   dimensions. Each adds roughly 1–1.5 points to your AI-readiness
   score (out of 10)." 7-card grid (3-3-1 layout):
   - 01 Content Typing · 02 Metadata Coverage · 03 Section Addressability
   - 04 Vocabulary Control · 05 Semantic Markup · 06 Reuse Architecture
   - 07 Output Pipeline Maturity (full-width)
   Each card: Question / Why it matters / Score 0/1/2
4. **Interpreting Your Score** — 4 row rubric (0-4 / 5-7 / 8-10 / 12-14)
5. **The Preparation Roadmap** — Intro + 5 cards horizontally:
   Audit & Baseline · Structure & Type · Enrich Metadata · Build the
   Pipeline · Integrate & Validate. Each with body + Deliverable line.
6. **Typical Timeline** — 3 rows: Small/Medium/Large corpus
7. **What AI-Ready Content Looks Like** — Intro + 3 sub-sections:
   - Metadata That AI Systems Can Filter (3-card: Audience · Difficulty · Intent)
   - Section-Aware Chunking (2-card before/after: Without IDs · With IDs)
   - Controlled Vocabulary vs. Free-Text Tags (2-card before/after)
8. **The Output: Chatbot-Ready JSONL** — Full-width "What Gets Exported"
   paragraph + 3-card files (chunks.jsonl · glossary-index.json ·
   content-manifest.json)
9. **Free AI-Readiness Assessment** — dark navy CTA banner
10. **Related Resources** — 4-card grid
11. Stay Connected newsletter (banned)

## 3. Inventory — NEW site (current state)

The page already exists and is substantial. Section list:
1. Hero (universal, with `ScorecardDimensionCard` side panel showing dim 01)
2. Framing prose — 3 paragraphs replacing the old 3-card "Why" opener
3. 7-dim scorecard — **horizontal rows** (desktop: num | name | question | why | scoring) — dense, data-table-like
4. Interpret your score — 4-row rubric
5. Preparation roadmap — vertical stack with phase numbers + deliverable callouts
6. Typical timeline — 3-row table
7. Worked examples — 3 sub-sections (metadata 3-card · before/after chunking · before/after vocabulary)
8. Output schema — 3-row table (chunks / glossary / manifest)
9. CTAModule

Strengths to preserve: the 7-dim content, the roadmap content,
the worked examples, the output schema, the interpretation rubric.

Weaknesses to fix: the horizontal-row scorecard is hard to scan; the
framing prose loses the punch the old 3-card opener had; the vertical
5-phase stack takes a lot of vertical space; no hero side-visual
matching the rest of the new site's idiom.

---

## 4. Mapping decisions

- **D-1 — Adopt the document-grade rail-grid aesthetic** site-wide we
  established on `/company/our-process`: mono rail labels, hairline
  dividers, no card-style shadows or rounded corners. The current
  scorecard already uses hairlines but doesn't carry the rail label;
  the redesign formalizes the pattern across every section.
- **D-2 — Hero gets a compact SVG side-visual** in the document-grade
  idiom (corner reg-marks, mono FIG. chrome, amber elements,
  `IntersectionObserver` `.drawn` reveal). Concept TBD — sketches in
  S1 below. Replaces the `ScorecardDimensionCard` side panel.
- **D-3 — Restore the 3-card "Why this matters" opener** (Problem ·
  Cost of Inaction · Opportunity), styled as 3 rail-rows instead of
  the original old-page marketing cards. Replaces the current
  3-paragraph framing prose, which buries the load-bearing claims
  ("retrieval precision in the 25–35% range" / "85%+ precision") in
  body text. The 3-card framing reads in a glance.
- **D-4 — Restructure the 7-dim scorecard** from horizontal rows to a
  3-col grid (matching the old page's 3-3-1 layout). Each dimension
  becomes its own scannable card with: number + name (top) · question
  (middle) · why it matters (middle) · scoring 0/1/2 (bottom). Rail-grid
  styled — hairline-bordered cells, mono labels, no rounded corners.
- **D-5 — Compact the roadmap** from a vertical stack to a 5-card
  horizontal strip at desktop (like the 5-phase overview strip on
  `/company/our-process`). Each card carries: number · phase name ·
  body (2-3 sentences) · "Deliverable:" line. Stacks vertically on
  mobile.
- **D-6 — Timeline as inline addendum** to the roadmap — 3-row compact
  data block right after the strip, not a separate section.
- **D-7 — Worked examples (S6) restructured** as 3 mini-sections inside
  one container, each with a rail label and tight before/after cells.
  Less section heading repetition.
- **D-8 — Output schema (S7) as a clean rail-row table** — 3 rows, one
  per file. Each row: filename (mono code-style) · purpose. With a
  short "What gets exported" intro above.
- **D-9 — Drop the old page's "Related Resources" 4-card grid.** The
  TopNav already routes to Resources, and we have CTAs elsewhere.
  Cleaner ending.
- **D-10 — Drop newsletter** (locked rule).
- **D-11 — Banded rhythm:** S1 plain · S2 band · S3 plain · S4 plain ·
  S5 band · S6 plain · S7 band · S8 plain (CTA).
  Or simplified to: alternate every other for the deeper sections.

---

## 5. Wireframe

### S1 — Hero
- **H1** `[NEW-current, kept]`: "AI-readiness is a content engineering
  problem."
- **Subdeck** `[NEW-current, kept]`: "Retrieval precision is upstream of
  model selection. A practitioner guide to the seven dimensions of
  content engineering that determine whether your AI pipeline returns
  the right answer or the closest keyword match."
- Layout: 2-column lead+aside at ≥1024px (matches `/company/our-process`
  hero pattern). Lead block on left (max-width 540px). Compact SVG on
  right.
- **Hero side-visual (DRAFT — pick one):**
  - **A. Score arc** — Horizontal scale 0–14 with a muted dot at
    "baseline ~3" and an amber dot at "target ~10". Amber arc between.
    `FIG. 01 / readiness.score`. Same idiom as the index page hero E
    candidate.
  - **B. 7-dim spokes** — Central amber `extense.readiness` chip with
    7 small spoke labels around it (the 7 dimensions). Reads as
    "readiness has 7 dimensions, scored together."
  - **C. Linear-with-loopback** (same as `/company/our-process`) —
    less appropriate here; would just duplicate.
  - **My pick: A.** Quickly communicates the scorecard's core
    promise (you can measure this).

### S2 — Why this matters · 3 rail-row cards `[OLD]` (banded)
- **Heading** `[NEW-DRAFT]`: "Why AI-readiness matters." (or restored
  old: "Why AI-Readiness Matters Now.")
- **Intro** `[NEW-current, trimmed to 1 sentence]`: "Most enterprise
  content sits in unstructured formats. When that lands in a vector
  store, the AI treats every paragraph as undifferentiated text."
- **3 rail-rows** `[OLD verbatim, lightly edited]`:
  - **The problem** — "AI can't distinguish a safety warning from a
    marketing blurb, a step-by-step procedure from a concept
    explanation, or a beginner topic from an expert reference."
  - **The cost of inaction** — "Organizations that deploy chatbots on
    unstructured content see retrieval precision around 25–35%. Users
    get wrong answers, lose trust, and escalate to human support.
    Worse, AI hallucinations fill gaps where metadata should have
    guided the system."
  - **The opportunity** — "Content that is semantically typed,
    metadata-enriched, and section-addressable delivers 85%+ retrieval
    precision. The AI knows what each piece of content is, who it's
    for, and when to surface it. That's the difference between a
    chatbot that guesses and one that answers."

### S3 — The 7-dimension scorecard `[NEW-current content, RE-LAID-OUT]`
- **Heading** `[NEW-current, kept]`: "The seven-dimension scorecard."
- **Intro** `[NEW-current, kept]`: "Rate your content on each dimension
  below: 0, 1, or 2 points. Total range is 0–14. Sum your score and
  consult the interpretation rubric below."
- **Layout:** 3-col grid (3 + 3 + 1 = 7 cards). Each card:
  - Top: mono amber number (`01`) + dimension name (`Content Typing`)
  - Italic question: "Is every document formally typed…"
  - Mono "WHY IT MATTERS" label + body
  - Mono "SCORING" label + 3 score rows (0/1/2 with body)
- All 7 dimensions kept verbatim from the current page data array.

### S4 — Interpret your score `[NEW-current, kept]`
- **Heading**: "Interpret your score."
- 4 ranges in compact rail-row table (range mono left | meaning right):
  - 0 – 4 / 5 – 7 / 8 – 10 / 11 – 14
- Content unchanged.

### S5 — The preparation roadmap `[NEW-current content, RE-LAID-OUT]` (banded)
- **Heading**: "The preparation roadmap."
- **Intro** `[NEW-current]`: "Five phases to take content from
  unstructured to AI-ready. Each phase builds on the previous one;
  skipping the foundation phases is the most common way these programs
  fail."
- **5-card horizontal strip** (like `/company/our-process` overview):
  01 Audit & baseline · 02 Structure & type · 03 Enrich metadata ·
  04 Build the pipeline · 05 Integrate & validate
  Each card: number · phase name · 2-3 sentence body · `Deliverable:`
  line at the bottom (mono label + value).
- **Typical timeline** addendum inline below the strip:
  - "Typical timeline" eyebrow + 3 rail-rows (Small corpus 50–200 / Medium
    200–1,000 / Large 1,000+) with timeline values.

### S6 — What AI-ready content looks like `[NEW-current content, kept]`
- **Heading**: "What AI-ready content looks like."
- **Intro** `[NEW-current]`: "Concrete examples of the transformations
  the scorecard measures. Each pair shows the failure mode at score 0
  and the working pattern at score 2."
- **3 sub-sections**, each with a rail-grid layout:
  - **Metadata that AI systems can filter** — 3 rail-rows: Audience
    filtering · Difficulty matching · Intent routing
  - **Section-aware chunking** — 2-col before/after rail-row: Without
    section IDs · With section IDs
  - **Controlled vocabulary vs free-text tags** — 2-col before/after:
    Free-text chaos · Controlled vocabulary

### S7 — Output: chatbot-ready JSONL `[NEW-current content, kept]` (banded)
- **Heading**: "Output: chatbot-ready JSONL."
- **Intro** `[NEW-current]`: "Each section becomes a JSONL record with
  the text content, topic title, section heading, topic type, all
  metadata fields, the section ID for deep-linking, and the parent map
  path for breadcrumb context."
- **3 files table** (rail-row: mono filename | body purpose):
  - `chunks.jsonl` — One JSON object per section…
  - `glossary-index.json` — Term definitions with synonyms…
  - `content-manifest.json` — Topic inventory with metadata…

### S8 — CTAModule `[shared component]`
- **Body** `[NEW-current, kept]`: "Submit a 20-topic sample. We'll score
  it on all seven dimensions, return a gap analysis with recommended
  next steps, and indicate the engineering effort required to reach
  production-grade retrieval. No obligation to proceed."

---

## 6. Decision log
- **D-1** *(locked)* — Document-grade rail-grid aesthetic across all
  sections.
- **D-2** *(pending — pick a visual)* — Hero gets a compact SVG side
  visual.
- **D-3** *(locked)* — Restore 3-card "Why this matters" opener as
  3 rail-rows.
- **D-4** *(locked)* — 7-dim scorecard restructured to 3-col grid.
- **D-5** *(locked)* — Roadmap compacted to 5-card horizontal strip.
- **D-6** *(locked)* — Timeline inline addendum to roadmap.
- **D-7** *(locked)* — Worked examples as 3 mini-sections in one
  container with rail layout.
- **D-8** *(locked)* — Output schema as clean rail-row table.
- **D-9** *(locked)* — Drop "Related Resources" 4-card grid.
- **D-10** *(locked)* — Drop newsletter.
- **D-11** *(pending)* — Banded rhythm (TBD which sections band).

---

## 7. [DRAFT] copy inventory (sign-off needed before ship)

| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[DRAFT]` | Hero side-visual concept choice (A/B/C) |
| S2  | `[NEW-DRAFT]` | Section heading "Why AI-readiness matters." (or restore old "Why AI-Readiness Matters Now.") |
| S2  | `[NEW-DRAFT]` | Trimmed 1-sentence intro |
| S2  | `[OLD verbatim]` | 3 rail-row bodies (Problem · Cost · Opportunity) |

All other body copy is `[NEW-current]` kept verbatim from the existing
page (7-dim content, interpretation rubric, roadmap, worked examples,
output schema, CTA body).

---

## 8. Build notes / dependencies

- Page-local CSS prefix: keep existing `air-` from the current page.
- Reuse rail-row pattern from `CaseStudyPageLayout`/`/company/our-process`.
  The `.cs-rail-row*` classes are global from CaseStudyPageLayout but not
  loaded on `/resources/ai-readiness` (different layout). Either:
  (a) define `.air-rail-row*` page-locally (recommended — same pattern,
  scoped name), or (b) refactor `.cs-rail-row*` to a truly global layout
  primitive in `global.css`. Going with (a) for this page.
- Hero SVG: viewBox 480×220, follows `/company/our-process` aside SVG
  sizing exactly. IntersectionObserver scroll-reveal.
- Drop the `ScorecardDimensionCard` import once the hero side visual
  replaces it (component may still be used elsewhere — check first).
