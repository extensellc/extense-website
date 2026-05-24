# Solutions (main page) — Reframe Plan

> Status: inventory **done**, mapping **done**, wireframe **done** — awaiting
> review. Tags: `[OLD]` (ex-tense.co) / `[NEW]` (current extense.co) / `[DRAFT]`
> (net-new, approved where noted). Conventions in [README.md](README.md).
>
> **Key finding:** the current new `/solutions` is *already* a clean,
> cognitive-flow page (no Ops Stack repeat, no placeholder logos, no
> newsletter — the old site's problems are already absent). So this reframe is
> light. Direction A–F (agreed) was framed against the *old* site; several
> items (C logos, E newsletter) are already satisfied.

---

## FINAL STRUCTURE (as built — supersedes the §5 proposal below)

After review, the page was built to the **old-site order** (framing before the
cards), not the "lead with solutions" reorder §5 first proposed:

1. **Hero** — `SolutionsHero` (kept): "Content compounds. So does the cost of
   getting it wrong." + content-pipeline visual.
2. **Solving the Content Problem at Scale** — `SolutionsProblem` (repurposed):
   old-site intro (*"…Our solutions **turn** unstructured, siloed information
   into reusable, standards-based, automatically publishable knowledge."* —
   "transform"→"turn") **+ the Assess → Architect → Implement → Optimize strip**
   (4 hairline step cards, amber arrows).
3. **Our Solutions** — `SolutionsAreas` (edited): the 4 cards with the locked
   old-site card copy + full old-site names. **Pull-quote hooks dropped.**
   - Technical Documentation & Publishing `[OLD]`
   - Content Migration & Modernization `[OLD, "convert"]`
   - XML Data Interoperability `[OLD]`
   - AI-Ready Content `[DRAFT, approved]`
4. **CTA** — `CTAModule` (kept).

**Dropped:** the standalone "Documentation is a system, not a deliverable"
principle (`SolutionsApproach.astro` deleted — it restated the thesis the hero +
framing already carry); the new-site "The problem at scale" 3-item diagnosis
(replaced by the framing block); the pull-quote hooks.

**Decisions:** D-2 keep the 4-step strip (in the framing section); D-3 keep the
"Solving…" copy, rename from "The problem at scale"; D-4 drop hooks + rename
"Where the principle becomes practice" → "Our Solutions"; old-site order
(framing → cards), reversing earlier A. Voice: "transform"→"convert" (Migration
card) / "turn" (intro).

**Build:** repurposed `SolutionsProblem`, edited `SolutionsAreas`, deleted
`SolutionsApproach`, removed it from `index.astro`. No new components.

---

## 1. Page job

- **URL:** `/solutions`
- **Primary reader:** problem-aware, shopping buyer who entered by **problem**
  ("my migration is stuck," "my content can't feed a RAG pipeline") rather than
  by service offering.
- **The one job:** show the buyer **the solutions to their content problem**
  fast, route them to the specific solution sub-page, and convert. The "why"
  is already settled — don't re-lecture the problem.

---

## 2. Inventory — OLD site (ex-tense.co/solutions)

1. Hero — "Our Solutions" / "Comprehensive strategies for your content
   engineering challenges" (dark navy).
2. The Extense Content Ops Stack (Strategy/Engineering/Automation/Delivery) —
   *same block as the homepage.*
3. "Solving the Content Problem at Scale" + intro ("…Our solutions **transform**
   unstructured, siloed information…") + process row **Assess → Architect →
   Implement → Optimize**.
4. 4 solution cards (Technical Documentation & Publishing, Content Migration &
   Modernization, XML Data Interoperability, AI-Ready Content) + "Explore" links.
5. "Not Sure Where to Start?" → Content Health Check CTA.
6. "Trusted by Engineering Leaders Worldwide" + 6 **placeholder** logos
   (RailConnect, DefenseCore, MediTech Devices, GlobalFinance, AutoSystems,
   AeroJet Dynamics).
7. Newsletter.
8. Footer.

## 3. Inventory — NEW site (current extense.co/solutions)

1. **SolutionsHero** — kicker `MODEL · MIGRATE · INTEGRATE · RETRIEVE`; H1
   "Content compounds. So does the cost of getting it wrong."; asset/liability
   body; animated content-pipeline visual.
2. **SolutionsProblem** — "The problem at scale." + 3 diagnostic items (more
   products/jurisdictions/languages; six output channels; errata that never
   catch up).
3. **SolutionsApproach** — eyebrow "The approach"; principle "Documentation is
   a *system*, not a deliverable."; elaboration ("Treat content like code…").
4. **SolutionsAreas** — "Where the principle becomes practice." + 4 editorial
   blocks: number `01–04` · name · body (new-site copy) · italic pull-quote
   **hook** · Explore link. Per-block scroll reveal.
5. **CTAModule** — Sample Content Assessment.

---

## 4. Mapping decisions

### Keep from NEW `[NEW]`
- `SolutionsHero` (thesis + pipeline visual) — strong, on-brand. Keep as the
  brief orient.
- `SolutionsApproach` principle ("Documentation is a system, not a deliverable")
  — keep, but **reposition after the solutions** (see D-2).
- `SolutionsAreas` structure (number · name · body · hook · link) + its
  per-block reveal animation. Keep the chassis; swap the **body** copy.
- `CTAModule`.
- The pull-quote **hooks** (`[NEW]`) — keep; they add curiosity. Minor tuning so
  they still match the swapped body (see D-4).

### Swap in `[OLD]` (the locked card copy)
- The 4 areas' **body** copy → the old-site card copy you supplied (Migration
  card: "transform"→"convert"; AI-Ready: the approved `[DRAFT]`).
- Area **names** → the old-site full names (Technical Documentation &
  Publishing, Content Migration & Modernization, …).

### Cut
- **SolutionsProblem** ("The problem at scale") — problem-education for a
  problem-aware buyer; the hero already carries the asset/liability frame.
  (D-3.)
- Everything the old site had that the new site already lacks — Ops Stack
  repeat, placeholder logos, newsletter — N/A (already absent).

---

## 5. Wireframe

Order follows the page's mini cognitive-flow: **orient → solutions (lead) →
principle → convert.**

### Section 1 — Hero  · `SolutionsHero` (keep) · `[NEW]`
- Kicker `[NEW]`: `MODEL · MIGRATE · INTEGRATE · RETRIEVE`
- H1 `[NEW]`: "Content compounds. So does the cost of getting it wrong."
- Body `[NEW]`: asset/liability paragraph (unchanged).
- Visual `[NEW]`: content-pipeline diagram (unchanged).
- *Rationale:* brief orient + the asset/liability framing; the pipeline visual
  previews model→migrate→integrate→retrieve. Strong as-is; no change.

### Section 2 — Solution Areas (4)  · `SolutionsAreas` (reused, body swapped) · `[OLD]` copy
- **Heading** `[DRAFT]`: "What we solve." — *(replaces "Where the principle
  becomes practice," which presumed the Approach came first; now Areas lead).*
- **Sub-deck** `[DRAFT]`: "Four areas where engineered content replaces a
  hand-authored, copy-and-rebuild cycle."
- **01 — Technical Documentation & Publishing** `[OLD]`
  "Modernize your authoring and publishing workflows. We build single-source
  pipelines that produce pixel-perfect PDF, responsive HTML5, EPUB, and
  context-sensitive help from the same DITA map — eliminating the
  'copy-paste-reformat' cycle that costs enterprises thousands of hours per
  year." · hook `[NEW]` (keep) · → `/solutions/technical-docs-and-publishing`
- **02 — Content Migration & Modernization** `[OLD, "convert"]`
  "Legacy Word, FrameMaker, and InDesign content doesn't have to be rewritten
  by hand. Our migration engine combines automated conversion scripts with
  expert manual refinement to convert unstructured documents into clean,
  validated DITA XML — typically at 10x the speed of manual conversion." ·
  hook `[NEW]` · → `/solutions/content-migration`
- **03 — XML Data Interoperability** `[OLD]`
  "Your content must flow between systems: CCMS to PIM, ERP to Portal, CMS to
  Translation Memory. We design XSLT/XQuery transformation layers, REST/GraphQL
  APIs, and OData connectors that make your XML data a first-class citizen in
  your enterprise architecture." · hook `[NEW]` ·
  → `/solutions/xml-data-interoperability`
- **04 — AI-Ready Content** `[DRAFT, approved]`
  "Your content is becoming an AI retrieval source — whether it was engineered
  for that or not. We structure it for RAG pipelines: semantic chunking,
  retrieval metadata, and embedding-ready markup, validated so answers stay
  grounded in the source — the difference between 85% retrieval precision and a
  system that confidently hallucinates." · hook `[NEW]` ·
  → `/solutions/ai-ready-content`
- *Rationale:* the buyer is here for solutions → lead with them. Keeps the
  editorial number + pull-quote treatment and the per-block scroll reveal.

### Section 3 — Approach principle  · `SolutionsApproach` (keep, repositioned) · `[NEW]`
- Eyebrow "The approach" · principle "Documentation is a *system*, not a
  deliverable." · elaboration ("Treat content like code…").
- *Rationale:* a tight one-line engineering principle as a coda before
  converting — not a method lecture, so it doesn't violate "lead with
  solutions." Repositioned from before the areas to after them. (D-2.)

### Section 4 — CTA  · `CTAModule` (keep) · `[NEW]`
- Sample Content Assessment (existing body).

### Removed
- **SolutionsProblem** ("The problem at scale"). (D-3.)

---

## 6. Decision log

- **A — Lead with solutions.** Reordered so the 4 areas sit right after the
  hero (above the approach principle). *(Agreed.)*
- **D-2 — Approach framing.** Direction B (from the old site) said keep
  **Assess→Architect→Implement→Optimize**. But the new site already has a
  tighter approach element — **"Documentation is a system, not a deliverable."**
  My rec: **keep the new principle**, drop the old 4-step strip (it would add a
  third process diagram alongside the homepage's Ops Stack + Lifecycle).
  *Confirm: new principle (rec) vs. old Assess→Optimize strip?*
- **D-3 — Cut SolutionsProblem.** Recommend cut (problem-education; the hero
  frames the stakes already). *Confirm: cut (rec) / compress to one line / keep?*
- **D-4 — Pull-quote hooks.** Keep the `[NEW]` hooks; they still broadly match
  the swapped body. Minor wording tune may be wanted on #1 (translation-cost
  hook vs. the output-format body). *Keep / drop / tune?*
- **C, E — logos / newsletter:** already absent on the new page. No action.
- **D (voice):** "transform"→"convert" handled in the card copy; hero/areas are
  already clean.
- **F — Solutions ↔ Services:** each area links to its `/solutions/*` sub-page;
  the sub-pages cross-link to the relevant `/services` (already repointed in the
  capabilities-cut work).

---

## 7. Build inventory

| Section | Component | Action |
|---|---|---|
| Hero | `SolutionsHero` | Keep (no change) |
| Solution Areas | `SolutionsAreas` | **Edit** — swap 4 body strings + names + heading; reorder above Approach |
| Approach | `SolutionsApproach` | Keep; **reposition** after Areas |
| Problem | `SolutionsProblem` | **Remove** from the page (component can stay unused or be deleted) |
| CTA | `CTAModule` | Keep |
| Page order | `solutions/index.astro` | **Edit** — Hero → Areas → Approach → CTA |

Net: 1 content edit (`SolutionsAreas`), 1 reorder (`index.astro`), 1 section
removed. No new components.

---

## 8. Open items / next

- The **4 sub-pages** (`/solutions/technical-docs-and-publishing`,
  `/content-migration`, `/xml-data-interoperability`, `/ai-ready-content`) are
  the next step: crawl the old sub-pages, then wireframe. Note the old AI-Ready
  lived at root (`/ai-ready.html`); it maps to `/solutions/ai-ready-content`.
- Sub-pages should cross-link to the relevant `/services` (per F).
