# Extense Site Reframe 2026 — Master Planning Doc

Page-by-page reframe of **extense.co** to lead with **solutions and outcomes**,
pulling solution/benefit-led messaging forward from the old site
(**ex-tense.co**) while keeping the new site's design system and document-grade
voice.

The merge in one line: **old site's solution-orientation + new site's design +
locked document-grade voice.**

---

## The unlock (delta to the design brief)

Approved this session. To be folded into `EXTENSE_DESIGN_BRIEF.md` as a formal
amendment **after the homepage validates the approach** (not before).

**UNLOCKED**
- Positioning / ordering: lead-with-solutions, outcome-first sequencing.
- Permission to **cut or compress problem-education** sections (the buyer is
  already problem-aware and actively shopping for a solution).

**STAYS LOCKED (unchanged)**
- Voice: no aspiration/marketing verbs (`transform`, `empower`, `enable`,
  `harness`). Solution-led, not aspiration-led.
- Design tokens, brand colors, hairline construction, mono labels.
- 5-phase methodology (Discovery → Architecture → Migration → Implementation →
  Enablement).
- Three-markets framing (Technical Publishing / Content Technology / Intelligent
  Content → ITCS).
- Canonical thesis: "documentation has to be right."
- Prohibited mentions: no woman-owned / minority-owned / SBA 8(a) / WOSB / MBE /
  sole-source eligibility (Extense holds none).
- No newsletter. No client logos outside the homepage marquee.

---

## Voice principle (the thing that's easy to get wrong)

Solution-led + benefit-led **in the document-grade voice**: lead with named
solutions and measurable outcomes; let the benefit land through **specificity
and numbers**, not adjectives or promises. Reads like a capability statement,
not ad copy.

- **Good (active, operational):** migrate, cut, recover, ship, engineer,
  implement, consolidate.
- **Banned (aspiration/marketing):** transform, empower, enable, harness,
  unlock, revolutionize.
- Benefit through specificity: "Cut translation spend 72%" beats "transform
  your localization."

"Document-grade" ≠ "informational / passive." The current site's flaw is
passivity, not document-grade-ness. The fix is **active, specific,
outcome-first** — all inside the locked voice.

---

## Copy source tags (used in every wireframe)

Every line of copy in a wireframe is tagged so approval is trivial:

- `[OLD]` — pulled forward verbatim (or near-verbatim) from ex-tense.co.
- `[NEW]` — kept as-is from the current extense.co.
- `[DRAFT]` — net-new copy proposed by Claude. **Requires explicit approval.**

Default is reuse (`[OLD]` / `[NEW]`). `[DRAFT]` is the exception that gets
signed off. Per direction: most body copy stays `[NEW]`; solution/benefit-led
messaging is pulled from `[OLD]`.

---

## Per-page doc template

Each page (or shared template) gets one doc following this shape:

1. **Page job** — URL, primary reader, the single thing the page must do.
2. **Inventory: old site** — section-by-section of the old page.
3. **Inventory: new site** — section-by-section of the current page.
4. **Mapping decisions** — pull-forward / keep / cut, each with rationale.
5. **Wireframe** — section-by-section: purpose, drafted copy (source-tagged),
   component, inline rationale.
6. **Decision log** — consolidated page-level calls + the "why."

Most subpages are templated, so the *unique* doc count is far below the ~25
page count: the 4 capabilities subpages share `PillarPageLayout`, the 6
industries subpages share `IndustryPageLayout`, etc. Those become one
template wireframe + a content-variant table, not N independent docs.

---

## Status tracker

| Page / template        | Inventory | Mapping  | Wireframe | Reviewed | Implemented | Doc |
|------------------------|-----------|----------|-----------|----------|-------------|-----|
| Home                   | done      | done     | done      | pending  | –           | [home.md](home.md) |
| Capabilities (index)   | –         | –        | –         | –        | –           | – |
| Solutions (index)      | done      | done     | done      | pending  | –           | [solutions.md](solutions.md) |
| Services (index)       | done      | done     | done      | done     | done        | [services.md](services.md) |
| Industries (index)     | –         | –        | –         | –        | –           | – |
| Resources (index)      | –         | –        | –         | –        | –           | – |
| Company                | –         | –        | –         | –        | –           | – |
| Contact                | –         | –        | –         | –        | –           | – |
| Industry template (×6) | –         | –        | –         | –        | –           | – |
| Service template (×3)  | –         | –        | –         | –        | –           | – |
| Solution › Tech Docs   | done      | done     | done      | done     | done (uncommitted) | [technical-docs-and-publishing.md](technical-docs-and-publishing.md) |
| Solution › Migration   | done      | done     | done      | done     | done (uncommitted) | [content-migration.md](content-migration.md) |
| Solution › XML Interop  | done     | done     | done      | done     | done (uncommitted) | [xml-data-interoperability.md](xml-data-interoperability.md) |
| Solution › AI-Ready    | done      | done     | done      | done     | done        | [ai-ready-content.md](ai-ready-content.md) |
| Service › Tech Writing | done      | done     | done      | done     | done        | [technical-writing-content-development.md](technical-writing-content-development.md) |
| Service › Content Strat| done      | done     | done      | done     | done        | [structured-content-strategy.md](structured-content-strategy.md) |
| Service › DITA Eng     | done      | done     | done      | done     | done        | [dita-engineering.md](dita-engineering.md) |

> The 4 `/solutions/*` sub-pages are **bespoke** (each has its own components —
> `TechDocs*`, etc.), so they get one doc each, not a shared template. (The
> retired `/capabilities` pillar pages were the templated set.)

---

## Workflow per page

inventory → mapping → wireframe → **review / iterate** → implement.

Implementation follows the standard repo workflow: edit on `redesign-2026`,
`npm run build`, commit, push, fast-forward `main`. One page at a time;
nothing implemented until its wireframe is signed off.
