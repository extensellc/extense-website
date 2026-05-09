# Extended customization guide (this starter repo)

This document explains the additional features added to the starter repo:

- **DITAVAL filtering examples** for `audience` and `platform`
- **Build variants** (web/print/admin/novice)
- **topichead/topicgroup** map patterns for clean non-clickable TOC groups
- **Expanded XSLT overrides** covering more common elements with consistent classes + `data-*` hooks

---

## 1) Filtering with DITAVAL (audience/platform)

### 1.1 Where the DITAVAL files are

- `build/ditaval/web.ditaval` — excludes `platform="print"`
- `build/ditaval/print.ditaval` — excludes `platform="web"`
- `build/ditaval/audience-admin.ditaval` — excludes `audience="novice"`
- `build/ditaval/audience-novice.ditaval` — excludes `audience="admin"`

Each file uses the standard DITAVAL format:

```xml
<val>
  <prop action="exclude" att="platform" val="print"/>
</val>
```

### 1.2 Which topics contain filter examples

- `dita/topics/concepts/what-is-dita.dita`
  - paragraphs filtered by `audience` and `platform`
- `dita/topics/concepts/elements-cookbook.dita`
  - nested list items filtered by `platform`
- `dita/topics/reference/glossary.dita`
  - whole sections filtered by `platform`

### 1.3 How variants are built

Variant property files:

- `build/html5-sidebar-web.properties`
- `build/html5-sidebar-print.properties`
- `build/html5-sidebar-admin.properties`
- `build/html5-sidebar-novice.properties`

Each adds a line like:

```properties
args.filter=build/ditaval/web.ditaval
```

Run variants using the provided scripts, for example:

```bash
./build/build-web.sh
./build/build-admin.sh
```

---

## 2) TOC grouping with topichead/topicgroup

The map `dita/maps/guides/getting-started.ditamap` demonstrates:

- `<topichead navtitle="Getting started">`  
  Creates a **non-clickable** group heading in the TOC
- `<topicgroup navtitle="Reference">`  
  Creates a **non-clickable** grouping container in the TOC

This keeps sidebar navigation clean when you have many topics and want headings without landing pages.

---

## 3) Expanded HTML5 XSLT overrides

The file:

- `plugins/com.acme.html5.sidebar/xsl/html5/override.xsl`

Now provides consistent, production-friendly hooks for additional elements:

### 3.1 Phrasing content

- `topic/ph` → `<span class="dita-ph ...">` with `data-dita-class`

### 3.2 Links

- `topic/xref` preserves default link generation and re-emits with:
  - `class="dita-xref"` (+ `external` if needed)
  - `data-dita-class` from the source xref
  - external links get `target="_blank"` and `rel="noopener noreferrer"`

### 3.3 Figures and images

- `topic/fig` → `<figure class="dita-fig">`
- `topic/fig/title` → `<figcaption class="dita-figcaption">`
- `topic/image` → `<img class="dita-image" ... src="...">`

### 3.4 Lists

- `topic/li` → `<li class="dita-li" data-dita-class="...">`

### 3.5 Definition lists

- `topic/dl` → `<dl class="dita-dl">`
- `topic/dt` → `<dt class="dita-dt">`
- `topic/dd` → `<dd class="dita-dd">`

### 3.6 Draft content

- `topic/draft-comment` → `<aside class="draft-comment">`

In production, draft content is often excluded with DITAVAL.

### 3.7 Safety content

- `hazard-d/hazardstatement` and key sub-elements:
  - hazardtype
  - consequence
  - howtoavoid

---

## 4) CSS additions

See `css/brand.css` for minimal styles for:

- definition lists
- draft comments
- hazard statements

---

## 5) JS copying requirement

`override.xsl` injects `js/site.js` into `<head>`.  
The build scripts now copy `js/` into the output folder automatically.

If you run `dita ...` manually, remember to copy `js/` into the output:

```bash
mkdir -p out/html5/js
cp -r js/* out/html5/js/
```
