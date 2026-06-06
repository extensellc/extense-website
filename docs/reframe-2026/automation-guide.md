# Publishing Automation Guide (Resources sub-page) — Redesign Plan

> Status: **shipped on staging**. Full redesign mirroring the
> `/resources/migration-playbook` treatment (centered heads, gray
> hairline dividers, single amber line at the CTA, one aligned content
> width, stat band, contrast panel, document-grade hero SVG).
>
> Tags: `[OLD]` / `[NEW]` / `[DRAFT]`. Conventions in [README.md](README.md).

---

## 1. Page job
- **URL:** `/resources/automation-guide`
- **Primary reader:** documentation lead / content-engineering manager /
  DevOps owner evaluating CI/CD for docs; often arrived from search
  ("DITA CI/CD", "automated publishing pipeline"), the Resources
  dropdown, or the Publishing Engineering service page.
- **The one job:** convince the reader that manual publishing is a risk
  surface and that a validated, containerized CI/CD pipeline removes it —
  showing the pipeline, the container model, the multi-format output
  (incl. JSONL), the platforms, and the plugins. Convert to a free
  pipeline gap analysis.

---

## 2. Inventory — OLD page (ex-tense.co/publishing-automation)
1. Hero — "Publishing Automation Guide" + subdeck "CI/CD for
   documentation: containerized builds, multi-format output, validation
   gates, AI-ready export — from a single source, on every commit."
2. **Manual Publishing Is Broken** — Before/After 2-card (7 items each).
3. Stats band — 40min→3min · 1→4 · 0→100% · ~70%.
4. **The Automated Pipeline** — 8 cards (Git Push → Promote).
5. **Containerized Builds with Docker** — Why Docker? + What's in the
   Image cards, Dockerfile code, Pipeline Usage code.
6. **Multi-Format Output** — 4 cards (HTML5, PDF, JSONL, Additional) +
   build.gradle. JSONL card cross-links AI Content Readiness Guide.
7. **Supported CI/CD Platforms** — GitHub Actions (recommended) + YAML,
   then Azure DevOps / Jenkins / GitLab CI cards.
8. **Validation Gates** — 6 cards (Schema & Schematron, Link & Reference
   Integrity, Terminology & Style, Image & Asset Audit, Metadata
   Completeness, Build Notifications).
9. **Custom DITA-OT Plugins** — 3 cards + Plugin Development &
   Maintenance box.
10. Free Pipeline Assessment — dark navy CTA banner.
11. Related Resources — 3 cards. + Stay Connected newsletter (banned).

## 3. Inventory — NEW page (pre-redesign)
Hero (static `PublishingPipelineCard` 8-stage list) → "Why manual
publishing fails" (3 prose paras + outcomes strip) → eight-stage pipeline
(What runs / Result) → containerization → output formats → CI/CD
platforms → plugins → CTA. Strengths: far more detailed pipeline + code;
document-grade. Weaknesses: hero card duplicated the pipeline; 5 of 6
sections sat in narrow `container-prose` (marooned, awkward empty space);
no Before/After visual; no prominent stats.

---

## 4. Mapping decisions
- **D-1 — Hero copy = combined OLD + NEW.** H1 reverts to OLD
  "Publishing Automation Guide" (search-friendly). Subdeck `[DRAFT-merge]`
  opens with the NEW "risk surface" thesis, folds in the OLD CI/CD line
  + first-class-JSONL, closes "from a single source on every commit"
  (OLD). `subdeckMaxWidth="560px"`.
- **D-2 — Hero side-visual = "Gated build" SVG (Concept C).** Picked
  in-browser from three mocked on `/automation-guide-mock` (A linear
  run / B fan-out / C gated build). C chosen: a valid commit passes the
  amber `validate` gate and ships ×3; an invalid commit is blocked
  (struck) at the gate — renders the page's central thesis (validation
  catches defects before merge) and is distinct from the
  publishing-engineering fan-out. Document-grade idiom + IntersectionObserver
  `.drawn` scroll-reveal (staggered fade + dash-draw connectors/strike +
  reduced-motion fallback). Width `520px; max-width: 100%` (SVG width
  trap). Prefix `.pa-hero-flow`.
- **D-3 — Replace the static `PublishingPipelineCard`** (it duplicated
  the eight-stage pipeline section) with the SVG. *(Redundancy fix #1.)*
- **D-4 — Fold "Validation Gates" into the pipeline; no separate
  section.** 4 of the 6 old gates ARE pipeline stages (schema 02, links
  03, terminology 04, image audit 06); the other two live in stage 02
  (metadata completeness) and stage 08 (build notifications). A separate
  section would repeat the pipeline. Owner confirmed fold.
  *(Redundancy fix #2 — the main de-dup the owner asked for.)*
- **D-5 — Bring the OLD Before/After forward as a Manual vs Automated
  contrast panel** (same 2-up idiom as migration-playbook's
  Transcription-vs-Recovery), replacing the wordy 3-paragraph framing
  with a 2-sentence lead + the panel.
- **D-6 — Stat band** for the OLD before→after numbers (40m→3m / 1→4 /
  0→100% / ~70%), centered document-grade band (same idiom as
  migration-playbook).
- **D-7 — Fix the empty space:** every section → `container-data`
  (one shared 1080px edge); the pipeline already used it. Headings +
  leads centered; code/stack eyebrows and structured rows stay left.
- **D-8 — Divider treatment:** drop all amber `AnimatedDivider`s; gray
  `border-top` on `.pa-section`; single amber line = the CTA `accentLine`.
- **D-9 — Keep the shared CTAModule** (accentLine); drop the OLD custom
  "Free Pipeline Assessment" banner, Related Resources, and newsletter.
- **D-11 — Containerization intro left-aligned (pass b).** Owner: the
  centered lead clashed with the left body/stack/code. Left-aligned the
  lead + body paragraphs; heading stays centered (page rhythm). Scoped to
  `.pa-section--container`.
- **D-12 — Sticky code panels in Output formats + CI/CD platforms
  (pass b).** Owner: the full-width code blocks left a dead right half.
  Reworked both into a `.pa-split` 2-col grid (≥1024px): the numbered
  list scrolls on the left, the code sits in a `position: sticky` aside
  on the right (`top: 120px` to clear the 105px sticky TopNav). The left
  list is taller than the code in both sections, so the sticky has scroll
  room. Stacks to one column (code below list, static) <1024px.
- **D-13 — Plugins principle = centered amber callout (pass b).** Owner:
  centered the closing principle in a light-amber (`#fef3c7`) callout box,
  near-black text for legibility, and removed the hairline above it.
- **D-10 — Keep all four code blocks** (Dockerfile, docker run, Gradle,
  GitHub Actions) — they're the practitioner substance; now aligned in
  the wider container with horizontal scroll guard.

---

## 5. Section wireframe (as shipped)
1. **Hero** — H1 "Publishing Automation Guide" `[OLD]` + combined subdeck
   `[DRAFT-merge]` + gated-build SVG.
2. **Why manual publishing fails** — centered lead `[DRAFT]` + Manual vs
   Automated contrast panel `[DRAFT, from OLD Before/After]`.
3. **Stat band** — 40m→3m / 1→4 / 0→100% / ~70% `[OLD numbers]`.
4. **The eight-stage pipeline** `[NEW, kept]` — validation folded in.
5. **Containerization** `[NEW, kept]` — prose + stack + Dockerfile +
   pipeline-usage code.
6. **Output formats from a single source** `[NEW, kept]` — 4 rows + Gradle.
7. **CI/CD platforms** `[NEW, kept]` — 4 rows + GitHub Actions YAML.
8. **Custom DITA-OT plugins** `[NEW, kept]` — 3 rows + maintenance principle.
9. **CTAModule** (general, accentLine) `[shared]`.

---

## 6. [DRAFT] copy inventory (signed off in-session)
| Loc | Tag | Item |
|-----|-----|------|
| Hero | `[DRAFT-merge]` | Combined subdeck (H1 is OLD verbatim) |
| S2 | `[DRAFT]` | Condensed lead + Manual vs Automated panel copy |
| S3 | `[OLD]` | Stat band numbers (reformatted) |

All pipeline / container / format / platform / plugin body copy is
`[NEW]` kept verbatim from the prior implementation.

---

## 7. Pending / follow-up
- **`PublishingPipelineCard` cleanup.** No longer imported anywhere
  (only self-reference). Safe to `git rm` in a follow-up — same status
  as `MigrationLifecycleCard`.
- Per-section lead widths are the centered 70/76ch default; could stretch
  specific ones (as on migration-playbook) if any read narrow on review.
- Page is code-heavy (4 blocks); if it reads long, a banded-rhythm pass
  or collapsing the longer code samples could tighten it.

---

## 8. Build notes
- Page-local CSS prefix: `pa-`.
- Hero SVG: `width: 520px; max-width: 100%` (the `.hero__side` flex trap).
- Reveal scripts `setupPaHero()` + `setupPaStats()` share the page's
  script block; `document.readyState` guard for the module-defer race;
  stat band is JS-armed so it's never hidden without JS; reduced-motion
  fallbacks keep everything visible.
- Spacing-token trap: only 1,2,3,4,5,6,8,12,16,20,24,32 exist on the
  `--space-N` scale.
