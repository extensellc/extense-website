# Our Work & Case Studies (Company sub-page) — Reframe Plan

> Status: **wireframe pending sign-off.** Combines two old ex-tense.co
> pages — "Our Work" (3 anonymized outcome cards) and "Case Studies"
> (3 detailed named case studies + impact metrics + methodology
> disclosure + cross-links + CTA) — into one Company sub-page. The 3
> detailed case studies **already exist as sub-pages** built on
> `CaseStudyPageLayout`, currently at `/resources/case-studies/<slug>`;
> they will move under `/company/our-work-and-case-studies/<slug>` for
> IA consistency (per owner — Option B). Bespoke build (page-local CSS,
> prefix `owcs-`), reusing the shared atoms.
>
> **Locked this session (2026-06-03):** H1 = [OLD-merge] "Measurable
> Results, Real Deliverables"; detail-page move from `/resources/
> case-studies/<slug>` to `/company/our-work-and-case-studies/<slug>`
> with vercel.json redirects.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md);
> model = [insurance.md](insurance.md) (faithful structural port).

---

## 1. Page job
- **URL:** `/company/our-work-and-case-studies` (new combined index)
- **Sub-pages:** `/company/our-work-and-case-studies/<slug>` (3 detail
  pages, moved from `/resources/case-studies/<slug>`)
- **Primary reader:** procurement / evaluator / champion at a
  prospective client, evaluating credibility through demonstrated
  outcomes and inspectable artifacts.
- **The one job:** prove credibility on two fronts — anonymized
  outcomes across client work (Manufacturing OEM / Medical Device /
  FinTech) AND deep technical artifacts from Extense-internal projects
  (DITA Training Curriculum / AI-Ready Pipeline / Publishing
  Automation). Then convert.

---

## 2. Inventory — OLD pages (ex-tense.co)
**Two separate pages.** Combined here for the first time.

### OLD: Our Work
1. **Hero** — H1 "Our Work" + subdeck "Proven results for global
   enterprises."
2. **Measurable Results for Global Enterprises** — intro + 3 outcome
   cards (Global Heavy Equipment OEM / Class III Medical Device
   Manufacturer / FinTech Startup — API Documentation), each with
   industry-tag eyebrow + headline result + 2 key stats.
3. Newsletter sign-up (dropped — newsletter banned per locked rules).

### OLD: Case Studies
1. **Hero** — H1 "Case Studies" + subdeck "Real projects. Real
   deliverables. Every metric backed by artifacts you can inspect."
2. **Measured Impact** — 4-stat band (`2 → 9`, `0 → 100%`, `350%`,
   `−70%`) + intro line.
3. **What These Numbers Mean Downstream** — 3 cards (Translation &
   Localization · Chatbot & AI Retrieval · Publishing & Maintenance).
4. **How We Calculate AI-Readiness** — methodology paragraph (10-point
   scoring across topic typing, metadata, section addressability,
   vocabulary, semantic markup, reuse, output pipeline).
5. **Case Study 1: Enterprise DITA Training Curriculum** — full
   Challenge/Approach + 4 stats (76 topics / 10 parts / 12 labs / 218
   pages) + "What We Delivered" 3 cards + 10-part curriculum coverage
   strip.
6. **Case Study 2: AI-Ready Content Pipeline** — full Challenge/
   Approach + Before & After comparison + 3 stats (100% metadata · 5
   facets · 150+ section IDs) + "Tools Built" 2 cards + Controlled
   Vocabulary detail.
7. **Case Study 3: Custom DITA-OT Publishing Automation** — full
   Challenge/Approach + Plugin Architecture 2 cards + Build Pipeline 3
   cards + 4 stats (4 formats / 2 plugins / 0 manual steps / 1 source).
8. **Downstream Savings Projection** — 4-stat band (40-60% translation
   savings · 3-5x faster releases · 85%+ chatbot precision · ~70% less
   rework) + "A Note on These Numbers" methodology caveat.
9. **Have a Similar Challenge?** — dark navy mid-page CTA banner.
10. **Continue Exploring** — 3-card cross-link (DITA Engineering ·
    Publishing Engineering · Content Migration).

## 3. Inventory — NEW site (current)
- **`/company/our-work-and-case-studies`** — stub page (Hero only,
  "Coming soon" subdeck), created last session.
- **`/resources/case-studies/`** — substantive index page + 3 detail
  sub-pages on `CaseStudyPageLayout` (`ai-content-pipeline`,
  `dita-training-curriculum`, `publishing-automation`). The detail
  pages already carry the full Challenge / Approach / Stats / What We
  Delivered content from the screenshots — no rebuild needed, just a
  move.
- Currently orphaned from nav after the IA refresh (since "Case
  Studies" left the Resources dropdown).

---

## 4. Mapping decisions
- **D-1 — H1 = [OLD-merge-locked] "Measurable Results, Real
  Deliverables".** Owner-chosen. Punchier than the menu-label match;
  carries the page's load-bearing claim in the hero.
- **D-2 — Hero subdeck = [DRAFT-merge]** combining both old subdecks
  into one sentence:
  > "Proven results for global enterprises — real projects, real
  > deliverables, every metric backed by artifacts you can inspect."

  Old "Our Work" subdeck "Proven results for global enterprises."
  combined with old "Case Studies" subdeck "Real projects. Real
  deliverables. Every metric backed by artifacts you can inspect."
- **D-3 — Detail-page move (Option B, locked):** move the 3 case-study
  detail pages from `/resources/case-studies/<slug>` to `/company/
  our-work-and-case-studies/<slug>`. Add 301 redirects in `vercel.json`
  for the old URLs. `CaseStudyPageLayout` import paths stay the same
  (both old and new are 3 levels deep under `src/pages/`).
- **D-4 — Drop full inline case-study detail from the index.** Old
  Case Studies page rendered all 3 cases inline at full detail
  (very long page). New index renders **summary cards** per case study,
  each linking to the dedicated detail page. Detail pages own the full
  Challenge/Approach/Stats/Deliverables content.
- **D-5 — Add "our-work-and-case-studies" variant to
  `SectionSiblings`** for cross-navigation between the 3 detail pages.
  Back-link "← Our Work & Case Studies" → `/company/
  our-work-and-case-studies`. 3 sibling items.
- **D-6 — Drop newsletter sign-up** (Stay Connected with Extense) per
  locked rule (no newsletter site-wide).
- **D-7 — Section order:** outcome cards (specific, recognizable) →
  case-study summary cards (deep examples) → aggregate impact (big
  picture) → downstream savings projection (forward-looking) → cross-
  links → CTA. Concrete → deep → big-picture → projection → next
  actions.
- **D-8 — Banded-section rhythm:** S3 plain · S4 band · S5 plain · S6
  band · S7 plain.
- **D-9 — Retire `/resources/case-studies/index.astro`** (replaced by
  the new combined index at `/company/our-work-and-case-studies/`).
  Add a redirect for `/resources/case-studies/` → `/company/
  our-work-and-case-studies/`.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal, no side visual)
- **H1** `[OLD-merge-locked]`: "Measurable Results, Real Deliverables"
- **Subdeck** `[DRAFT-merge]`: "Proven results for global enterprises
  — real projects, real deliverables, every metric backed by artifacts
  you can inspect."
- `subdeckMaxWidth="520px"`.
- No side visual — text-only hero (matches /company/faqs and other
  evidence-heavy Company pages).

### S2 — (No `SectionSiblings` on the index) — Company sub-pages don't currently use a unified sibling nav. Detail pages get their own.

### S3 — Measurable Results for Global Enterprises `[OLD]` · 3-card outcome grid
- **Heading** `[OLD]`: "Measurable Results for Global Enterprises"
- **Intro** `[OLD]`: "We measure success in dollars saved, hours
  recovered, and compliance risks eliminated. Here's a sample of
  recent engagements."
- **3 cards** `[OLD]` (mono uppercase industry-tag eyebrow + title +
  body + 2 key stats; document-grade hairline cards):
  1. eyebrow "MANUFACTURING" · **Global Heavy Equipment OEM** —
     body, stats `60%` Cost Reduction / `25K+` Pages Migrated
  2. eyebrow "MEDICAL DEVICE" · **Class III Medical Device
     Manufacturer** — body, stats `100%` Audit Pass Rate / `30+`
     Markets
  3. eyebrow "FINTECH" · **FinTech Startup — API Documentation** —
     body, stats `0` Doc Lag Days / `CI/CD` Fully Automated
  (Full body copy per screenshots — [OLD] verbatim.)

### S4 — Detailed Case Studies `[OLD + DRAFT-summarized]` · 3 summary cards (banded)
- **Heading** `[DRAFT]`: "Detailed Case Studies"
- **Intro** `[DRAFT]`: "Three Extense-internal projects, each with
  inspectable artifacts and measured outcomes. The summaries below are
  the headline; each links to a dedicated page with the full Challenge
  / Approach / Deliverables breakdown."
- **3 summary cards** (each: title + subtitle + 3-4 sentence summary +
  3 key stats + "Read full case study →" link):
  1. **Enterprise DITA Training Curriculum** — subtitle [OLD]: "76
     topics across a 10-part learning program — authored, enriched,
     and published entirely in DITA." Summary [DRAFT-summarized]:
     distilled from old Case Studies S5 Challenge + Approach.
     Stats [OLD]: `76` DITA topics / `218` PDF pages / `12` hands-on
     labs. Link → `/company/our-work-and-case-studies/dita-training-curriculum`.
  2. **AI-Ready Content Pipeline** — subtitle [OLD]: "Transforming
     unstructured content into machine-readable, chatbot-optimized
     DITA with measurable AI-readiness scoring." Summary
     [DRAFT-summarized]. Stats [OLD]: `100%` metadata coverage / `5`
     classification facets / `150+` section IDs. Link → `/company/
     our-work-and-case-studies/ai-content-pipeline`.
  3. **Custom DITA-OT Publishing Automation** — subtitle [OLD]: "Two
     branded DITA-OT plugins and a multi-format build pipeline
     producing interactive HTML5, print-ready PDF, and PWA-installable
     output from a single source." Summary [DRAFT-summarized]. Stats
     [OLD]: `4` output formats / `2` custom plugins / `0` manual
     steps. Link → `/company/our-work-and-case-studies/publishing-automation`.

### S5 — Measured Impact `[OLD]` · 4-stat band + 3 explanatory cards + methodology sub-block
- **Heading** `[OLD]`: "Measured Impact"
- **Intro** `[OLD]`: "Aggregate improvements across the content
  transformation — from raw source to AI-ready, multi-format output."
- **4-stat band** `[OLD]`:
  - `2 → 9` — AI-Readiness Score (out of 10)
  - `0 → 100%` — Metadata Coverage
  - `350%` — More Reusable Content
  - `−70%` — Less Rework on Updates
- **Sub-heading** `[OLD]`: "What These Numbers Mean Downstream"
- **3 cards** `[OLD]` (Translation & Localization · Chatbot & AI
  Retrieval · Publishing & Maintenance) — full body per screenshots.
- **"How We Calculate AI-Readiness" sub-block** `[OLD]` — methodology
  paragraph with bolded 7 scoring factors.

### S6 — Downstream Savings Projection `[OLD]` · 4-stat band + caveat (banded)
- **Heading** `[OLD]`: "Downstream Savings Projection"
- **Intro** `[OLD]`: "Conservative estimates based on industry
  benchmarks for organizations managing 500+ topics across multiple
  languages and channels."
- **4-stat band** `[OLD]` (themed differently — these are
  forward-looking projections, not measured results — render with a
  visual marker like a blue/orange split or "PROJECTION" caption).
  Each stat has a short body line beneath the value+label (also `[OLD]`
  — pulled forward from old page, originally missed in the port and
  added 2026-06-03):
  - `40-60%` — Translation Savings — "Content reuse at scale eliminates
    re-translation of unchanged segments across language variants."
  - `3-5x` — Faster Release Cycles — "Single-source automation cuts
    multi-format publishing from weeks to days or hours."
  - `85%+` — Chatbot Precision — "Metadata-filtered retrieval with
    intent routing replaces keyword guessing with precise answer
    delivery."
  - `~70%` — Less Update Rework — "Fix once, propagate everywhere. No
    more hunting through copies across documents and formats."
- **"A Note on These Numbers" caveat** `[OLD]` — methodology
  disclosure paragraph (industry benchmarks from OASIS / Gartner /
  CIDM; measurement-before-projection framing).

### S7 — Continue Exploring `[OLD]` · 3-card cross-link
- **Heading** `[OLD]`: "Continue Exploring"
- **3 cards** `[OLD]`:
  - SERVICE · **DITA Engineering** → `/services/dita-engineering`
  - SERVICE · **Publishing Engineering** → `/services/publishing-engineering`
  - SOLUTION · **Content Migration** → `/solutions/content-migration`

### S8 — CTA · `CTAModule` (audience="general")
- **Heading** `[OLD]`: "Have a Similar Challenge?"
- **Body** `[OLD]`: "Whether you're building a training program,
  preparing content for AI, or automating multi-format publishing —
  we've done it and can show you the artifacts."
- **Button label** `[OLD]`: "Schedule a Conversation"

---

## 6. Detail-page move plan (D-3)
- **Move** (preserving git history via `git mv` where possible):
  - `src/pages/resources/case-studies/ai-content-pipeline.astro` →
    `src/pages/company/our-work-and-case-studies/ai-content-pipeline.astro`
  - `src/pages/resources/case-studies/dita-training-curriculum.astro` →
    `src/pages/company/our-work-and-case-studies/dita-training-curriculum.astro`
  - `src/pages/resources/case-studies/publishing-automation.astro` →
    `src/pages/company/our-work-and-case-studies/publishing-automation.astro`
- **Delete** (replaced by the new combined index):
  - `src/pages/resources/case-studies/index.astro`
  - `src/pages/company/our-work-and-case-studies.astro` (the stub
    from last session — replaced by the new
    `src/pages/company/our-work-and-case-studies/index.astro`)
- **Update** `CaseStudyPageLayout.astro` if it carries hardcoded
  back-links or sibling references pointing to `/resources/
  case-studies` — point them at `/company/our-work-and-case-studies`.
- **Update** `SectionSiblings.astro` — add
  `"our-work-and-case-studies"` variant with the 3 case-study items
  and back-link to `/company/our-work-and-case-studies`. Retire the
  prior case-studies variant if one exists.
- **vercel.json redirects** (301, host-agnostic):
  - `/resources/case-studies` → `/company/our-work-and-case-studies`
  - `/resources/case-studies/ai-content-pipeline` →
    `/company/our-work-and-case-studies/ai-content-pipeline`
  - `/resources/case-studies/dita-training-curriculum` →
    `/company/our-work-and-case-studies/dita-training-curriculum`
  - `/resources/case-studies/publishing-automation` →
    `/company/our-work-and-case-studies/publishing-automation`
- **Cross-references in repo** to `/resources/case-studies` —
  search-replace to `/company/our-work-and-case-studies`. Likely
  candidates: any "Continue Exploring" / related-card link on
  industry/solution/service pages that point to case studies; the
  CaseStudyRecordCard component (if it has a hardcoded link); the
  /resources index page (if it lists case-studies as a child).

---

## 7. Decision log
- **D-1** *(locked)* — H1 = [OLD-merge] "Measurable Results, Real
  Deliverables".
- **D-2** *(locked)* — Hero subdeck = [DRAFT-merge] one-sentence
  combination of both old subdecks.
- **D-3** *(locked, Option B)* — Move detail pages to
  `/company/our-work-and-case-studies/<slug>`; redirects in
  vercel.json.
- **D-4** *(locked)* — Index renders summary cards per case study, not
  full inline detail. Detail content lives on the dedicated pages.
- **D-5** *(locked)* — Add "our-work-and-case-studies" variant to
  `SectionSiblings`.
- **D-6** *(locked)* — Drop newsletter sign-up.
- **D-7** *(locked)* — Section order: outcomes → case studies →
  measured impact → savings projection → cross-links → CTA.
- **D-8** *(locked)* — Banded rhythm S3 plain · S4 band · S5 plain ·
  S6 band · S7 plain.
- **D-9** *(locked)* — Retire `/resources/case-studies/index.astro`.

---

## 8. [DRAFT] copy inventory (sign-off needed before ship)
| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[OLD-merge-locked]` | H1 |
| S1  | `[DRAFT-merge]` | Subdeck (one-sentence combination) |
| S4  | `[DRAFT]` | Section heading "Detailed Case Studies" + intro paragraph |
| S4  | `[DRAFT-summarized]` | 3 case-study summary body paragraphs (3-4 sentences each, distilled from existing detail-page Challenge + Approach) |

All other body copy + stats + cards in S3, S5, S6, S7, S8 are `[OLD]`
verbatim from the old pages.
