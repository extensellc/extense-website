# DITA Learner's Study Guide

**From Zero to Developer-Level Mastery**
**Date:** March 2026. Generated from analysis of 76 DITA training topics, 7 learner exercises, 5 XSLT labs, 2 starter projects, and gap analysis. Updated after fluency restructuring, metadata enrichment, and Oxygen XML Editor migration.

---

## How to Use This Guide

This guide serves **two personas**:
- **[W] Technical Writer** — Master authoring, reuse, metadata, maps, and publishing workflows
- **[E] Software Engineer** — Master DITA-OT architecture, plugin development, XSLT, CI/CD, and Docker

Items marked **[Both]** are required for everyone. Follow the phases in order. Each phase has:
- **Read** — Topics to study (with file references)
- **Do** — Hands-on exercises
- **Checkpoint** — What you must be able to demonstrate before moving on

> **Total estimated time:** [W] 25–30 hours | [E] 40–50 hours | [Both tracks] 55–65 hours

---

## 1. Prerequisite Check

### Required Software

| Tool | Version | Purpose |
|------|---------|---------|
| **Java JDK** | 17+ | DITA-OT runtime |
| **DITA-OT** | 4.x | Documentation build engine |
| **Text/XML editor** | Oxygen XML Editor (recommended) or VS Code + XML extension | Authoring DITA topics |
| **Git** | Any recent | Version control |
| **Terminal** | bash/zsh/PowerShell | Running builds |
| **Python 3** | 3.8+ | Preview scripts (optional) |
| **Docker** | Latest | [E] Containerized builds |
| **Node.js** | 18+ | [E] Optional — for plugin JS tooling |

### Installation Status Assessment

| Item | Status | Notes |
|------|--------|-------|
| DITA-OT installation guide | ✅ Covered | `topics/part02-prepare/installing-dita-ot.dita` — step-by-step download, install, and verify |
| Editor setup guide | ✅ Covered | `topics/part02-prepare/setting-up-authoring-tools.dita` — Oxygen XML Editor setup (8 steps: install, preferences, Author mode, templates, Maps Manager, transforms, validation, Git) |
| Java verification | ✅ Covered | `topics/part02-prepare/` includes Java environment notes |
| DITA-OT verification | ✅ Covered | `dita --version` check referenced in multiple topics |

> **⚠️ Watch Out:** Before starting Phase 1, verify: `java -version` (must show 17+) and `dita --version` (must show 4.x). If either fails, resolve before proceeding.

---

## 2. Structured Learning Path

---

### Phase 1: Foundation — Why DITA & Environment Setup

**Personas:** [Both] | **Estimated time:** 3–4 hours | **Parts:** 1 & 2

#### Read (in order)

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 1 | What Is Intelligent Content? | `topics/part01-why/ch01-what-is-intelligent-content.dita` | Concept | 15 min | Business case for structured content |
| 2 | The Problem with Unstructured Content | `topics/part01-why/ch02-problem-with-unstructured-content.dita` | Concept | 15 min | Why unstructured formats fail AI |
| 3 | DITA Introduction Guide | `topics/part02-prepare/dita-intro-guide.dita` | Concept | 25 min | What DITA is — topics, maps, specialization. Includes XML syntax primer (elements, attributes, nesting, DOCTYPE) |
| 4 | DITA Overview | `topics/part02-prepare/dita-overview.dita` | Concept | 15 min | Information typing philosophy (intermediate level) |
| 5 | Preface & Audience | `topics/frontmatter/preface.dita` | Concept | 10 min | Training structure, learning paths per role |
| 6 | Installing DITA-OT | `topics/part02-prepare/installing-dita-ot.dita` | Task | 20 min | Download, install, and verify DITA-OT 4.x |
| 7 | Setting Up Authoring Tools | `topics/part02-prepare/setting-up-authoring-tools.dita` | Task | 25 min | Configure Oxygen XML Editor for DITA authoring |
| 8 | Quick Start Guide | `topics/part02-prepare/quick-start.dita` | Concept | 30 min | Role-based onboarding (choose your track here) |

#### Key Vocabulary to Learn
- **Topic** — Self-contained unit of content (concept, task, or reference)
- **Map / Bookmap** — Organizes topics into hierarchy and navigation
- **DITA-OT** — Open Toolkit that transforms DITA to output formats
- **Transtype** — Output format identifier (html5, pdf, etc.)
- **Conref / Keyref** — Content reuse mechanisms (inline explanations now provided in the tutorial)
- **DITAVAL** — Filtering file for conditional content
- **Element / Attribute** — XML building blocks (covered in the new XML primer in `dita-intro-guide.dita`)
- **DOCTYPE** — Declaration that tells the parser which DITA topic type a file uses (explained inline in the tutorial)
- See full glossary: `topics/appendices/glossary.dita` (~700 lines, 15+ terms)

#### Do

**Exercise:** `learner-exercises/phase1-setup-verification.dita` (30–45 min)
- Install or verify DITA-OT 4.x
- Create your first DITA topic (concept)
- Run your first build: `dita -i my-topic.dita -f html5 -o out/`
- Verify output opens in browser

> **💡 Try This:** After running your first build, explore the output directory. Open the HTML file in a browser. Try changing text in the `.dita` source, rebuild, and refresh the browser. This is the fundamental authoring cycle.

> **⚠️ Watch Out:** If `dita` command not found, ensure `DITA_HOME/bin` is in your `PATH`. On macOS/Linux: `export PATH=$PATH:$DITA_HOME/bin`

#### Checkpoint ✓
- [ ] `dita --version` returns 4.x
- [ ] You created a valid concept topic from scratch
- [ ] You built HTML5 output and viewed it in a browser
- [ ] You can explain what a "topic" and a "map" are in your own words

---

### Phase 2: Authoring Skills — Write Real Content

**Personas:** [Both] | **Estimated time:** 6–8 hours | **Parts:** 3 & 4

#### Read (in order)

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 1 | DITA Authoring Foundations | `topics/part03-author/dita-authoring.dita` | Concept | 45 min | Topic types, templates, element catalog |
| 2 | Writing Your First Project | `topics/part03-author/writing-first-dita-project.dita` | Task | 60 min | Complete 9-step hands-on tutorial ("WidgetPro"). Includes inline tips explaining DOCTYPE, keyref, and conref syntax |
| 3 | Information Typing Basics | `topics/part03-author/ch05-information-typing-basics.dita` | Concept | 20 min | Concept, task, and reference — choosing the right topic type. Decision guide for content placement |
| 4 | Information Typing for AI [E] | `topics/part03-author/ch05-dita-information-typing.dita` | Concept | 25 min | How information types enable intent routing and AI answer formatting (intermediate — builds on #3) |
| 5 | Content Reuse & Variants | `topics/part03-author/dita-reuse-variants.dita` | Concept | 45 min | Conref, keyref, conkeyref, content lifecycle. Includes "What's Next" transition to Part 4 |
| 6 | Topic-Based Architecture | `topics/part04-architect/ch08-topic-based-architecture.dita` | Concept | 20 min | Topic granularity, hierarchy, map-driven architecture |
| 7 | Taxonomy & Controlled Vocabulary | `topics/part04-architect/ch09-taxonomy-controlled-vocabulary.dita` | Concept | 15 min | Subject scheme, AI classification, controlled terms |

#### Do

**Exercise 2A:** `learner-exercises/phase2-first-topics.dita` (60–90 min)
- Write a concept topic explaining a fictional product ("TaskFlow")
- Write a task topic with prerequisites, 5+ numbered steps, and a result
- Write a reference topic with a parameter/settings table
- Practice: concept = what/why, task = how, reference = lookup

**Exercise 2B:** `learner-exercises/phase2-maps-and-reuse.dita` (60–90 min)
- Create a ditamap organizing your 3 topics
- Add keydefs for product name and version
- Create a conref warehouse (`shared/reuse-snippets.dita`)
- Pull shared notes and product names via conref and keyref
- Build the map: `dita -i my-project.ditamap -f html5 -o out/`

> **💡 Try This:** The `writing-first-dita-project.dita` topic has 9 steps plus 3 "experiments." Follow every step — create the WidgetPro concept, task, and reference. Then do the experiments: add an image, create a glossary entry, add a relationship table. This single topic is the most valuable hands-on tutorial in the entire course. The tutorial now includes inline tip notes that explain DOCTYPE declarations, keyref syntax, and conref mechanics as you encounter them — so you learn the "why" alongside the "how."

> **💡 Try This:** After finishing Reuse & Variants (row 5), read the "What’s Next" section at the end — it bridges directly into the architecture topics in Part 4, setting up the mental model for maps, hierarchies, and taxonomy.

> **⚠️ Watch Out:** Common beginner mistake — putting block content inside inline elements. A `<note>` cannot go inside a `<p>`. A `<codeblock>` cannot go inside a `<cmd>`. If your build fails with "element not allowed here," check nesting rules.

> **⚠️ Watch Out:** Conref targets must have matching element types. `<p conref="..."/>` can only pull a `<p>`, not a `<section>` or `<note>`. This is explicitly called out in GAP-03 of the gap analysis.

#### Checkpoint ✓
- [ ] You authored 3 topics (concept, task, reference) from scratch
- [ ] You created a ditamap that organizes them with a hierarchy
- [ ] You used keyref for product name and conref for a shared note
- [ ] You built a multi-topic HTML5 output from your map
- [ ] You understand when to use concept vs. task vs. reference
- [ ] You can explain how information typing helps both human readers and AI systems

**Exercise 2C (Optional):** Taxonomy Mini-Exercise (20–30 min)
- Create a simple subject scheme map (`taskflow-taxonomy.ditamap`) defining controlled values for `audience` (end-user, admin, developer) and `platform` (web, desktop, mobile)
- Use `<subjectScheme>` with `<subjectdef>` for each controlled value
- Bind the scheme to your TaskFlow project map
- Verify that Oxygen XML Editor (or DITA-OT validation) restricts attribute values to your defined terms
- This directly prepares you for DITAVAL filtering in Phase 3W and reinforces the taxonomy concepts from Part 4

> **💡 Try This:** The `samples/` directory demonstrates before/after migration patterns. Browse `samples/before/` to see common unstructured XML problems, then compare with the matching `samples/after/` DITA topics. This builds intuition for content typing decisions.

---

### Phase 3W: Publishing & Metadata — Writer Track

**Personas:** [W] | **Estimated time:** 4–5 hours | **Parts:** 5 & 6

#### Read (in order)

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 1 | DITA Publishing | `topics/part06-publish/dita-publishing.dita` | Concept | 50 min | Build system, HTML5/PDF, parameters |
| 2 | CI/CD Publishing Pipelines | `topics/part06-publish/cicd-publishing-pipelines.dita` | Concept | 45 min | Automated publishing (GitHub Actions, GitLab CI, Jenkins) |
| 3 | Metadata Enrichment | `topics/part05-enrich/ch10-metadata-enrichment.dita` | Task | 20 min | Prolog metadata, audience, classification |
| 4 | Schema.org Mapping | `topics/part05-enrich/schema-org-mapping.dita` | Reference | 15 min | DITA-to-Schema.org type mapping for AI |
| 5 | Migration Step-by-Step | `topics/part05-enrich/ch06-migration-step-by-step.dita` | Task | 30 min | 9-step migration from Markdown to DITA. Taxonomy prerequisite is now optional — includes an inline starter subject scheme so you can proceed without Part 4 taxonomy knowledge |
| 6 | DITAVAL Filtering | `topics/part08-customize/ditaval-filtering-variants.dita` | Concept | 20 min | Multi-variant builds for audience/platform |

#### Do

**Exercise 3W:** `learner-exercises/phase3-publishing-builds.dita` (60–90 min)
- Create DITAVAL files for web vs. print variants
- Add `platform` and `audience` attributes to your content
- Build HTML5 with `--args.filter=web.ditaval`
- Build PDF output
- Compare outputs — verify filtering worked
- Add prolog metadata to improve findability

**Starter Project:** Explore `examples/dita-html5-sidebar-starter-v1/` first (minimal), then `examples/dita-html5-sidebar-starter-v2/` (multi-variant). Build both:
```bash
# v1 - simple
cd examples/dita-html5-sidebar-starter-v1
dita -i sample.ditamap -f html5 -o out/ --nav-toc=full

# v2 - with variants
cd examples/dita-html5-sidebar-starter-v2
dita -i sample.ditamap -f html5 -o out/html-web --args.filter=ditaval/web.ditaval
dita -i sample.ditamap -f html5 -o out/html-print --args.filter=ditaval/print.ditaval
```

> **💡 Try This:** After building v2 with web.ditaval and then print.ditaval, compare the two outputs side-by-side. Elements with `platform="web"` should appear in the web build only and vice versa. This is conditional publishing in action.

> **⚠️ Watch Out:** Exercise topics now include `platform` and `audience` attributes for filtering practice. Build with `web.ditaval` and `print.ditaval` and compare — elements marked `platform="web"` should only appear in the web build, and vice versa.

**Migration Practice:** Explore the `samples/` directory (11 files)
- Open `samples/before/training-overview.xml` alongside `samples/after/what-is-dita.dita` and `samples/after/training-modules.dita`
- Identify the three content types mixed in the before file (concept, task, reference)
- Try splitting `samples/before/docker-for-dita-ot.xml` into a DITA concept yourself, then compare with `samples/after/docker-for-dita-ot.dita`
- See `samples/README.md` for the full cross-reference table mapping each pair to guide chapters

#### Checkpoint ✓ [W]
- [ ] You built HTML5 and PDF output from the same source
- [ ] You created DITAVAL files and built filtered variants
- [ ] You added prolog metadata (audience, category, keywords)
- [ ] You can explain single-source multi-channel publishing

---

### Phase 3E: Architecture Deep Dive — Engineer Track

**Personas:** [E] | **Estimated time:** 5–7 hours | **Parts:** 6 & 7

#### Read (in order)

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 1 | DITA-OT Architecture & DevOps | `topics/part07-develop/dita-ot-developer-handbook.dita` | Concept | 25 min | DITA-OT as a pipeline: input → preprocess → transform → output |
| 2 | Core Architecture | `topics/part07-develop/ot-mental-model.dita` | Concept | 25 min | How DITA-OT is built, multi-stage processing |
| 3 | Preprocessing Deep Dive | `topics/part07-develop/preprocessing-deep-dive.dita` | Concept | 30 min | 11-step preprocessing pipeline |
| 4 | Map-First Preprocessing | `topics/part07-develop/map-first-preprocessing.dita` | Concept | 15 min | preprocess vs preprocess2 (DITA-OT 4.x default) |
| 5 | Extension Points | `topics/part07-develop/extension-points-fundamentals.dita` | Concept | 15 min | How plugins hook into the pipeline |
| 6 | Repository Layout | `topics/part07-develop/repo-layout-and-variants.dita` | Reference | 10 min | Project structure for multi-variant docs |
| 7 | Architecture Diagram | `topics/appendices/architecture-diagram.dita` | Reference | 10 min | Visual map of entire DITA-OT pipeline |
| 8 | DITA Publishing | `topics/part06-publish/dita-publishing.dita` | Concept | 50 min | Build commands, parameters, properties files |
| 9 | Docker Basics | `topics/part07-develop/docker-basics.dita` | Concept | 10 min | Canonical Docker pattern for DITA-OT |
| 10 | CI/CD Pipelines | `topics/part06-publish/cicd-publishing-pipelines.dita` | Concept | 45 min | GitHub Actions, GitLab CI, Jenkins examples |

#### Do

**Exercise 3E:** `learner-exercises/phase3-architecture-exploration.dita` (60–90 min)
- Run a build with `--temp /tmp/my-dita-temp` and examine the temp directory
- Run with `-v` (verbose) flag and identify each preprocessing step in the log
- Run `dita plugins` to list installed plugins and extension points
- Debug a build: find the preprocessed XML in temp, compare with source
- Trace how a conref is resolved by inspecting temp files before/after

> **💡 Try This:** Run the same build twice — once with default `preprocess` and once forcing `preprocess2`. Compare the temp directories. In DITA-OT 4.x, `preprocess2` is the default for HTML5 (map-first approach). Understanding this distinction is critical for plugin development.

> **⚠️ Watch Out:** GAP-08 notes that architecture topics have no runnable code. You must create your own experiments. The temp directory inspection is not documented step-by-step — your exercise file fills this gap.

#### Checkpoint ✓ [E]
- [ ] You can describe the 11-step preprocessing pipeline from memory
- [ ] You've inspected the temp directory and identified intermediate files
- [ ] You understand preprocess vs preprocess2 and when each applies
- [ ] You can list installed plugins and their extension points
- [ ] You know what `dita.xsl.html5` and `dita.xsl.html5.toc` extension points do

---

### Phase 4: Developer Mastery — Plugin & XSLT Customization

**Personas:** [E] primary, optional [W] for awareness | **Estimated time:** 12–18 hours | **Parts:** 7 & 8

This is the most substantial phase. Read the concept topics first, then work through the labs progressively.

#### Read (in order)

**Foundation (read before any lab):**

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 1 | XSLT Prerequisites | `topics/part08-customize/xslt-prerequisites.dita` | Concept | 15 min | XSLT basics, import precedence, @class matching |
| 2 | HTML5 Transform Architecture | `topics/part08-customize/html5-transform-architecture.dita` | Concept | 20 min | What you're customizing — 3 phases of HTML5 transform |
| 3 | Safe Customization Strategies | `topics/part08-customize/safe-customization-strategies.dita` | Concept | 15 min | Plugin + import (Strategy A) vs args.xsl (Strategy B) |
| 4 | Create HTML5 Plugin | `topics/part08-customize/create-html5-plugin.dita` | Task | 25 min | Your first plugin — plugin.xml + dita --install |
| 5 | First Override XSLT | `topics/part08-customize/first-override-xslt.dita` | Concept | 20 min | Import defaults, xsl:next-match, safe layering |
| 6 | Plugin Template | `topics/part07-develop/plugin-template.dita` | Task | 30 min | Complete working plugin example |

**Intermediate (read after Labs 1–2):**

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 7 | Extended Element Overrides | `topics/part08-customize/extended-element-overrides.dita` | Reference | 25 min | Copy-paste XSLT for ph, xref, fig, li, dl, hazard |
| 8 | Sidebar TOC Baseline | `topics/part08-customize/sidebar-toc-chunking-baseline.dita` | Concept | 15 min | nav-toc=full, properties files, chunking |
| 9 | Sidebar TOC Customization | `topics/part08-customize/sidebar-toc-customization.dita` | Concept | 20 min | CSS-only vs XSLT TOC markup customization |
| 10 | TOC Grouping | `topics/part08-customize/toc-grouping.dita` | Concept | 10 min | topichead/topicgroup for non-clickable headings |
| 11 | Production Patterns | `topics/part08-customize/production-patterns.dita` | Reference | 25 min | Topic wrappers, paragraph hooks, note callouts |

**Advanced (read after Labs 3–4):**

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 12 | Passing Parameters | `topics/part08-customize/passing-parameters.dita` | Reference | 10 min | CLI, properties files, conductor param injection |
| 13 | DITAVAL Filtering & Variants | `topics/part08-customize/ditaval-filtering-variants.dita` | Concept | 20 min | Multi-variant build patterns |
| 14 | Debugging Workflow | `topics/part08-customize/debugging-workflow.dita` | Task | 20 min | Inspect temp → find template → override → verify |
| 15 | Debugging Playbook | `topics/part07-develop/debugging-playbook.dita` | Reference | 20 min | Symptom → cause table for common failures |
| 16 | Production Hardening | `topics/part08-customize/production-hardening.dita` | Concept | 15 min | Version pinning, CI pipeline, upgrade strategy |
| 17 | Safe XSLT Import | `topics/part07-develop/safe-customization-xslt-import.dita` | Concept | 15 min | Import layer patterns |
| 18 | Robust XSLT Patterns | `topics/part07-develop/robust-xslt-patterns.dita` | Concept | 15 min | Class-based matching, wrappers, next-match |
| 19 | Technical Reference | `topics/part08-customize/dita-ot-technical-reference.dita` | Concept | 30 min | Glossary of XSLT patterns |
| 20 | Quick Checklists | `topics/part08-customize/quick-checklists.dita` | Reference | 10 min | Safe override, sidebar, release checklists |

**DevOps & Infrastructure:**

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 21 | Docker Basics | `topics/part07-develop/docker-basics.dita` | Concept | 10 min | Canonical `docker run` pattern for DITA-OT |
| 22 | Custom Docker Images | `topics/part07-develop/custom-docker-images.dita` | Task | 15 min | Dockerfile with custom plugins baked in |
| 23 | Docker Compose Preview | `topics/part07-develop/docker-compose-preview.dita` | Task | 15 min | Local preview environment |
| 24 | GitHub Actions CI/CD | `topics/part07-develop/github-actions-cicd.dita` | Reference | 40 min | 4 production-ready YAML workflows |
| 25 | Developing from Source | `topics/part07-develop/developing-from-source.dita` | Task | 25 min | Gradle build from source |

#### Do — Progressive Labs

The labs in `exercises/` are the core hands-on experience. They use a scaffold approach — code is commented out in the plugin files, and you uncomment each section as you progress.

**Lab Setup:**
```bash
# Install the exercise plugin
cd /path/to/dita-ot
dita --install /path/to/exercises/plugins/com.extense.html5.labs

# Build baseline (no customization yet)
dita -i /path/to/exercises/lab-sample.ditamap -f html5 \
  -o out/baseline --nav-toc=full
```

| Lab | Goal | Time | Files to Edit | What You Learn |
|-----|------|------|---------------|---------------|
| **Lab 1** | Callout note styling | 30 min | `override.xsl`, `brand.css` | `xsl:next-match`, `@outputclass`, CSS hooks |
| **Lab 2** | Step anchors + deep linking | 45 min | `override.xsl`, `step-highlight.js`, `brand.css` | Template matching on `topic/task/steps/step`, generating IDs |
| **Lab 3** | Custom `<meta>` tag injection | 30 min | `override.xsl` | Overriding `chapterHead` named template |
| **Lab 4** | Collapsible sidebar TOC | 45 min | `toc-override.xsl`, `sidebar-toggle.js`, `brand.css` | `dita.xsl.html5.toc` extension point |
| **Lab 5** | Full plugin packaging + CI | 30 min | `plugin.xml`, `sample-github-workflow.yml` | Plugin metadata, versioning, CI integration |

Detailed lab instructions: `topics/part08-customize/exercises-and-labs.dita` (~500 lines, 120 min)

**Exercise 4:** `learner-exercises/phase4-plugin-development.dita` (90–120 min)
- Build a complete HTML5 plugin from scratch
- Implement XSLT override with `xsl:import` and `xsl:next-match`
- Add custom CSS and JavaScript
- Install, test, and iterate

> **💡 Try This:** After completing each lab, compare the output with the baseline build. Use browser dev tools to inspect the HTML. Look for the `data-*` attributes, CSS classes, and wrapper `<div>` elements your XSLT added. This is how you verify XSLT overrides work correctly.

> **⚠️ Watch Out:** ~~GAP-04 identifies a bug in Lab 3 — it uses `xsl:next-match` inside a named template (`chapterHead`).~~ **Resolved:** Lab 3 now correctly overrides the `gen-user-head` named template, which is DITA-OT’s designated hook for adding custom `<head>` content. No `xsl:next-match` is needed.

> **⚠️ Watch Out:** Always match on DITA `@class` attributes, never on element names directly. `match="*[contains(@class, ' topic/note ')]"` works for all specializations. `match="note"` only matches the base element and breaks specialized content.

**Starter Repo Integration:**
After completing labs, follow `topics/part08-customize/starter-repo-guide.dita` to integrate your plugin into the v2 starter project for production use.

#### Checkpoint ✓ [E]
- [ ] You created a DITA-OT plugin from scratch (plugin.xml + XSLT + CSS)
- [ ] You completed Labs 1–5 with verified output
- [ ] You can override any HTML5 element using `@class`-based matching
- [ ] You understand import precedence and `xsl:next-match` layering
- [ ] You can debug XSLT issues using temp directory inspection
- [ ] You've packaged a plugin for CI/CD deployment

---

### Phase 5: Advanced Integration & Capstone

**Personas:** [Both] | **Estimated time:** 5–8 hours | **Parts:** 9 & 10

#### Read

**AI Integration — [E] primary, [W] awareness:**

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 1 | RAG Pipeline Architecture | `topics/part09-integrate/ch11-rag-pipeline-architecture.dita` | Concept | 15 min | 4-stage pipeline: ingest → retrieve → rerank → generate |
| 2 | Chunking & Embedding | `topics/part09-integrate/ch12-chunking-and-embedding.dita` | Concept | 15 min | Section-aware chunking, metadata inheritance |
| 3 | Retrieval & Generation | `topics/part09-integrate/ch13-retrieval-and-generation.dita` | Concept | 15 min | Filtered vector search, cross-encoder reranking |

**Measuring Impact — [W] primary, [E] awareness:**

| # | Topic | File | Type | Time | Key Takeaway |
|---|-------|------|------|------|--------------|
| 4 | Benefits & ROI | `topics/part10-measure/ch14-benefits-and-roi.dita` | Concept | 10 min | Before/after metrics (8 KPIs) |
| 5 | Utilizing Intelligent Features | `topics/part10-measure/ch15-utilizing-intelligent-features.dita` | Reference | 15 min | 6 features: metadata retrieval, intent routing, schema.org |
| 6 | Impact on Final Product | `topics/part10-measure/ch16-impact-on-final-product.dita` | Concept | 10 min | Chatbot, web, PDF, and maintenance impact |

**Reference (keep as lookup):**

| # | Topic | File | Type | Purpose |
|---|-------|------|------|---------|
| 7 | Plugin Reference | `topics/appendices/plugin-reference.dita` | Reference | Complete code listings |
| 8 | Architecture Diagram | `topics/appendices/architecture-diagram.dita` | Reference | Pipeline visual reference |
| 9 | Glossary | `topics/appendices/glossary.dita` | Glossary | 15+ DITA terms |

#### Do — Capstone Project

**Exercise 5:** `learner-exercises/phase5-capstone-project.dita` (2–3 hours)

**[W] Writer Capstone:**
- Expand your TaskFlow project to 8+ topics across all 3 types
- Create a bookmap with frontmatter and 3 chapters
- Implement keydefs, conrefs, and relationship tables
- Build 3 variants (web, print, admin-audience)
- Add complete prolog metadata to every topic

**[E] Engineer Capstone:**
- Create a CI/CD pipeline (GitHub Actions) that:
  - Installs DITA-OT in Docker
  - Installs your custom plugin
  - Builds all variants
  - Deploys HTML to GitHub Pages
- Set up Docker Compose for local preview
- Implement quality gates (strict mode, link checking)

**[Both] Quality Review:**
- Cross-check all conrefs resolve correctly
- Verify DITAVAL filtering produces correct variants
- Run in strict mode: `--processing-mode=strict`
- Review output for consistency

> **💡 Try This:** For the capstone, model your project on a real documentation need. If you have actual product docs to migrate, use the 9-step migration process in `ch06-migration-step-by-step.dita` as your guide.

#### Checkpoint ✓ [Both]
- [ ] [W] Authored 8+ topics organized in a bookmap with 3 chapters
- [ ] [W] Built 3 filtered variants from single source
- [ ] [E] Created a Docker-based CI/CD pipeline
- [ ] [E] Deployed automated documentation builds
- [ ] [Both] All builds pass in strict mode with zero errors

---

## 3. Exercise Inventory & Gaps

### Available Exercises

| Exercise | Location | Persona | Self-Contained? | Clear Instructions? | Expected Output? |
|----------|----------|---------|-----------------|---------------------|-----------------|
| Phase 1: Setup Verification | `learner-exercises/phase1-setup-verification.dita` | [Both] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| Phase 2: First Topics | `learner-exercises/phase2-first-topics.dita` | [Both] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| Phase 2: Maps & Reuse | `learner-exercises/phase2-maps-and-reuse.dita` | [Both] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| Phase 3W: Publishing | `learner-exercises/phase3-publishing-builds.dita` | [W] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| Phase 3E: Architecture | `learner-exercises/phase3-architecture-exploration.dita` | [E] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| Phase 4: Plugin Dev | `learner-exercises/phase4-plugin-development.dita` | [E] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| Phase 5: Capstone | `learner-exercises/phase5-capstone-project.dita` | [Both] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| WidgetPro Tutorial | `topics/part03-author/writing-first-dita-project.dita` | [Both] | ✅ Yes | ✅ Yes (9 steps + 3 experiments) | ⚠️ No screenshots |
| Migration Exercise | `topics/part05-enrich/ch06-migration-step-by-step.dita` | [Both] | ✅ Yes | ✅ Yes (9 steps) | ⚠️ Partial |
| Lab 1: Callout Notes | `topics/part08-customize/exercises-and-labs.dita` | [E] | ✅ Yes | ✅ Yes | ⚠️ No screenshots |
| Lab 2: Step Anchors | `topics/part08-customize/exercises-and-labs.dita` | [E] | ✅ Yes | ✅ Yes | ⚠️ No screenshots |
| Lab 3: Meta Tags | `topics/part08-customize/exercises-and-labs.dita` | [E] | ✅ Yes | ✅ Yes (gen-user-head override) | ⚠️ No screenshots |
| Lab 4: Collapsible TOC | `topics/part08-customize/exercises-and-labs.dita` | [E] | ✅ Yes | ✅ Yes | ⚠️ No screenshots |
| Lab 5: Plugin + CI | `topics/part08-customize/exercises-and-labs.dita` | [E] | ✅ Yes | ✅ Yes | ⚠️ Partial |
| Exercise Topics (5) | `exercises/topics/*.dita` | [E] | ✅ Yes | ✅ Yes | ✅ Build target provided |

### Missing Exercises (Gaps)

| Gap | Phase | Persona | Why It Matters |
|-----|-------|---------|----------------|
| No inline "Try It" in concept topics | Phase 1–2 | [Both] | Passive reading without reinforcement (GAP-06) |
| No PDF customization exercise | Phase 4 | [E] | PDF is a primary output but has zero hands-on coverage (GAP-10) |
| No conref/keyref debugging exercise | Phase 2 | [Both] | When conrefs break, beginners don't know how to diagnose |
| ~~No DITAVAL exercise with visible filtering~~ | ~~Phase 3W~~ | ~~[W]~~ | ~~Resolved: exercise topics now have `platform` and `audience` attributes~~ |
| ~~No keyref usage in exercises~~ | ~~Phase 2~~ | ~~[Both]~~ | ~~Resolved: exercise topics now use `<keyword keyref="product-name"/>`~~ |
| No plugin unit testing exercise | Phase 4 | [E] | No coverage of testing custom plugins (GAP-13) |
| No visual output examples anywhere | All | [Both] | Can't verify if output looks correct (GAP-07) |

---

## 4. Example Project Walkthrough

### Recommended Order

**[W] Technical Writer Path:**

1. **Start with v1 starter** → `examples/dita-html5-sidebar-starter-v1/`
   - Minimal, 3 topics, no filtering
   - Build: `dita -i sample.ditamap -f html5 -o out/ --nav-toc=full`
   - Goal: See basic DITA → HTML5 transform in action

2. **Progress to v2 starter** → `examples/dita-html5-sidebar-starter-v2/`
   - Multi-variant with DITAVAL filtering
   - Build all variants using provided scripts
   - Goal: Understand production-grade conditional publishing

3. **Explore exercise topics** → `exercises/topics/`
   - 5 realistic topics (AcmeDoc product)
   - Build: `dita -i exercises/lab-sample.ditamap -f html5 -o out/ --propertyfile=exercises/build/html5.properties`
   - Goal: See professionally structured content

**[E] Software Engineer Path:**

1. **Start with v1 starter** → same as Writer (understand the content first)

2. **Exercise labs** → `exercises/plugins/com.extense.html5.labs/`
   - Install plugin, work through Labs 1–5
   - Inspect `plugin.xml`, understand extension point declarations
   - Goal: Master the plugin development workflow

3. **v2 starter plugin** → `examples/dita-html5-sidebar-starter-v2/`
   - Study the multi-variant build system
   - Examine DITAVAL files and build scripts
   - Goal: Understand production architecture

4. **Starter repo integration** → follow `topics/part08-customize/starter-repo-guide.dita`
   - Integrate your custom plugin into the starter project
   - Goal: Production deployment pattern

### Build Script Status

| Script/Config | Location | Status |
|------|----------|--------|
| `html5.properties` | `exercises/build/html5.properties` | ✅ Working |
| `web.ditaval` | `exercises/build/ditaval/web.ditaval` | ✅ Valid XML |
| `print.ditaval` | `exercises/build/ditaval/print.ditaval` | ✅ Valid XML |
| `lab-sample.ditamap` | `exercises/lab-sample.ditamap` | ✅ Valid |
| v2 build scripts | `examples/dita-html5-sidebar-starter-v2/` | ✅ Present |
| `dita-preview.py` | Root directory | ✅ Available for instant preview |
| `build-branded-html5.sh` | Root directory | ✅ Available |
| `build-branded-pdf.sh` | Root directory | ✅ Available |

---

## 5. Difficulty Progression Assessment

### Progression Map

```
Phase 1: ●○○○○ (Beginner)     — Read concepts, install tools
Phase 2: ●●○○○ (Beginner+)    — Write topics, learn information typing, create maps
Phase 3W: ●●●○○ (Intermediate) — Build & filter outputs
Phase 3E: ●●●○○ (Intermediate) — Understand pipeline architecture
Phase 4:  ●●●●○ (Advanced)     — XSLT, plugins, production patterns
Phase 5:  ●●●●● (Expert)       — CI/CD, Docker, AI integration, capstone
```

### Difficulty Jump Analysis

| Transition | Smoothness | Issue | Mitigation |
|-----------|------------|-------|------------|
| Phase 1 → 2 | ✅ Smooth | — | XML syntax primer in Part 2 bridges the gap; WidgetPro tutorial includes inline tips explaining DOCTYPE, keyref, and conref as you encounter them |
| Phase 2 → 3W | ✅ Smooth | — | Natural progression from authoring to publishing |
| Phase 2 → 3E | ⚠️ Moderate jump | Leap from authoring to pipeline internals | Read `ot-mental-model.dita` first; it provides a good on-ramp |
| Phase 3E → 4 | ⚠️ Significant jump | XSLT prerequisites assumed | `xslt-prerequisites.dita` helps but assumes some XSLT knowledge. Engineers without XSLT background need external XSLT tutorial first |
| Phase 4 Labs 1–2 → Labs 3–4 | ✅ Smooth | — | Progressive difficulty within labs is well-designed |
| Phase 4 → 5 | ⚠️ Moderate jump | AI integration (Part 9) is purely conceptual; no hands-on | Phase 5 capstone bridges this for engineers; writers may feel disconnected from AI topics |

### Missing Prerequisites

| Topic | Assumes | What's Missing |
|-------|---------|---------------|
| XSLT customization topics | XSLT 2.0 knowledge | External XSLT tutorial or expanded `xslt-prerequisites.dita` |
| Docker topics | Docker basics | Docker installation and container concepts |
| GitHub Actions CI/CD | Git + GitHub familiarity | No Git basics topic |
| RAG Pipeline (Part 9) | ML/embedding concepts | No AI/ML primer — acceptable for advanced section |

### Track Isolation Assessment

- **[W] Writer track avoids unnecessary complexity:** ✅ Yes. Writers can complete Phases 1, 2, 3W, and 5 without touching XSLT, Docker, or CI/CD. The publishing topic covers build commands at a user level.
- **[E] Engineer track builds on authoring fundamentals:** ✅ Yes. Phase 2 ensures engineers understand the content they'll be automating. The progression from "use DITA-OT as a tool" (Phase 2) to "understand DITA-OT as a system" (Phase 3E) to "extend DITA-OT as a developer" (Phase 4) is logical.

---

## 6. Actionable Recommendations

### Critical (blocks learning)

| # | What's Missing | Phase | Persona | Why It Matters | Suggested Content |
|---|---------------|-------|---------|---------------|-------------------|
| ~~1~~ | ~~DITA-OT installation task topic~~ | ~~Phase 1~~ | ~~[Both]~~ | ~~Resolved~~ | ✅ Now covered: `topics/part02-prepare/installing-dita-ot.dita` |
| ~~2~~ | ~~Fix Lab 3 XSLT error~~ | ~~Phase 4~~ | ~~[E]~~ | ~~Resolved~~ | ✅ Changed to `gen-user-head` named template (no `xsl:next-match` needed). GAP-04. |
| 3 | Fix conref errors in v2 install.dita | Phase 3 | [Both] | Build fails in strict mode | Fix `<p conref>` to `<note conref>` and add IDs to target elements. GAP-03. |
| ~~4~~ | ~~Add `platform` attributes to exercise topics~~ | ~~Phase 3W~~ | ~~[W]~~ | ~~Resolved~~ | ✅ Exercise topics now include `platform` and `audience` attributes. GAP-14. |

### High Priority (significant learning improvement)

| # | What's Missing | Phase | Persona | Why It Matters | Suggested Content |
|---|---------------|-------|---------|---------------|-------------------|
| 5 | Visual output examples (before/after screenshots) | All | [Both] | Learners can't verify their output is correct | Add HTML snippets or screenshots showing expected output for each lab and key transformation. GAP-07. |
| 6 | Cross-references between topics | All | [Both] | Topics feel isolated; no guided flow | Add `<related-links>` and relationship tables. GAP-02. |
| 7 | Learning objectives on each topic | All | [Both] | Learners don't know what to expect or verify | Add "After this topic, you will be able to..." section at top. GAP-05. |
| 8 | Inline micro-exercises in concept topics | Phase 1–2 | [Both] | Passive reading for 4+ hours without practice | Add "Try It" boxes: write a conref, define a key, build with nav-toc. GAP-06. |
| ~~9~~ | ~~Use keyref in exercise topics~~ | ~~Phase 2~~ | ~~[Both]~~ | ~~Resolved~~ | ✅ Exercise topics now use `<keyword keyref="product-name"/>`. GAP-15. |

### Medium Priority (completeness)

| # | What's Missing | Phase | Persona | Why It Matters | Suggested Content |
|---|---------------|-------|---------|---------------|-------------------|
| 10 | PDF customization topic | Phase 4 | [E] | PDF is a primary output format with no customization guidance | FO basics, fonts, margins, headers/footers, extension points. GAP-10. |
| ~~11~~ | ~~Editor setup guide~~ | ~~Phase 1~~ | ~~[Both]~~ | ~~Resolved~~ | ✅ Now covered: `topics/part02-prepare/setting-up-authoring-tools.dita` (Oxygen XML Editor, 8 steps) |
| 12 | Plugin unit testing | Phase 4 | [E] | No way to validate plugin correctness automatically | Test framework, assertion patterns, CI integration. GAP-13. |
| 13 | Expand glossary | Reference | [Both] | Only 15+ terms; missing many terms used in training | Add 20+ terms: bookmap, key scope, branch filtering, conkeyref, etc. GAP-17. |
| 14 | Flesh out passing-parameters.dita | Phase 4 | [E] | Weakest reference topic; stubs without code | Complete properties file example, conductor params, build commands. GAP-20. |

---

## 7. Summary Table

| Phase | Persona | Topics to Read | Exercises | Estimated Hours |
|-------|---------|---------------|-----------|-----------------|
| **1: Foundation** | [Both] | 8 topics (Parts 1–2) | `phase1-setup-verification.dita` | 3–4 hrs |
| **2: Authoring** | [Both] | 7 topics (Parts 3–4) | `phase2-first-topics.dita`, `phase2-maps-and-reuse.dita`, WidgetPro tutorial | 6–8 hrs |
| **3W: Publishing** | [W] | 6 topics (Parts 5–6) | `phase3-publishing-builds.dita`, v1/v2 starters | 4–5 hrs |
| **3E: Architecture** | [E] | 10 topics (Parts 6–7) | `phase3-architecture-exploration.dita` | 5–7 hrs |
| **4: Developer Mastery** | [E] | 25 topics (Parts 7–8) + Labs 1–5 | `phase4-plugin-development.dita`, `exercises-and-labs.dita` | 12–18 hrs |
| **5: Advanced & Capstone** | [Both] | 9 topics (Parts 9–10 + appendices) | `phase5-capstone-project.dita` | 5–8 hrs |
| | | | | |
| **Total [W] Track** | Writer | Phases 1+2+3W+5 = 30 topics | 5 exercises | **18–25 hrs** |
| **Total [E] Track** | Engineer | Phases 1+2+3E+4+5 = 59 topics | 7 exercises + 5 labs | **31–45 hrs** |
| **Total [Both]** | Combined | All 76 topics | All exercises + labs | **49–64 hrs** |

---

## Quick Reference: File Locations

| Resource | Path |
|----------|------|
| Training topics | `dev/Ex-tense/training-doc/organized-dita-docs/topics/` |
| Learner exercises | `dev/Ex-tense/training-doc/organized-dita-docs/learner-exercises/` |
| XSLT labs | `dev/Ex-tense/training-doc/organized-dita-docs/exercises/` |
| Example starters | `dev/Ex-tense/training-doc/organized-dita-docs/examples/` |
| Lab plugin | `dev/Ex-tense/training-doc/organized-dita-docs/exercises/plugins/com.extense.html5.labs/` |
| Build configs | `dev/Ex-tense/training-doc/organized-dita-docs/exercises/build/` |
| Master bookmap | `dev/Ex-tense/training-doc/organized-dita-docs/extense-supermap.ditamap` |
| DITA-OT install | `dev/DITA-OT-Extense/dita-ot/` |
| DITA samples | `dev/DITA-OT-Extense/dita-samples/` |
| Branded plugins | `dev/Ex-tense/training-doc/organized-dita-docs/plugins/` |
| Samples (before/after) | `dev/Ex-tense/training-doc/organized-dita-docs/samples/` |
| Preview script | `dev/Ex-tense/training-doc/organized-dita-docs/tools/dita-preview.py` |

---

*Generated by analyzing 76 DITA training topics, 7 learner exercises, 5 XSLT labs, 2 starter projects, and appendix materials. Updated March 2026 to reflect: fluency restructuring, Oxygen XML Editor migration, metadata enrichment, before/after samples, branded PDF/HTML5 plugins, and AI-ready prolog on all topics.*
