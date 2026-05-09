# Extense DITA Complete: From First Topic to AI-Powered Delivery

**A progressive training guide covering DITA authoring, publishing, DITA-OT development, XSLT customization, and AI pipeline integration.**

Produced by Extense LLC. 76 structured DITA topics organized in a 10-part bookmap with appendices, relationship tables, and AI-ready metadata on every topic.

---

## Documentation Structure

All content is authored in DITA XML and published via DITA-OT 4.x with branded Extense plugins for HTML5 and PDF output.

### Master Bookmap

`extense-supermap.ditamap` — the root bookmap defining the complete progressive learning path:

| Part | Title | Level | Topics |
|------|-------|-------|--------|
| I | Why Intelligent Content Matters | Beginner | 4 |
| II | Content Preparation | Beginner | 5 |
| III | Authoring DITA Content | Intermediate | 5 |
| IV | Information Architecture | Intermediate | 2 |
| V | Making Content Intelligent | Intermediate | 5 |
| VI | Publishing & Automation | Intermediate | 6 |
| VII | DITA-OT Development | Advanced | 17 |
| VIII | Advanced XSLT Customization | Advanced | 20 |
| IX | AI Pipeline & Chatbot Integration | Advanced | 3 |
| X | Benefits, Utilization & Impact | Beginner | 3 |
| App. | Appendices — Reference Material | Mixed | 5 |
| — | Frontmatter (preface) | Beginner | 1 |
| | **Total** | | **76** |

---

## Topic Types

| Type | Count | Purpose |
|------|-------|---------|
| concept | 40 | Explain what/why — foundational knowledge |
| task | 17 | Step-by-step how-to procedures |
| reference | 17 | Lookup tables, code listings, checklists |
| glossgroup | 1 | DITA/DITA-OT terminology definitions |
| topic | 1 | Before/after comparison (generic) |

---

## Getting Started

### For newcomers to DITA
1. Start with Part I — understand why structured content matters
2. Part II — install DITA-OT, set up Oxygen XML Editor, learn DITA fundamentals
3. Part III — write your first project (WidgetPro tutorial), learn topic types and reuse

### For experienced DITA authors
1. Skim Parts I–III for AI-readiness concepts
2. Part V — metadata enrichment and migration workflows
3. Part VI — publishing and CI/CD automation

### For DITA-OT developers
1. Parts VII–VIII — architecture, preprocessing, plugin development, XSLT labs
2. Part IX — RAG pipeline integration with DITA content

See `LEARNERS-STUDY-GUIDE.md` for detailed role-based learning paths with estimated times.

---

## Building the Training Guide

### Branded PDF (218 pages)
```bash
./build-branded-pdf.sh
# Output: ../output/pdf-branded/extense-supermap.pdf
```

### Branded HTML5
```bash
./build-branded-html5.sh
# Output: ../output/html5-branded/
```

### Instant Preview (single topic)
```bash
python3 dita-preview.py topics/part03-author/dita-authoring.dita --port 8124
```

### Validate DITA files
```bash
dita -i extense-supermap.ditamap -f html5 --processing-mode=strict --debug
```

---

## Learning Paths

### Path 1: Technical Writer
Parts I → II → III → IV → V → VI → X + Appendices

**Focus:** Authoring, reuse, metadata, maps, publishing workflows
**Estimated time:** 25–30 hours

### Path 2: Software Engineer
Parts I → II → III → VI → VII → VIII → IX + Appendices

**Focus:** DITA-OT architecture, plugin development, XSLT, CI/CD, Docker, AI pipelines
**Estimated time:** 40–50 hours

### Path 3: Content Strategist / Manager
Parts I → IV → V → X

**Focus:** Business case, information architecture, taxonomy, ROI measurement
**Estimated time:** 8–12 hours

---

## Hands-On Resources

### Learner Exercises (`learner-exercises/`)
7 progressive exercises aligned to the learning phases:

| Exercise | Phase | Persona |
|----------|-------|---------|
| `phase1-setup-verification.dita` | Foundation | Both |
| `phase2-first-topics.dita` | Authoring | Both |
| `phase2-maps-and-reuse.dita` | Authoring | Both |
| `phase3-publishing-builds.dita` | Publishing | Writer |
| `phase3-architecture-exploration.dita` | Architecture | Engineer |
| `phase4-plugin-development.dita` | Plugin Dev | Engineer |
| `phase5-capstone-project.dita` | Capstone | Both |

### XSLT Labs (`exercises/`)
5 hands-on labs using scaffold plugin (`com.extense.html5.labs`):

| Lab | Goal |
|-----|------|
| Lab 1 | Callout note styling |
| Lab 2 | Step anchors + deep linking |
| Lab 3 | Custom meta tag injection |
| Lab 4 | Collapsible sidebar TOC |
| Lab 5 | Full plugin packaging + CI |

### Starter Projects (`examples/`)

- **v1** (`dita-html5-sidebar-starter-v1/`) — Minimal single-variant HTML5 project. Good for learning.
- **v2** (`dita-html5-sidebar-starter-v2/`) — Production multi-variant project with DITAVAL filtering, responsive CSS, and per-variant build scripts.

### Sample Files (`samples/`)
Before/after examples showing the transformation from unstructured XML to AI-ready DITA:

- `samples/before/` — 5 unstructured XML files (no metadata, flat structure)
- `samples/after/` — 6 AI-ready DITA files (typed, full prolog, section IDs, taxonomy)
- `samples/README.md` — Description and usage guide

---

## Branded Publishing Plugins

### `plugins/com.extense.html5.branded/`
Custom HTML5 plugin with Extense branding:
- CSS styling (`brand.css`) including highlight classes (`.hi-yellow`)
- JavaScript enhancements
- Responsive layout

### `plugins/com.extense.pdf.branded/`
Custom PDF plugin with Extense branding:
- XSL-FO customizations (`custom.xsl`)
- Font configuration
- Cover page and headers/footers
- Yellow highlight support for `<ph outputclass="hi-yellow">`

---

## Shared Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Subject scheme taxonomy | `shared/extense-taxonomy.subjectScheme` | Controlled vocabulary for AI classification |
| Chatbot config | `shared/chatbot-config.json` | RAG pipeline configuration |
| Chatbot data | `shared/chatbot-data/` | Exported content for vector store |
| Metadata enrichment script | `tools/enrich-metadata.py` | Batch-add prolog metadata to topics |
| DITA-to-JSON exporter | `tools/dita-to-chatbot-json.py` | Export DITA to chatbot-ready JSON |
| Preview server | `tools/dita-preview.py` | Instant browser preview of DITA topics |

---

## Directory Layout

```
organized-dita-docs/
├── README.md                          ← This file
├── LEARNERS-STUDY-GUIDE.md            ← Detailed role-based study guide
├── extense-supermap.ditamap           ← Master bookmap (10 parts + appendices)
│
├── submaps/                           ← Part-level submaps
│   ├── part01-why-intelligent-content.ditamap
│   ├── part02-content-preparation.ditamap
│   ├── part03-authoring-dita-content.ditamap
│   ├── part04-information-architecture.ditamap
│   ├── part05-making-content-intelligent.ditamap
│   ├── part06-publishing-automation.ditamap
│   ├── part07-dita-ot-development.ditamap
│   ├── part08-xslt-customization.ditamap
│   ├── part09-ai-pipeline-integration.ditamap
│   ├── part10-benefits-utilization-impact.ditamap
│   └── appendices.ditamap
│
├── topics/                            ← All 76 DITA topics
│   ├── frontmatter/      (1 topic — preface)
│   ├── part01-why/        (4 topics)
│   ├── part02-prepare/    (5 topics)
│   ├── part03-author/     (5 topics)
│   ├── part04-architect/  (2 topics)
│   ├── part05-enrich/     (5 topics)
│   ├── part06-publish/    (6 topics)
│   ├── part07-develop/   (17 topics)
│   ├── part08-customize/ (20 topics)
│   ├── part09-integrate/  (3 topics)
│   ├── part10-measure/    (3 topics)
│   └── appendices/        (5 topics — glossary, diagrams, references)
│
├── plugins/                           ← Branded publishing plugins
│   ├── com.extense.html5.branded/     (CSS, JS, HTML5 customization)
│   └── com.extense.pdf.branded/      (XSL-FO, fonts, PDF customization)
│
├── samples/                           ← Before/after transformation examples
│   ├── before/            (5 unstructured XML files)
│   └── after/             (6 AI-ready DITA files)
│
├── exercises/                         ← XSLT lab materials
│   ├── lab-sample.ditamap
│   ├── topics/            (5 sample DITA topics)
│   ├── plugins/           (com.extense.html5.labs scaffold)
│   └── build/             (properties, DITAVALs, CI workflow)
│
├── learner-exercises/                 ← Phase-aligned exercises (7 files)
├── examples/                          ← Starter projects (v1 + v2)
├── shared/                            ← Taxonomy, chatbot config, chatbot data
├── tools/                             ← Build and utility scripts
└── web/                               ← (reserved for web output assets)
```

---

## Advanced Topics Covered

- Information architecture and topic-based design
- Key scopes and advanced key management
- Relationship tables and cross-referencing
- Subject scheme taxonomy for AI classification
- Containerized builds (Docker + docker-compose)
- CI/CD with GitHub Actions, Jenkins, Azure DevOps
- Multi-format output (HTML5, PDF)
- DITAVAL conditional filtering for audience/platform variants
- XSLT-import override patterns for upgrade-safe customization
- AI-ready metadata (prolog enrichment, Schema.org mapping)
- RAG pipeline architecture (chunking, embedding, retrieval, reranking)
- Migration from unstructured XML to DITA

---

## Additional Resources

**Official DITA Resources:**
- OASIS DITA Technical Committee: [www.oasis-open.org/committees/dita](https://www.oasis-open.org/committees/dita/)
- DITA-OT Documentation: [www.dita-ot.org](https://www.dita-ot.org)
- DITA Specification: [docs.oasis-open.org/dita](https://docs.oasis-open.org/dita/)

**Community:**
- DITA Users Group: [groups.io/g/dita-users](https://groups.io/g/dita-users)
- DITA-OT GitHub: [github.com/dita-ot/dita-ot](https://github.com/dita-ot/dita-ot)

---

**Last Updated:** March 2026
**Documentation Version:** 2.0
**DITA-OT Target Version:** 4.x
**Total:** 76 topics | 10 parts + appendices | 218-page branded PDF
