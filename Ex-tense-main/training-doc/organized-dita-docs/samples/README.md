# Sample Files: Before and After

This directory contains sample source files that demonstrate the transformation from **unstructured XML** to **AI-ready DITA**. These are the same examples referenced throughout the training guide — open them side by side to see every improvement.

## Directory Structure

```
samples/
├── before/                          ← Unstructured XML source files
│   ├── reuse-and-variants.xml       ← Mixed concept content, no typing
│   ├── installing-dita-ot.xml       ← Procedure as a flat ordered list
│   ├── dita-ot-parameters.xml       ← Reference table with no semantics
│   ├── docker-for-dita-ot.xml       ← Concept with no metadata
│   └── training-overview.xml        ← Mixed content (concept + task + reference in one file)
│
└── after/                           ← AI-ready DITA topics
    ├── reuse-and-variants.dita      ← Typed concept with full metadata
    ├── installing-dita-ot.dita      ← Typed task with prereqs, steps, results
    ├── dita-ot-parameters.dita      ← Typed reference with structured tables
    ├── docker-for-dita-ot.dita      ← Concept with audience/domain targeting
    ├── what-is-dita.dita            ← Split from training-overview.xml (concept portion)
    └── training-modules.dita        ← Split from training-overview.xml (reference portion)
```

## How to Use These Files

### 1. Side-by-side comparison
Open a `before/` file and its matching `after/` file side by side. Note every structural and metadata improvement.

### 2. Practice migration
Use `before/training-overview.xml` as a migration exercise:
- Identify the three content types mixed in the file (concept, task, reference)
- Split it into separate DITA topics
- Add full AI-ready metadata following the patterns in `after/`
- Compare your result with the provided `after/` files

### 3. Follow along with the guide
These samples correspond to specific chapters:

| Sample pair | Guide reference |
|---|---|
| `reuse-and-variants` | Part 1 Ch.2, Part 3 Ch.5, Part 5 Ch.7 (Example 1) |
| `installing-dita-ot` | Part 3 Ch.5, Part 5 Ch.7 (Example 2) |
| `dita-ot-parameters` | Part 3 Ch.5 (reference type example) |
| `docker-for-dita-ot` | Part 5 Ch.7 (Example 3 — metadata comparison) |
| `training-overview` → split into `what-is-dita` + `training-modules` + `installing-dita-ot` | Part 1 Ch.4, Part 3 Ch.5 (splitting mixed content) |

## What to Look For

Each `before/` file has XML comments listing its specific problems. Each `after/` file has comments explaining every key change. Focus on:

- **Content typing:** How `<article>` becomes `<concept>`, `<task>`, or `<reference>`
- **Metadata enrichment:** The complete `<prolog>` with audience, difficulty, domain, intent
- **Structural semantics:** `<prereq>`, `<steps>/<cmd>`, `<stepresult>`, `<result>`
- **Section IDs:** Addressable sections for deep-linking and chunk boundaries
- **Question-phrased titles:** Section titles that match how users ask chatbots
- **Content splitting:** One mixed file → multiple typed, independently retrievable topics
