# XSLT Customization Lab Exercises

Complete, self-contained sample files for the 5 progressive XSLT customization labs in the DITA training guide.

## Directory Structure

```
exercises/
├── README.md                          ← You are here
├── lab-sample.ditamap                 ← Sample DITA map (build target)
│
├── topics/                            ← Sample DITA topics to build against
│   ├── what-is-acmedoc.dita           ← Concept — has all 4 note types (Lab 1)
│   ├── install-acmedoc.dita           ← Task — has 5 steps with IDs (Lab 2)
│   ├── creating-a-project.dita        ← Task — project creation walkthrough
│   ├── publishing-output.dita         ← Task — build commands with notes
│   └── cli-reference.dita             ← Reference — parameter tables
│
├── plugins/
│   └── com.extense.html5.labs/        ← Starter plug-in (Labs 1–5)
│       ├── plugin.xml                 ← Plug-in descriptor
│       ├── xsl/
│       │   ├── html5/
│       │   │   └── override.xsl       ← Topic overrides (Labs 1–3)
│       │   └── toc/
│       │       └── toc-override.xsl   ← TOC overrides (Lab 4)
│       ├── css/
│       │   └── brand.css              ← Styles for all labs
│       └── js/
│           ├── step-highlight.js      ← Step anchor JS (Lab 2)
│           └── sidebar-toggle.js      ← Sidebar toggle JS (Lab 4)
│
└── build/
    ├── html5.properties               ← Build properties for HTML5
    ├── sample-github-workflow.yml     ← CI workflow reference (Lab 5)
    └── ditaval/
        ├── web.ditaval                ← Web filter (excludes print content)
        └── print.ditaval              ← Print filter (excludes web content)
```

## Prerequisites

- **DITA-OT 4.x** installed (download from [dita-ot.org](https://www.dita-ot.org/download))
- **Java 17+** (required by DITA-OT)
- A text/XML editor (Oxygen XML Editor recommended, or VS Code with XML extension)

## Quick Start

### 1. Build the sample project (no plug-in)

```bash
# From this exercises/ directory:
dita -i lab-sample.ditamap -f html5 -o out/html5 --nav-toc=full
```

Open `out/html5/index.html` in a browser. This is your **baseline** — default DITA-OT output before any customization.

### 2. Install the starter plug-in

```bash
# Copy the plug-in into your DITA-OT installation:
cp -r plugins/com.extense.html5.labs /path/to/dita-ot/plugins/

# Integrate:
cd /path/to/dita-ot
dita --install
```

### 3. Start Lab 1

1. Open `plugins/com.extense.html5.labs/xsl/html5/override.xsl`
2. **Uncomment** the Lab 1 template (callout note styling)
3. Open `plugins/com.extense.html5.labs/css/brand.css`
4. **Uncomment** the Lab 1 CSS section
5. Rebuild:
   ```bash
   dita -i lab-sample.ditamap -f html5 -o out/html5 \
     --propertyfile=build/html5.properties
   ```
6. Compare the output — notes should now appear as colored callout boxes

### 4. Progress through Labs 2–5

Each lab builds on the previous one. Follow the same pattern:
- Uncomment the relevant XSLT template in `override.xsl` or `toc-override.xsl`
- Uncomment the corresponding CSS in `brand.css`
- Uncomment any JS files needed
- Rebuild and verify

## Lab Summary

| Lab | Focus | Files to Edit |
|-----|-------|---------------|
| 1 | Callout note styling | `override.xsl`, `brand.css` |
| 2 | Step anchors + highlighting | `override.xsl`, `brand.css`, `step-highlight.js` |
| 3 | Custom meta tag injection | `override.xsl` |
| 4 | Collapsible sidebar TOC | `toc-override.xsl`, `brand.css`, `sidebar-toggle.js` |
| 5 | Full plug-in packaging + CI | `plugin.xml`, `sample-github-workflow.yml` |

## Sample Content for Testing

The sample topics are designed to exercise each lab:

- **what-is-acmedoc.dita** — Contains all 4 note types (`note`, `tip`, `warning`, `caution`) for Lab 1 callout testing
- **install-acmedoc.dita** — Contains 5 task steps with `id` attributes for Lab 2 step-anchor testing
- **creating-a-project.dita** — Additional task topic with notes for cross-verification
- **publishing-output.dita** — Build commands topic with `caution` and `tip` notes
- **cli-reference.dita** — Reference table for verifying reference topic rendering

## Verification Checklist

After each lab, check:

- [ ] **Lab 1**: Notes in `what-is-acmedoc.html` appear as colored boxes (blue/green/orange/red)
- [ ] **Lab 2**: Navigate to `install-acmedoc.html#step-3` — step 3 scrolls into view and highlights yellow
- [ ] **Lab 3**: View source of any output page — `<meta name="generator">` tag is present in `<head>`
- [ ] **Lab 4**: Sidebar TOC appears on all pages; collapses on mobile viewport
- [ ] **Lab 5**: GitHub Actions workflow runs successfully; output is consistent across DITA-OT versions
