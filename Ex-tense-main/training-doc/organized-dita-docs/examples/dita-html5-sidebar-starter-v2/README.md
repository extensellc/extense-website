# DITA-OT 4.x HTML5 Sidebar TOC + Chunking — Starter Repo

This starter repo gives you a complete, working baseline for:

- **DITA-OT 4.x**
- **HTML5 output**
- **Chunking** (map-driven) so topics become separate pages
- **Sidebar TOC** embedded on every topic page (`nav-toc=full`)
- A **custom DITA-OT plug-in** that:
  - standardizes HTML wrappers across **all topic types** (topic/concept/task/reference)
  - adds useful CSS hooks + data attributes
  - renders notes as callouts
  - adds anchors + data-step attributes for task steps
  - wraps tables/codeblocks for responsive styling
  - injects `js/site.js` into the HTML `<head>`

It also includes:
- `css/brand.css` with a **sticky sidebar layout**
- `js/site.js` for:
  - codeblock **Copy** button
  - auto-highlighting the current page in the TOC (basic)
- build scripts and a properties file for repeatable builds

---

## Prerequisites

- Java (DITA-OT requirement)
- DITA-OT 4.x installed locally
- `dita` on your PATH (or call it with a full path)

---

## Repo Layout

```
dita-html5-sidebar-starter/
  build/
    html5-sidebar.properties
    build.sh
    build.ps1
  css/
    brand.css
  js/
    site.js
  dita/
    maps/
      guides/
        getting-started.ditamap
    topics/
      concepts/
        what-is-dita.dita
      tasks/
        install.dita
      reference/
        cli-reference.dita
      shared/
        reuse-snippets.dita
    media/
      images/
        sample-diagram.svg
  plugins/
    com.acme.html5.sidebar/
      plugin.xml
      xsl/
        html5/
          override.xsl
        toc/
          toc-override.xsl
  out/
    (build output goes here)
```

---

## 1) Install the plug-in into your DITA-OT

From your DITA-OT directory:

```bash
# Option A: copy
cp -r /path/to/dita-html5-sidebar-starter/plugins/com.acme.html5.sidebar /path/to/dita-ot/plugins/
dita --install
```

Or symlink and install:

```bash
ln -s /path/to/dita-html5-sidebar-starter/plugins/com.acme.html5.sidebar /path/to/dita-ot/plugins/com.acme.html5.sidebar
dita --install
```

---

## 2) Build the sample docs

### Linux/macOS
```bash
./build/build.sh
```

### Windows PowerShell
```powershell
./build/build.ps1
```

### Or run DITA-OT directly
```bash
dita -i dita/maps/guides/getting-started.ditamap -f html5 -o out/html5 \
  --propertyfile=build/html5-sidebar.properties
```

---

## 3) What to customize first

### Branding / layout (CSS)
- Edit `css/brand.css` to change sidebar width, typography, spacing, and responsiveness.

### Behavior (JS)
- Edit `js/site.js` for TOC highlight rules, search hooks, or UI enhancements.

### HTML structure (XSLT)
- Edit `plugins/com.acme.html5.sidebar/xsl/html5/override.xsl` to change HTML markup.
- Edit `plugins/com.acme.html5.sidebar/xsl/toc/toc-override.xsl` to customize TOC markup.

---

## Notes on Chunking

Chunking is primarily controlled in the map. In the sample map:
- the root branch is chunked using `chunk="to-content"` so children become separate pages (common pattern).
- you can change chunking per branch or per topicref as your IA evolves.

---

## Troubleshooting

- If your XSL override changes do not appear:
  - ensure the plug-in is installed (`dita --install`)
  - confirm you are building with `-f html5`
- If the sidebar TOC is missing:
  - confirm `nav-toc=full` in `build/html5-sidebar.properties`


---

## Build variants (DITAVAL examples: audience/platform)

This repo includes **DITAVAL** files and build variants so you can publish different outputs from the same source:

- **Platform variants**
  - **WEB**: excludes `platform="print"`
  - **PRINT**: excludes `platform="web"`
- **Audience variants**
  - **ADMIN**: excludes `audience="novice"`
  - **NOVICE**: excludes `audience="admin"`

### Where the files live

- DITAVAL files: `build/ditaval/`
- Variant properties:
  - `build/html5-sidebar-web.properties`
  - `build/html5-sidebar-print.properties`
  - `build/html5-sidebar-admin.properties`
  - `build/html5-sidebar-novice.properties`

Each variant sets `args.filter=build/ditaval/<file>.ditaval`.

### Run a variant build

Linux/macOS:
```bash
./build/build-web.sh
./build/build-print.sh
./build/build-admin.sh
./build/build-novice.sh
```

Windows PowerShell:
```powershell
./build/build-web.ps1
./build/build-print.ps1
./build/build-admin.ps1
./build/build-novice.ps1
```

### What content is filtered?

See:
- `dita/topics/concepts/what-is-dita.dita` (audience + platform paragraphs)
- `dita/topics/concepts/elements-cookbook.dita` (nested list items filtered by platform)
- `dita/topics/reference/glossary.dita` (platform-only sections)

---

## TOC grouping with topichead/topicgroup

The map (`dita/maps/guides/getting-started.ditamap`) demonstrates **non-clickable TOC groups** using:

- `<topichead navtitle="...">` for headings
- `<topicgroup navtitle="...">` for grouping

This produces clean, non-clickable TOC groups in the sidebar when `nav-toc=full`.

---

## Extended XSLT overrides (more common elements)

The HTML5 override now adds consistent CSS hooks + `data-dita-class` attributes for additional elements:

- `ph`
- `xref` (preserves default link generation and adds hooks; external links get `target/_blank` + `rel`)
- `fig` + `fig/title`
- `image`
- `li`
- `dl`, `dlentry`, `dt`, `dd`
- `draft-comment`
- `hazardstatement` (and sub-elements)

See: `plugins/com.acme.html5.sidebar/xsl/html5/override.xsl`



## More documentation

- See `docs/extended-xslt-customization.md` for the filtering + TOC grouping + expanded XSLT override details.
