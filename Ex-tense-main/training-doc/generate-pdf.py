#!/usr/bin/env python3
"""
Generate a branded, reorganized DITA Training Guide PDF.

Reorganization strategy:
 - Merge two overlapping intro files (#2 short + #3 deep) into one chapter
   by using the short intro as "Chapter 1" and the deep overview as "Chapter 2"
   with the deep overview's duplicate appendix stripped.
 - Merge two near-duplicate developer guides (#7 + #8) by keeping the handbook
   as the primary and the tech guide as a companion chapter, stripping its
   duplicate architecture/preprocessing content already covered.
 - Strip the identical "Appendix — Expanded notes" boilerplate that is
   copy-pasted into 4 core files and consolidate into one Appendix at the end.
 - Group chapters into 4 training Parts for a clear learning path.
 - Add the architecture diagram as a visual reference appendix.
"""

import markdown
from weasyprint import HTML
from pathlib import Path
import re

DOCS_ROOT = Path("/home/upkar/dev/Ex-tense/training-doc/organized-dita-docs/markdown-source")
OUTPUT_PDF = Path("/home/upkar/dev/Ex-tense/training-doc/DITA-Documentation-Guide.pdf")

# ── Emoji → styled text replacement map ─────────────────────────────────
# WeasyPrint fonts don't include emoji glyphs, so we replace them with
# readable text labels that render cleanly in the PDF.
EMOJI_MAP = {
    "⚡": "»",
    "🎯": "◆",
    "✅": "✓",
    "❌": "✗",
    "📖": "▸",
    "✍️": "▸",
    "🔄": "▸",
    "🚀": "▸",
    "🏗️": "▸",
    "🔧": "▸",
    "🐳": "▸",
    "⚙️": "▸",
    "📊": "▸",
    "📈": "▸",
    "💼": "▸",
    "🤝": "▸",
    "📚": "■",
    "👀": "▸",
    "🧪": "▸",
    "📋": "▸",
    "💡": "★",
    "🎓": "■",
    "🏁": "■",
    "🚨": "▲",
    "📞": "■",
    "🔍": "■",
    "🛠️": "■",
    "🧪": "■",
    "📦": "■",
    "🎨": "■",
    "🔗": "■",
    "→": "→",      # keep real arrow (renders fine)
}

def replace_emoji(text):
    """Replace emoji characters with PDF-safe symbols."""
    for emoji, replacement in EMOJI_MAP.items():
        text = text.replace(emoji, replacement)
    return text


# ── helpers ──────────────────────────────────────────────────────────────
def read_md(path):
    return replace_emoji(path.read_text(encoding="utf-8"))

def strip_duplicate_appendix(text):
    """Remove the duplicate 'Appendix — Expanded notes' boilerplate and
       'Next topic' / 'Closing guidance' nav sections that are copy-pasted
       across multiple files.  Keep content before the first occurrence."""
    # Find FIRST occurrence of the appendix heading
    patterns = [
        r'\n## Appendix — Expanded notes.*',
        r'\n## Next topic\s*\n.*?(?=\n## |\Z)',
        r'\n## Closing guidance\s*\n.*?(?=\n## Appendix|\Z)',
    ]
    for pat in patterns:
        text = re.split(pat, text, maxsplit=1)[0]
    return text.rstrip()

def strip_sections_by_heading(text, headings_to_strip):
    """Remove specific H2 sections by heading text."""
    for heading in headings_to_strip:
        # Remove from "## heading" to the next "## " or end
        pattern = rf'\n## {re.escape(heading)}.*?(?=\n## |\Z)'
        text = re.sub(pattern, '', text, count=1, flags=re.DOTALL)
    return text

def strip_first_h1(text):
    """Remove the first H1 line since we add our own chapter title."""
    return re.sub(r'^# .+\n+', '', text, count=1)

def process_chapter(path, strip_appendix=True, strip_h1=True, strip_headings=None):
    """Read a markdown file, optionally clean it up."""
    text = read_md(path)
    if strip_appendix:
        text = strip_duplicate_appendix(text)
    if strip_headings:
        text = strip_sections_by_heading(text, strip_headings)
    if strip_h1:
        text = strip_first_h1(text)
    return text


# ── Define the reorganized training structure ────────────────────────────
# Matches the ditamap: dita-training-guide.ditamap
#   PART I:   FOUNDATIONS (5 chapters)
#   PART II:  CORE AUTHORING SKILLS (3 chapters)
#   PART III: ARCHITECTURE & PUBLISHING (2 chapters)
#   PART IV:  DITA-OT DEVELOPMENT (3 chapters)
#   APPENDICES: Glossary + Plugin Reference

PARTS = [
    {
        "part_num": "I",
        "part_title": "Foundations",
        "part_desc": "Understanding DITA, setting up your environment, and getting started",
        "chapters": [
            {
                "num": "1",
                "title": "Quick Start Guide",
                "subtitle": "Get oriented in 30 minutes \u2014 role-based learning paths",
                "source": DOCS_ROOT / "QUICK-START.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "2",
                "title": "DITA at a Glance",
                "subtitle": "The mental model \u2014 topics, maps, reuse, and publishing",
                "source": DOCS_ROOT / "getting-started/dita_intro_guide.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "3",
                "title": "DITA Deep Dive",
                "subtitle": "Information typing, specialization, the Darwin philosophy, and when DITA is the right fit",
                "source": DOCS_ROOT / "getting-started/dita-topic-1-overview.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "4",
                "title": "Installing DITA-OT",
                "subtitle": "Download, install, and verify DITA-OT on Windows, macOS, and Linux",
                "source": DOCS_ROOT / "getting-started/installing-dita-ot.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "5",
                "title": "Setting Up Authoring Tools",
                "subtitle": "Configure VS Code, Oxygen XML, or a text editor for DITA authoring",
                "source": DOCS_ROOT / "getting-started/setting-up-authoring-tools.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
        ],
    },
    {
        "part_num": "II",
        "part_title": "Core Authoring Skills",
        "part_desc": "Hands-on authoring, your first project, content reuse, and variant management",
        "chapters": [
            {
                "num": "6",
                "title": "Authoring DITA Topics",
                "subtitle": "Topic types, chunking, IDs, writing style, templates, and team workflows",
                "source": DOCS_ROOT / "core-topics/dita-topic-2-authoring.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "7",
                "title": "Writing Your First DITA Project",
                "subtitle": "End-to-end tutorial \u2014 create topics, a map, keys, conref, and build HTML5 output",
                "source": DOCS_ROOT / "core-topics/writing-first-dita-project.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "8",
                "title": "Reuse, Keys & Variant Management",
                "subtitle": "Conref, keyref, conkeyref, DITAVAL filtering, and governance patterns",
                "source": DOCS_ROOT / "core-topics/dita-topic-3-reuse-variants.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
        ],
    },
    {
        "part_num": "III",
        "part_title": "Architecture & Publishing",
        "part_desc": "Understand the DITA-OT pipeline, then master publishing workflows",
        "chapters": [
            {
                "num": "9",
                "title": "DITA-OT Architecture",
                "subtitle": "Visual reference of the processing pipeline \u2014 preprocess, transform, and output",
                "source": DOCS_ROOT / "reference/dita-ot-architecture-ascii-snippet.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "10",
                "title": "Publishing with DITA-OT",
                "subtitle": "Build commands, project files, output customization, debugging, and CI automation",
                "source": DOCS_ROOT / "core-topics/dita-topic-4-publishing-dita-ot.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
        ],
    },
    {
        "part_num": "IV",
        "part_title": "DITA-OT Development",
        "part_desc": "Plugin development, XSLT customization, DevOps, and building from source",
        "chapters": [
            {
                "num": "11",
                "title": "DITA-OT Developer Handbook",
                "subtitle": "Pipeline internals, preprocessing, Docker, GitHub Actions, and repo layout",
                "source": DOCS_ROOT / "developer-guides/dita-ot-developer-handbook.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "12",
                "title": "Technical Reference",
                "subtitle": "XSLT patterns, extension points, and developer glossary",
                "source": DOCS_ROOT / "developer-guides/dita-ot-dev-technical-guide.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
            {
                "num": "13",
                "title": "XSLT Customization Tutorial",
                "subtitle": "Hands-on labs \u2014 build a complete HTML5 customization plugin from scratch",
                "source": DOCS_ROOT / "plugins-and-customization/dita-ot-html5-xslt-customization-final.md",
                "strip_appendix": False,
                "strip_headings": None,
            },
        ],
    },
]

# Appendices (matching ditamap)
APPENDICES = []

# ── Markdown converter ──────────────────────────────────────────────────
md_converter = markdown.Markdown(
    extensions=["fenced_code", "tables", "toc", "codehilite", "smarty"]
)

def md_to_html(text):
    md_converter.reset()
    return md_converter.convert(text)


# ── Build the HTML ───────────────────────────────────────────────────────
print("Building DITA Training Guide PDF…\n")

all_sections = []  # (type, html)
flat_toc = []      # for TOC

for part in PARTS:
    pn = part["part_num"]
    pt = part["part_title"]
    pd = part["part_desc"]

    # Part divider page
    all_sections.append(("part", f"""
    <section class="part-page">
      <div class="part-label">PART {pn}</div>
      <h1 class="part-title">{pt}</h1>
      <p class="part-desc">{pd}</p>
    </section>
    """))

    flat_toc.append(("part", pn, pt, pd))

    for ch in part["chapters"]:
        print(f"  Chapter {ch['num']}: {ch['title']}")
        text = process_chapter(
            ch["source"],
            strip_appendix=ch["strip_appendix"],
            strip_h1=True,
            strip_headings=ch.get("strip_headings"),
        )
        html_body = md_to_html(text)

        all_sections.append(("chapter", f"""
        <section class="chapter">
          <div class="chapter-header">
            <span class="chapter-num">Chapter {ch['num']}</span>
            <h1 class="chapter-title">{ch['title']}</h1>
            <p class="chapter-subtitle">{ch['subtitle']}</p>
          </div>
          {html_body}
        </section>
        """))

        flat_toc.append(("chapter", ch["num"], ch["title"], ch["subtitle"]))

# Appendices
all_sections.append(("part", """
<section class="part-page">
  <div class="part-label">APPENDICES</div>
  <h1 class="part-title">Reference Material</h1>
  <p class="part-desc">Glossary and plugin reference resources</p>
</section>
"""))
flat_toc.append(("part", "", "Appendices", "Reference Material"))

# Appendix A: Glossary
print("  Appendix A: Glossary")
glossary_md = """## Glossary

### General DITA Terms

- **Topic**: A modular unit of content (concept/task/reference).
- **Map**: An assembly structure that organizes topics for publishing.
- **Information typing**: Using different topic structures for different user intents.
- **Reuse**: Referencing content instead of duplicating it (conref, keyref, conkeyref).
- **Filtering**: Producing variants by including/excluding content based on attributes (DITAVAL).
- **Specialization**: Extending DITA to represent domain concepts while keeping compatibility.
- **Constraints**: Restricting the DITA model to enforce consistency.
- **Conref**: Content reference — pulls content from another element by ID.
- **Keyref**: Key reference — resolves links/text via map-defined keys (late binding).
- **Conkeyref**: Combines keys and content pulling for flexible multi-context reuse.

### DITA-OT Developer Terms

- **Transtype**: The transform type, e.g., `html5`, `pdf`.
- **Preprocess / preprocess2**: Legacy vs map-first preprocessing pipelines.
- **Plug-in**: Extension package that can inject XSLT, Ant targets, resources.
- **Extension point**: Named hook where a plug-in can contribute behavior.
- **Intermediate files**: Normalized/filtered content used by later processing stages.
- **DITAVAL**: XML file defining conditional processing (include/exclude) rules.
- **Chunking**: How DITA-OT decides to split or combine topics into output pages/files.
"""
glossary_html = md_to_html(glossary_md)
all_sections.append(("chapter", f"""
<section class="chapter">
  <div class="chapter-header">
    <span class="chapter-num">Appendix A</span>
    <h1 class="chapter-title">Glossary</h1>
  </div>
  {glossary_html}
</section>
"""))
flat_toc.append(("appendix", "A", "Glossary", ""))

# Add Appendix B: Complete Plugin Reference (v2 starter)
print("  Appendix B: Complete Plugin Reference")
plugin_ref_md = r"""## Complete Plugin Reference

This appendix contains the full source code of the **v2 starter plugin** (`com.acme.html5.sidebar`) — a production-ready DITA-OT HTML5 customization that demonstrates every pattern taught in this training guide.

### plugin.xml

The plugin descriptor declares the plugin ID, its dependency on the HTML5 transtype, and two extension points for topic transforms and TOC generation.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<plugin id="com.acme.html5.sidebar" version="1.0.0">
  <require plugin="org.dita.html5"/>
  <feature extension="dita.xsl.html5" file="xsl/html5/override.xsl"/>
  <feature extension="dita.xsl.html5.toc" file="xsl/toc/toc-override.xsl"/>
</plugin>
```

### override.xsl — Topic Transform (key excerpts)

This stylesheet overrides 20+ default HTML5 templates. Below are the most instructive patterns:

**Import + JS injection:**
```xslt
<xsl:import href="plugin:org.dita.html5:xsl/dita2html5.xsl"/>

<xsl:template name="gen-user-head">
  <xsl:next-match/>
  <script src="{concat($PATH2PROJ, 'js/site.js')}"></script>
</xsl:template>
```

**Topic wrapper (standardizes across concept/task/reference):**
```xslt
<xsl:template match="*[contains(@class,' topic/topic ')]">
  <article class="dita-topic" data-topic-type="{local-name()}">
    <xsl:apply-templates select="*[contains(@class,' topic/title ')]"/>
    <xsl:apply-templates select="*[contains(@class,' topic/shortdesc ')]"/>
    <main class="dita-body">
      <xsl:apply-templates
        select="*[contains(@class,' topic/body ')]
              | *[contains(@class,' concept/conbody ')]
              | *[contains(@class,' task/taskbody ')]
              | *[contains(@class,' reference/refbody ')]"/>
    </main>
  </article>
</xsl:template>
```

**Notes as callout boxes:**
```xslt
<xsl:template match="*[contains(@class,' topic/note ')]">
  <aside class="callout{if (@type) then concat(' callout-', @type) else ''}">
    <xsl:if test="@type">
      <div class="callout-title">
        <xsl:value-of select="upper-case(@type)"/>
      </div>
    </xsl:if>
    <div class="callout-body"><xsl:apply-templates/></div>
  </aside>
</xsl:template>
```

**Code blocks with Copy button:**
```xslt
<xsl:template match="*[contains(@class,' topic/codeblock ')]">
  <div class="codeblock">
    <button class="copy-btn" type="button">Copy</button>
    <pre><code><xsl:apply-templates/></code></pre>
  </div>
</xsl:template>
```

**Task steps with anchors:**
```xslt
<xsl:template match="*[contains(@class,' task/step ')]">
  <li class="task-step"
      data-step="{count(preceding-sibling::*[contains(@class,' task/step ')]) + 1}">
    <xsl:apply-templates/>
  </li>
</xsl:template>
```

**External links with rel/target handling:**
```xslt
<xsl:template match="*[contains(@class,' topic/xref ')]">
  <xsl:variable name="out" as="node()*"><xsl:next-match/></xsl:variable>
  <xsl:for-each select="$out">
    <xsl:choose>
      <xsl:when test="self::a">
        <xsl:variable name="isExternal"
                      select="starts-with(@href,'http') or @target='_blank'"/>
        <a>
          <xsl:copy-of select="@*"/>
          <xsl:if test="$isExternal">
            <xsl:attribute name="target">_blank</xsl:attribute>
            <xsl:attribute name="rel">noopener noreferrer</xsl:attribute>
          </xsl:if>
          <xsl:attribute name="class"
            select="normalize-space(string-join(
              (@class, 'dita-xref',
               if ($isExternal) then 'external' else ()), ' '))"/>
          <xsl:apply-templates select="node()"/>
        </a>
      </xsl:when>
      <xsl:otherwise><xsl:sequence select="."/></xsl:otherwise>
    </xsl:choose>
  </xsl:for-each>
</xsl:template>
```

### toc-override.xsl — Sidebar Navigation

```xslt
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">
  <xsl:import href="plugin:org.dita.html5:xsl/toc.xsl"/>

  <xsl:template match="nav">
    <nav class="sidebar-toc">
      <xsl:apply-templates select="@* | node()"/>
    </nav>
  </xsl:template>

  <xsl:template match="li">
    <li data-level="{count(ancestor::li)+1}">
      <xsl:apply-templates select="@* | node()"/>
    </li>
  </xsl:template>
</xsl:stylesheet>
```

### Sample DITAVAL (web variant)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<val>
  <prop action="exclude" att="platform" val="print"/>
</val>
```

### Additional DITAVAL variants

**print.ditaval** — exclude web-only content:
```xml
<val>
  <prop action="exclude" att="platform" val="web"/>
</val>
```

**audience-admin.ditaval** — show only admin content:
```xml
<val>
  <prop action="include" att="audience" val="admin"/>
  <prop action="exclude" att="audience" val="novice"/>
</val>
```

### Build command

```bash
dita -i dita/maps/guides/getting-started.ditamap -f html5 -o out/html5 \
  --nav-toc=full \
  --args.copycss=yes \
  --args.cssroot=css/ \
  --args.css=brand.css \
  --args.filter=build/ditaval/web.ditaval
```
"""
plugin_ref_html = md_to_html(plugin_ref_md)
all_sections.append(("chapter", f"""
<section class="chapter">
  <div class="chapter-header">
    <span class="chapter-num">Appendix B</span>
    <h1 class="chapter-title">Complete Plugin Reference</h1>
  </div>
  {plugin_ref_html}
</section>
"""))
flat_toc.append(("appendix", "B", "Complete Plugin Reference", ""))

# ── Build TOC HTML ───────────────────────────────────────────────────────
toc_html_items = []
for item in flat_toc:
    if item[0] == "part":
        _, num, title, desc = item
        label = f"PART {num}" if num else title.upper()
        toc_html_items.append(f"""
        <li class="toc-part">
          <span class="toc-part-label">{label}</span>
          <span class="toc-part-title">{title if num else ''}</span>
          <span class="toc-part-desc">{desc}</span>
        </li>""")
    elif item[0] == "chapter":
        _, num, title, subtitle = item
        toc_html_items.append(f"""
        <li class="toc-chapter">
          <span class="toc-num">{num}</span>
          <div>
            <span class="toc-title">{title}</span>
            <span class="toc-sub">{subtitle}</span>
          </div>
        </li>""")
    elif item[0] == "appendix":
        _, letter, title, _ = item
        toc_html_items.append(f"""
        <li class="toc-chapter toc-appendix">
          <span class="toc-num">{letter}</span>
          <div><span class="toc-title">{title}</span></div>
        </li>""")

toc_body = "\n".join(toc_html_items)
body_sections = "\n".join(html for _, html in all_sections)


# ── Full HTML ────────────────────────────────────────────────────────────
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page {{
    size: letter;
    margin: 0.95in 0.85in 0.95in 0.85in;
    @top-center {{
      content: "DITA Training Guide — Extense LLC";
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 8pt;
      color: #aaa;
    }}
    @bottom-right {{
      content: counter(page);
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 9pt;
      color: #666;
    }}
    @bottom-left {{
      content: "© 2026 Extense LLC  •  www.ex-tense.co";
      font-family: 'Helvetica Neue', Arial, sans-serif;
      font-size: 8pt;
      color: #bbb;
    }}
  }}

  @page:first {{
    margin: 0;
    @top-center {{ content: none; }}
    @bottom-right {{ content: none; }}
    @bottom-left {{ content: none; }}
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Helvetica Neue', 'Segoe UI', Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.7;
    color: #2a2a2a;
  }}

  /* ════════ COVER PAGE ════════ */
  .cover {{
    width: 100vw;
    height: 100vh;
    background: linear-gradient(145deg, #1D397C 0%, #0f2350 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 2.5in 1.5in;
    page-break-after: always;
    position: relative;
    overflow: hidden;
  }}
  .cover::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 8px;
    background: #E9AC15;
  }}
  .cover::after {{
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 8px;
    background: #E9AC15;
  }}
  .cover-badge {{
    display: inline-block;
    background: rgba(233,172,21,0.2);
    color: #E9AC15;
    font-size: 9pt;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 16px;
    letter-spacing: 2px;
    margin-bottom: 24px;
  }}
  .cover h1 {{
    font-weight: 300;
    font-size: 38pt;
    color: white;
    letter-spacing: 1px;
    margin-bottom: 10px;
    line-height: 1.15;
  }}
  .cover h1 em {{
    font-style: normal;
    color: #E9AC15;
  }}
  .cover .cover-subtitle {{
    font-size: 14pt;
    color: #81AFCB;
    font-weight: 300;
    letter-spacing: 1px;
    margin-bottom: 48px;
    line-height: 1.5;
  }}
  .cover .cover-contents {{
    font-size: 10pt;
    color: rgba(255,255,255,0.5);
    line-height: 2;
  }}
  .cover .cover-contents strong {{
    color: rgba(255,255,255,0.75);
    font-weight: 600;
  }}
  .cover-footer {{
    position: absolute;
    bottom: 1.2in;
    left: 1.5in;
    right: 1.5in;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  .cover-company {{
    font-size: 26pt;
    font-weight: 300;
    color: white;
    letter-spacing: 7px;
  }}
  .cover-meta {{
    color: rgba(255,255,255,0.4);
    font-size: 9pt;
    text-align: right;
    line-height: 1.6;
  }}
  .cover-meta strong {{
    color: #0ACB8B;
  }}

  /* ════════ TOC PAGE ════════ */
  .toc-page {{
    page-break-after: always;
    padding-top: 16px;
  }}
  .toc-page > h1 {{
    font-size: 20pt;
    color: #1D397C;
    font-weight: 300;
    letter-spacing: 3px;
    margin-bottom: 6px;
    padding-bottom: 10px;
    border-bottom: 3px solid #E9AC15;
  }}
  .toc-list {{
    list-style: none;
    padding: 0;
    margin-top: 16px;
  }}
  .toc-part {{
    padding: 16px 0 4px;
    border-bottom: none;
  }}
  .toc-part-label {{
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 8pt;
    font-weight: 700;
    color: #E9AC15;
    letter-spacing: 2px;
    text-transform: uppercase;
    display: block;
  }}
  .toc-part-title {{
    font-size: 13pt;
    font-weight: 600;
    color: #1D397C;
    display: block;
    margin-top: 2px;
  }}
  .toc-part-desc {{
    font-size: 9pt;
    color: #888;
    display: block;
    margin-top: 2px;
  }}
  .toc-chapter {{
    display: flex;
    align-items: baseline;
    padding: 10px 0 10px 20px;
    border-bottom: 1px solid #f0f0f0;
    gap: 14px;
  }}
  .toc-num {{
    font-size: 11pt;
    color: #E9AC15;
    font-weight: 700;
    min-width: 22px;
    flex-shrink: 0;
  }}
  .toc-title {{
    font-size: 11.5pt;
    color: #2a2a2a;
    display: block;
    font-weight: 500;
  }}
  .toc-sub {{
    font-size: 9pt;
    color: #999;
    display: block;
    margin-top: 2px;
  }}

  /* ════════ PART DIVIDER ════════ */
  .part-page {{
    page-break-before: always;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 60vh;
    padding: 3in 0.5in;
    position: relative;
  }}
  .part-page::after {{
    content: '';
    position: absolute;
    right: 0;
    top: 30%;
    bottom: 30%;
    width: 6px;
    background: linear-gradient(to bottom, #E9AC15, #1D397C);
    border-radius: 3px;
  }}
  .part-label {{
    font-size: 10pt;
    font-weight: 700;
    color: #E9AC15;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }}
  .part-title {{
    font-size: 30pt;
    font-weight: 300;
    color: #1D397C;
    letter-spacing: 1px;
    margin-bottom: 12px;
    border-bottom: 3px solid #E9AC15;
    padding-bottom: 16px;
    display: inline-block;
  }}
  .part-desc {{
    font-size: 12pt;
    color: #666;
    line-height: 1.7;
    max-width: 480px;
  }}

  /* ════════ CHAPTER ════════ */
  .chapter {{
    page-break-before: always;
  }}
  .chapter-header {{
    margin-bottom: 36px;
    padding-bottom: 20px;
    border-bottom: 3px solid #E9AC15;
    position: relative;
  }}
  .chapter-header::after {{
    content: '';
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 80px;
    height: 3px;
    background: #1D397C;
  }}
  .chapter-num {{
    font-size: 9pt;
    font-weight: 700;
    color: #E9AC15;
    letter-spacing: 3px;
    text-transform: uppercase;
    display: block;
    margin-bottom: 8px;
  }}
  .chapter-title {{
    font-size: 22pt;
    font-weight: 300;
    color: #1D397C;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
    border: none;
    padding: 0;
  }}
  .chapter-subtitle {{
    font-size: 10.5pt;
    color: #888;
    font-style: italic;
  }}

  /* ════════ HEADINGS ════════ */
  h1 {{
    font-size: 17pt;
    font-weight: 600;
    color: #1D397C;
    margin-top: 34px;
    margin-bottom: 14px;
  }}
  h2 {{
    font-size: 14pt;
    font-weight: 600;
    color: #1D397C;
    margin-top: 30px;
    margin-bottom: 12px;
    padding-bottom: 6px;
    border-bottom: 2px solid #E9AC15;
  }}
  h3 {{
    font-size: 12pt;
    font-weight: 700;
    color: #2c3e50;
    margin-top: 22px;
    margin-bottom: 10px;
    padding-left: 10px;
    border-left: 3px solid #4682B4;
  }}
  h4 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #4682B4;
    margin-top: 18px;
    margin-bottom: 8px;
  }}
  h5, h6 {{
    font-size: 10pt;
    font-weight: 700;
    color: #555;
    margin-top: 14px;
    margin-bottom: 6px;
  }}

  /* ════════ BODY ════════ */
  p {{
    margin-bottom: 10px;
    text-align: justify;
    hyphens: auto;
  }}
  strong {{ color: #1a1a1a; }}
  a {{ color: #4682B4; text-decoration: none; border-bottom: 1px dotted #4682B4; }}

  ul, ol {{ margin: 10px 0 14px 24px; }}
  li {{
    margin-bottom: 5px;
    line-height: 1.65;
  }}
  li > ul, li > ol {{ margin-top: 4px; margin-bottom: 4px; }}

  /* Nested list visual hierarchy */
  li > ul > li {{ color: #444; }}

  /* Checklist items — markdown [x] and [ ] */
  li {{ list-style-position: outside; }}

  /* ════════ CODE ════════ */
  code {{
    font-family: 'Menlo', 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    background: #f0f3f7;
    color: #c7254e;
    padding: 2px 5px;
    border-radius: 3px;
    border: 1px solid #e1e4e8;
  }}
  pre {{
    background: #1e2432;
    color: #e0e6ed;
    padding: 16px 20px;
    border-radius: 6px;
    margin: 14px 0;
    overflow-x: auto;
    font-size: 8pt;
    line-height: 1.55;
    border-left: 4px solid #E9AC15;
    page-break-inside: avoid;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }}
  pre code {{
    background: none;
    color: inherit;
    padding: 0;
    border: none;
    font-size: 8pt;
  }}

  /* ════════ TABLES ════════ */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 9pt;
    page-break-inside: avoid;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    border-radius: 4px;
    overflow: hidden;
  }}
  thead {{ background: linear-gradient(135deg, #1D397C, #2a4a8c); color: white; }}
  th {{
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
    font-size: 8.5pt;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}
  td {{
    padding: 9px 14px;
    border-bottom: 1px solid #eaedf0;
    vertical-align: top;
  }}
  tbody tr:nth-child(even) {{ background: #f8f9fb; }}
  tbody tr:hover {{ background: #eef3f8; }}

  /* ════════ BLOCKQUOTES / CALLOUTS ════════ */
  blockquote {{
    border-left: 4px solid #4682B4;
    padding: 12px 18px;
    margin: 16px 0;
    background: linear-gradient(135deg, #f0f5fa, #e8eef5);
    color: #3a3a3a;
    font-style: italic;
    border-radius: 0 6px 6px 0;
    page-break-inside: avoid;
  }}
  blockquote p {{ margin-bottom: 4px; }}
  blockquote p:last-child {{ margin-bottom: 0; }}

  /* ════════ HORIZONTAL RULES ════════ */
  hr {{
    border: none;
    height: 1px;
    background: linear-gradient(to right, #E9AC15, #e0e0e0, transparent);
    margin: 28px 0;
  }}
</style>
</head>
<body>

<!-- ════════ COVER ════════ -->
<div class="cover">
  <span class="cover-badge">TRAINING GUIDE</span>
  <h1>DITA Documentation<br><em>Training Guide</em></h1>
  <p class="cover-subtitle">
    A structured learning path for DITA &amp; DITA Open Toolkit 4.x<br>
    From first concepts to production plugin development
  </p>
  <div class="cover-contents">
    <strong>Part I</strong> &nbsp;Foundations — Understanding DITA and getting started<br>
    <strong>Part II</strong> &nbsp;Core Authoring Skills — Authoring, first project, reuse &amp; variants<br>
    <strong>Part III</strong> &nbsp;Architecture &amp; Publishing — Pipeline internals and build workflows<br>
    <strong>Part IV</strong> &nbsp;DITA-OT Development — Plugins, XSLT customization, and DevOps
  </div>
  <div class="cover-footer">
    <span class="cover-company">EXTENSE</span>
    <span class="cover-meta">
      <strong>13 chapters</strong> &nbsp;•&nbsp; 4 learning tracks &nbsp;•&nbsp; 2 appendices<br>
      February 2026
    </span>
  </div>
</div>

<!-- ════════ TOC ════════ -->
<div class="toc-page">
  <h1>CONTENTS</h1>
  <ul class="toc-list">
    {toc_body}
  </ul>
</div>

<!-- ════════ BODY ════════ -->
{body_sections}

</body>
</html>
"""

# ── Generate PDF ─────────────────────────────────────────────────────────
print("\nRendering PDF…")
HTML(string=full_html).write_pdf(str(OUTPUT_PDF))
size_kb = OUTPUT_PDF.stat().st_size / 1024
print(f"✅ PDF created: {OUTPUT_PDF}")
print(f"   Size: {size_kb:.0f} KB")
print(f"\nTraining flow:")
for part in PARTS:
    print(f"\n  PART {part['part_num']}: {part['part_title']}")
    for ch in part['chapters']:
        print(f"    Ch {ch['num']}  {ch['title']}")
print(f"\n  APPENDICES")
print(f"    App A  Glossary")
print(f"    App B  Complete Plugin Reference")
