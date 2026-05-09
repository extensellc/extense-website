#!/usr/bin/env python3
"""
Extense DITA Instant Preview
=============================
Renders DITA XML (topic, concept, task, reference, glossgroup, map, bookmap)
as styled HTML for fast in-editor preview — no DITA-OT processing required.

Usage:
    python3 dita-preview.py <file.dita|file.ditamap>
    python3 dita-preview.py <file.dita> --port 8124
    python3 dita-preview.py <file.dita> --no-serve   # just write HTML, don't serve
"""

import xml.etree.ElementTree as ET
import sys, os, argparse, html, http.server, socketserver, threading, webbrowser, re, time, json
from pathlib import Path

# ── CSS ──────────────────────────────────────────────────────────────────────
CSS = """
:root {
  --bg: #ffffff; --fg: #1e1e1e; --accent: #0066cc; --accent2: #004999;
  --border: #d4d4d4; --code-bg: #f5f5f5; --note-bg: #e8f4fd;
  --warn-bg: #fff3cd; --danger-bg: #f8d7da; --tip-bg: #d4edda;
  --sidebar-bg: #f8f9fa; --header-bg: #1a1a2e; --header-fg: #ffffff;
  --table-stripe: #f8f9fa; --shadow: 0 1px 3px rgba(0,0,0,.12);
  --radius: 6px; --font: "Segoe UI", system-ui, -apple-system, sans-serif;
  --mono: "Cascadia Code", "Fira Code", "JetBrains Mono", monospace;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1e1e1e; --fg: #d4d4d4; --accent: #569cd6; --accent2: #9cdcfe;
    --border: #404040; --code-bg: #2d2d2d; --note-bg: #1a3a4a;
    --warn-bg: #4a3a1a; --danger-bg: #4a1a1a; --tip-bg: #1a4a2a;
    --sidebar-bg: #252526; --header-bg: #0d1117; --header-fg: #e6edf3;
    --table-stripe: #252526; --shadow: 0 1px 3px rgba(0,0,0,.4);
  }
}
*, *::before, *::after { box-sizing: border-box; }
body {
  font-family: var(--font); color: var(--fg); background: var(--bg);
  margin: 0; padding: 0; line-height: 1.65; font-size: 15px;
}
.page-header {
  background: var(--header-bg); color: var(--header-fg);
  padding: 12px 24px; font-size: 12px; display: flex;
  justify-content: space-between; align-items: center;
}
.page-header .badge {
  background: var(--accent); color: #fff; padding: 2px 8px;
  border-radius: 3px; font-size: 11px; font-weight: 600; text-transform: uppercase;
}
.layout { display: flex; min-height: calc(100vh - 44px); }
.sidebar {
  width: 260px; background: var(--sidebar-bg); border-right: 1px solid var(--border);
  padding: 16px; overflow-y: auto; flex-shrink: 0; font-size: 13px;
}
.sidebar h3 { margin: 0 0 12px; font-size: 13px; text-transform: uppercase;
  letter-spacing: .5px; color: var(--accent); }
.sidebar ul { list-style: none; padding: 0; margin: 0; }
.sidebar li { margin: 2px 0; }
.sidebar a {
  color: var(--fg); text-decoration: none; display: block;
  padding: 4px 8px; border-radius: 4px; transition: background .15s;
}
.sidebar a:hover { background: var(--border); }
.sidebar .active { background: var(--accent); color: #fff; }
.content { flex: 1; max-width: 900px; margin: 0 auto; padding: 32px 40px; }
h1 { font-size: 28px; font-weight: 700; margin: 0 0 8px; color: var(--fg); }
h2 { font-size: 22px; font-weight: 600; margin: 32px 0 12px;
  padding-bottom: 6px; border-bottom: 2px solid var(--accent); }
h3 { font-size: 18px; font-weight: 600; margin: 24px 0 8px; }
h4 { font-size: 15px; font-weight: 600; margin: 20px 0 6px; }
.shortdesc {
  font-size: 16px; color: var(--accent2); margin: 0 0 24px;
  padding: 12px 16px; background: var(--note-bg); border-radius: var(--radius);
  border-left: 4px solid var(--accent);
}
p { margin: 0 0 12px; }
ul, ol { margin: 0 0 12px; padding-left: 24px; }
li { margin: 4px 0; }
a { color: var(--accent); }

/* Tables */
table {
  width: 100%; border-collapse: collapse; margin: 16px 0;
  box-shadow: var(--shadow); border-radius: var(--radius); overflow: hidden;
}
th, td { padding: 10px 14px; text-align: left; border: 1px solid var(--border); }
th { background: var(--accent); color: #fff; font-weight: 600; font-size: 13px; }
tr:nth-child(even) td { background: var(--table-stripe); }

/* Code */
pre {
  background: var(--code-bg); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 14px 18px;
  overflow-x: auto; font-size: 13px; line-height: 1.5; margin: 12px 0;
}
code, .codeph {
  font-family: var(--mono); background: var(--code-bg);
  padding: 1px 5px; border-radius: 3px; font-size: 13px;
}
pre code { background: none; padding: 0; }

/* Notes */
.note {
  padding: 12px 16px; margin: 12px 0; border-radius: var(--radius);
  border-left: 4px solid var(--accent); background: var(--note-bg);
}
.note.warning  { border-color: #ffc107; background: var(--warn-bg); }
.note.danger, .note.caution { border-color: #dc3545; background: var(--danger-bg); }
.note.tip      { border-color: #28a745; background: var(--tip-bg); }
.note-label { font-weight: 700; text-transform: uppercase; font-size: 12px;
  letter-spacing: .5px; margin-bottom: 4px; }

/* Task steps */
.steps { counter-reset: step; list-style: none; padding-left: 0; }
.steps > li {
  counter-increment: step; position: relative; padding: 12px 16px 12px 48px;
  margin: 8px 0; background: var(--sidebar-bg); border-radius: var(--radius);
  border: 1px solid var(--border);
}
.steps > li::before {
  content: counter(step); position: absolute; left: 12px; top: 12px;
  width: 26px; height: 26px; background: var(--accent); color: #fff;
  border-radius: 50%; display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 13px;
}
.step-cmd { font-weight: 600; }
.step-info { margin-top: 6px; font-size: 14px; color: var(--fg); opacity: .85; }
.stepresult { margin-top: 6px; padding: 8px 12px; background: var(--tip-bg);
  border-radius: 4px; font-size: 13px; }

/* Choices */
.choices { margin: 8px 0 8px 16px; }
.choices li { margin: 4px 0; }

/* Definition list */
dl { margin: 12px 0; }
dt { font-weight: 600; margin-top: 10px; }
dd { margin: 2px 0 8px 20px; }

/* Map / Bookmap TOC */
.map-toc { font-size: 14px; }
.map-toc ul { list-style: none; padding-left: 20px; margin: 4px 0; }
.map-toc > ul { padding-left: 0; }
.map-toc li { margin: 3px 0; padding: 3px 0; }
.map-toc .topichead { font-weight: 700; color: var(--accent); margin-top: 12px; }
.map-toc .href { color: var(--fg); font-family: var(--mono); font-size: 12px;
  opacity: .6; margin-left: 8px; }

/* Metadata panel */
.metadata {
  margin-top: 32px; padding: 16px; background: var(--sidebar-bg);
  border: 1px solid var(--border); border-radius: var(--radius); font-size: 13px;
}
.metadata h3 { margin: 0 0 8px; font-size: 14px; }
.metadata table { box-shadow: none; font-size: 13px; }
.metadata th { background: var(--border); color: var(--fg); }

/* Image */
.image-wrapper { margin: 12px 0; text-align: center; }
.image-wrapper img { max-width: 100%; border-radius: var(--radius); }

/* Glossary */
.glossentry { margin: 12px 0; padding: 12px 16px; background: var(--sidebar-bg);
  border-left: 3px solid var(--accent); border-radius: var(--radius); }
.glossterm { font-weight: 700; font-size: 16px; }
.glossdef { margin: 4px 0 0; }
.glossSurfaceForm { font-style: italic; font-size: 13px; opacity: .7; }

/* Section links */
.section-anchor { text-decoration: none; opacity: 0; margin-left: 6px;
  transition: opacity .15s; }
h2:hover .section-anchor, h3:hover .section-anchor { opacity: .5; }

/* Related links */
.related-links { margin-top: 32px; padding-top: 16px;
  border-top: 1px solid var(--border); }
.related-links h3 { font-size: 15px; }
"""

# ── Helpers ──────────────────────────────────────────────────────────────────

def text(el):
    """Get all text content from an element, including tails of children."""
    if el is None:
        return ""
    parts = []
    if el.text:
        parts.append(el.text)
    for ch in el:
        parts.append(render_inline(ch))
        if ch.tail:
            parts.append(html.escape(ch.tail))
    return "".join(parts)

def render_inline(el):
    """Render inline elements like <b>, <i>, <codeph>, <xref>, <uicontrol>, etc."""
    tag = local(el.tag)
    t = text(el)
    if tag in ("b", "bold"):
        return f"<strong>{t}</strong>"
    if tag in ("i", "italic"):
        return f"<em>{t}</em>"
    if tag in ("codeph", "apiname", "option", "parmname", "varname", "synph"):
        return f"<code class='codeph'>{t}</code>"
    if tag == "xref":
        href = el.get("href", "#")
        scope = el.get("scope", "local")
        label = t if t.strip() else href
        if scope == "external":
            return f"<a href='{html.escape(href)}' target='_blank'>{label}</a>"
        return f"<a href='{html.escape(href)}'>{label}</a>"
    if tag == "uicontrol":
        return f"<strong style='background:var(--code-bg);padding:1px 6px;border-radius:3px;'>{t}</strong>"
    if tag == "menucascade":
        items = [render_inline(u) for u in el.findall(".//" + ns("uicontrol", el))]
        if not items:
            items = [render_inline(u) for u in el.findall(".//uicontrol")]
        return " ▸ ".join(items) if items else t
    if tag == "filepath":
        return f"<code class='codeph' style='color:var(--accent2)'>{t}</code>"
    if tag == "wintitle":
        return f"<em>{t}</em>"
    if tag in ("term", "keyword"):
        return f"<em>{t}</em>"
    if tag == "ph":
        return t
    if tag == "fn":
        return f"<sup title='{html.escape(t)}'>[*]</sup>"
    if tag == "cite":
        return f"<cite>{t}</cite>"
    if tag == "q":
        return f"&ldquo;{t}&rdquo;"
    if tag == "image":
        src = el.get("href", "")
        alt = el.get("alt", "")
        return f"<img src='{html.escape(src)}' alt='{html.escape(alt)}' style='max-height:1.2em;vertical-align:middle;'/>"
    if tag == "sup":
        return f"<sup>{t}</sup>"
    if tag == "sub":
        return f"<sub>{t}</sub>"
    if tag in ("data", "resourceid"):
        return ""
    # Unknown inline — just return text
    return t

def ns(tag, el):
    """Construct namespaced tag if needed."""
    m = re.match(r'\{(.+?)\}', el.tag)
    if m:
        return f"{{{m.group(1)}}}{tag}"
    return tag

def local(tag):
    """Strip namespace from tag."""
    if "}" in tag:
        return tag.split("}")[1]
    return tag

def find_all_local(el, *tags):
    """Find child elements matching any of the given local tag names."""
    results = []
    for ch in el:
        if local(ch.tag) in tags:
            results.append(ch)
    return results

def find_local(el, *tags):
    """Find first child element matching any of the given local tag names."""
    for ch in el:
        if local(ch.tag) in tags:
            return ch
    return None

def find_recursive(el, tag):
    """Find all descendants with matching local tag name."""
    results = []
    for ch in el.iter():
        if local(ch.tag) == tag:
            results.append(ch)
    return results

# ── Block renderers ──────────────────────────────────────────────────────────

def render_block(el, depth=0):
    """Render a block-level DITA element to HTML."""
    tag = local(el.tag)
    out = []

    if tag == "p":
        out.append(f"<p>{text(el)}</p>")
    elif tag == "shortdesc":
        out.append(f"<div class='shortdesc'>{text(el)}</div>")
    elif tag == "section":
        sid = el.get("id", "")
        title_el = find_local(el, "title")
        if title_el is not None:
            t = text(title_el)
            anchor = f"<a class='section-anchor' href='#{sid}'>§</a>" if sid else ""
            out.append(f"<h2 id='{sid}'>{t}{anchor}</h2>")
        for ch in el:
            if local(ch.tag) != "title":
                out.append(render_block(ch, depth))
    elif tag in ("ul", "sl"):
        items = "".join(f"<li>{text(li)}{render_children(li)}</li>"
                        for li in el if local(li.tag) in ("li", "sli"))
        out.append(f"<ul>{items}</ul>")
    elif tag == "ol":
        items = "".join(f"<li>{text(li)}{render_children(li)}</li>"
                        for li in el if local(li.tag) == "li")
        out.append(f"<ol>{items}</ol>")
    elif tag == "li":
        out.append(f"<li>{text(el)}{render_children(el)}</li>")
    elif tag in ("codeblock", "screen"):
        lang = el.get("outputclass", "")
        out.append(f"<pre><code class='{lang}'>{html.escape(text_raw(el))}</code></pre>")
    elif tag == "note":
        ntype = el.get("type", "note")
        labels = {"note": "Note", "tip": "Tip", "warning": "Warning",
                  "caution": "Caution", "danger": "Danger", "important": "Important",
                  "remember": "Remember", "attention": "Attention"}
        label = labels.get(ntype, ntype.title())
        out.append(f"<div class='note {ntype}'><div class='note-label'>{label}</div>{text(el)}{render_children(el)}</div>")
    elif tag == "fig":
        title_el = find_local(el, "title")
        img_el = find_local(el, "image")
        cap = f"<figcaption>{text(title_el)}</figcaption>" if title_el is not None else ""
        img = ""
        if img_el is not None:
            src = img_el.get("href", "")
            alt_el = find_local(img_el, "alt")
            alt = text(alt_el) if alt_el is not None else ""
            img = f"<img src='{html.escape(src)}' alt='{html.escape(alt)}'/>"
        out.append(f"<figure class='image-wrapper'>{img}{cap}</figure>")
    elif tag == "image":
        src = el.get("href", "")
        alt_el = find_local(el, "alt")
        alt = text(alt_el) if alt_el is not None else ""
        placement = el.get("placement", "inline")
        if placement == "break":
            out.append(f"<div class='image-wrapper'><img src='{html.escape(src)}' alt='{html.escape(alt)}'/></div>")
        else:
            out.append(f"<img src='{html.escape(src)}' alt='{html.escape(alt)}' style='max-height:1.2em;vertical-align:middle;'/>")
    elif tag == "table":
        out.append(render_table(el))
    elif tag == "simpletable":
        out.append(render_simpletable(el))
    elif tag == "dl":
        out.append("<dl>")
        for entry in find_all_local(el, "dlentry"):
            dt = find_local(entry, "dt")
            dd = find_local(entry, "dd")
            if dt is not None:
                out.append(f"<dt>{text(dt)}</dt>")
            if dd is not None:
                out.append(f"<dd>{text(dd)}{render_children(dd)}</dd>")
        out.append("</dl>")
    elif tag == "lq":
        out.append(f"<blockquote>{text(el)}{render_children(el)}</blockquote>")
    elif tag == "lines":
        out.append(f"<pre style='font-family:var(--font)'>{html.escape(text_raw(el))}</pre>")
    elif tag in ("steps", "steps-unordered"):
        ordered = tag == "steps"
        items = []
        for step in find_all_local(el, "step"):
            items.append(render_step(step))
        cls = "steps" if ordered else ""
        list_tag = "ol" if ordered else "ul"
        out.append(f"<{list_tag} class='{cls}'>{''.join(items)}</{list_tag}>")
    elif tag in ("context", "prereq", "result", "postreq"):
        labels = {"context": "Context", "prereq": "Before you begin",
                  "result": "Result", "postreq": "What to do next"}
        out.append(f"<div style='margin:12px 0;'><h3>{labels.get(tag, tag.title())}</h3>")
        out.append(f"{text(el)}{render_children(el)}</div>")
    elif tag in ("example",):
        title_el = find_local(el, "title")
        if title_el is not None:
            out.append(f"<h3>Example: {text(title_el)}</h3>")
        else:
            out.append("<h3>Example</h3>")
        for ch in el:
            if local(ch.tag) != "title":
                out.append(render_block(ch, depth))
    elif tag == "choices":
        items = "".join(f"<li>{text(ch)}</li>" for ch in find_all_local(el, "choice"))
        out.append(f"<ul class='choices'>{items}</ul>")
    elif tag == "choicetable":
        out.append(render_choicetable(el))
    elif tag in ("stepsection",):
        out.append(f"<div style='margin:8px 0;font-style:italic;'>{text(el)}</div>")
    elif tag == "title":
        level = min(depth + 1, 6)
        out.append(f"<h{level}>{text(el)}</h{level}>")
    elif tag in ("related-links",):
        out.append("<div class='related-links'><h3>Related Links</h3><ul>")
        for link in find_recursive(el, "link"):
            href = link.get("href", "")
            lt = find_local(link, "linktext")
            label = text(lt) if lt is not None else href
            out.append(f"<li><a href='{html.escape(href)}'>{label}</a></li>")
        out.append("</ul></div>")
    elif tag in ("prolog", "titlealts", "metadata", "resourceid", "data"):
        pass  # skip — we extract metadata separately
    elif tag in ("body", "conbody", "taskbody", "refbody", "glossBody",
                 "abstract", "bodydiv", "sectiondiv", "div"):
        for ch in el:
            out.append(render_block(ch, depth))
    elif tag in ("title",):
        pass  # handled by parent
    else:
        # Fallback: render children
        if len(el) > 0:
            for ch in el:
                out.append(render_block(ch, depth))
        elif el.text and el.text.strip():
            out.append(f"<p>{text(el)}</p>")

    return "\n".join(out)

def render_children(el):
    """Render all child block elements."""
    parts = []
    for ch in el:
        if local(ch.tag) not in ("text",):
            parts.append(render_block(ch))
    return "\n".join(parts)

def render_step(step):
    """Render a <step> element."""
    cmd = find_local(step, "cmd")
    info = find_local(step, "info")
    stepresult = find_local(step, "stepresult")
    choices = find_local(step, "choices")
    substeps = find_local(step, "substeps")

    parts = [f"<div class='step-cmd'>{text(cmd)}</div>" if cmd is not None else ""]
    if info is not None:
        parts.append(f"<div class='step-info'>{text(info)}{render_children(info)}</div>")
    if choices is not None:
        parts.append(render_block(choices))
    if substeps is not None:
        items = "".join(render_step(s) for s in find_all_local(substeps, "substep"))
        parts.append(f"<ol class='steps' style='margin-left:16px'>{items}</ol>")
    if stepresult is not None:
        parts.append(f"<div class='stepresult'>Result: {text(stepresult)}</div>")

    return f"<li>{''.join(parts)}</li>"

def text_raw(el):
    """Get raw text content (preserving whitespace) for codeblocks."""
    return ET.tostring(el, encoding="unicode", method="text")

def render_table(el):
    """Render a DITA <table> with <tgroup>."""
    parts = ["<table>"]
    title_el = find_local(el, "title")
    if title_el is not None:
        parts.append(f"<caption>{text(title_el)}</caption>")
    for tg in find_all_local(el, "tgroup"):
        thead = find_local(tg, "thead")
        tbody = find_local(tg, "tbody")
        if thead is not None:
            parts.append("<thead>")
            for row in find_all_local(thead, "row"):
                parts.append("<tr>")
                for entry in find_all_local(row, "entry"):
                    parts.append(f"<th>{text(entry)}{render_children(entry)}</th>")
                parts.append("</tr>")
            parts.append("</thead>")
        if tbody is not None:
            parts.append("<tbody>")
            for row in find_all_local(tbody, "row"):
                parts.append("<tr>")
                for entry in find_all_local(row, "entry"):
                    parts.append(f"<td>{text(entry)}{render_children(entry)}</td>")
                parts.append("</tr>")
            parts.append("</tbody>")
    parts.append("</table>")
    return "\n".join(parts)

def render_simpletable(el):
    """Render a DITA <simpletable>."""
    parts = ["<table>"]
    head = find_local(el, "sthead")
    if head is not None:
        parts.append("<thead><tr>")
        for e in find_all_local(head, "stentry"):
            parts.append(f"<th>{text(e)}</th>")
        parts.append("</tr></thead>")
    parts.append("<tbody>")
    for row in find_all_local(el, "strow"):
        parts.append("<tr>")
        for e in find_all_local(row, "stentry"):
            parts.append(f"<td>{text(e)}{render_children(e)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "\n".join(parts)

def render_choicetable(el):
    """Render a DITA <choicetable>."""
    parts = ["<table>"]
    head = find_local(el, "chhead")
    if head is not None:
        parts.append("<thead><tr>")
        for e in list(head):
            parts.append(f"<th>{text(e)}</th>")
        parts.append("</tr></thead>")
    else:
        parts.append("<thead><tr><th>Option</th><th>Description</th></tr></thead>")
    parts.append("<tbody>")
    for row in find_all_local(el, "chrow"):
        cols = list(row)
        parts.append("<tr>")
        for c in cols:
            parts.append(f"<td>{text(c)}{render_children(c)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "\n".join(parts)

# ── Metadata extraction ─────────────────────────────────────────────────────

def extract_metadata(root):
    """Extract prolog metadata for the info sidebar."""
    meta = {}
    prolog = find_recursive(root, "prolog")
    if not prolog:
        return meta
    prolog = prolog[0]

    # Author
    authors = find_recursive(prolog, "author")
    if authors:
        meta["Author"] = ", ".join(text(a) for a in authors)

    # Critdates
    created = find_recursive(prolog, "created")
    if created:
        meta["Created"] = created[0].get("date", "")
    revised = find_recursive(prolog, "revised")
    if revised:
        meta["Revised"] = revised[-1].get("modified", "")

    # Category
    cats = find_recursive(prolog, "category")
    if cats:
        meta["Category"] = ", ".join(text(c) for c in cats)

    # Audience
    auds = find_recursive(prolog, "audience")
    if auds:
        meta["Audience"] = ", ".join(a.get("type", text(a)) for a in auds)

    # Custom data elements
    for d in find_recursive(prolog, "data"):
        name = d.get("name", "")
        val = d.get("value", "") or text(d)
        if name and val:
            meta[name.replace("-", " ").title()] = val

    # Resource ID
    rids = find_recursive(prolog, "resourceid")
    if rids:
        meta["Resource ID"] = rids[0].get("id", "") or rids[0].get("appid", "")

    return meta

# ── Map / Bookmap renderer ──────────────────────────────────────────────────

def render_map(root, filepath):
    """Render a DITA map or bookmap as a structured TOC."""
    tag = local(root.tag)
    title_el = find_local(root, "title")
    title = text(title_el) if title_el is not None else Path(filepath).stem
    badge = "bookmap" if tag == "bookmap" else "ditamap"

    # Count topics
    topicrefs = find_recursive(root, "topicref") + find_recursive(root, "chapter") + find_recursive(root, "appendix")
    count = len(topicrefs)

    body = f"<h1>{title}</h1>"
    body += f"<div class='shortdesc'>Map type: <strong>{badge}</strong> — {count} topic references</div>"
    body += "<div class='map-toc'>"
    body += render_map_children(root)
    body += "</div>"

    # Reltable
    reltables = find_recursive(root, "reltable")
    if reltables:
        body += "<h2>Relationship Table</h2>"
        for rt in reltables:
            body += render_reltable(rt)

    # Keydefs
    keydefs = [el for el in root.iter() if local(el.tag) in ("keydef",)]
    if keydefs:
        body += "<h2>Key Definitions</h2><table><thead><tr><th>Key</th><th>Href / Scope</th></tr></thead><tbody>"
        for kd in keydefs:
            key = kd.get("keys", "")
            href = kd.get("href", "—")
            scope = kd.get("scope", "")
            body += f"<tr><td><code>{html.escape(key)}</code></td><td>{html.escape(href)} {f'({scope})' if scope else ''}</td></tr>"
        body += "</tbody></table>"

    return build_html(title, body, badge, filepath)

def render_map_children(el, depth=0):
    """Recursively render map children as nested lists."""
    items = []
    for ch in el:
        tag = local(ch.tag)
        if tag in ("topicref", "chapter", "appendix", "appendices", "part",
                    "notices", "mapref", "glossref"):
            href = ch.get("href", "")
            navtitle = ch.get("navtitle", "")
            fmt = ch.get("format", "")
            # Try to find navtitle element
            if not navtitle:
                tm = find_local(ch, "topicmeta")
                if tm is not None:
                    nt = find_local(tm, "navtitle")
                    if nt is not None:
                        navtitle = text(nt)
            label = navtitle or href or tag
            type_badge = f" <span class='badge' style='font-size:10px;padding:1px 4px;'>{tag}</span>" if tag in ("chapter", "appendix", "part", "mapref") else ""
            href_span = f" <span class='href'>{html.escape(href)}</span>" if href else ""
            sub = render_map_children(ch, depth + 1)
            items.append(f"<li>{html.escape(label)}{type_badge}{href_span}{sub}</li>")
        elif tag in ("topichead", "topicgroup"):
            navtitle = ch.get("navtitle", tag)
            sub = render_map_children(ch, depth + 1)
            items.append(f"<li><span class='topichead'>{html.escape(navtitle)}</span>{sub}</li>")
        elif tag in ("frontmatter", "backmatter"):
            sub = render_map_children(ch, depth + 1)
            if sub:
                items.append(f"<li><span class='topichead'>{tag.replace('matter', ' matter').title()}</span>{sub}</li>")
        elif tag in ("booklists",):
            sub = render_map_children(ch, depth + 1)
            if sub:
                items.append(f"<li><span class='topichead'>Book Lists</span>{sub}</li>")
        elif tag in ("toc", "indexlist", "figurelist", "tablelist", "glossarylist"):
            items.append(f"<li>{tag.title()}</li>")

    if items:
        return f"<ul>{''.join(items)}</ul>"
    return ""

def render_reltable(rt):
    """Render a relationship table."""
    parts = ["<table><thead><tr>"]
    header = find_local(rt, "relheader")
    if header is not None:
        for col in find_all_local(header, "relcolspec"):
            t = col.get("type", "topic")
            parts.append(f"<th>{t}</th>")
    parts.append("</tr></thead><tbody>")
    for row in find_all_local(rt, "relrow"):
        parts.append("<tr>")
        for cell in find_all_local(row, "relcell"):
            refs = [tr.get("href", "") for tr in find_all_local(cell, "topicref")]
            parts.append(f"<td>{'<br>'.join(html.escape(r) for r in refs)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "\n".join(parts)

# ── Topic renderer ───────────────────────────────────────────────────────────

def render_topic(root, filepath):
    """Render a DITA topic/concept/task/reference/glossgroup."""
    tag = local(root.tag)
    title_el = find_local(root, "title")
    title = text(title_el) if title_el is not None else Path(filepath).stem

    badge_map = {
        "topic": "topic", "concept": "concept", "task": "task",
        "reference": "reference", "glossentry": "glossentry",
        "glossgroup": "glossgroup", "troubleshooting": "troubleshooting",
        "learningContent": "learning",
    }
    badge = badge_map.get(tag, tag)

    body_parts = []

    # Shortdesc
    sd = find_local(root, "shortdesc")
    if sd is not None:
        body_parts.append(render_block(sd))

    # Abstract
    abstract = find_local(root, "abstract")
    if abstract is not None:
        body_parts.append(render_block(abstract))

    # Body
    body_tags = ("body", "conbody", "taskbody", "refbody")
    for bt in body_tags:
        body_el = find_local(root, bt)
        if body_el is not None:
            for ch in body_el:
                body_parts.append(render_block(ch))

    # Glossgroup — render each glossentry
    if tag == "glossgroup":
        for ge in find_recursive(root, "glossentry"):
            gt = find_local(ge, "glossterm")
            gd = find_local(ge, "glossdef")
            gb = find_local(ge, "glossBody")
            body_parts.append("<div class='glossentry'>")
            if gt is not None:
                body_parts.append(f"<div class='glossterm'>{text(gt)}</div>")
            if gd is not None:
                body_parts.append(f"<div class='glossdef'>{text(gd)}</div>")
            if gb is not None:
                sf = find_local(gb, "glossSurfaceForm")
                if sf is not None:
                    body_parts.append(f"<div class='glossSurfaceForm'>Surface form: {text(sf)}</div>")
                usage = find_local(gb, "glossUsage")
                if usage is not None:
                    body_parts.append(f"<p><strong>Usage:</strong> {text(usage)}</p>")
                scope = find_local(gb, "glossScopeNote")
                if scope is not None:
                    body_parts.append(f"<p><strong>Scope:</strong> {text(scope)}</p>")
                for alt in find_all_local(gb, "glossAlt"):
                    abbr = find_local(alt, "glossAbbreviation")
                    if abbr is not None:
                        body_parts.append(f"<p><strong>Abbreviation:</strong> <code>{text(abbr)}</code></p>")
            body_parts.append("</div>")

    # Single glossentry
    if tag == "glossentry":
        gt = find_local(root, "glossterm")
        gd = find_local(root, "glossdef")
        body_parts.append("<div class='glossentry'>")
        if gt is not None:
            body_parts.append(f"<div class='glossterm'>{text(gt)}</div>")
        if gd is not None:
            body_parts.append(f"<div class='glossdef'>{text(gd)}</div>")
        body_parts.append("</div>")

    # Related links
    rl = find_local(root, "related-links")
    if rl is not None:
        body_parts.append(render_block(rl))

    # Nested topics
    nested = find_all_local(root, "topic", "concept", "task", "reference")
    for nt in nested:
        nt_title = find_local(nt, "title")
        if nt_title is not None:
            body_parts.append(f"<h2>{text(nt_title)}</h2>")
        nt_sd = find_local(nt, "shortdesc")
        if nt_sd is not None:
            body_parts.append(render_block(nt_sd))
        for bt in body_tags:
            nb = find_local(nt, bt)
            if nb is not None:
                for ch in nb:
                    body_parts.append(render_block(ch))

    body_html = f"<h1>{title}</h1>\n" + "\n".join(body_parts)

    # Metadata sidebar
    meta = extract_metadata(root)
    if meta:
        body_html += "\n<div class='metadata'><h3>Topic Metadata</h3><table>"
        for k, v in meta.items():
            body_html += f"<tr><th>{html.escape(k)}</th><td>{html.escape(str(v))}</td></tr>"
        body_html += "</table></div>"

    # Build section links for sidebar
    sections = find_recursive(root, "section")
    nav_items = []
    for s in sections:
        s_title = find_local(s, "title")
        if s_title is not None:
            sid = s.get("id", "")
            nav_items.append((sid, text(s_title)))

    return build_html(title, body_html, badge, filepath, nav_items)

# ── HTML builder ─────────────────────────────────────────────────────────────

def build_html(title, body_html, badge, filepath, nav_items=None):
    """Assemble the complete HTML page."""
    sidebar = ""
    if nav_items:
        sidebar_items = "".join(
            f"<li><a href='#{html.escape(sid)}'>{label}</a></li>"
            for sid, label in nav_items
        )
        sidebar = f"""
        <nav class="sidebar">
          <h3>Sections</h3>
          <ul>{sidebar_items}</ul>
        </nav>"""

    fname = Path(filepath).name

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{html.escape(title)} — DITA Preview</title>
  <style>{CSS}</style>
</head>
<body>
  <header class="page-header">
    <div>
      <strong>DITA Author View</strong> &nbsp;·&nbsp; {html.escape(fname)}
    </div>
    <div>
      <span id="status" style="font-size:11px;margin-right:8px;"></span>
      <span class="badge">{html.escape(badge)}</span>
    </div>
  </header>
  <div class="layout">
    {sidebar}
    <main class="content">
      {body_html}
    </main>
  </div>
  <script>
  (function() {
    var es = new EventSource('/__reload');
    var status = document.getElementById('status');
    es.onmessage = function(e) {
      if (e.data === 'reload') {
        status.textContent = 'Reloading…';
        var scroll = window.scrollY;
        fetch(location.href + '?t=' + Date.now())
          .then(function(r) { return r.text(); })
          .then(function(html) {
            var parser = new DOMParser();
            var doc = parser.parseFromString(html, 'text/html');
            var newContent = doc.querySelector('.content');
            var newSidebar = doc.querySelector('.sidebar');
            if (newContent) document.querySelector('.content').innerHTML = newContent.innerHTML;
            if (newSidebar) document.querySelector('.sidebar').innerHTML = newSidebar.innerHTML;
            window.scrollTo(0, scroll);
            status.textContent = '';
          });
      }
    };
    es.onerror = function() { status.textContent = '⏳ Reconnecting…'; };
    es.onopen = function() { status.textContent = ''; };
  })();
  </script>
</body>
</html>"""

# ── Main ─────────────────────────────────────────────────────────────────────

# ── Live-reload server ────────────────────────────────────────────────────────

_reload_clients = []  # list of SSE response wfile objects

def build_preview(filepath, out_dir):
    """Parse DITA and write preview HTML. Returns True on success."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r'<!DOCTYPE[^>]*>', '', content, count=1)
        root = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"  ✗ XML parse error: {e}", file=sys.stderr)
        return False

    tag = local(root.tag)
    if tag in ("map", "bookmap"):
        html_out = render_map(root, filepath)
    else:
        html_out = render_topic(root, filepath)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html_out, encoding="utf-8")
    return True

def notify_reload():
    """Send reload event to all connected SSE clients."""
    dead = []
    for wfile in _reload_clients:
        try:
            wfile.write(b"data: reload\n\n")
            wfile.flush()
        except Exception:
            dead.append(wfile)
    for d in dead:
        _reload_clients.remove(d)

def watch_file(filepath, out_dir, interval=0.5):
    """Watch the DITA file for changes and rebuild + notify on save."""
    last_mtime = os.path.getmtime(filepath)
    while True:
        time.sleep(interval)
        try:
            mtime = os.path.getmtime(filepath)
            if mtime != last_mtime:
                last_mtime = mtime
                print(f"  ↻ File changed, rebuilding…")
                if build_preview(filepath, out_dir):
                    print(f"  ✓ Preview updated")
                    notify_reload()
        except Exception:
            pass

class LiveReloadHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler that also serves SSE reload events at /__reload."""

    def do_GET(self):
        if self.path == "/__reload":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            _reload_clients.append(self.wfile)
            # Send initial heartbeat
            try:
                self.wfile.write(b": connected\n\n")
                self.wfile.flush()
            except Exception:
                return
            # Keep connection open
            while True:
                time.sleep(1)
                try:
                    self.wfile.write(b": heartbeat\n\n")
                    self.wfile.flush()
                except Exception:
                    break
            return
        return super().do_GET()

    def log_message(self, format, *args):
        pass  # silence request logs


def main():
    parser = argparse.ArgumentParser(description="Instant DITA Preview — no DITA-OT required")
    parser.add_argument("file", help="Path to .dita or .ditamap file")
    parser.add_argument("--port", type=int, default=8124, help="HTTP server port (default: 8124)")
    parser.add_argument("--no-serve", action="store_true", help="Just write HTML, don't start server")
    parser.add_argument("--no-watch", action="store_true", help="Don't watch for file changes")
    parser.add_argument("--output", "-o", default="/tmp/dita-preview", help="Output directory")
    args = parser.parse_args()

    filepath = os.path.abspath(args.file)
    if not os.path.isfile(filepath):
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.output)
    print(f"▸ Parsing {Path(filepath).name}...")

    if not build_preview(filepath, out_dir):
        sys.exit(1)
    print(f"  ✓ Preview written to {out_dir / 'index.html'}")

    if args.no_serve:
        return

    # Kill any existing server on the port
    os.system(f"fuser -k {args.port}/tcp 2>/dev/null")

    # Start file watcher thread
    if not args.no_watch:
        watcher = threading.Thread(target=watch_file, args=(filepath, out_dir), daemon=True)
        watcher.start()
        print(f"  ✓ Watching {Path(filepath).name} for changes")

    # Start HTTP server with live-reload support
    os.chdir(out_dir)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", args.port), LiveReloadHandler) as httpd:
        url = f"http://localhost:{args.port}"
        print(f"  ✓ Author View at {url}")
        print(f"    Open in VS Code: Ctrl+Shift+P → 'Simple Browser: Show' → {url}")
        print(f"    Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  ✓ Server stopped")

if __name__ == "__main__":
    main()
