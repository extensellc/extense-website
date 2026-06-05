# Migration Playbook (Resources sub-page) — Redesign Plan

> Status: **shipped on staging** (retroactive wireframe doc). The
> redesign happened in two passes:
>   (a) Hero swap — replaced the static `MigrationLifecycleCard` side
>       panel with the document-grade **Option C** "recovery before /
>       after" SVG, and combined OLD + NEW hero copy.
>   (b) Body restructure — split the single 5-discipline section into
>       **Phase 1: Analysis & Strategy** and **Phase 2: Conversion &
>       Enrichment**, and inserted the **Migration Lifecycle** 5-card
>       strip between Phase 1 and Source Formats, restoring the old
>       page's narrative arc.
>
> Live as of commit `ede84f3`. A third pass (c) added the **practice
> stat band** (2M+ / 13 / 4) after the framing prose — see D-10 / S2.5,
> resolving pending item #1.
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md).

---

## 1. Page job
- **URL:** `/resources/migration-playbook`
- **Primary reader:** documentation lead, content engineering manager,
  or RFP team scoping a migration from Word / FrameMaker / MadCap /
  RoboHelp / AuthorIT / other legacy formats into typed DITA. Often
  arrived from search ("how to migrate to DITA"), Solutions →
  Content Migration, or a procurement team comparing vendors.
- **The one job:** convince the reader that migration is recovery (not
  transcription) by showing the disciplines, the lifecycle, the source
  formats handled, and the field rules — backed by the practice (the
  old page leaned on "2M+ pages" credibility). Convert to a sample
  conversion analysis at the end.

---

## 2. Inventory — OLD page (extense.co/migration-playbook, dated 2026-06-05)

1. **Hero** — dark navy banner
   - H1: "The Ultimate DITA Migration Playbook"
   - Subdeck: "Don't just copy-paste. Transform. A step-by-step guide to
     moving from Word/Markdown to DITA XML."
   - Breadcrumb: Home › Resources › DITA Migration Playbook
2. **Phase 1: Analysis & Strategy** — centered title with green
   underline + intro: "Before you convert a single file, you must
   understand your current content estate. 'Garbage in, Structured
   Garbage out.'" Three colored-bar steps (red/amber/blue) for Content
   Audit / Information Architecture / Pilot Migration.
3. **The Migration Lifecycle** — heading + 5-card horizontal flow with
   green arrows: Audit (Delete ROT) → Map (Word Styles → DITA) →
   Convert (Scripted Transformation) → Refine (Manual Cleanup) → Publish
   (Test Outputs).
4. **Formats Covered in This Playbook** — heading + pill-style format
   tags: Word · FrameMaker · InDesign · RoboHelp · MadCap Flare ·
   DocBook · HTML · Markdown · AuthorIT · Confluence · SGML · Excel ·
   PDF (OCR).
5. **Phase 2: Conversion & Enrichment** — centered title with green
   underline (no intro). Two colored-bar steps for Batch Conversion /
   Deduplication & Enrichment.
6. **Pro Tips from 2M+ Pages of Migration Experience** — light box with
   4 bullets (same content as the current page's Field Rules).
7. **Free Content Health Check** — dark navy CTA banner with "Submit a
   20-page sample" framing.
8. **Related Resources** — 3-card grid (Publishing Automation Guide ·
   AI Content Readiness Guide · Content Migration & Modernization).
9. Stay Connected newsletter (banned per locked rules).

## 3. Inventory — NEW site (state going into this redesign)

Before the redesign, the page already had:
1. Hero (universal) with H1 "Migration is recovery, not transcription."
   + framing subdeck, and a static `MigrationLifecycleCard` side panel
   (text-only 5-stage list).
2. Framing prose — "Why migration is recovery." (3 paragraphs).
3. The five disciplines (single flat list — 01 Content audit, 02
   Information architecture, 03 Pilot migration, 04 Batch conversion,
   05 Deduplication & enrichment).
4. Source formats covered (13 mono-style format names).
5. Field rules from the practice (4 horizontal-row rules — same content
   as old page's Pro Tips, in document-grade voice).
6. CTAModule (shared general).

**Strengths to preserve:** the discipline content (more detailed than
old), the field rules, the source formats, the document-grade aesthetic.
**Weaknesses to fix:** the `MigrationLifecycleCard` static panel wasn't
visually distinctive (just text in a card); the 5-discipline flat list
lost the old page's 2-phase narrative arc; the lifecycle row that gave
the old page a clear visual breakpoint was buried inside the hero.

---

## 4. Mapping decisions

- **D-1 — Hero copy = combined OLD + NEW.** H1 reverts to the OLD page's
  "The Ultimate DITA Migration Playbook" (search-friendly, genre-
  appropriate). Subdeck combines OLD + NEW: opens with OLD "Don't just
  copy-paste — transform" + OLD format list, folds in NEW thesis
  ("Migration is recovery, not transcription"), closes with NEW
  rationale ("the disciplines, the lifecycle, and the field rules
  drawn from the practice"). Same pattern as `/resources/ai-readiness`.
- **D-2 — Hero side-visual = Option C "Recovery before / after".** From
  the 3 mocked candidates (A: format fan-in, B: lifecycle strip, C:
  recovery before/after). Picked C because it renders the H1 thesis
  literally: 10 source pages on left with 4 marked ROT and struck-
  through, central amber `↻ extense.recover` chip on a drawn flow
  connector, 6 typed DITA topics on the right. Document-grade idiom
  (corner reg-marks, mono FIG. chrome, amber elements, IntersectionObserver
  `.drawn` scroll-reveal with staggered fade-in + stroke-dasharray draw
  + reduced-motion fallback). FIG. 01 / corpus.recovered / 10 → 6 + 4
  ROT.
- **D-3 — Restore the 2-phase grouping.** Split the single "Five
  disciplines" section into two phased sections, mirroring the old
  page's narrative arc. **Phase 1: Analysis & Strategy** holds
  disciplines 01–03 (Content audit · Information architecture · Pilot
  migration). **Phase 2: Conversion & Enrichment** holds disciplines
  04–05 (Batch conversion · Deduplication & enrichment). Each phase
  gets a mono "Phase 1" / "Phase 2" eyebrow above its H2 and a
  one-sentence intro.
- **D-4 — Add the Migration Lifecycle 5-card strip between Phase 1 and
  Source Formats** — same position as on the old page. Document-grade
  5-card horizontal strip (Audit → Map → Convert → Refine → Publish)
  with amber arrows between cells, hairline-bordered cards, mono
  number + display name + one-line body per card. Same pattern as the
  /company/our-process 5-phase overview strip. Stacks vertically at
  <1024px.
- **D-5 — Drop the static `MigrationLifecycleCard` component usage.**
  Its content (the 5 lifecycle stages) now lives in the public-facing
  Migration Lifecycle strip (D-4). Component file left in place — not
  yet deleted — in case it's used elsewhere (it isn't, but the cleanup
  is a follow-up).
- **D-6 — Keep the shared CTAModule** at the bottom. Drop the OLD
  page's custom "Free Content Health Check" dark navy banner — the
  shared module already carries an equivalent "20-page sample" offer.
  (Could be revisited if a custom CTA per-resource pages becomes
  desirable.)
- **D-7 — Drop the OLD page's "Related Resources" 3-card grid.** The
  TopNav Resources dropdown handles cross-navigation; no need to
  repeat it per page.
- **D-8 — Drop newsletter.** Locked rule.
- **D-9 — Keep AnimatedDivider between sections** (current pattern on
  this page). No banded rhythm yet — sections all sit on plain page
  background.

---

## 5. Wireframe

### S1 — Hero · `Hero` (universal, with SVG side aside)
- **H1** `[OLD]`: "The Ultimate DITA Migration Playbook"
- **Subdeck** `[DRAFT-merge]`: "Don't just copy-paste — transform. A
  practitioner playbook for moving content from unstructured legacy
  formats (Word, FrameMaker, MadCap, RoboHelp, AuthorIT) into typed,
  validated DITA. Migration is recovery, not transcription — the
  disciplines, the lifecycle, and the field rules drawn from the
  practice."
- `subdeckMaxWidth="540px"`.
- **Side visual (D-2):** document-grade SVG `#mp-hero-flow`, viewBox
  520×260. Width: `520px; max-width: 100%` (NOT `width: 100%` — the
  Hero component's `.hero__side` is `flex: 0 0 auto` shrink-to-fit, so
  100% has no definite parent and the SVG falls back to its intrinsic
  ~300px). Page-locked under CSS prefix `.mp-hero-flow`.
  - Left column: 10 source pages, 4 marked ROT (struck-through with
    `stroke-dasharray` draw)
  - Center: amber `↻ extense.recover` chip on a drawn flow connector
  - Right column: 6 typed DITA topics in amber
  - Top chrome: `in :: corpus.recovered`
  - Bottom chrome: `FIG. 01 / corpus.recovered · 10 → 6 + 4 ROT`
  - IntersectionObserver `.drawn` scroll-reveal, staggered fade-in (~14
    elements with cascading delays), reduced-motion fallback.

### S2 — Why migration is recovery `[DRAFT condensed + visual, pass f]`
- **Heading**: "Why migration is recovery."
- **Lead** `[DRAFT]`: "Migration is recovery, not transcription. How a
  migration is approached decides whether the new system inherits the
  old corpus's problems or sheds them." (Replaces the 3 verbose
  paragraphs — owner found them too wordy; the detail moved into the
  visual below.)
- **Visual: Transcription vs Recovery contrast panel** (`.mp-contrast`,
  2-up). Picked from four mocked concepts (A contrast panel / B three-
  fates router SVG / C pull-quote / D compact != band) on the temporary
  `/migration-playbook-mock` route. Concept A chosen — renders the "X,
  not Y" thesis literally and is distinct from the hero's corpus
  before/after.
  - Left card (Transcription / lift-and-shift, muted, gray top border):
    "Copy-paste source content into a new schema." + list (same
    redundancies / broken navigation / ungoverned metadata) + outcome
    "x  Two years on, the CCMS investment hasn't paid off."
  - Right card (Recovery / extense, amber top border): "Lift reusable
    assets; retire ROT; rewrite the rest with intent." + list (typed,
    validated topics / governed metadata / architecture before
    conversion rules) + outcome "v  The architecture pays off."
  - Equal-height cards (outcome line pinned to the bottom via
    margin-top:auto); stacks to one column <768px.
- The dropped 3rd paragraph's "2M+ pages / sectors" credibility is now
  carried by the S2.5 stat band, so removing it is not a loss.

### S2.5 — Practice stat band `[DRAFT, numbers grounded in copy already live]`
- **Purpose:** surface the "2M+ pages" credibility that was buried in the
  framing prose into a visually prominent, document-grade stat band.
  Resolves pending item #1.
- **3 stats** (`container-data`, `.mp-stats`):
  - **2M+** / "Pages migrated" / "to date" — from the framing prose's
    "two million pages of migration work."
  - **13** / "Source formats" / "handled" — from "thirteen named source
    formats" (S5).
  - **4** / "Sectors served" / "Federal · defense · life sciences ·
    commercial" — from "federal, defense, life sciences, and enterprise
    commercial engagements" (framing prose).
- **Treatment:** large display-serif numbers (`clamp(40px, 6vw, 56px)`,
  text-primary) + mono amber-pressed uppercase label + body sub-line.
  Bracketed top/bottom hairlines (`mp-rule`), vertical hairline dividers
  between stats at ≥768px, stacks to one column on mobile.
- **No `.section-band` tint** — kept on plain bg so this pass doesn't
  pre-empt the deferred banded-rhythm decision (pending item #4);
  prominence comes from the type scale. Tint is a one-line toggle.
- **Reveal:** JS-armed (`.mp-stats--armed`) so the band is never hidden
  for no-JS users; IntersectionObserver adds `.in-view` for a staggered
  rise (0/100/200ms), reduced-motion fallback keeps it static-visible.
  Wired alongside `setupMpHero()` in the page's script block.
- **Position:** after S2 (framing prose), before S3 (Phase 1), keeping
  the existing AnimatedDivider rhythm on both sides.

### S3 — Phase 1: Analysis & strategy `[DRAFT, derived from OLD 2-phase grouping]`
- **Eyebrow** `[DRAFT]`: "Phase 1" (mono amber-pressed uppercase)
- **Heading** `[DRAFT]`: "Analysis & strategy."
- **Intro** `[DRAFT]`: "Three disciplines that take you from corpus to
  architecture. Skip them and you migrate dead weight into a new
  system."
- **3 disciplines** `[NEW-current, kept]`: 01 Content audit · 02
  Information architecture · 03 Pilot migration. Each with mono
  "Lifecycle stage · Audit" / "Map" / "Map → Convert" tag, display
  name, and ~80-word body paragraph.

### S4 — The migration lifecycle (5-card strip) `[OLD lifecycle content, new layout]`
- **Heading** `[DRAFT]`: "The migration lifecycle."
- **Intro** `[DRAFT]`: "Five stages that sit underneath the
  disciplines. The disciplines are *what* a migration team does; the
  lifecycle is *where* in the program each one applies."
- **5-card horizontal strip** (`container-data`), each card carries:
  - Mono "01"–"05" number (amber-pressed)
  - Display name (Audit / Map / Convert / Refine / Publish)
  - One-line body (kept from the pre-redesign `MigrationLifecycleCard`
    data: "Catalog the corpus. Delete ROT before anything converts." /
    etc.)
- Amber arrow SVG between each pair at desktop; stacks vertically
  <1024px.

### S5 — Source formats covered `[NEW-current, unchanged]`
- **Heading**: "Source formats covered."
- 13 mono-styled format names in a 3-col grid (Word · FrameMaker ·
  InDesign · RoboHelp · MadCap Flare · DocBook · HTML · Markdown ·
  AuthorIT · Confluence · SGML · Excel · PDF (OCR)).

### S6 — Phase 2: Conversion & enrichment `[DRAFT, derived from OLD 2-phase grouping]`
- **Eyebrow** `[DRAFT]`: "Phase 2"
- **Heading** `[DRAFT]`: "Conversion & enrichment."
- **Intro** `[DRAFT]`: "Two disciplines that take you from converted
  content to enriched, validated DITA — the part where the
  architecture pays off."
- **2 disciplines** `[NEW-current, kept]`: 04 Batch conversion · 05
  Deduplication & enrichment.

### S7 — Field rules from the practice `[NEW-current, unchanged]`
- **Heading**: "Field rules from the practice."
- 4 horizontal-row rules: Delete ROT first · Pilot with fifty pages,
  not five, not five hundred · Don't fix formatting in source · Convert
  all languages simultaneously. Each with a "Why:" elaboration.
- Same content as OLD page's "Pro Tips from 2M+ Pages of Migration
  Experience" but in document-grade voice (no "Pro Tips" framing).

### S8 — CTAModule (audience="general") `[shared component]`
- Body (kept from pre-redesign): "Submit a 20-page sample document.
  We'll return conversion feasibility, expected content recovery rate,
  ROT estimate, and engineering effort within two business days. The
  analysis is the basis for any further engagement, with no obligation
  to proceed."
- Replaces the OLD page's custom "Free Content Health Check" dark navy
  banner.

---

## 6. Decision log
- **D-1** *(locked, shipped)* — Hero copy combines OLD + NEW per the
  AI-Readiness pattern.
- **D-2** *(locked, shipped)* — Hero side-visual = Option C "Recovery
  before/after."
- **D-3** *(locked, shipped)* — Restore 2-phase grouping (Phase 1 /
  Phase 2) over the 5 disciplines.
- **D-4** *(locked, shipped)* — Insert Migration Lifecycle 5-card strip
  between Phase 1 and Source Formats.
- **D-5** *(locked, shipped)* — Drop `MigrationLifecycleCard` usage;
  component file kept for now.
- **D-6** *(locked, shipped)* — Keep shared CTAModule; drop OLD custom
  CTA banner.
- **D-7** *(locked, shipped)* — Drop OLD Related Resources 3-card grid.
- **D-8** *(locked)* — Drop newsletter.
- **D-9** *(superseded by D-12)* — ~~AnimatedDivider between sections;
  no banded rhythm.~~
- **D-14** *(locked, shipped — pass g)* — Section polish round (owner
  requests): (1) added a 4th stat — **~40% typical ROT** ("dead content
  in a legacy corpus", grounded in the audit copy) so the band is now
  2M+ / 13 / 4 / ~40% in a 4-col row; (2) extended the Phase 1, Phase 2,
  and Field-rules intros by one sentence each `[DRAFT]`; (3) stretched
  the Source-formats and Field-rules leads to the full container width
  (scoped `max-width: none`, like the framing lead); (4) **Source
  formats are now amber pill badges** (`#fef3c7` wash + amber-pressed
  text + amber border, centered wrap cloud) replacing the mono hairline
  grid — dropped the redundant "Formats" eyebrow and the bracketing
  rules. "Colored" = amber-toned (locked amber-only palette).
- **D-13** *(locked, shipped — pass f)* — Framing section: condense +
  add a visual. Owner found the 3-paragraph prose too wordy and wanted a
  visual to help convey it. Condensed to a 2-sentence lead and added the
  Transcription vs Recovery contrast panel (Concept A, chosen in-browser
  from four mocked on `/migration-playbook-mock`, since deleted). Detail
  lives in the panel; the dropped credibility recitation is covered by
  the S2.5 stat band. Supersedes the D-11 two-column framing-prose
  treatment (no longer prose).
- **D-12** *(locked, shipped — pass e)* — Divider treatment. Owner: the
  only amber horizontal line should be the one above the CTA; everything
  else a regular gray hairline like the other pages. Removed all eight
  amber `AnimatedDivider`s and the import; separate sections with a gray
  `border-top: var(--border-hairline)` on `.mp-section` (the
  /resources/ai-readiness model); enabled the CTA's `accentLine` (its
  moving amber top edge) as the single amber line. Removed the stat
  band's two bracket `mp-rule` hairlines and the `:last-child`
  bottom-borders on disciplines / rules so they don't double with the
  new section borders.
- **D-11** *(locked, shipped — pass d)* — Fix the marooned prose
  sections. Framing, Phase 1, Source formats, and Phase 2 were on
  `container-prose` (720px) while the lifecycle / field-rules / stat
  band were on `container-data` (1080px), leaving ~280px dead margin
  each side on the prose sections (owner-flagged). Widened all four to
  `container-data` so the whole page shares one 1080px edge, AND
  horizontalized the discipline rows into the same 3-column grid the
  Field Rules section uses (`64px | name+stage | body` at >=1024px) so
  they fill the width. Framing prose flows into two columns at >=1024px
  for the same reason (capped at 72ch below that). Chosen over the
  lighter "align only" and the wider `container-page` (1280px) options.
- **D-10** *(locked, shipped — pass c)* — Add the practice stat band
  (2M+ / 13 / 4) after the framing prose, resolving pending item #1.
  Numbers are grounded in copy already live on the page (no new claims).
  Hairline-ruled on plain bg (not `.section-band`) to avoid pre-empting
  the deferred banded-rhythm call. Chosen over the Field Rules eyebrow
  and hero-SVG chrome alternatives because it directly fixes the
  "not visually prominent" problem.

---

## 7. [DRAFT] copy inventory (all signed off and live)

| Loc | Tag | Item |
|-----|-----|------|
| S1  | `[DRAFT-merge]` | Combined subdeck |
| S2  | `[DRAFT]` | Condensed lead + Transcription vs Recovery contrast panel copy |
| S2.5| `[DRAFT]` | Practice stat band (2M+ / 13 / 4) — numbers grounded in live copy |
| S3  | `[DRAFT]` | Phase 1 eyebrow + heading + intro |
| S4  | `[DRAFT]` | Migration lifecycle heading + intro |
| S6  | `[DRAFT]` | Phase 2 eyebrow + heading + intro |

All other body copy (disciplines, lifecycle stage bodies, source
formats, field rules, CTA body, framing prose) is `[OLD]` or
`[NEW-current]` verbatim from the existing implementations.

---

## 8. Pending / not-yet-done items

These came up during the discussion but weren't implemented in the
redesign — flagging them as candidates for a follow-up pass:

- ~~**"2M+ pages of migration experience" credibility framing.**~~
  **DONE (pass c, D-10):** shipped as the S2.5 practice stat band
  (2M+ / 13 / 4) after the framing prose. The Field-Rules-eyebrow and
  hero-SVG-chrome alternatives were considered and not taken.
- **Color-coded phase bars.** The OLD page's discipline steps had
  colored vertical bars (red/amber/blue/green) per phase. Currently
  all disciplines use the same hairline + amber-number styling. Could
  add a subtle phase-color indicator to differentiate disciplines
  visually within their phase.
- **`MigrationLifecycleCard` component cleanup.** The component file
  at `src/components/site/MigrationLifecycleCard.astro` is no longer
  imported anywhere. Safe to `git rm` in a follow-up — but verify no
  other page picks it up first.
- **Banded rhythm vs. AnimatedDivider between sections.** Current
  pattern is AnimatedDivider between every section. Other redesigned
  pages (e.g. /company/our-process) mix banded + plain sections for
  a tighter vertical rhythm. Could revisit if the page reads as too
  long.

---

## 9. Build notes / dependencies

- Page-local CSS prefix: `mp-`.
- Hero side-visual: SVG needs `width: 520px; max-width: 100%` (not
  `width: 100%`) because the `Hero` component's `.hero__side` is
  `flex: 0 0 auto` and 100% has no definite parent to fill. **This bit
  us once already.**
- Migration Lifecycle strip reuses the same 5-card horizontal pattern
  as `/company/our-process` (eyebrow/name/body, amber arrow SVGs
  between cells, stacks vertically at <1024px). Container `container-data`.
- Phase eyebrow style (`.mp-phase__eyebrow`): mono 11px semibold,
  letter-spacing 0.12em, accent-primary-pressed color, uppercased via
  CSS. Same idiom as the `Example profile` eyebrow on Our Process
  facet panels.
- IntersectionObserver script lives at bottom of the page file —
  `setupMpHero()` — checks `document.readyState` to handle the
  module-defer race (DOMContentLoaded may already have fired by the
  time the module executes).
- Spacing-token trap: when adding new gaps/margins to this page, use
  only **1, 2, 3, 4, 5, 6, 8, 12, 16, 20, 24, 32** from the `--space-N`
  scale. Skipped values silently compute to 0.
