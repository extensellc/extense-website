#!/usr/bin/env python3
"""
Generate an interactive, single-page HTML5 DITA Training Guide.

Features:
  - Collapsible sidebar navigation with part/chapter hierarchy
  - Full-text search with highlighted results
  - Dark/light mode toggle with persistence
  - Code blocks with syntax-aware copy-to-clipboard
  - Reading progress bar
  - Smooth scroll & active-chapter tracking
  - Keyboard shortcuts (/, Esc, ←, →)
  - Responsive mobile layout
  - Branded with Extense LLC colors
"""

import markdown, re, html as html_mod
from pathlib import Path

DOCS_ROOT = Path("/home/upkar/dev/Ex-tense/training-doc/organized-dita-docs")
OUTPUT = Path("/home/upkar/dev/Ex-tense/training-doc/DITA-Training-Guide-Interactive.html")

# ── Markdown helpers ────────────────────────────────────────────────────

EMOJI_MAP = {
    "⚡": "»", "🎯": "◆", "✅": "✓", "❌": "✗", "📖": "▸", "✍️": "▸",
    "🔄": "▸", "🚀": "▸", "🏗️": "▸", "🔧": "▸", "🐳": "▸", "⚙️": "▸",
    "📊": "▸", "📈": "▸", "💼": "▸", "🤝": "▸", "📚": "■", "👀": "▸",
    "🧪": "▸", "📋": "▸", "💡": "★", "🎓": "■", "🏁": "■", "🚨": "▲",
    "📞": "■", "🔍": "■", "🛠️": "■", "📦": "■", "🎨": "■", "🔗": "■",
}

def replace_emoji(text):
    for e, r in EMOJI_MAP.items():
        text = text.replace(e, r)
    return text

md_converter = markdown.Markdown(
    extensions=["fenced_code", "tables", "toc", "codehilite", "smarty"]
)

def md_to_html(text):
    md_converter.reset()
    return md_converter.convert(text)

def read_md(path):
    return replace_emoji(path.read_text(encoding="utf-8"))

def strip_first_h1(text):
    return re.sub(r'^# .+\n+', '', text, count=1)

def process_chapter(path):
    text = read_md(path)
    text = strip_first_h1(text)
    return md_to_html(text)


# ── Content structure (mirrors generate-pdf.py) ─────────────────────────

PARTS = [
    {
        "part_num": "I", "part_title": "Foundations",
        "part_desc": "Understanding DITA — what it is, why it matters, and how to get started",
        "chapters": [
            {"num": "1", "title": "Quick Start Guide",
             "subtitle": "Get oriented in 30 minutes — role-based learning paths",
             "source": DOCS_ROOT / "QUICK-START.md"},
            {"num": "2", "title": "DITA at a Glance",
             "subtitle": "The mental model — topics, maps, reuse, and publishing",
             "source": DOCS_ROOT / "getting-started/dita_intro_guide.md"},
            {"num": "3", "title": "DITA Deep Dive",
             "subtitle": "Information typing, specialization, and when DITA is the right fit",
             "source": DOCS_ROOT / "getting-started/dita-topic-1-overview.md"},
        ],
    },
    {
        "part_num": "II", "part_title": "Core Skills",
        "part_desc": "Hands-on authoring, content reuse, and variant management",
        "chapters": [
            {"num": "4", "title": "Authoring DITA Topics",
             "subtitle": "Topic types, chunking, IDs, writing style, templates, and workflows",
             "source": DOCS_ROOT / "core-topics/dita-topic-2-authoring.md"},
            {"num": "5", "title": "Reuse, Keys & Variants",
             "subtitle": "Conref, keyref, conkeyref, DITAVAL filtering, governance",
             "source": DOCS_ROOT / "core-topics/dita-topic-3-reuse-variants.md"},
        ],
    },
    {
        "part_num": "III", "part_title": "Publishing & Automation",
        "part_desc": "From maps to deliverables — builds, pipelines, and CI/CD",
        "chapters": [
            {"num": "6", "title": "Publishing with DITA-OT",
             "subtitle": "Build commands, parameters, output customization, debugging, CI",
             "source": DOCS_ROOT / "core-topics/dita-topic-4-publishing-dita-ot.md"},
            {"num": "7", "title": "Architecture & DevOps",
             "subtitle": "Pipeline internals, preprocessing, Docker, GitHub Actions",
             "source": DOCS_ROOT / "developer-guides/dita-ot-developer-handbook.md"},
        ],
    },
    {
        "part_num": "IV", "part_title": "Advanced Development",
        "part_desc": "Plugin development, XSLT customization, and building from source",
        "chapters": [
            {"num": "8", "title": "Technical Reference",
             "subtitle": "XSLT patterns, glossary, and advanced debugging",
             "source": DOCS_ROOT / "developer-guides/dita-ot-dev-technical-guide.md"},
            {"num": "9", "title": "XSLT Customization Tutorial",
             "subtitle": "Hands-on labs — build a complete HTML5 plugin from scratch",
             "source": DOCS_ROOT / "plugins-and-customization/dita-ot-html5-xslt-customization-final.md"},
        ],
    },
]

APPENDICES = [
    {"id": "A", "title": "Architecture Diagram",
     "source": DOCS_ROOT / "reference/dita-ot-architecture-ascii-snippet.md"},
]

# Inline appendices (same content used in generate-pdf.py)
GLOSSARY_MD = """
### General DITA Terms

- **Topic**: A modular unit of content (concept/task/reference).
- **Map**: An assembly structure that organizes topics for publishing.
- **Information typing**: Using different topic structures for different user intents.
- **Reuse**: Referencing content instead of duplicating it (conref, keyref, conkeyref).
- **Filtering**: Producing variants by including/excluding content based on attributes (DITAVAL).
- **Specialization**: Extending DITA to represent domain concepts while keeping compatibility.
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

PLUGIN_REF_MD = r"""
This appendix contains the full source code of the **v2 starter plugin** (`com.acme.html5.sidebar`).

### plugin.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<plugin id="com.acme.html5.sidebar" version="1.0.0">
  <require plugin="org.dita.html5"/>
  <feature extension="dita.xsl.html5" file="xsl/html5/override.xsl"/>
  <feature extension="dita.xsl.html5.toc" file="xsl/toc/toc-override.xsl"/>
</plugin>
```

### override.xsl — Key Excerpts

```xslt
<xsl:import href="plugin:org.dita.html5:xsl/dita2html5.xsl"/>

<xsl:template match="*[contains(@class,' topic/topic ')]">
  <article class="dita-topic" data-topic-type="{local-name()}">
    <xsl:apply-templates select="*[contains(@class,' topic/title ')]"/>
    <main class="dita-body">
      <xsl:apply-templates select="*[contains(@class,' topic/body ')]
        | *[contains(@class,' concept/conbody ')]
        | *[contains(@class,' task/taskbody ')]
        | *[contains(@class,' reference/refbody ')]"/>
    </main>
  </article>
</xsl:template>
```

### toc-override.xsl — Sidebar Navigation

```xslt
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0">
  <xsl:import href="plugin:org.dita.html5:xsl/toc.xsl"/>
  <xsl:template match="nav">
    <nav class="sidebar-toc">
      <xsl:apply-templates select="@* | node()"/>
    </nav>
  </xsl:template>
</xsl:stylesheet>
```

### Build Command

```bash
dita -i maps/getting-started.ditamap -f html5 -o out/html5 \
  --nav-toc=full --args.copycss=yes --args.css=brand.css
```
"""


# ── Build everything ────────────────────────────────────────────────────

print("Building Interactive DITA Training Guide HTML5…\n")

# -- Sidebar nav + main content -------------------------------------------
nav_items = []
content_sections = []
chapter_ids = []

for part in PARTS:
    pn, pt = part["part_num"], part["part_title"]
    part_id = f"part-{pn.lower()}"
    ch_nav = []

    for ch in part["chapters"]:
        ch_id = f"ch-{ch['num']}"
        chapter_ids.append(ch_id)
        print(f"  Chapter {ch['num']}: {ch['title']}")
        body_html = process_chapter(ch["source"])

        ch_nav.append(
            f'<a href="#{ch_id}" class="nav-chapter" data-chapter="{ch_id}">'
            f'<span class="nav-num">{ch["num"]}</span>{ch["title"]}</a>'
        )
        content_sections.append(f'''
<section id="{ch_id}" class="chapter-section" data-chapter-num="{ch['num']}">
  <div class="chapter-header">
    <span class="chapter-label">Chapter {ch['num']}</span>
    <h1>{ch['title']}</h1>
    <p class="chapter-subtitle">{ch['subtitle']}</p>
  </div>
  <div class="chapter-body">{body_html}</div>
</section>''')

    nav_items.append(f'''
<div class="nav-part" data-part="{part_id}">
  <button class="nav-part-btn" aria-expanded="true" onclick="togglePart(this)">
    <svg class="chevron" viewBox="0 0 24 24" width="16" height="16"><path d="M9 18l6-6-6-6"/></svg>
    <span class="nav-part-num">Part {pn}</span>
    <span class="nav-part-title">{pt}</span>
  </button>
  <div class="nav-chapters">{''.join(ch_nav)}</div>
</div>''')

# Appendices
app_nav = []
for ap in APPENDICES:
    ap_id = f"app-{ap['id'].lower()}"
    chapter_ids.append(ap_id)
    print(f"  Appendix {ap['id']}: {ap['title']}")
    text = strip_first_h1(read_md(ap["source"]))
    body_html = md_to_html(text)
    app_nav.append(
        f'<a href="#{ap_id}" class="nav-chapter nav-appendix" data-chapter="{ap_id}">'
        f'<span class="nav-num">{ap["id"]}</span>{ap["title"]}</a>'
    )
    content_sections.append(f'''
<section id="{ap_id}" class="chapter-section" data-chapter-num="A{ap['id']}">
  <div class="chapter-header">
    <span class="chapter-label">Appendix {ap['id']}</span>
    <h1>{ap['title']}</h1>
  </div>
  <div class="chapter-body">{body_html}</div>
</section>''')

# Glossary
print("  Appendix B: Glossary")
chapter_ids.append("app-b")
app_nav.append('<a href="#app-b" class="nav-chapter nav-appendix" data-chapter="app-b">'
               '<span class="nav-num">B</span>Glossary</a>')
content_sections.append(f'''
<section id="app-b" class="chapter-section" data-chapter-num="AB">
  <div class="chapter-header">
    <span class="chapter-label">Appendix B</span>
    <h1>Glossary</h1>
  </div>
  <div class="chapter-body">{md_to_html(GLOSSARY_MD)}</div>
</section>''')

# Plugin Ref
print("  Appendix C: Plugin Reference")
chapter_ids.append("app-c")
app_nav.append('<a href="#app-c" class="nav-chapter nav-appendix" data-chapter="app-c">'
               '<span class="nav-num">C</span>Plugin Reference</a>')
content_sections.append(f'''
<section id="app-c" class="chapter-section" data-chapter-num="AC">
  <div class="chapter-header">
    <span class="chapter-label">Appendix C</span>
    <h1>Complete Plugin Reference</h1>
  </div>
  <div class="chapter-body">{md_to_html(PLUGIN_REF_MD)}</div>
</section>''')

nav_items.append(f'''
<div class="nav-part" data-part="appendices">
  <button class="nav-part-btn" aria-expanded="true" onclick="togglePart(this)">
    <svg class="chevron" viewBox="0 0 24 24" width="16" height="16"><path d="M9 18l6-6-6-6"/></svg>
    <span class="nav-part-num"></span>
    <span class="nav-part-title">Appendices</span>
  </button>
  <div class="nav-chapters">{''.join(app_nav)}</div>
</div>''')

sidebar_html = '\n'.join(nav_items)
main_html = '\n'.join(content_sections)


# ── Assemble final HTML ────────────────────────────────────────────────

final_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>DITA Training Guide — Extense LLC</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Questrial&family=JetBrains+Mono:wght@400;500&family=Syne:wght@700;800&display=swap" rel="stylesheet"/>
<style>
/* ═══════════════════════════════════════════════════════════════════
   CSS VARIABLES & RESET
   ═══════════════════════════════════════════════════════════════════ */
:root {{
  --navy: #1D397C;
  --navy-dark: #142a5e;
  --gold: #E9AC15;
  --blue: #4682B4;
  --blue-mid: #81AFCB;
  --green: #0ACB8B;
  --bg: #ffffff;
  --bg-alt: #f6f8fb;
  --bg-sidebar: #0f1b38;
  --bg-code: #1e2736;
  --text: #1a1a2e;
  --text-muted: #5a6377;
  --text-sidebar: #c3cde0;
  --text-sidebar-active: #ffffff;
  --border: #e2e8f0;
  --shadow: 0 1px 3px rgba(0,0,0,.08);
  --shadow-lg: 0 8px 30px rgba(0,0,0,.12);
  --sidebar-w: 300px;
  --header-h: 56px;
  --radius: 8px;
  --transition: .25s cubic-bezier(.4,0,.2,1);
}}

[data-theme="dark"] {{
  --bg: #0f1420;
  --bg-alt: #161d2e;
  --bg-code: #0d1117;
  --text: #e2e8f0;
  --text-muted: #8892a8;
  --border: #2d3748;
  --shadow: 0 1px 3px rgba(0,0,0,.3);
  --shadow-lg: 0 8px 30px rgba(0,0,0,.4);
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

html {{ scroll-behavior: smooth; scroll-padding-top: calc(var(--header-h) + 24px); }}

body {{
  font-family: 'Questrial', system-ui, sans-serif;
  font-size: 16px;
  line-height: 1.7;
  color: var(--text);
  background: var(--bg);
  transition: background var(--transition), color var(--transition);
}}

/* ═══════════════════════════════════════════════════════════════════
   PROGRESS BAR
   ═══════════════════════════════════════════════════════════════════ */
#progress-bar {{
  position: fixed; top: 0; left: 0; z-index: 1000;
  height: 3px; width: 0%;
  background: linear-gradient(90deg, var(--gold), var(--green));
  transition: width .15s;
}}

/* ═══════════════════════════════════════════════════════════════════
   TOP HEADER
   ═══════════════════════════════════════════════════════════════════ */
#top-header {{
  position: fixed; top: 3px; left: 0; right: 0; z-index: 900;
  height: var(--header-h);
  background: var(--navy);
  display: flex; align-items: center; padding: 0 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,.2);
}}

#top-header .logo {{
  font-family: 'Syne', sans-serif; font-weight: 800; font-size: 20px;
  color: var(--gold); letter-spacing: .5px; white-space: nowrap;
}}
#top-header .logo span {{ color: #fff; font-weight: 700; }}

#menu-toggle {{
  display: none; background: none; border: none; color: #fff;
  cursor: pointer; padding: 8px; margin-right: 8px; border-radius: 4px;
}}
#menu-toggle:hover {{ background: rgba(255,255,255,.1); }}

.header-actions {{
  margin-left: auto; display: flex; align-items: center; gap: 8px;
}}

/* Search bar */
.search-wrap {{
  position: relative;
}}
#search-input {{
  width: 240px; padding: 7px 12px 7px 34px;
  border: 1px solid rgba(255,255,255,.2); border-radius: 6px;
  background: rgba(255,255,255,.08); color: #fff;
  font-family: inherit; font-size: 14px;
  transition: all var(--transition);
}}
#search-input::placeholder {{ color: rgba(255,255,255,.45); }}
#search-input:focus {{
  outline: none; border-color: var(--gold);
  background: rgba(255,255,255,.12); width: 300px;
}}
.search-icon {{
  position: absolute; left: 10px; top: 50%; transform: translateY(-50%);
  color: rgba(255,255,255,.4); pointer-events: none;
}}
.search-kbd {{
  position: absolute; right: 8px; top: 50%; transform: translateY(-50%);
  font-size: 11px; color: rgba(255,255,255,.3); border: 1px solid rgba(255,255,255,.15);
  border-radius: 3px; padding: 1px 5px; pointer-events: none;
}}

/* Search results dropdown */
#search-results {{
  position: absolute; top: 100%; right: 0; margin-top: 6px;
  width: 420px; max-height: 480px; overflow-y: auto;
  background: var(--bg); border: 1px solid var(--border);
  border-radius: var(--radius); box-shadow: var(--shadow-lg);
  display: none; z-index: 999;
}}
#search-results.active {{ display: block; }}
.sr-item {{
  display: block; padding: 12px 16px; text-decoration: none;
  color: var(--text); border-bottom: 1px solid var(--border);
  transition: background .15s;
}}
.sr-item:hover {{ background: var(--bg-alt); }}
.sr-item .sr-chapter {{ font-size: 11px; color: var(--blue); font-weight: 600; text-transform: uppercase; }}
.sr-item .sr-text {{ font-size: 14px; margin-top: 2px; }}
.sr-item mark {{ background: rgba(233,172,21,.3); color: inherit; border-radius: 2px; padding: 0 2px; }}
.sr-empty {{ padding: 24px; text-align: center; color: var(--text-muted); font-size: 14px; }}

/* Theme toggle */
#theme-toggle {{
  background: none; border: 1px solid rgba(255,255,255,.2);
  color: #fff; border-radius: 6px; padding: 6px 10px; cursor: pointer;
  font-size: 16px; transition: all var(--transition);
}}
#theme-toggle:hover {{ border-color: var(--gold); background: rgba(255,255,255,.08); }}

/* ═══════════════════════════════════════════════════════════════════
   SIDEBAR
   ═══════════════════════════════════════════════════════════════════ */
#sidebar {{
  position: fixed; top: calc(var(--header-h) + 3px); left: 0; bottom: 0;
  width: var(--sidebar-w); background: var(--bg-sidebar);
  overflow-y: auto; z-index: 800;
  transition: transform var(--transition);
  scrollbar-width: thin; scrollbar-color: rgba(255,255,255,.15) transparent;
}}
#sidebar::-webkit-scrollbar {{ width: 5px; }}
#sidebar::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,.15); border-radius: 3px; }}

.nav-part {{ border-bottom: 1px solid rgba(255,255,255,.06); }}
.nav-part-btn {{
  display: flex; align-items: center; gap: 8px;
  width: 100%; padding: 14px 16px; background: none; border: none;
  color: var(--gold); cursor: pointer; text-align: left;
  font-family: 'Montserrat', sans-serif; font-size: 11px;
  font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px;
  transition: background .15s;
}}
.nav-part-btn:hover {{ background: rgba(255,255,255,.04); }}
.nav-part-btn .chevron {{
  fill: none; stroke: currentColor; stroke-width: 2;
  stroke-linecap: round; stroke-linejoin: round;
  transition: transform var(--transition); flex-shrink: 0;
}}
.nav-part-btn[aria-expanded="false"] .chevron {{ transform: rotate(-90deg); }}
.nav-part-num {{ margin-right: 4px; }}
.nav-part-title {{ }}
.nav-chapters {{
  overflow: hidden; transition: max-height .3s ease;
}}
.nav-part-btn[aria-expanded="false"] + .nav-chapters {{ max-height: 0 !important; }}
.nav-chapter {{
  display: flex; align-items: center; gap: 10px;
  padding: 9px 16px 9px 28px; text-decoration: none;
  color: var(--text-sidebar); font-size: 14px;
  transition: all .15s; border-left: 3px solid transparent;
}}
.nav-chapter:hover {{
  color: #fff; background: rgba(255,255,255,.05);
}}
.nav-chapter.active {{
  color: var(--text-sidebar-active); background: rgba(70,130,180,.15);
  border-left-color: var(--gold); font-weight: 600;
}}
.nav-num {{
  display: inline-flex; align-items: center; justify-content: center;
  width: 24px; height: 24px; border-radius: 50%;
  background: rgba(255,255,255,.08); font-size: 12px;
  font-family: 'Montserrat', sans-serif; font-weight: 700;
  flex-shrink: 0; color: var(--blue-mid);
}}
.nav-chapter.active .nav-num {{ background: var(--gold); color: var(--navy); }}

/* Chapter completion checkmarks */
.nav-chapter.completed .nav-num::after {{
  content: '✓'; position: absolute;
  font-size: 9px; color: var(--green);
  top: -4px; right: -4px;
}}
.nav-num {{ position: relative; }}

/* ═══════════════════════════════════════════════════════════════════
   MAIN CONTENT
   ═══════════════════════════════════════════════════════════════════ */
#main {{
  margin-left: var(--sidebar-w);
  padding-top: calc(var(--header-h) + 3px);
  min-height: 100vh;
  transition: margin var(--transition);
}}

/* Landing / cover */
#cover {{
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; text-align: center;
  min-height: 80vh; padding: 60px 40px;
  background: linear-gradient(135deg, var(--navy) 0%, var(--navy-dark) 100%);
  color: #fff; position: relative; overflow: hidden;
}}
#cover::before {{
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle at 30% 70%, rgba(70,130,180,.15) 0%, transparent 60%),
              radial-gradient(circle at 80% 20%, rgba(233,172,21,.08) 0%, transparent 50%);
}}
#cover * {{ position: relative; z-index: 1; }}
#cover .cover-brand {{
  font-family: 'Syne', sans-serif; font-weight: 800; font-size: 14px;
  letter-spacing: 3px; text-transform: uppercase; color: var(--gold);
  margin-bottom: 24px;
}}
#cover h1 {{
  font-family: 'Montserrat', sans-serif; font-weight: 800;
  font-size: clamp(32px, 5vw, 52px); line-height: 1.15;
  margin-bottom: 16px;
}}
#cover h1 em {{
  font-style: normal; color: var(--gold);
  background: linear-gradient(90deg, var(--gold), #f0c040);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}}
#cover .cover-sub {{
  font-size: 18px; color: rgba(255,255,255,.7); max-width: 600px;
  margin-bottom: 40px; line-height: 1.6;
}}
#cover .cover-stats {{
  display: flex; gap: 32px; flex-wrap: wrap; justify-content: center;
}}
.cover-stat {{
  text-align: center;
}}
.cover-stat .stat-num {{
  font-family: 'Montserrat', sans-serif; font-weight: 800;
  font-size: 36px; color: var(--gold); display: block;
}}
.cover-stat .stat-label {{
  font-size: 13px; color: rgba(255,255,255,.5); text-transform: uppercase;
  letter-spacing: 1px;
}}
.cover-start {{
  margin-top: 40px; display: inline-flex; align-items: center; gap: 8px;
  padding: 14px 32px; border-radius: 8px; text-decoration: none;
  background: var(--gold); color: var(--navy); font-weight: 700;
  font-family: 'Montserrat', sans-serif; font-size: 15px;
  transition: all .2s; box-shadow: 0 4px 15px rgba(233,172,21,.3);
}}
.cover-start:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(233,172,21,.4); }}

/* ─── Chapter sections ─── */
.chapter-section {{
  padding: 48px 48px 64px;
  max-width: 900px;
  margin: 0 auto;
  border-bottom: 1px solid var(--border);
}}
.chapter-header {{
  margin-bottom: 40px; padding-bottom: 24px;
  border-bottom: 2px solid var(--border);
}}
.chapter-label {{
  display: inline-block;
  font-family: 'Montserrat', sans-serif; font-weight: 700;
  font-size: 12px; letter-spacing: 2px; text-transform: uppercase;
  color: var(--gold); background: rgba(233,172,21,.1);
  padding: 4px 12px; border-radius: 4px; margin-bottom: 12px;
}}
.chapter-header h1 {{
  font-family: 'Montserrat', sans-serif; font-weight: 800;
  font-size: 32px; color: var(--navy); line-height: 1.2;
  margin-bottom: 8px;
}}
[data-theme="dark"] .chapter-header h1 {{ color: #fff; }}
.chapter-subtitle {{
  font-size: 16px; color: var(--text-muted); margin: 0;
}}

/* ─── Typography inside chapters ─── */
.chapter-body h2 {{
  font-family: 'Montserrat', sans-serif; font-weight: 700;
  font-size: 22px; color: var(--navy); margin: 40px 0 16px;
  padding-bottom: 8px; border-bottom: 1px solid var(--border);
}}
[data-theme="dark"] .chapter-body h2 {{ color: var(--blue-mid); }}
.chapter-body h3 {{
  font-family: 'Montserrat', sans-serif; font-weight: 600;
  font-size: 18px; color: var(--blue); margin: 28px 0 12px;
}}
.chapter-body h4 {{
  font-family: 'Montserrat', sans-serif; font-weight: 600;
  font-size: 15px; margin: 20px 0 8px;
}}
.chapter-body p {{ margin: 0 0 14px; }}
.chapter-body a {{ color: var(--blue); text-decoration: none; border-bottom: 1px solid transparent; }}
.chapter-body a:hover {{ border-bottom-color: var(--blue); }}
.chapter-body strong {{ font-weight: 700; }}
.chapter-body em {{ font-style: italic; }}

/* Lists */
.chapter-body ul, .chapter-body ol {{
  margin: 0 0 16px 24px; padding: 0;
}}
.chapter-body li {{ margin-bottom: 6px; }}
.chapter-body li::marker {{ color: var(--blue); }}

/* Tables */
.chapter-body table {{
  width: 100%; border-collapse: collapse; margin: 16px 0 24px;
  font-size: 14px;
}}
.chapter-body th {{
  background: var(--navy); color: #fff; font-family: 'Montserrat', sans-serif;
  font-weight: 600; font-size: 13px; text-transform: uppercase;
  letter-spacing: .5px; padding: 10px 14px; text-align: left;
}}
[data-theme="dark"] .chapter-body th {{ background: #1e2a45; }}
.chapter-body td {{ padding: 10px 14px; border-bottom: 1px solid var(--border); }}
.chapter-body tr:hover td {{ background: var(--bg-alt); }}

/* Code blocks */
.chapter-body pre {{
  position: relative;
  background: var(--bg-code); color: #e2e8f0;
  border-radius: var(--radius); padding: 20px;
  overflow-x: auto; margin: 16px 0 24px;
  font-family: 'JetBrains Mono', monospace; font-size: 13px;
  line-height: 1.6; border: 1px solid rgba(255,255,255,.06);
}}
.chapter-body code {{
  font-family: 'JetBrains Mono', monospace; font-size: .9em;
}}
.chapter-body p code, .chapter-body li code, .chapter-body td code {{
  background: rgba(70,130,180,.1); color: var(--blue);
  padding: 2px 6px; border-radius: 4px; font-size: .85em;
}}
[data-theme="dark"] .chapter-body p code,
[data-theme="dark"] .chapter-body li code,
[data-theme="dark"] .chapter-body td code {{
  background: rgba(70,130,180,.2); color: var(--blue-mid);
}}

/* Copy button on code blocks */
.copy-btn {{
  position: absolute; top: 8px; right: 8px;
  background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.15);
  color: rgba(255,255,255,.6); border-radius: 4px;
  padding: 4px 10px; font-size: 12px; cursor: pointer;
  font-family: 'Montserrat', sans-serif; font-weight: 600;
  transition: all .15s; opacity: 0;
}}
.chapter-body pre:hover .copy-btn {{ opacity: 1; }}
.copy-btn:hover {{ background: rgba(255,255,255,.2); color: #fff; }}
.copy-btn.copied {{ background: var(--green); color: #fff; border-color: var(--green); }}

/* Blockquotes → callout notes */
.chapter-body blockquote {{
  border-left: 4px solid var(--gold); background: rgba(233,172,21,.06);
  padding: 14px 20px; margin: 16px 0 24px; border-radius: 0 var(--radius) var(--radius) 0;
  font-size: 15px; color: var(--text);
}}
[data-theme="dark"] .chapter-body blockquote {{ background: rgba(233,172,21,.08); }}

/* HR */
.chapter-body hr {{
  border: none; height: 1px; background: var(--border); margin: 32px 0;
}}

/* ═══════════════════════════════════════════════════════════════════
   KEYBOARD SHORTCUTS MODAL
   ═══════════════════════════════════════════════════════════════════ */
#shortcuts-modal {{
  position: fixed; inset: 0; z-index: 2000;
  background: rgba(0,0,0,.5); backdrop-filter: blur(4px);
  display: none; align-items: center; justify-content: center;
}}
#shortcuts-modal.active {{ display: flex; }}
.shortcuts-card {{
  background: var(--bg); border-radius: 12px; padding: 32px;
  max-width: 400px; width: 90%; box-shadow: var(--shadow-lg);
}}
.shortcuts-card h2 {{
  font-family: 'Montserrat', sans-serif; font-weight: 700;
  font-size: 18px; margin-bottom: 20px;
}}
.shortcut-row {{
  display: flex; justify-content: space-between; align-items: center;
  padding: 8px 0; border-bottom: 1px solid var(--border);
}}
.shortcut-row:last-child {{ border: none; }}
.shortcut-key {{
  font-family: 'JetBrains Mono', monospace; font-size: 13px;
  background: var(--bg-alt); border: 1px solid var(--border);
  border-radius: 4px; padding: 2px 8px; font-weight: 500;
}}

/* ═══════════════════════════════════════════════════════════════════
   BACK-TO-TOP
   ═══════════════════════════════════════════════════════════════════ */
#back-to-top {{
  position: fixed; bottom: 24px; right: 24px; z-index: 900;
  width: 44px; height: 44px; border-radius: 50%;
  background: var(--navy); color: #fff; border: none;
  cursor: pointer; box-shadow: var(--shadow-lg);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transform: translateY(20px);
  transition: all var(--transition); pointer-events: none;
}}
#back-to-top.visible {{ opacity: 1; transform: translateY(0); pointer-events: auto; }}
#back-to-top:hover {{ background: var(--gold); color: var(--navy); }}

/* ═══════════════════════════════════════════════════════════════════
   CHAPTER NAV FOOTER (prev / next)
   ═══════════════════════════════════════════════════════════════════ */
.chapter-nav {{
  display: flex; justify-content: space-between; gap: 16px;
  margin-top: 48px; padding-top: 24px;
  border-top: 1px solid var(--border);
}}
.chapter-nav a {{
  display: flex; flex-direction: column; gap: 4px;
  padding: 16px 20px; border-radius: var(--radius);
  background: var(--bg-alt); text-decoration: none; color: var(--text);
  transition: all .15s; flex: 1; max-width: 48%;
}}
.chapter-nav a:hover {{ background: rgba(70,130,180,.08); transform: translateY(-1px); }}
.chapter-nav .cn-label {{
  font-size: 11px; color: var(--text-muted); text-transform: uppercase;
  font-weight: 600; letter-spacing: .5px;
}}
.chapter-nav .cn-title {{
  font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 15px;
  color: var(--blue);
}}
.chapter-nav .nav-next {{ text-align: right; margin-left: auto; }}

/* ═══════════════════════════════════════════════════════════════════
   RESPONSIVE
   ═══════════════════════════════════════════════════════════════════ */
@media (max-width: 900px) {{
  #sidebar {{ transform: translateX(-100%); }}
  #sidebar.open {{ transform: translateX(0); box-shadow: var(--shadow-lg); }}
  #main {{ margin-left: 0; }}
  #menu-toggle {{ display: block; }}
  .chapter-section {{ padding: 32px 20px 48px; }}
  #search-input {{ width: 160px; }}
  #search-input:focus {{ width: 200px; }}
  #search-results {{ width: 300px; }}
}}

@media (max-width: 600px) {{
  .cover-stats {{ gap: 20px; }}
  .cover-stat .stat-num {{ font-size: 28px; }}
  .chapter-header h1 {{ font-size: 24px; }}
  .chapter-body h2 {{ font-size: 18px; }}
}}

/* ═══════════════════════════════════════════════════════════════════
   PRINT
   ═══════════════════════════════════════════════════════════════════ */
@media print {{
  #sidebar, #top-header, #progress-bar, #back-to-top,
  .copy-btn, .chapter-nav, #shortcuts-modal {{ display: none !important; }}
  #main {{ margin-left: 0; padding-top: 0; }}
  .chapter-section {{ break-inside: avoid; page-break-inside: avoid; }}
}}

/* ═══════════════════════════════════════════════════════════════════
   HIGHLIGHT FOR SEARCH
   ═══════════════════════════════════════════════════════════════════ */
.search-highlight {{
  background: rgba(233,172,21,.35); border-radius: 2px;
  padding: 1px 0; outline: 2px solid rgba(233,172,21,.5);
}}
</style>
</head>
<body>

<!-- Progress bar -->
<div id="progress-bar"></div>

<!-- Top header -->
<header id="top-header">
  <button id="menu-toggle" onclick="document.getElementById('sidebar').classList.toggle('open')" aria-label="Toggle sidebar">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
  </button>
  <div class="logo">Ex<span>tense</span></div>
  <div class="header-actions">
    <div class="search-wrap">
      <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      <input type="text" id="search-input" placeholder="Search training guide…" autocomplete="off"/>
      <span class="search-kbd">/</span>
      <div id="search-results"></div>
    </div>
    <button id="theme-toggle" onclick="toggleTheme()" title="Toggle dark/light mode">🌙</button>
    <button id="theme-toggle" onclick="showShortcuts()" title="Keyboard shortcuts" style="font-size:14px;background:none;border:1px solid rgba(255,255,255,.2);color:#fff;border-radius:6px;padding:6px 10px;cursor:pointer;">⌨</button>
  </div>
</header>

<!-- Sidebar -->
<nav id="sidebar">
  {sidebar_html}
</nav>

<!-- Main content -->
<main id="main">

  <!-- Cover page -->
  <section id="cover">
    <div class="cover-brand">Extense LLC — Training Division</div>
    <h1>DITA Documentation &amp;<br/><em>DITA-OT Training Guide</em></h1>
    <p class="cover-sub">
      A structured learning path from foundations to advanced plugin development.
      Interactive edition with search, progress tracking, and hands-on labs.
    </p>
    <div class="cover-stats">
      <div class="cover-stat"><span class="stat-num">9</span><span class="stat-label">Chapters</span></div>
      <div class="cover-stat"><span class="stat-num">4</span><span class="stat-label">Parts</span></div>
      <div class="cover-stat"><span class="stat-num">5</span><span class="stat-label">Hands-on Labs</span></div>
      <div class="cover-stat"><span class="stat-num">3</span><span class="stat-label">Appendices</span></div>
    </div>
    <a href="#ch-1" class="cover-start">
      Start Learning
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14m-7-7 7 7-7 7"/></svg>
    </a>
  </section>

  {main_html}

</main>

<!-- Back to top -->
<button id="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" title="Back to top">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 15l-6-6-6 6"/></svg>
</button>

<!-- Shortcuts modal -->
<div id="shortcuts-modal" onclick="if(event.target===this)this.classList.remove('active')">
  <div class="shortcuts-card">
    <h2>⌨ Keyboard Shortcuts</h2>
    <div class="shortcut-row"><span>Focus search</span><span class="shortcut-key">/</span></div>
    <div class="shortcut-row"><span>Close search / modal</span><span class="shortcut-key">Esc</span></div>
    <div class="shortcut-row"><span>Previous chapter</span><span class="shortcut-key">←</span></div>
    <div class="shortcut-row"><span>Next chapter</span><span class="shortcut-key">→</span></div>
    <div class="shortcut-row"><span>Toggle dark mode</span><span class="shortcut-key">D</span></div>
    <div class="shortcut-row"><span>Show shortcuts</span><span class="shortcut-key">?</span></div>
  </div>
</div>

<script>
/* ═══════════════════════════════════════════════════════════════════
   JAVASCRIPT — Interactive Features
   ═══════════════════════════════════════════════════════════════════ */

// ── Chapter list (for prev/next navigation) ──
const chapterIds = {chapter_ids};
const chapterSections = chapterIds.map(id => document.getElementById(id));
const navLinks = document.querySelectorAll('.nav-chapter');

// ── Add copy buttons to all code blocks ──
document.querySelectorAll('.chapter-body pre').forEach(pre => {{
  const btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.textContent = 'Copy';
  btn.onclick = () => {{
    const code = pre.querySelector('code') || pre;
    navigator.clipboard.writeText(code.textContent).then(() => {{
      btn.textContent = 'Copied!';
      btn.classList.add('copied');
      setTimeout(() => {{ btn.textContent = 'Copy'; btn.classList.remove('copied'); }}, 2000);
    }});
  }};
  pre.appendChild(btn);
}});

// ── Add prev/next navigation to each chapter ──
chapterSections.forEach((section, i) => {{
  const nav = document.createElement('div');
  nav.className = 'chapter-nav';
  if (i > 0) {{
    const prev = chapterSections[i-1];
    const prevTitle = prev.querySelector('h1').textContent;
    const prevLabel = prev.querySelector('.chapter-label').textContent;
    nav.innerHTML += `<a href="#${{chapterIds[i-1]}}"><span class="cn-label">← ${{prevLabel}}</span><span class="cn-title">${{prevTitle}}</span></a>`;
  }}
  if (i < chapterSections.length - 1) {{
    const next = chapterSections[i+1];
    const nextTitle = next.querySelector('h1').textContent;
    const nextLabel = next.querySelector('.chapter-label').textContent;
    nav.innerHTML += `<a href="#${{chapterIds[i+1]}}" class="nav-next"><span class="cn-label">${{nextLabel}} →</span><span class="cn-title">${{nextTitle}}</span></a>`;
  }}
  section.appendChild(nav);
}});

// ── Progress bar & active chapter tracking ──
function updateProgress() {{
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
  document.getElementById('progress-bar').style.width = pct + '%';

  // Back to top visibility
  document.getElementById('back-to-top').classList.toggle('visible', scrollTop > 400);

  // Active chapter in sidebar
  let activeId = null;
  for (let i = chapterSections.length - 1; i >= 0; i--) {{
    if (chapterSections[i].getBoundingClientRect().top < 120) {{
      activeId = chapterIds[i];
      break;
    }}
  }}
  navLinks.forEach(link => {{
    link.classList.toggle('active', link.dataset.chapter === activeId);
  }});

  // Mark chapters as read (scrolled past 70%)
  chapterSections.forEach((s, i) => {{
    const rect = s.getBoundingClientRect();
    if (rect.bottom < window.innerHeight * 0.3) {{
      const link = document.querySelector(`[data-chapter="${{chapterIds[i]}}"]`);
      if (link && !link.classList.contains('completed')) {{
        link.classList.add('completed');
        saveProgress();
      }}
    }}
  }});
}}

let scrollTick = false;
window.addEventListener('scroll', () => {{
  if (!scrollTick) {{
    requestAnimationFrame(() => {{ updateProgress(); scrollTick = false; }});
    scrollTick = true;
  }}
}});

// ── Sidebar toggle ──
function togglePart(btn) {{
  const expanded = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', !expanded);
}}

// ── Theme toggle ──
function toggleTheme() {{
  const html = document.documentElement;
  const isDark = html.dataset.theme === 'dark';
  html.dataset.theme = isDark ? 'light' : 'dark';
  document.getElementById('theme-toggle').textContent = isDark ? '🌙' : '☀️';
  localStorage.setItem('dita-theme', html.dataset.theme);
}}

// Restore theme
(function() {{
  const saved = localStorage.getItem('dita-theme');
  if (saved === 'dark') {{
    document.documentElement.dataset.theme = 'dark';
    document.getElementById('theme-toggle').textContent = '☀️';
  }}
}})();

// ── Full-text search ──
const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');
let searchTimeout;

// Build search index
const searchIndex = [];
chapterSections.forEach((section, i) => {{
  const label = section.querySelector('.chapter-label').textContent;
  const title = section.querySelector('h1').textContent;
  const body = section.querySelector('.chapter-body');
  // Index each paragraph/heading/list item
  body.querySelectorAll('p, li, h2, h3, h4, td, th, blockquote').forEach(el => {{
    const text = el.textContent.trim();
    if (text.length > 10) {{
      searchIndex.push({{ chapterId: chapterIds[i], label, title, text, el }});
    }}
  }});
}});

searchInput.addEventListener('input', () => {{
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(performSearch, 200);
}});

searchInput.addEventListener('focus', () => {{
  if (searchInput.value.length >= 2) performSearch();
}});

function performSearch() {{
  const query = searchInput.value.trim().toLowerCase();
  if (query.length < 2) {{
    searchResults.classList.remove('active');
    clearHighlights();
    return;
  }}

  const matches = [];
  const queryWords = query.split(/\s+/);

  searchIndex.forEach(item => {{
    const text = item.text.toLowerCase();
    if (queryWords.every(w => text.includes(w))) {{
      matches.push(item);
    }}
  }});

  if (matches.length === 0) {{
    searchResults.innerHTML = '<div class="sr-empty">No results found</div>';
  }} else {{
    const shown = matches.slice(0, 20);
    searchResults.innerHTML = shown.map(m => {{
      // Highlight the query in context
      let snippet = m.text;
      if (snippet.length > 150) {{
        const idx = snippet.toLowerCase().indexOf(queryWords[0]);
        const start = Math.max(0, idx - 50);
        snippet = (start > 0 ? '…' : '') + snippet.substr(start, 150) + '…';
      }}
      // Wrap query words in <mark>
      queryWords.forEach(w => {{
        snippet = snippet.replace(new RegExp(`(${{w.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&')}})`, 'gi'), '<mark>$1</mark>');
      }});
      return `<a href="#${{m.chapterId}}" class="sr-item" onclick="jumpToResult(event, '${{m.chapterId}}')">`
        + `<div class="sr-chapter">${{m.label}} — ${{m.title}}</div>`
        + `<div class="sr-text">${{snippet}}</div></a>`;
    }}).join('') + (matches.length > 20 ? `<div class="sr-empty">${{matches.length - 20}} more results…</div>` : '');
  }}
  searchResults.classList.add('active');
}}

function jumpToResult(event, chapterId) {{
  searchResults.classList.remove('active');
  // Mobile: close sidebar
  document.getElementById('sidebar').classList.remove('open');
}}

// Close search on outside click
document.addEventListener('click', e => {{
  if (!e.target.closest('.search-wrap')) {{
    searchResults.classList.remove('active');
  }}
}});

function clearHighlights() {{
  document.querySelectorAll('.search-highlight').forEach(el => {{
    el.outerHTML = el.textContent;
  }});
}}

// ── Keyboard shortcuts ──
function showShortcuts() {{
  document.getElementById('shortcuts-modal').classList.add('active');
}}

document.addEventListener('keydown', e => {{
  // Don't intercept when typing in search
  const isInput = e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA';

  if (e.key === '/' && !isInput) {{
    e.preventDefault();
    searchInput.focus();
    return;
  }}
  if (e.key === 'Escape') {{
    searchResults.classList.remove('active');
    searchInput.blur();
    document.getElementById('shortcuts-modal').classList.remove('active');
    document.getElementById('sidebar').classList.remove('open');
    return;
  }}
  if (isInput) return;

  if (e.key === '?' && !e.shiftKey) {{
    showShortcuts();
    return;
  }}
  if (e.key === 'd' || e.key === 'D') {{
    toggleTheme();
    return;
  }}

  // Arrow navigation
  if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {{
    const activeLink = document.querySelector('.nav-chapter.active');
    if (!activeLink) return;
    const currentIdx = chapterIds.indexOf(activeLink.dataset.chapter);
    if (currentIdx < 0) return;
    const nextIdx = e.key === 'ArrowRight' ? currentIdx + 1 : currentIdx - 1;
    if (nextIdx >= 0 && nextIdx < chapterIds.length) {{
      document.getElementById(chapterIds[nextIdx]).scrollIntoView({{ behavior: 'smooth' }});
    }}
  }}
}});

// ── Progress persistence ──
function saveProgress() {{
  const completed = [...document.querySelectorAll('.nav-chapter.completed')].map(a => a.dataset.chapter);
  localStorage.setItem('dita-progress', JSON.stringify(completed));
}}

function loadProgress() {{
  try {{
    const saved = JSON.parse(localStorage.getItem('dita-progress') || '[]');
    saved.forEach(id => {{
      const link = document.querySelector(`[data-chapter="${{id}}"]`);
      if (link) link.classList.add('completed');
    }});
  }} catch(e) {{}}
}}
loadProgress();

// ── Sidebar auto-scroll active link into view ──
const observer = new IntersectionObserver(entries => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      const active = document.querySelector('.nav-chapter.active');
      if (active) active.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
    }}
  }});
}}, {{ rootMargin: '-50% 0px' }});

chapterSections.forEach(s => observer.observe(s));

// Initial update
updateProgress();

// ── Mobile: close sidebar on nav click ──
navLinks.forEach(link => {{
  link.addEventListener('click', () => {{
    if (window.innerWidth <= 900) {{
      document.getElementById('sidebar').classList.remove('open');
    }}
  }});
}});
</script>

</body>
</html>
'''

OUTPUT.write_text(final_html, encoding='utf-8')
size_kb = OUTPUT.stat().st_size / 1024
print(f"\n✅ Interactive HTML5 training guide generated!")
print(f"   {OUTPUT}")
print(f"   Size: {size_kb:.0f} KB")
print(f"   Chapters: {len(chapter_ids)}")
