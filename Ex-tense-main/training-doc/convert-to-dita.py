#!/usr/bin/env python3
"""Convert training markdown files to DITA concept topics.

Handles: headings → sections, code blocks → codeblock, tables → simpletable,
lists → ul/ol, inline code → codeph, bold → b, italic → i, links → xref.
"""

import re, sys, html
from pathlib import Path

DOCS = Path("/home/upkar/dev/Ex-tense/training-doc/organized-dita-docs")
DITA_OUT = DOCS / "dita-topics"


# ── helpers ──────────────────────────────────────────────────────────────

def esc(text):
    """Escape XML special chars."""
    return html.escape(text, quote=True)


def inline(text):
    """Convert inline markdown to DITA inline elements."""
    # code spans first (so backtick content isn't processed further)
    text = re.sub(r'`([^`]+)`', lambda m: f'<codeph>{esc(m.group(1))}</codeph>', text)
    # bold+italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # italic
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    # links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<xref href="{esc(m.group(2))}" scope="external" format="html">{esc(m.group(1))}</xref>', text)
    return text


def make_id(title):
    """Create a valid DITA id from a title."""
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
    s = re.sub(r'\s+', '-', s.strip())
    return s[:60] or 'topic'


def convert_table(lines):
    """Convert a markdown table (list of lines) to DITA simpletable XML."""
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)
    if len(rows) < 2:
        return ''
    # skip separator row (row[1])
    header = rows[0]
    data = [r for i, r in enumerate(rows) if i > 1 or (i == 1 and not re.match(r'^[\s\-:|]+$', lines[i]))]
    # Check if row 1 is separator
    if len(rows) > 1 and re.match(r'^[\s\-:|]+$', '|'.join(rows[1])):
        data = rows[2:]
    else:
        data = rows[1:]

    xml = ['<simpletable>']
    xml.append('  <sthead>')
    for cell in header:
        xml.append(f'    <stentry>{inline(esc(cell))}</stentry>')
    xml.append('  </sthead>')
    for row in data:
        xml.append('  <strow>')
        for cell in row:
            xml.append(f'    <stentry>{inline(esc(cell))}</stentry>')
        xml.append('  </strow>')
    xml.append('</simpletable>')
    return '\n'.join(xml)


def md_to_dita_body(md_text):
    """Convert markdown body text to DITA conbody XML content."""
    lines = md_text.split('\n')
    output = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Fenced code block
        m = re.match(r'^```(\w*)', line)
        if m:
            lang = m.group(1)
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_content = esc('\n'.join(code_lines))
            if lang:
                output.append(f'<codeblock outputclass="language-{lang}">{code_content}</codeblock>')
            else:
                output.append(f'<codeblock>{code_content}</codeblock>')
            continue

        # Table detection
        if '|' in line and i + 1 < len(lines) and re.match(r'^[\s|:\-]+$', lines[i + 1]):
            table_lines = []
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            output.append(convert_table(table_lines))
            continue

        # H2 → section
        m = re.match(r'^## (.+)', line)
        if m:
            title = re.sub(r'^\d+\)\s*', '', m.group(1).strip())
            title = re.sub(r'^Appendix [A-Z]:\s*', '', title)
            # Close previous section if any
            if any('<section' in o for o in output):
                output.append('</section>')
            sid = make_id(title)
            output.append(f'<section id="{sid}">')
            output.append(f'<title>{inline(esc(title))}</title>')
            i += 1
            continue

        # H3 → paragraph with bold title (DITA doesn't nest sections)
        m = re.match(r'^### (.+)', line)
        if m:
            title = re.sub(r'^[\d.]+ ', '', m.group(1).strip())
            output.append(f'<p><b>{inline(esc(title))}</b></p>')
            i += 1
            continue

        # H4 → paragraph with bold
        m = re.match(r'^#### (.+)', line)
        if m:
            output.append(f'<p><b>{inline(esc(m.group(1).strip()))}</b></p>')
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            bq_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                bq_lines.append(lines[i][2:])
                i += 1
            bq_text = ' '.join(bq_lines)
            output.append(f'<note>{inline(esc(bq_text))}</note>')
            continue

        # Ordered list
        if re.match(r'^\d+[\.\)] ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+[\.\)] ', lines[i]):
                item_text = re.sub(r'^\d+[\.\)] ', '', lines[i])
                items.append(f'  <li>{inline(esc(item_text))}</li>')
                i += 1
            output.append('<ol>')
            output.extend(items)
            output.append('</ol>')
            continue

        # Unordered list
        if re.match(r'^[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                item_text = re.sub(r'^[-*] ', '', lines[i])
                items.append(f'  <li>{inline(esc(item_text))}</li>')
                i += 1
            output.append('<ul>')
            output.extend(items)
            output.append('</ul>')
            continue

        # Checkbox list
        if re.match(r'^- \[[ x]\] ', line):
            items = []
            while i < len(lines) and re.match(r'^- \[[ x]\] ', lines[i]):
                item_text = re.sub(r'^- \[[ x]\] ', '', lines[i])
                items.append(f'  <li>{inline(esc(item_text))}</li>')
                i += 1
            output.append('<ul>')
            output.extend(items)
            output.append('</ul>')
            continue

        # Horizontal rule
        if re.match(r'^---+\s*$', line):
            i += 1
            continue

        # Empty line
        if line.strip() == '':
            i += 1
            continue

        # H1 — skip (already used for topic title)
        if re.match(r'^# ', line):
            i += 1
            continue

        # Regular paragraph — collect consecutive non-empty lines
        para_lines = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,4} |```|[-*] |\d+[\.\)] |> |---|\|)', lines[i]):
            para_lines.append(lines[i])
            i += 1
        if para_lines:
            text = ' '.join(para_lines)
            output.append(f'<p>{inline(esc(text))}</p>')
        else:
            i += 1

    # Close last section
    if any('<section' in o for o in output):
        output.append('</section>')

    return '\n'.join(output)


def convert_md_to_concept(md_path, topic_id, title=None):
    """Convert a markdown file to a DITA concept topic."""
    text = md_path.read_text(encoding='utf-8')

    # Extract H1 title if not provided
    if title is None:
        m = re.match(r'^# (.+)', text, re.MULTILINE)
        title = m.group(1).strip() if m else topic_id

    # Get first paragraph as shortdesc
    paragraphs = re.findall(r'^(?!#|\s*$|```|[-*]|\d|\||>|---)(.*)', text, re.MULTILINE)
    shortdesc = ''
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('*') and len(p) > 20:
            shortdesc = re.sub(r'[*`\[\]()]', '', p)[:200]
            break

    body = md_to_dita_body(text)

    dita = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">
<concept id="{topic_id}">
  <title>{esc(title)}</title>
  <shortdesc>{esc(shortdesc)}</shortdesc>
  <conbody>
{body}
  </conbody>
</concept>
'''
    return dita


# ── File conversion map ─────────────────────────────────────────────────

CONVERSIONS = [
    {
        "src": DOCS / "QUICK-START.md",
        "id": "quick-start",
        "title": "Quick Start Guide",
        "out": "quick-start.dita",
    },
    {
        "src": DOCS / "getting-started/dita_intro_guide.md",
        "id": "dita-intro-guide",
        "title": "DITA at a Glance",
        "out": "getting-started/dita-intro-guide.dita",
    },
    {
        "src": DOCS / "getting-started/dita-topic-1-overview.md",
        "id": "dita-overview",
        "title": "DITA Deep Dive",
        "out": "getting-started/dita-overview.dita",
    },
    {
        "src": DOCS / "core-topics/dita-topic-2-authoring.md",
        "id": "dita-authoring",
        "title": "Authoring DITA Topics",
        "out": "core-topics/dita-authoring.dita",
    },
    {
        "src": DOCS / "core-topics/dita-topic-3-reuse-variants.md",
        "id": "dita-reuse-variants",
        "title": "Reuse, Keys, and Variant Management",
        "out": "core-topics/dita-reuse-variants.dita",
    },
    {
        "src": DOCS / "core-topics/dita-topic-4-publishing-dita-ot.md",
        "id": "dita-publishing",
        "title": "Publishing with DITA-OT",
        "out": "core-topics/dita-publishing.dita",
    },
    {
        "src": DOCS / "developer-guides/dita-ot-developer-handbook.md",
        "id": "dita-ot-developer-handbook",
        "title": "DITA-OT Architecture and DevOps",
        "out": "developer-guides/dita-ot-developer-handbook.dita",
    },
    {
        "src": DOCS / "developer-guides/dita-ot-dev-technical-guide.md",
        "id": "dita-ot-technical-reference",
        "title": "Technical Reference: XSLT Patterns and Glossary",
        "out": "developer-guides/dita-ot-technical-reference.dita",
    },
    {
        "src": DOCS / "plugins-and-customization/dita-ot-html5-xslt-customization-final.md",
        "id": "xslt-customization-tutorial",
        "title": "XSLT Customization Tutorial",
        "out": "plugins-and-customization/xslt-customization-tutorial.dita",
    },
    {
        "src": DOCS / "reference/dita-ot-architecture-ascii-snippet.md",
        "id": "architecture-diagram",
        "title": "DITA-OT Architecture Diagram",
        "out": "reference/architecture-diagram.dita",
    },
]


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    DITA_OUT.mkdir(parents=True, exist_ok=True)

    for conv in CONVERSIONS:
        src = conv["src"]
        if not src.exists():
            print(f"  SKIP (not found): {src}")
            continue

        out_path = DITA_OUT / conv["out"]
        out_path.parent.mkdir(parents=True, exist_ok=True)

        print(f"  Converting: {src.name} → {conv['out']}")
        dita_xml = convert_md_to_concept(src, conv["id"], conv["title"])
        out_path.write_text(dita_xml, encoding='utf-8')

    # ── Glossary (Appendix B) ────────────────────────────────────────
    print("  Creating: glossary.dita")
    glossary_dita = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">
<concept id="glossary">
  <title>Glossary</title>
  <shortdesc>General DITA and DITA-OT developer terminology.</shortdesc>
  <conbody>
    <section id="general-dita-terms">
      <title>General DITA Terms</title>
      <dl>
        <dlentry><dt>Topic</dt><dd>A modular unit of content (concept/task/reference).</dd></dlentry>
        <dlentry><dt>Map</dt><dd>An assembly structure that organizes topics for publishing.</dd></dlentry>
        <dlentry><dt>Information typing</dt><dd>Using different topic structures for different user intents.</dd></dlentry>
        <dlentry><dt>Reuse</dt><dd>Referencing content instead of duplicating it (conref, keyref, conkeyref).</dd></dlentry>
        <dlentry><dt>Filtering</dt><dd>Producing variants by including/excluding content based on attributes (DITAVAL).</dd></dlentry>
        <dlentry><dt>Specialization</dt><dd>Extending DITA to represent domain concepts while keeping compatibility.</dd></dlentry>
        <dlentry><dt>Constraints</dt><dd>Restricting the DITA model to enforce consistency.</dd></dlentry>
        <dlentry><dt>Conref</dt><dd>Content reference — pulls content from another element by ID.</dd></dlentry>
        <dlentry><dt>Keyref</dt><dd>Key reference — resolves links/text via map-defined keys (late binding).</dd></dlentry>
        <dlentry><dt>Conkeyref</dt><dd>Combines keys and content pulling for flexible multi-context reuse.</dd></dlentry>
      </dl>
    </section>
    <section id="developer-terms">
      <title>DITA-OT Developer Terms</title>
      <dl>
        <dlentry><dt>Transtype</dt><dd>The transform type, e.g., <codeph>html5</codeph>, <codeph>pdf</codeph>.</dd></dlentry>
        <dlentry><dt>Preprocess / preprocess2</dt><dd>Legacy vs map-first preprocessing pipelines.</dd></dlentry>
        <dlentry><dt>Plug-in</dt><dd>Extension package that can inject XSLT, Ant targets, resources.</dd></dlentry>
        <dlentry><dt>Extension point</dt><dd>Named hook where a plug-in can contribute behavior.</dd></dlentry>
        <dlentry><dt>Intermediate files</dt><dd>Normalized/filtered content used by later processing stages.</dd></dlentry>
        <dlentry><dt>DITAVAL</dt><dd>XML file defining conditional processing (include/exclude) rules.</dd></dlentry>
        <dlentry><dt>Chunking</dt><dd>How DITA-OT decides to split or combine topics into output pages/files.</dd></dlentry>
      </dl>
    </section>
  </conbody>
</concept>
'''
    (DITA_OUT / "reference").mkdir(parents=True, exist_ok=True)
    (DITA_OUT / "reference/glossary.dita").write_text(glossary_dita, encoding='utf-8')

    # ── Plugin Reference (Appendix C) ────────────────────────────────
    print("  Creating: plugin-reference.dita")
    plugin_ref_dita = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">
<concept id="plugin-reference">
  <title>Complete Plugin Reference</title>
  <shortdesc>Full source of the v2 starter plugin (com.acme.html5.sidebar) demonstrating production-ready DITA-OT HTML5 customization.</shortdesc>
  <conbody>
    <section id="plugin-xml">
      <title>plugin.xml</title>
      <p>The plugin descriptor declares the plugin ID, its dependency on the HTML5 transtype, and two extension points.</p>
      <codeblock outputclass="language-xml">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;plugin id="com.acme.html5.sidebar" version="1.0.0"&gt;
  &lt;require plugin="org.dita.html5"/&gt;
  &lt;feature extension="dita.xsl.html5" file="xsl/html5/override.xsl"/&gt;
  &lt;feature extension="dita.xsl.html5.toc" file="xsl/toc/toc-override.xsl"/&gt;
&lt;/plugin&gt;</codeblock>
    </section>
    <section id="override-xsl">
      <title>override.xsl — Topic Transform (key excerpts)</title>
      <p><b>Import + JS injection:</b></p>
      <codeblock outputclass="language-xslt">&lt;xsl:import href="plugin:org.dita.html5:xsl/dita2html5.xsl"/&gt;

&lt;xsl:template name="gen-user-head"&gt;
  &lt;xsl:next-match/&gt;
  &lt;script src="{concat($PATH2PROJ, 'js/site.js')}"/&gt;
&lt;/xsl:template&gt;</codeblock>
      <p><b>Topic wrapper (standardizes across concept/task/reference):</b></p>
      <codeblock outputclass="language-xslt">&lt;xsl:template match="*[contains(@class,' topic/topic ')]"&gt;
  &lt;article class="dita-topic" data-topic-type="{local-name()}"&gt;
    &lt;xsl:apply-templates select="*[contains(@class,' topic/title ')]"/&gt;
    &lt;xsl:apply-templates select="*[contains(@class,' topic/shortdesc ')]"/&gt;
    &lt;main class="dita-body"&gt;
      &lt;xsl:apply-templates
        select="*[contains(@class,' topic/body ')]
              | *[contains(@class,' concept/conbody ')]
              | *[contains(@class,' task/taskbody ')]
              | *[contains(@class,' reference/refbody ')]"/&gt;
    &lt;/main&gt;
  &lt;/article&gt;
&lt;/xsl:template&gt;</codeblock>
      <p><b>Notes as callout boxes:</b></p>
      <codeblock outputclass="language-xslt">&lt;xsl:template match="*[contains(@class,' topic/note ')]"&gt;
  &lt;aside class="callout{if (@type) then concat(' callout-', @type) else ''}"&gt;
    &lt;xsl:if test="@type"&gt;
      &lt;div class="callout-title"&gt;&lt;xsl:value-of select="upper-case(@type)"/&gt;&lt;/div&gt;
    &lt;/xsl:if&gt;
    &lt;div class="callout-body"&gt;&lt;xsl:apply-templates/&gt;&lt;/div&gt;
  &lt;/aside&gt;
&lt;/xsl:template&gt;</codeblock>
      <p><b>Code blocks with Copy button:</b></p>
      <codeblock outputclass="language-xslt">&lt;xsl:template match="*[contains(@class,' topic/codeblock ')]"&gt;
  &lt;div class="codeblock"&gt;
    &lt;button class="copy-btn" type="button"&gt;Copy&lt;/button&gt;
    &lt;pre&gt;&lt;code&gt;&lt;xsl:apply-templates/&gt;&lt;/code&gt;&lt;/pre&gt;
  &lt;/div&gt;
&lt;/xsl:template&gt;</codeblock>
      <p><b>Task steps with anchors:</b></p>
      <codeblock outputclass="language-xslt">&lt;xsl:template match="*[contains(@class,' task/step ')]"&gt;
  &lt;li class="task-step"
      data-step="{count(preceding-sibling::*[contains(@class,' task/step ')]) + 1}"&gt;
    &lt;xsl:apply-templates/&gt;
  &lt;/li&gt;
&lt;/xsl:template&gt;</codeblock>
    </section>
    <section id="toc-override-xsl">
      <title>toc-override.xsl — Sidebar Navigation</title>
      <codeblock outputclass="language-xslt">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0"&gt;
  &lt;xsl:import href="plugin:org.dita.html5:xsl/toc.xsl"/&gt;
  &lt;xsl:template match="nav"&gt;
    &lt;nav class="sidebar-toc"&gt;
      &lt;xsl:apply-templates select="@* | node()"/&gt;
    &lt;/nav&gt;
  &lt;/xsl:template&gt;
  &lt;xsl:template match="li"&gt;
    &lt;li data-level="{count(ancestor::li)+1}"&gt;
      &lt;xsl:apply-templates select="@* | node()"/&gt;
    &lt;/li&gt;
  &lt;/xsl:template&gt;
&lt;/xsl:stylesheet&gt;</codeblock>
    </section>
    <section id="ditaval-samples">
      <title>Sample DITAVAL Files</title>
      <p><b>web.ditaval</b> — exclude print-only content:</p>
      <codeblock outputclass="language-xml">&lt;val&gt;
  &lt;prop action="exclude" att="platform" val="print"/&gt;
&lt;/val&gt;</codeblock>
      <p><b>print.ditaval</b> — exclude web-only content:</p>
      <codeblock outputclass="language-xml">&lt;val&gt;
  &lt;prop action="exclude" att="platform" val="web"/&gt;
&lt;/val&gt;</codeblock>
      <p><b>audience-admin.ditaval</b> — admin content only:</p>
      <codeblock outputclass="language-xml">&lt;val&gt;
  &lt;prop action="include" att="audience" val="admin"/&gt;
  &lt;prop action="exclude" att="audience" val="novice"/&gt;
&lt;/val&gt;</codeblock>
    </section>
    <section id="build-command">
      <title>Build Command</title>
      <codeblock outputclass="language-bash">dita -i dita/maps/guides/getting-started.ditamap -f html5 -o out/html5 \
  --nav-toc=full \
  --args.copycss=yes \
  --args.cssroot=css/ \
  --args.css=brand.css \
  --args.filter=build/ditaval/web.ditaval</codeblock>
    </section>
  </conbody>
</concept>
'''
    (DITA_OUT / "reference/plugin-reference.dita").write_text(plugin_ref_dita, encoding='utf-8')

    print(f"\n✅ All DITA topics created in: {DITA_OUT}/")


if __name__ == "__main__":
    main()
