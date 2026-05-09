<?xml version="1.0" encoding="UTF-8"?>
<!--
  Extense LLC — Branded HTML5 Override
  Extends the default DITA-OT HTML5 transform with:
    • Extense brand colors (navy/gold/green) and typography
    • Topbar with company branding and dark mode toggle
    • Styled notes as callout boxes (tip/warning/important/note)
    • Code blocks with copy-to-clipboard buttons
    • Topic wrappers with data-topic-type attributes
    • Task step anchors with position index
    • Responsive table wrappers
    • External link handling (rel="noopener noreferrer")
    • Footer with company branding
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                version="3.0"
                exclude-result-prefixes="xs">

  <!--
    NOTE: Do NOT import dita2html5.xsl here.
    The dita.xsl.html5 extension point integrates this stylesheet
    into the pipeline automatically — importing would create a
    circular reference.
  -->

  <!-- ══════════════════════════════════════════════════════════════
       CUSTOM HEAD — inject brand CSS + meta
       ══════════════════════════════════════════════════════════════ -->
  <xsl:template name="gen-user-head">
    <meta name="generator" content="Extense LLC — DITA-OT Branded Plugin v1.0"/>
    <meta name="theme-color" content="#1D397C"/>
    <!-- PWA / iPad Add-to-Home-Screen -->
    <link rel="manifest">
      <xsl:attribute name="href"><xsl:value-of select="$PATH2PROJ"/>manifest.json</xsl:attribute>
    </link>
    <meta name="apple-mobile-web-app-capable" content="yes"/>
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"/>
    <meta name="apple-mobile-web-app-title" content="DITA Guide"/>
    <link rel="apple-touch-icon">
      <xsl:attribute name="href"><xsl:value-of select="$PATH2PROJ"/>icons/apple-touch-icon.png</xsl:attribute>
    </link>
    <meta name="mobile-web-app-capable" content="yes"/>
    <!-- Local fonts (offline-capable — no Google Fonts CDN) -->
    <link rel="stylesheet">
      <xsl:attribute name="href"><xsl:value-of select="$PATH2PROJ"/>css/fonts.css</xsl:attribute>
    </link>
    <!-- Restore saved sidebar width BEFORE render to prevent flash/snap -->
    <script>
      (function(){
        try {
          var w = localStorage.getItem('extense-sidebar-width');
          if (w) { var n = parseInt(w,10); if (n >= 180 &amp;&amp; n &lt;= 600) document.documentElement.style.setProperty('--sidebar-w', n+'px'); }
        } catch(e){}
      })();
    </script>
    <!-- Service Worker registration -->
    <script>
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
          navigator.serviceWorker.register('<xsl:value-of select="$PATH2PROJ"/>service-worker.js', { scope: '<xsl:value-of select="$PATH2PROJ"/>' })
            .then(function(reg) { console.log('[PWA] SW registered, scope:', reg.scope); })
            .catch(function(err) { console.warn('[PWA] SW registration failed:', err); });
        });
      }
    </script>
  </xsl:template>

  <!-- ══════════════════════════════════════════════════════════════
       CUSTOM STYLES — Extense brand design system
       ══════════════════════════════════════════════════════════════ -->
  <xsl:template name="gen-user-styles">
    <style>
      /* ═══ Extense Brand Design Tokens ═══ */
      :root {
        --navy: #1D397C;
        --blue: #4682B4;
        --blue-mid: #81AFCB;
        --gold: #E9AC15;
        --green: #0ACB8B;
        --bg: #f8f9fb;
        --bg-card: #fff;
        --bg-code: #1e1e2e;
        --text: #23272f;
        --text-sec: #5a6270;
        --radius: 10px;
        --shadow: 0 2px 12px rgba(29,57,124,.08);
        --sidebar-w: 280px;
        --topbar-h: 56px;
        --font-body: 'Inter','Segoe UI',system-ui,-apple-system,sans-serif;
        --font-mono: 'JetBrains Mono','Fira Code','Cascadia Code',monospace;
        --right-sidebar-w: 220px;
      }

      /* ═══ Dark Mode ═══ */
      body.dark {
        --bg: #0f1117; --bg-card: #181c25; --bg-code: #12141c;
        --text: #e0e4ec; --text-sec: #8b92a0;
        --shadow: 0 2px 12px rgba(0,0,0,.3);
      }
      body.dark .extense-topbar { background: rgba(15,17,23,.95); border-color: #1e2330; }
      body.dark pre { background: #12141c !important; }
      body.dark th { background: #1a1e28; }
      body.dark .callout { border-color: #2a2e3a; }
      body.dark nav.toc { background: #12161f; border-color: #1e2330; }
      body.dark .right-sidebar { border-color: #1e2330; }
      body.dark .right-sidebar-title { color: #8b92a0; }
      body.dark .right-sidebar-list a { color: #8b92a0; }
      body.dark .right-sidebar-list a:hover { color: var(--blue-mid); }
      body.dark .right-sidebar-list a.active { color: var(--gold); border-left-color: var(--gold); }
      body.dark .toc-count-badge { background: rgba(129,175,203,.1); color: #8b92a0; }
      body.dark nav.toc a { color: #c0c6d4; }
      body.dark nav.toc a:hover { background: #1e2738; color: var(--gold); }
      body.dark nav.toc .toc-active { background: #1a2235; border-left-color: var(--gold); }
      body.dark nav.toc .toc-active > a { color: var(--gold); }
      body.dark .page-nav { border-color: #1e2330; }
      body.dark .page-nav a { color: var(--blue-mid); border-color: #2a2e3a; }
      body.dark .page-nav a:hover { background: #1a2235; border-color: var(--gold); }
      body.dark .extense-footer { background: #0d0f14; border-color: #1e2330; }
      body.dark .toc-part-label { color: var(--blue-mid); border-color: #2a2e3a; }
      body.dark .progress-bar { background: #1e2330; }

      /* ═══ Base ═══ */
      *, *::before, *::after { box-sizing: border-box; }
      html { scroll-behavior: smooth; font-size: 16px; }
      body {
        font-family: var(--font-body); color: var(--text);
        background: var(--bg); line-height: 1.65; margin: 0; padding: 0;
      }

      /* ═══ Topbar ═══ */
      .extense-topbar {
        position: fixed; top: 0; left: 0; right: 0;
        height: var(--topbar-h); z-index: 200;
        background: rgba(248,249,251,.95); backdrop-filter: blur(12px);
        border-bottom: 1px solid #e5e7eb;
        display: flex; align-items: center; padding: 0 1rem; gap: .75rem;
      }
      .extense-topbar .logo {
        font-weight: 800; font-size: 1.1rem; color: var(--navy);
        display: flex; align-items: baseline; gap: .5rem; text-decoration: none;
      }
      .extense-topbar .logo-sub {
        font-weight: 400; font-size: .75rem; color: var(--text-sec);
      }
      .extense-topbar .spacer { flex: 1; }
      .extense-topbar .topbar-btn {
        background: none; border: 1px solid #d1d5db; border-radius: 8px;
        padding: 5px 10px; cursor: pointer; font-size: .8rem; color: var(--text);
        transition: border-color .15s;
      }
      .extense-topbar .topbar-btn:hover { border-color: var(--blue); }
      #sidebarToggle {
        display: none; background: none; border: none;
        font-size: 1.4rem; cursor: pointer; color: var(--text);
        padding: 4px 8px; line-height: 1;
      }

      /* ═══ Progress bar ═══ */
      .progress-bar {
        position: fixed; top: var(--topbar-h); left: 0; right: 0;
        height: 3px; background: #e5e7eb; z-index: 199;
      }
      .progress-fill {
        height: 100%; width: 0;
        background: linear-gradient(90deg, var(--gold), var(--green));
        transition: width .12s ease-out;
      }

      /* ═══ Two-column layout ═══ */
      body {
        display: flex; flex-direction: column; min-height: 100vh;
      }
      header[role="banner"] {
        flex-shrink: 0;
      }
      .site-wrapper {
        display: flex; flex: 1; margin-top: calc(var(--topbar-h) + 3px);
      }

      /* ═══ Sidebar ═══ */
      nav.toc {
        position: fixed !important;
        top: calc(var(--topbar-h) + 3px);
        left: 0; bottom: 0;
        width: var(--sidebar-w);
        background: var(--bg-card);
        border-right: 1px solid #e5e7eb;
        overflow-y: auto;
        overflow-x: hidden;
        padding: .5rem .5rem 2rem .75rem;
        z-index: 50;
        transition: transform .25s ease;
        scrollbar-width: thin;
        scrollbar-color: rgba(29,57,124,.15) transparent;
      }
      nav.toc::-webkit-scrollbar { width: 5px; }
      nav.toc::-webkit-scrollbar-thumb { background: rgba(29,57,124,.15); border-radius: 3px; }
      nav.toc ul { list-style: none; padding: 0; margin: 0; }
      nav.toc li { margin: 0; }

      /* Part headings (non-link spans) */
      nav.toc > ul > li > span {
        display: flex; align-items: center; gap: .25rem;
        padding: .5rem 1rem .3rem;
        font-weight: 800; font-size: .68rem; color: var(--navy);
        text-transform: uppercase; letter-spacing: .06em;
        border-bottom: 1px solid rgba(29,57,124,.08);
        margin-top: .6rem; user-select: none;
        cursor: pointer;
      }
      .toc-count-badge {
        display: inline-flex; align-items: center; justify-content: center;
        min-width: 18px; height: 16px; padding: 0 4px;
        border-radius: 8px; background: rgba(29,57,124,.06);
        color: var(--text-sec); font-size: .58rem; font-weight: 600;
        margin-left: auto; text-transform: none; letter-spacing: 0;
      }
      nav.toc > ul > li > span::before {
        content: '\25BE '; font-size: .7rem;
      }
      nav.toc > ul > li.collapsed > span::before {
        content: '\25B8 ';
      }
      nav.toc > ul > li.collapsed > ul { display: none; }

      /* Sub-group headings (chapter groups) */
      nav.toc ul ul > li > span {
        display: block; padding: .4rem 1rem .25rem 1.5rem;
        font-weight: 700; font-size: .72rem; color: var(--text-sec);
        text-transform: uppercase; letter-spacing: .04em;
        cursor: pointer; user-select: none;
      }
      nav.toc ul ul > li > span::before {
        content: '\25BE '; font-size: .65rem;
      }
      nav.toc ul ul > li.collapsed > span::before {
        content: '\25B8 ';
      }
      nav.toc ul ul > li.collapsed > ul { display: none; }

      /* Links */
      nav.toc a {
        display: block; padding: .32rem .75rem .32rem 2rem;
        font-size: .82rem; color: var(--text); text-decoration: none;
        border-left: 3px solid transparent;
        transition: all .12s ease;
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
      }
      nav.toc a:hover {
        background: rgba(70,130,180,.06); color: var(--blue);
        text-decoration: none;
      }
      .toc-active > a {
        border-left-color: var(--gold) !important;
        color: var(--navy) !important; font-weight: 600;
        background: rgba(233,172,21,.08) !important;
      }
      /* Deeper nesting */
      nav.toc ul ul ul a { padding-left: 2.75rem; font-size: .8rem; }
      nav.toc ul ul ul ul a { padding-left: 3.5rem; font-size: .78rem; }

      /* ═══ Main content area ═══ */
      main[role="main"], main {
        margin-left: var(--sidebar-w);
        flex: 1;
        padding: calc(var(--topbar-h) + 1.5rem) 2.5rem 3rem;
        max-width: 900px;
        min-height: calc(100vh - var(--topbar-h));
      }

      /* ═══ Right Sidebar — on-page outline ═══ */
      .right-sidebar {
        position: fixed;
        top: calc(var(--topbar-h) + 3px);
        right: 0; bottom: 0;
        width: var(--right-sidebar-w);
        overflow-y: auto;
        padding: 1.25rem .75rem 2rem;
        z-index: 40;
        scrollbar-width: thin;
        scrollbar-color: rgba(29,57,124,.1) transparent;
      }
      .right-sidebar::-webkit-scrollbar { width: 4px; }
      .right-sidebar::-webkit-scrollbar-thumb { background: rgba(29,57,124,.1); border-radius: 2px; }
      .right-sidebar-title {
        font-size: .7rem; font-weight: 700;
        text-transform: uppercase; letter-spacing: .06em;
        color: var(--text-sec); margin-bottom: .6rem; padding-left: .5rem;
      }
      .right-sidebar-list { list-style: none; padding: 0; margin: 0; }
      .right-sidebar-list a {
        display: block;
        padding: .2rem .5rem .2rem .75rem;
        font-size: .78rem; color: var(--text-sec);
        text-decoration: none;
        border-left: 2px solid transparent;
        transition: all .15s; line-height: 1.4;
      }
      .right-sidebar-list a:hover {
        color: var(--blue); border-left-color: var(--gold); text-decoration: none;
      }
      .right-sidebar-list a.active {
        color: var(--navy); border-left-color: var(--gold); font-weight: 600;
      }
      .right-sidebar-list .rso-h3 a {
        padding-left: 1.5rem; font-size: .75rem;
      }
      body.has-right-sidebar main[role="main"],
      body.has-right-sidebar main {
        margin-right: var(--right-sidebar-w);
        max-width: none;
      }
      body.has-right-sidebar .extense-footer {
        margin-right: var(--right-sidebar-w);
      }

      /* ═══ Headings ═══ */
      h1, .topictitle1 {
        font-size: 2rem; font-weight: 800; color: var(--navy);
        margin: 0 0 .5rem; padding-bottom: .4rem;
        border-bottom: 3px solid var(--gold);
      }
      h2, .sectiontitle {
        font-size: 1.35rem; font-weight: 700; color: var(--navy);
        margin: 2rem 0 .7rem; padding-bottom: .3rem;
        border-bottom: 2px solid var(--gold);
      }
      h3 { font-size: 1.1rem; font-weight: 700; color: var(--text); margin: 1.4rem 0 .5rem; }
      h4 { font-size: .92rem; font-weight: 600; color: var(--text-sec); margin: 1rem 0 .4rem; }
      p { margin-bottom: .7rem; }
      a { color: var(--blue); text-decoration: none; }
      a:hover { text-decoration: underline; }

      /* ═══ Code ═══ */
      code, .codeph {
        font-family: var(--font-mono); font-size: .83em;
        background: rgba(70,130,180,.08); padding: 1px 5px; border-radius: 4px;
      }
      pre, .codeblock {
        background: var(--bg-code); color: #cdd6f4; border-radius: 8px;
        padding: 1rem 1.25rem; margin: .8rem 0; overflow-x: auto;
        font-family: var(--font-mono); font-size: .8rem; line-height: 1.55;
        position: relative; border-left: 4px solid var(--gold);
      }
      pre code, .codeblock code {
        background: none; color: inherit; padding: 0; font-size: .8rem;
      }
      .copy-btn {
        position: absolute; top: 8px; right: 8px;
        background: rgba(255,255,255,.1); color: #a0a8c0;
        border: none; border-radius: 6px; padding: 4px 10px;
        font-size: .7rem; cursor: pointer; opacity: 0; transition: opacity .2s;
      }
      pre:hover .copy-btn, .codeblock:hover .copy-btn { opacity: 1; }
      .copy-btn:hover { background: rgba(255,255,255,.2); color: #fff; }
      .copy-btn.copied { color: var(--green); }

      /* ═══ Notes / Callouts ═══ */
      .callout {
        border-left: 4px solid; border-radius: 0 8px 8px 0;
        padding: .85rem 1.1rem; margin: .8rem 0; background: var(--bg-card);
      }
      .callout-note { border-color: var(--blue); background: rgba(70,130,180,.06); }
      .callout-tip { border-color: var(--green); background: rgba(10,203,139,.04); }
      .callout-important { border-color: var(--navy); background: rgba(29,57,124,.04); }
      .callout-warning, .callout-caution, .callout-danger {
        border-color: var(--gold); background: rgba(233,172,21,.04);
      }
      .callout-label {
        font-weight: 700; font-size: .8rem; text-transform: uppercase;
        letter-spacing: .04em; margin-bottom: .3rem; display: block;
      }
      .callout-note .callout-label { color: var(--blue); }
      .callout-tip .callout-label { color: var(--green); }
      .callout-important .callout-label { color: var(--navy); }
      .callout-warning .callout-label,
      .callout-caution .callout-label,
      .callout-danger .callout-label { color: #b8860b; }

      /* ═══ Tables ═══ */
      table { width: 100%; border-collapse: collapse; margin: .8rem 0; font-size: .85rem; }
      th, td { padding: .55rem .75rem; text-align: left; border-bottom: 1px solid #e5e7eb; }
      th {
        font-weight: 700; background: #f3f4f6; color: var(--navy);
        font-size: .78rem; text-transform: uppercase; letter-spacing: .03em;
      }

      /* ═══ Next / Previous Navigation ═══ */
      .page-nav {
        display: flex; justify-content: space-between; align-items: stretch;
        margin-top: 3rem; padding-top: 1.5rem;
        border-top: 1px solid #e5e7eb; gap: 1rem;
      }
      .page-nav a {
        display: flex; flex-direction: column; flex: 1;
        padding: .75rem 1rem; border: 1px solid #e5e7eb;
        border-radius: 8px; text-decoration: none; color: var(--text);
        transition: all .15s; max-width: 48%;
      }
      .page-nav a:hover {
        border-color: var(--gold); background: rgba(233,172,21,.04);
        text-decoration: none;
      }
      .page-nav a .nav-label {
        font-size: .7rem; font-weight: 700; text-transform: uppercase;
        letter-spacing: .04em; color: var(--text-sec); margin-bottom: .2rem;
      }
      .page-nav a .nav-title {
        font-size: .88rem; font-weight: 600; color: var(--navy);
      }
      .page-nav .nav-next { text-align: right; margin-left: auto; }
      .page-nav .nav-prev .nav-label::before { content: '\2190 '; }
      .page-nav .nav-next .nav-label::after { content: ' \2192'; }

      /* ═══ Related links ═══ */
      nav.related-links {
        margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee;
      }
      nav.related-links strong { font-size: .82rem; color: var(--navy); }
      nav.related-links a { font-size: .85rem; }

      /* ═══ Short description ═══ */
      .shortdesc {
        font-size: 1.02rem; color: var(--text-sec); margin-bottom: 1rem;
        line-height: 1.6; font-style: italic;
      }

      /* ═══ Images ═══ */
      .fig img, img { max-width: 100%; height: auto; border-radius: 6px; }

      /* ═══ Footer ═══ */
      .extense-footer {
        margin-left: var(--sidebar-w);
        border-top: 1px solid #e5e7eb; padding: 1.5rem 2rem;
        text-align: center; color: var(--text-sec); font-size: .8rem;
        background: var(--bg-card);
      }
      .extense-footer .footer-brand {
        font-weight: 800; color: var(--navy); letter-spacing: 2px;
      }

      /* ═══ Progress Tracking ═══ */
      .progress-check {
        display: inline-flex; align-items: center; justify-content: center;
        width: 14px; height: 14px; min-width: 14px; border-radius: 3px;
        border: 1.5px solid #bbb; background: transparent; color: transparent;
        font-size: 10px; font-weight: 700; cursor: pointer;
        margin-right: 2px; vertical-align: middle;
        transition: all .15s; padding: 0; line-height: 1; flex-shrink: 0;
      }
      .progress-check:hover { border-color: var(--gold); }
      .progress-check.checked {
        background: var(--green); border-color: var(--green); color: #fff;
      }
      .topic-completed > a { opacity: .55; text-decoration: line-through; }
      body.dark .progress-check { border-color: #444; }
      body.dark .progress-check.checked { background: var(--green); border-color: var(--green); }

      /* Sidebar progress summary */
      .toc-progress-summary {
        padding: 10px 16px; border-bottom: 1px solid #e5e7eb;
        background: rgba(29,57,124,.03);
      }
      .toc-progress-label {
        display: flex; justify-content: space-between; align-items: center;
        font-size: .72rem; font-weight: 700; color: var(--navy);
        text-transform: uppercase; letter-spacing: .04em; margin-bottom: 4px;
      }
      .toc-progress-count { color: var(--green); }
      .toc-progress-bar {
        height: 4px; background: #e5e7eb; border-radius: 2px; overflow: hidden;
      }
      .toc-progress-fill {
        height: 100%; background: linear-gradient(90deg, var(--green), var(--blue));
        border-radius: 2px; transition: width .3s;
      }
      body.dark .toc-progress-summary { background: rgba(29,57,124,.1); border-color: #1e2330; }
      body.dark .toc-progress-bar { background: #1e2330; }

      /* Sidebar link with checkbox alignment */
      nav.toc li:has(.progress-check) {
        position: relative;
      }
      nav.toc li:has(.progress-check) > .progress-check {
        position: absolute;
        left: .5rem;
        top: .45rem;
        z-index: 1;
      }
      nav.toc li:has(.progress-check) > a {
        padding-left: 2rem;
      }
      nav.toc li:has(.progress-check) > ul {
        margin-left: 0; padding-left: 0;
      }

      /* ═══ Index Dashboard ═══ */
      .index-dashboard { padding: 0; }
      .dash-welcome { margin-bottom: 1.5rem; }
      .dash-intro {
        font-size: 1rem; color: var(--text-sec); line-height: 1.65;
      }
      .dash-progress-card {
        background: var(--bg-card); border-radius: 12px;
        border: 1px solid #e5e7eb; padding: 1.5rem; margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,.05);
      }
      .dash-card-title {
        font-size: 1.1rem; font-weight: 700; color: var(--navy);
        margin: 0 0 .75rem; padding: 0; border: none;
      }
      .dash-progress-bar {
        height: 10px; background: #e5e7eb; border-radius: 5px;
        overflow: hidden; margin-bottom: .5rem;
      }
      .dash-progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--green), var(--blue));
        border-radius: 5px; transition: width .4s;
      }
      .dash-progress-text {
        font-size: .85rem; color: var(--text-sec); margin-bottom: 1rem;
      }
      .dash-actions { display: flex; gap: .75rem; flex-wrap: wrap; }
      .dash-start-btn {
        display: inline-block; padding: .6rem 1.5rem;
        background: var(--navy); color: #fff; font-weight: 700;
        border-radius: 8px; text-decoration: none; font-size: .88rem;
        transition: background .15s;
      }
      .dash-start-btn:hover { background: #142B60; text-decoration: none; color: #fff; }
      .dash-reset-btn {
        padding: .6rem 1.2rem; background: transparent;
        color: var(--text-sec); border: 1px solid #ccc;
        border-radius: 8px; font-size: .85rem; cursor: pointer;
        transition: all .15s;
      }
      .dash-reset-btn:hover { border-color: var(--gold); color: var(--text); }

      .dash-parts { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1rem; }
      .dash-part-item {
        background: var(--bg-card); border-radius: 10px;
        border: 1px solid #e5e7eb; padding: 1rem;
        box-shadow: 0 1px 4px rgba(0,0,0,.04);
      }
      .dash-part-header {
        display: flex; justify-content: space-between; align-items: center;
        margin-bottom: .5rem;
      }
      .dash-part-title { font-weight: 700; font-size: .82rem; color: var(--navy); }
      .dash-part-stat { font-size: .78rem; color: var(--green); font-weight: 600; }
      .dash-part-bar {
        height: 5px; background: #e5e7eb; border-radius: 3px; overflow: hidden;
      }
      .dash-part-fill {
        height: 100%; background: linear-gradient(90deg, var(--green), var(--blue));
        border-radius: 3px; transition: width .3s;
      }
      body.dark .dash-progress-card,
      body.dark .dash-part-item { background: #181c26; border-color: #1e2330; }
      body.dark .dash-progress-bar,
      body.dark .dash-part-bar { background: #1e2330; }
      body.dark .dash-card-title { color: var(--blue-mid); }
      /* ═══ Sidebar Resizer ═══ */
      .sidebar-resizer {
        position: fixed;
        top: calc(var(--topbar-h) + 3px);
        left: calc(var(--sidebar-w) - 3px);
        bottom: 0;
        width: 6px;
        cursor: col-resize;
        z-index: 51;
        background: rgba(29,57,124,.08);
        transition: background .15s;
      }
      .sidebar-resizer::after {
        content: '';
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 2px; height: 32px;
        border-radius: 2px;
        background: rgba(29,57,124,.15);
        transition: background .15s, height .15s;
      }
      .sidebar-resizer:hover {
        background: rgba(233,172,21,.25);
      }
      .sidebar-resizer:hover::after {
        background: var(--gold); height: 48px;
      }
      body.resizing .sidebar-resizer {
        background: rgba(233,172,21,.3);
      }
      body.resizing .sidebar-resizer::after {
        background: var(--gold); height: 48px;
      }
      body.resizing {
        cursor: col-resize !important;
        -webkit-user-select: none !important;
        user-select: none !important;
      }
      body.resizing * {
        cursor: col-resize !important;
      }
      body.resizing iframe, body.resizing img {
        pointer-events: none;
      }
      body.dark .sidebar-resizer {
        background: rgba(129,175,203,.06);
      }
      body.dark .sidebar-resizer::after {
        background: rgba(129,175,203,.15);
      }
      body.dark .sidebar-resizer:hover,
      body.dark.resizing .sidebar-resizer {
        background: rgba(129,175,203,.2);
      }
      body.dark .sidebar-resizer:hover::after,
      body.dark.resizing .sidebar-resizer::after {
        background: var(--blue-mid);
      }

      /* ═══ SPA Loading ═══ */
      main.spa-loading {
        opacity: .45;
        transition: opacity .15s;
        pointer-events: none;
      }

      /* ═══ Go to top button ═══ */
      .go-top-btn {
        position: fixed; bottom: 2rem; right: 2rem;
        width: 42px; height: 42px;
        background: var(--navy); color: #fff;
        border: none; border-radius: 50%;
        font-size: 1.2rem; line-height: 1;
        cursor: pointer; z-index: 200;
        opacity: 0; transform: translateY(10px);
        transition: opacity .25s, transform .25s, background .15s;
        box-shadow: 0 2px 10px rgba(0,0,0,.2);
        display: flex; align-items: center; justify-content: center;
      }
      .go-top-btn.visible { opacity: 1; transform: translateY(0); }
      .go-top-btn:hover { background: var(--blue); }
      body.dark .go-top-btn { background: var(--gold); color: var(--navy); }
      body.dark .go-top-btn:hover { background: #f0c040; }

      /* ═══ Print ═══ */
      @media print {
        .extense-topbar, .copy-btn, nav.toc, .page-nav, .progress-bar,
        .progress-check, .toc-progress-summary, .index-dashboard,
        #sidebarToggle, .go-top-btn, .sidebar-resizer, .right-sidebar { display: none !important; }
        main[role="main"], main { margin-left: 0; margin-right: 0; padding: 0; max-width: 100%; }
        .extense-footer { margin-left: 0; margin-right: 0; }
        body { font-size: 10pt; }
        pre { white-space: pre-wrap; word-break: break-all; }
        a[href^="http"]::after { content: " (" attr(href) ")"; font-size: .75em; color: #666; }
      }

      /* ═══ Responsive ═══ */
      @media (max-width: 1100px) {
        .right-sidebar { display: none !important; }
        body.has-right-sidebar main[role="main"],
        body.has-right-sidebar main { margin-right: 0; max-width: 900px; }
        body.has-right-sidebar .extense-footer { margin-right: 0; }
      }
      @media (max-width: 900px) {
        :root { --sidebar-w: 260px; }
        main[role="main"], main { padding: 1.5rem 1.5rem 2rem; }
      }
      @media (max-width: 768px) {
        .sidebar-resizer { display: none !important; }
        #sidebarToggle { display: block; }
        nav.toc {
          transform: translateX(-100%);
          box-shadow: none;
        }
        nav.toc.open {
          transform: translateX(0);
          box-shadow: 4px 0 20px rgba(0,0,0,.15);
        }
        .sidebar-overlay {
          display: none; position: fixed; inset: 0;
          background: rgba(0,0,0,.3); z-index: 49;
        }
        .sidebar-overlay.open { display: block; }
        main[role="main"], main {
          margin-left: 0; padding: calc(var(--topbar-h) + 1rem) 1rem 2rem;
        }
        .extense-footer { margin-left: 0; }
        .page-nav { flex-direction: column; }
        .page-nav a { max-width: 100%; }
        .go-top-btn { bottom: 1.2rem; right: 1.2rem; width: 38px; height: 38px; }
      }
    </style>
  </xsl:template>

  <!-- ══════════════════════════════════════════════════════════════
       CUSTOM SCRIPTS — dark mode, copy buttons, step highlight
       ══════════════════════════════════════════════════════════════ -->
  <xsl:template name="gen-user-scripts">
    <script src="{concat($PATH2PROJ, 'js/site.js')}"></script>
  </xsl:template>

  <!-- ══════════════════════════════════════════════════════════════
       CUSTOM HEADER — Extense topbar
       ══════════════════════════════════════════════════════════════ -->
  <xsl:template name="gen-user-header">
    <div class="extense-topbar">
      <button id="sidebarToggle" onclick="extToggleSidebar()" title="Toggle navigation" aria-label="Toggle sidebar">&#9776;</button>
      <a class="logo" href="{$PATH2PROJ}index.html">
        <span>Extense LLC</span>
        <span class="logo-sub">DITA Training Guide</span>
      </a>
      <div class="spacer"></div>
      <button class="topbar-btn" onclick="openSearch()" title="Search (Ctrl+K)" aria-label="Search topics">&#128269; Search</button>
      <button class="topbar-btn" onclick="window.print()" title="Print / Save as PDF">&#128424; Print</button>
      <button class="topbar-btn" id="themeBtn" onclick="toggleDark()" title="Toggle dark mode">&#9681; Dark</button>
    </div>
    <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="extToggleSidebar()"></div>
  </xsl:template>

  <!-- ══════════════════════════════════════════════════════════════
       CUSTOM FOOTER — Extense branding
       ══════════════════════════════════════════════════════════════ -->
  <xsl:template name="gen-user-footer">
    <button class="go-top-btn" id="goTopBtn" onclick="window.scrollTo(0,0)" title="Back to top" aria-label="Scroll to top">&#8593;</button>
    <footer class="extense-footer">
      <div class="footer-brand">EXTENSE</div>
      <xsl:text>© 2026 Extense LLC — DITA Training Guide — Built with DITA-OT</xsl:text>
    </footer>
  </xsl:template>

  <!--
    NOTE: Element-matching templates are intentionally minimal.
    We rely on CSS (brand.css + inline gen-user-styles) to style
    all default DITA-OT output classes. This avoids breaking the
    built-in page structure generation (html/head/body wrapper)
    which the base topic/topic template handles.
    
    Only add element overrides here that cannot be achieved with
    CSS alone (e.g. injecting HTML elements like copy buttons).
  -->

  <!-- ======================================================
       NOTES: styled as callout boxes
       The default DITA-OT note template outputs a div.note
       with noteType class. Our CSS already styles these.
       This override adds semantic aside wrapper plus a
       visible label for richer UX.
       ====================================================== -->
  <xsl:template match="*[contains(@class,' topic/note ')]">
    <xsl:variable name="type" select="if (@type) then @type else 'note'"/>
    <aside class="callout callout-{$type}" role="note">
      <span class="callout-label">
        <xsl:choose>
          <xsl:when test="$type = 'tip'">&#9733; TIP</xsl:when>
          <xsl:when test="$type = 'warning'">&#9888; WARNING</xsl:when>
          <xsl:when test="$type = 'caution'">&#9888; CAUTION</xsl:when>
          <xsl:when test="$type = 'danger'">&#9888; DANGER</xsl:when>
          <xsl:when test="$type = 'important'">&#8505; IMPORTANT</xsl:when>
          <xsl:otherwise>&#8505; NOTE</xsl:otherwise>
        </xsl:choose>
      </span>
      <div class="callout-body">
        <xsl:apply-templates/>
      </div>
    </aside>
  </xsl:template>

</xsl:stylesheet>
