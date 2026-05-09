# Extense LLC — Website Design Brief

**Status:** Phase 3 closed. Phase 4 (implementation) in progress.
**Branch:** `redesign-2026`
**Stack:** Astro + TypeScript (strict) + vanilla CSS with design tokens. Deployed to Vercel. Formspree for contact form. Playwright for build-time PDF generation.

This document is the bridge between strategy (Phases 1–3) and implementation (Phase 4). Every locked decision lives here. If implementation deviates from this brief, the deviation requires explicit approval and an update to this document.

---

## 1. Positioning Statement

> Extense LLC is an XML content engineering firm for organizations whose documentation has to be right — federal agencies, Fortune 500 manufacturers, life sciences companies, financial institutions, and defense contractors. Founded in 2012, the firm owns the full stack from information architecture through automated CI/CD publishing, with operating expertise in DITA, S1000D, CCMS platforms (IXIASOFT, Heretto, Paligo, Tridion Docs), and AI-ready content engineering. For clients including the IRS, the U.S. House of Representatives, Toyota, FedEx, and Morgan Stanley, Extense engagements typically produce 60% faster publishing cycles, 72% lower translation costs, and 85% retrieval precision in RAG pipelines. SBA 8(a) certified, woman-owned, minority-owned — sole-source eligible for federal contracts.

**This sentence is canonical.** It's the firm's anchor and appears verbatim (or with minor tightening only) on `/about` Hero. Variant phrasings on other pages must preserve the substance.

---

## 2. Audience Strategy

Two distinct buyer audiences served via three landing pages:

| Page | Primary reader | Aesthetic register |
|------|----------------|--------------------|
| `/` | Unsegmented visitor (referrals, brand search, partners, candidates) | Anthropic-warmth dominant, document-grade |
| `/public-sector` | Federal procurement officer / agency tech lead | Anduril-gravitas tilt, capability-statement structure |
| `/private-sector` | Fortune 500 documentation / compliance director | Anthropic-warmth, ROI-fluent, business-outcome framing |

**Visual direction recipe:** Anduril gravitas (dialed down) + Anthropic restraint + Stripe Docs density. Document-grade-not-luxury-brand. Free typography (Source Serif 4 / Inter / JetBrains Mono) fits the character.

**Guardrail (locked, non-negotiable):** Warmth in visual register, density in content register. Outside content blocks the page breathes; inside content blocks the page packs. Anthropic's body-copy looseness does not apply within content blocks.

---

## 3. Sitemap (13 pages)

```
/                                          unsegmented homepage
├── /public-sector                         federal capability-statement landing
│   └── /public-sector/government-and-defense    industry page (only one under public-sector)
├── /private-sector                        commercial outcomes landing
│   ├── /private-sector/financial-services
│   ├── /private-sector/life-sciences
│   ├── /private-sector/automotive
│   └── /private-sector/insurance
├── /capabilities                          integration story (4×5 phase-weight matrix is centerpiece)
│   ├── /capabilities/information-architecture
│   ├── /capabilities/content-migration
│   ├── /capabilities/ccms-and-publishing
│   └── /capabilities/ai-ready-content
├── /about                                 load-bearing identity page
├── /insights                              editorial publication surface
└── /contact                               conversion mechanics
```

**No `/careers` at launch** (no active hiring per Phase 3 verification).
**No `/public-sector/past-performance` subpage** (4–6 federal contracts absorbed directly into `/public-sector`).
**Privacy / Terms in footer only** (not in nav).
**No dropdowns in nav** (forces landing pages first; document-grade restraint).

---

## 4. Methodology — Three Framings

The 5-phase methodology (Discovery → Architecture → Migration → Implementation → Enablement) appears in three differentiated framings across the site. **If any two read alike in copy, the page is wrong.**

| Page | Framing | Tone | Reader |
|------|---------|------|--------|
| `/about` | Definitional | Identity — *this is how Extense works on every engagement* | Anyone wanting to know what kind of firm this is |
| `/capabilities` | Narrative / integration story | How phases concentrate and overlap when multiple pillars are in scope | Multi-pillar transformation buyer |
| Pillar pages | Applied / operational | What each phase looks like for *this* pillar specifically | Specific-problem buyer doing diligence |

The 4×5 phase-weight matrix on `/capabilities` is the load-bearing visualization that makes `/capabilities` non-redundant with the homepage's parallel four-pillar row.

---

## 5. Outcome Metrics — Five-Stat Record

Real Extense client outcomes (confirmed Phase 1):

| Stat | Metric | Primary placement |
|------|--------|-------------------|
| 60% | Faster publishing cycles | Homepage trio, `/private-sector`, `/capabilities/ccms-and-publishing` (anchor) |
| 72% | Translation cost savings | Homepage trio, `/private-sector`, `/private-sector/automotive` (anchor) |
| 45% | Content reuse rate | `/capabilities/content-migration` (anchor), `/private-sector/life-sciences`, `/about` |
| 90% | Fewer support tickets | `/capabilities/information-architecture` (anchor), `/about` |
| 85% | RAG retrieval precision | Homepage trio, `/capabilities/ai-ready-content` (anchor), `/private-sector/financial-services`, `/private-sector/insurance` |

**Homepage canonical trio: 60% / 72% / 85%.**
**Full deck (all five) appears only on `/about`.**
**Pillar pages anchor to one stat each.**
**Industry pages anchor to two stats each.**

No animated counters. Numbers in `color-text-primary`, never amber (single-semantic-accent rule).

---

## 6. Cost-of-Being-Wrong Scenarios

Three "content-wrong" scenarios rotate on the homepage. Each industry page surfaces its own. All confirmed real Extense engagements (Phase 1).

| Scenario | Industry | Where it lives |
|----------|----------|----------------|
| IFU error → FDA Class I recall | Life Sciences | Homepage trio, `/private-sector/life-sciences` (headline, told most fully) |
| S1000D conformance failure → stop-work order | Defense | Homepage trio, `/public-sector`, `/public-sector/government-and-defense` (extended) |
| Dealer service-manual error → warranty exposure | Automotive | Homepage trio, `/private-sector/automotive` |
| SOX deficiency → 10-K material weakness | Financial Services | `/private-sector/financial-services` (NOT homepage — control-wrong shape, different from content-wrong trio) |
| Policy form rejection by state DOI → launch delay | Insurance | `/private-sector/insurance` |

---

## 7. Conversion Mechanism

**Single conversion mechanism: Sample Content Assessment.**

- Same label everywhere (`/`, `/public-sector`, `/private-sector`, all child pages)
- Single 20-page sample upload
- Returns: conversion feasibility, content recovery rate, engineering effort
- Routes to `/contact` with audience toggle preset based on referring page
- Public-sector context body emphasizes RFP-response / sole-source-justification framing
- Private-sector context body emphasizes business-case framing
- Multi-pillar context body emphasizes scope-flexibility

**Phase 4 directive (locked):** the upload field label and helper text must surface the SCA connection explicitly. Direction:
- Label: `Upload a 20-page sample for a Sample Content Assessment (optional)`
- Helper: `Submitting a sample triggers a free assessment. We'll return conversion feasibility, content recovery rate, and engineering effort within two business days.`

**Response commitment: < 24 hours, business days.** Visible immediately above the submit button.

---

## 8. Page Wireframes

### `/` (homepage)

**Position:** Universal capability claim. Audience-neutral but specific. Both audiences served via in-page pivot.

**Section order:**
1. TopNav
2. Hero (`Hero.universal`) — H1 + sub-deck, no CTA, left-aligned, container-prose
3. Cost-of-being-wrong (`DocumentRow.failureMode` × 3) — IFU/Defense/Automotive
4. Four pillars (`PillarCard` × 4) — IA, Migration, CCMS, AI-Ready in lifecycle order
5. Outcome stats (`StatBlock.three`) — 60/72/85
6. Proof bench (`LogoBench.full`) — 12 logos
7. Audience pivot (`AudiencePivotCard` × 2) — Public Sector / Private Sector
8. CTA (`CTAModule`) — Sample Content Assessment, general toggle preset
9. Footer

### `/public-sector`

**Position:** Federal-procurement-fluent capability-statement landing. Reads as a working document.
**Section order (verification-first):**
1. TopNav
2. Hero (`Hero.identifying`) — declarative identity, no aspiration verbs
3. CapabilityStrip — NAICS / CAGE / UEI (no contract vehicles per verification)
4. PDFDownloadButton — capability statement PDF
5. LogoBench (`LogoBench.federal`) — 3 logos: IRS, U.S. House, U.S. District Courts
6. Certifications block (`DocumentRow.entry` × N) — 8(a), WOSB, MBE, sole-source eligibility, with procurement context per cert
7. Past performance (`DocumentRow.entry` × 4–6) — agency name + general work description (NDA-bounded)
8. Four pillars (`PillarCard` × 4) — federal copy register
9. Cost-of-being-wrong (`DocumentRow.failureMode` × 1) — S1000D/stop-work, extended
10. CTA (`CTAModule`) — Sample Content Assessment, public-sector toggle preset
11. Footer

### `/private-sector`

**Position:** Commercial outcomes landing. ROI-fluent.
**Section order (argument-first):**
1. TopNav
2. Hero (`Hero.outcome`) — outcome-led with concrete numbers, no transformation language
3. Cost-of-being-wrong (`DocumentRow.failureMode` × 3) — same trio as homepage
4. LogoBench (`LogoBench.commercial`) — 8 logos
5. Four pillars (`PillarCard` × 4) — business language register
6. Outcome stats (`StatBlock.three`) — 60/72/85, commercial framing
7. Industry navigation (`IndustryCard` × 4) — Financial Services, Life Sciences, Automotive, Insurance + orphans paragraph (AMD/HPE/FedEx)
8. CTA (`CTAModule`) — Sample Content Assessment, private-sector toggle preset
9. Footer

### `/capabilities`

**Position:** Integration story page. Multi-pillar buyer.
**Section order (centerpiece-led):**
1. TopNav
2. Hero (`Hero.universal`)
3. **PhaseWeightMatrix** (load-bearing centerpiece) — 4 pillars × 5 phases, with intro line in container-prose centered within section's container-data
4. Lifecycle narrative — 3–5 paragraphs of methodology-as-narrative prose
5. Anonymized end-to-end case study — H3 subsections (Situation / Work / Outcome)
6. Engagement shape — compact structured list of engagement types
7. Pivot to pillar pages (`PillarCard` × 4) — same component as homepage, routing role
8. CTA (`CTAModule`) — general toggle preset
9. Footer

### Pillar pages (4 total)

`/capabilities/information-architecture`, `/capabilities/content-migration`, `/capabilities/ccms-and-publishing`, `/capabilities/ai-ready-content`

**Section order (shared base):**
1. TopNav
2. Hero (`Hero.universal`, pillar-specific copy)
3. **SiblingsBreadcrumb (`.pillars`)** — IA · Migration · CCMS · AI-Ready, current bolded
4. Deliverables — compact structured list
5. Methodology phases applied (`DocumentRow.entry` × 5) — Discovery/Architecture/Migration/Implementation/Enablement, pillar-specific application notes per phase
6. Anchor stat + bridge (`StatBlock.one` + bridge prose, 2–4 sentences)
7. Standards and tooling — compact structured list
8. Cost-of-being-wrong (`DocumentRow.failureMode` × 1) — pillar-specific failure mode
9. CTA (`CTAModule`) — pillar-specific body
10. Lifecycle navigation — small inline "Next: [next pillar] →" link
11. Footer

**Per-pillar anchor stats:**
- IA → 90% (with bridge: when IA is right, users find what they need on the first try; when it isn't, they open tickets)
- Migration → 45% (with bridge: migration isn't moving content, it's identifying recoverable reusable assets)
- CCMS → 60% (with bridge: from quarterly publishing to per-merge releases)
- AI-Ready → 85% (with bridge: precision matters more than recall in regulated industries)

### Industry pages (5 total)

`/public-sector/government-and-defense`, `/private-sector/{financial-services, life-sciences, automotive, insurance}`

**Section order (shared base):**
1. TopNav
2. Hero (`Hero.universal`, vertical-specific framing)
3. **SiblingsBreadcrumb (`.industries`)** — only on `/private-sector` industries (G&D omits, no siblings)
4. Document types — compact structured list
5. Standards and frameworks — compact structured list
6. Cost-of-being-wrong (`DocumentRow.failureMode` × 1) — vertical-specific
7. Capability relevance — compact list of relevant pillars with cross-links
8. Proof — `LogoBench.industry` + 1–2 anonymized case studies (H3 + 2–3 sentences)
9. Outcome stats (`StatBlock.two`) — vertical-specific stat pair
10. CTA (`CTAModule`) — vertical-specific body
11. Footer

**Per-industry stat pairs:**
- G&D: 60% + 45%
- Financial Services: 60% + 85%
- Life Sciences: 45% + 72%
- Automotive: 72% + 60%
- Insurance: 60% + 85%

### `/about`

**Position:** Load-bearing identity page.
**Section order (identity-first):**
1. TopNav
2. Hero (`Hero.universal`) — uses Phase 1 canonical positioning sentence verbatim
3. 5-phase methodology, definitional framing (`DocumentRow.entry` × 5) — phase-as-character, not process documentation
4. Full five-stat outcome record (`StatBlock.five`) — only page with all five
5. Aggregate team framing — opening paragraph + compact structured list of practice areas (no individuals featured per locked decision)
6. Founding and growth — brief, identity-not-history (compressed padding `space-16`)
7. Certifications at depth (`DocumentRow.entry` × N) — each with procurement context
8. CTA (`CTAModule`) — general toggle preset
9. Footer

### `/insights`

**Section order:**
1. TopNav
2. Hero (`Hero.universal`, editorial register)
3. TopicFilter — pill chips: All / DITA / S1000D / CCMS Migration / RAG-AI / Methodology
4. Post list (`PostListItem` × N)
5. RSS link — small inline affordance with Phosphor "rss" icon
6. Footer

**Launch content audit:** the four existing Resources guides (AI Content Readiness, DITA Migration Playbook, Publishing Automation Guide, FAQs) get audited against the editorial bar. Survivors ship; failures don't. **FAQs cut at launch** (help content, wrong shape for editorial section).

**Editorial bar:** every post names tools and standards, takes a position, could be read by a working DITA architect without insulting their intelligence.

### `/contact`

**Section order:**
1. TopNav
2. Hero (`Hero.universal`, minimal-direct register)
3. AudienceToggle + form (Public Sector / Private Sector / General Inquiry)
4. Alternative channels — phone, email, mailing address, LinkedIn
5. Footer

**Form fields by audience:**
- Public Sector: Organization, Agency, Role, Brief description, Name, Email, Phone (optional), Sample upload (optional)
- Private Sector: Organization, Role, Problem area, Timeline, Brief description, Name, Email, Phone (optional), Sample upload (optional)
- General Inquiry: Brief description, Name, Email, Phone (optional), Sample upload (optional)

**Toggle preset by referrer:**
- From `/public-sector` or descendants → Public Sector
- From `/private-sector` or descendants → Private Sector
- From `/`, `/about`, `/capabilities`, `/insights` → General Inquiry

**Submission destination:** `contactus@ex-tense.co` via Formspree (free tier, 50/month).

---

## 9. Component Inventory

### System conventions (apply to all components unless overridden)

- **Focus ring:** 2px outline `color-link`, offset 2px, on every keyboard-accessible interactive element
- **Tap targets:** 44×44px minimum on mobile
- **Hover transitions:** `duration-base` (150ms), `easing-out`, on color and opacity only
- **Card pattern:** hairline border `color-border-subtle`, `radius-none`, no drop shadows
- **Link rendering:** `color-link` default, `color-link-hover` on hover/focus, underline appears on hover only
- **Brand-vs-link rule (non-negotiable):** `color-accent-primary` appears only as background or visual brand presence, never as rendered text on `color-page-bg`. `color-link` carries actionable text.
- **Reduced motion:** if `prefers-reduced-motion`, transitions become instant
- **`radius-pill`** reserved for chip-like interactive controls only (TopicFilter chips, AudienceToggle segments)

### Components

**Shared / foundational:**
- `TopNav` — sticky, 72px desktop / 56px mobile, no dropdowns, hamburger drawer on mobile
- `Footer` — 4-column desktop, single column mobile, LinkedIn icon in bottom row
- `Hero` — single component, three copy-mode variants (`.universal`, `.identifying`, `.outcome`), structurally identical

**Document patterns:**
- `DocumentRow` — two variants only:
  - `.entry` (default) — no eyebrow, `text-display-sm` heading, `text-body` body. Used for certs, past performance, methodology (applied + definitional). Content discipline enforced through copy guidance, not component-level.
  - `.failureMode` — eyebrow, `text-display-md` heading, `text-body` body. Used for cost-of-being-wrong scenarios.

**Navigation:**
- `SiblingsBreadcrumb` — two variants: `.pillars` (lifecycle order), `.industries` (stable order). Hairline rules above and below. Multi-word names use non-breaking spaces.

**Cards:**
- `PillarCard` — flex column, 48px badge, name + scope + "Read more →". Custom badges for 4 pillars (Phase 4 commission).
- `IndustryCard` — same structure as PillarCard, no badge. Editorial-load heading copy.
- `AudiencePivotCard` — paired on `/`. 4px left border (navy for public, warm-gray for private).

**Conversion:**
- `CTAModule` — single label "Sample Content Assessment" universally. Body adapts per page. Routes to `/contact` with toggle preset.

**Visualization:**
- `PhaseWeightMatrix` — 4×5 matrix, `/capabilities` centerpiece. Sticky headers. Primary-load shading + text both communicate emphasis.
- `StatBlock` — variant-explicit: `.one`, `.two`, `.three`, `.five`. No animated counters. No generic n-column variant.
- `LogoBench` — variants: `.full` (12), `.federal` (3), `.commercial` (8), `.industry` (1–2).

**Page-specific:**
- `CapabilityStrip` — NAICS / CAGE / UEI, hairline rules above and below, NAICS rendered as JetBrains Mono vertical stack.
- `PDFDownloadButton` — pattern (formalize if reused). Phosphor "file-pdf" icon + descriptive text including file size.

**`/insights`:**
- `TopicFilter` — pill chips, hairline rules above and below. URL state via query parameter (`/insights?topic=dita`).
- `PostListItem` — kept separate from DocumentRow. Whole item is a link. Metadata + title + summary.

**`/contact`:**
- `AudienceToggle` — segmented control, three options, referrer-based preset
- `FormField` — shared form primitive, 48–52px height, hairline border, focus state via `color-link` border, error state via `color-error`
- `Textarea` — FormField variant, min height 120px
- `FileUploadField` — drag-and-drop zone, single file, label/helper surfaces SCA connection

---

## 10. Design Tokens

### Color

```css
--color-page-bg: #FAF7F2;              /* page background */
--color-surface-elevated: #F2EEE8;     /* code blocks, CTA section, footer */
--color-text-primary: #1A1817;         /* body and headings */
--color-text-secondary: #6B6560;       /* sub-decks, captions */
--color-text-muted: #9C958E;           /* small footer copy, fine print */
--color-border-subtle: #E5DFD7;        /* hairline rules, table dividers */

--color-accent-primary: #f59e0b;       /* brand identity ONLY — never as text on page-bg */
--color-accent-primary-hover: #d97706;
--color-accent-primary-pressed: #b45309;
--color-link: #b45309;                 /* inline link text — passes WCAG AA on page-bg (~5.4:1) */
--color-link-hover: #9a3412;
--color-gravitas-navy: #1F2D3D;        /* /public-sector structural accent only */

--color-success: #15803d;
--color-warning: #9a3412;              /* distinct from accent-primary-pressed */
--color-error: #991b1b;
```

**Rule:** `color-accent-primary` is brand identity only. CTA backgrounds, brand presence, logo gradient. Never rendered as text on `color-page-bg` (fails AA contrast). `color-link` carries all actionable text.

### Typography

```css
--font-display: "Source Serif 4", Georgia, serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "JetBrains Mono", "Menlo", monospace;

--text-display-xl: clamp(2rem, 4vw + 1rem, 3rem);    /* H1: 32→48px */
--text-display-lg: clamp(1.625rem, 3vw + 0.5rem, 2.25rem);  /* H2: 26→36px */
--text-display-md: clamp(1.25rem, 1.5vw + 0.75rem, 1.5rem); /* H3: 20→24px */
--text-display-sm: 1.125rem;                          /* H4: 18px */
--text-stat: clamp(2.75rem, 5vw + 1rem, 4rem);       /* outcome stats: 44→64px */
--text-body-lg: 1.125rem;                             /* emphasis body: 18px */
--text-body: 1.0625rem;                               /* default body: 17px */
--text-body-sm: 0.9375rem;                            /* captions, footer: 15px */
--text-caption: 0.875rem;                             /* small labels, eyebrows: 14px */

--leading-tight: 1.2;
--leading-snug: 1.4;
--leading-normal: 1.5;
--leading-relaxed: 1.6;

--weight-regular: 400;
--weight-medium: 500;
--weight-semibold: 600;
```

**Phase 4 calibration:** H1 weight-regular vs. weight-medium under rendered output. Lock whichever reads correctly. Default token stays `weight-regular`; H1-specific override possible.

### Spacing (8px baseline)

```css
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
--space-20: 5rem;     /* 80px */
--space-24: 6rem;     /* 96px */
--space-32: 8rem;     /* 128px */
```

### Containers

```css
--container-prose: 720px;    /* warmth reading width */
--container-data: 1080px;    /* tables, matrix, multi-column */
--container-page: 1280px;    /* full content width */

--container-padding-mobile: var(--space-6);
--container-padding-tablet: var(--space-8);
--container-padding-desktop: var(--space-12);
```

### Breakpoints

```css
--bp-mobile: 360px;    /* smallest validated */
--bp-tablet: 768px;
--bp-desktop: 1024px;
--bp-max: 1280px;
```

### Borders / radius / motion / icons

```css
--border-hairline: 1px solid var(--color-border-subtle);
--radius-none: 0;
--radius-sm: 4px;       /* form fields, primary CTA */
--radius-md: 8px;       /* rare; app-flavored only */
--radius-pill: 9999px;  /* chip-like interactive controls only */

--duration-fast: 100ms;
--duration-base: 150ms;
--duration-medium: 200ms;
--easing-out: cubic-bezier(0, 0, 0.2, 1);

--stroke-icon: 1.5px;
```

---

## 11. Phase 4 Directives (Locked)

### Copy directives

1. `/about` Hero uses the canonical Phase 1 positioning sentence verbatim
2. `/private-sector` Hero uses real numbers (60/72/85), no transformation language ever
3. "Sample Content Assessment" is the universal CTA label across the site
4. File upload field label and helper surface SCA connection explicitly
5. Matrix introductory line is a copy seed — preserve "Each pillar concentrates work in different methodology phases. The shape of an Extense engagement is how those distributions overlap." or close variant
6. IndustryCard heading is editorially loaded — not placeholder slot, captures vertical's specific stake in one declarative sentence
7. Certifications block copy bar set higher than other body copy — each cert names what the badge enables in procurement
8. Aggregate team framing on `/about` — copy bar set higher than other body copy. Generic team-composition language fails. Named specificity required.
9. No verbs of aspiration anywhere ("transform," "empower," "enable" as marketing verbs)

### Implementation directives

1. Build-time PDF generation (Playwright headless render) with capability-document conventions: cover page, running header/footer, document metadata, print-tuned typography, LogoBench print restructuring (text list, not logo grid)
2. Nested-link pattern on PillarCard / AudiencePivotCard / IndustryCard / PostListItem: stretched-link `::after` OR `<a>` wrapper with inner affordance `aria-hidden`. Pick one, apply consistently.
3. H1 weight calibration: test 48px Source Serif 4 at weight-regular vs. weight-medium under rendered output, lock whichever reads correctly
4. TopicFilter URL state: filter selection updates URL via query parameter (`/insights?topic=dita`), shareable/bookmarkable/back-button-friendly. Not client-side only.
5. Mobile-first responsive validation at 360px before laptop. Tables don't collapse to cards.
6. Tabular numerals (`font-feature-settings: 'tnum'`) on number columns
7. Logo treatment: monochrome single-color (`color-text-secondary`), max 32px desktop / 24px mobile, optical-balance alignment

### Accessibility directives

1. Semantic HTML: `<nav>`, `<footer>`, `<main>`, `<article>`, `<table>` with `<thead>`/`<tbody>`/`<caption>`
2. Skip-to-content link visible on focus
3. Mobile drawer: focus trap, `aria-modal="true"`, Escape closes, scroll-locked behind
4. `aria-current="page"` on current item in SiblingsBreadcrumb and active TopNav item
5. Decorative elements (hairlines, icon-only badges): `aria-hidden="true"` or CSS only
6. PhaseWeightMatrix primary-load distinction must be communicated through cell text, not visual-only
7. `prefers-reduced-motion` respected throughout

---

## 12. Phase 4 Practitioner Session — Seven Deliverables

**One focused working session with the practitioner (Deepshika and team) before substantial copy work begins.** Outputs gate copy on `/capabilities`, `/public-sector/government-and-defense`, the four pillar pages, `/about`, and `/private-sector/life-sciences`.

1. **PhaseWeightMatrix cell content** — 20 cells (4 pillars × 5 phases) + 4 pillar row labels + 5 phase column labels = 29 calibrated items, each 8–15 words, accurate to actual engagement reality
2. **Per-pillar standards and tooling lists** — IA taxonomy management platforms; AI-Ready vector stores and orchestration frameworks (LangChain / LlamaIndex); CCMS CI/CD tooling specifics
3. **Engagement-shape items on `/capabilities`** — actual engagement types Extense scopes (single-pillar, multi-pillar, Discovery+Architecture only, ongoing support, etc.)
4. **Anonymized end-to-end case study realism check** — `/capabilities` central case study reads as plausible without exposing client identity. **Conditional:** if IDMP confirmed in scope, Life Sciences case study example stays; if dropped, reframe to FDA eCTD or another verified standard.
5. **MIL-PRF-32070 verification** — confirm whether this standard belongs in `/public-sector/government-and-defense` standards list
6. **IETP standards reframe** — replace catchall "IETP standards" with specific named standards Extense ships against
7. **Certifications list completeness** — confirm whether Extense holds any certifications beyond SBA 8(a), WOSB, MBE (specifically: ISO 9001, ISO 27001, security clearances, others)

---

## 13. NDA Constraints (Locked)

- **No specific client engagement details** can be shared (timelines, contract values, scope details)
- **What can be shared:** agency / client name, general (non-specific) description of work
- **Past performance entries** show: agency name + work description only. No contract numbers, period of performance, or contract value.
- **Anonymized methodology-led case studies** are the standard format throughout
- **NDA discipline reads as credibility** for federal procurement audience — do not apologize for it on the page

---

## 14. Brand Assets

- **Logo:** two overlapping squares with amber gradient (`#fcd34d` → `#fde047` → `#f59e0b`), wordmark "EXTENSE" in Montserrat ExtraLight (200), letter-spacing 0.2em
- **Logo files:** `C:\Users\deeps\Downloads\company_logos\` (extense-logo.svg, extense-logo-horizontal.svg, extense-logo-shimmer.html)
- **Wordmark color:** black on light backgrounds, white on dark backgrounds
- **Source Serif 4 + Inter + JetBrains Mono:** all free, all Google Fonts, all i18n-ready

---

## 15. Deployment

- **Host:** Vercel (free tier sufficient at launch)
- **Branch:** `redesign-2026` (current); merges to `main` on launch readiness
- **Domain:** ex-tense.co (eventually; staging on vercel preview URLs first)
- **Form handling:** Formspree (free tier, 50 submissions/month) → routes to `contactus@ex-tense.co`
- **PDF generation:** Playwright at build time, output to `/capability-statement.pdf`

---

## 16. Phase 4 Build Status

### Complete (committed to `redesign-2026` branch)

- Astro 5 + TypeScript strict + Vercel adapter
- Design tokens (color, typography, spacing, containers, borders, motion)
- Global stylesheet (reset, base typography, container utilities, prose, focus rings)
- BaseLayout with SEO/OG/Twitter meta + JSON-LD organization schema
- All 13 pages spec'd + 3 individual `/insights/[slug]` post pages + `/rss.xml` + auto-generated `sitemap-index.xml` + `/privacy` + `/terms`
- All components in inventory: TopNav, Footer, Hero, Logo, DocumentRow (`.entry`/`.failureMode`), SiblingsBreadcrumb, LifecycleNav, PillarCard + 4 badge icons, IndustryCard, AudiencePivotCard, CTAModule, PhaseWeightMatrix, StatBlock, LogoBench, CapabilityStrip, PDFDownloadButton, CompactList, TopicFilter, PostListItem, AudienceToggle, FormField, TextareaField, FileUploadField
- Two shared layouts: PillarPageLayout, IndustryPageLayout
- Content collections (`src/content/insights/`) with 3 placeholder posts
- Build passes; typecheck 0 errors; 21 pages generated

### Deferred to Phase 4 follow-up

**(a) Build-time PDF generation for capability statement.** The `PDFDownloadButton` component exists but is currently inactive on `/public-sector` (replaced with an "available on request" mailto line). Implementation pattern: Playwright headless render of `/public-sector` to PDF at build time, with capability-document conventions (cover page, running header/footer, document metadata, print-tuned typography, LogoBench print restructuring). Estimated: 1–2 days of focused work.

**(b) Phase 4 practitioner session — seven deliverables.** Single focused conversation that gates substantive copy work:

1. PhaseWeightMatrix cell content (29 calibrated items: 20 cells + 4 pillar row labels + 5 phase column labels)
2. Per-pillar standards and tooling lists (IA taxonomy management platforms; AI-Ready vector stores + orchestration frameworks; CCMS CI/CD tooling specifics)
3. Engagement-shape items on `/capabilities` (actual engagement types Extense scopes)
4. Anonymized end-to-end case study realism check (with conditional: IDMP confirmed → keep example; IDMP dropped → reframe to FDA eCTD)
5. MIL-PRF-32070 verification (confirm whether this standard belongs in `/public-sector/government-and-defense`)
6. IETP standards reframe (replace catchall "IETP standards" with specific standards Extense ships against)
7. Certifications list completeness (ISO 9001, ISO 27001, security clearances — anything beyond 8(a)/WOSB/MBE)

Without these answers, `/capabilities`, the four pillar pages, `/public-sector/government-and-defense`, `/about`, and `/private-sector/life-sciences` ship with placeholder copy that holds the structural shape but doesn't carry the practitioner-grade specificity locked in Phase 3 directives.

**(c) Brand asset sourcing.**

- Replace text-fallback labels in LogoBench with actual client logo SVGs (12 total). Single-color rendering at `--color-text-secondary`, max 32px desktop / 24px mobile.
- Pillar badge icons currently use Phosphor-aligned line drawings (IA grid, Migration arrows, CCMS stacks, AI-Ready network). Phase 4 may commission custom marks aligned to the same 1.5px stroke and 48×48px frame.

**(d) Phase 4 visual calibration tasks.**

- H1 weight calibration: test 48px Source Serif 4 at `weight-regular` vs. `weight-medium` under rendered output. Token default is regular; H1-specific override possible after rendered review.
- Mobile-first responsive validation at 360px before laptop (per locked spec).

### Required for production deployment

1. **Formspree form provisioning.** Create Formspree account, create a form with destination email `contactus@ex-tense.co`, set `PUBLIC_FORMSPREE_ENDPOINT` (in `.env` for local dev; in Vercel project env vars for production) to the Formspree action URL.
2. **Vercel project setup.** Connect `extensellc/extense-website` repo to Vercel. Astro auto-detects via `@astrojs/vercel` adapter. Set production branch to `main` after merge from `redesign-2026`.
3. **Domain mapping.** Point `www.ex-tense.co` and apex `ex-tense.co` (with redirect) to Vercel.
4. **Environment variables in Vercel:**
   - `PUBLIC_FORMSPREE_ENDPOINT` — set after Formspree provisioning
   - `PUBLIC_SITE_URL` — defaults to `https://www.ex-tense.co`; override only if staging on a different URL

---

*End of brief. Phase 4 implementation reads this document as canonical input.*
