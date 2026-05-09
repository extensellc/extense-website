/**
 * Extense LLC — DITA-OT Branded HTML5 Plugin
 * Interactive site functionality v5.0
 *
 * Features:
 *   • SPA navigation — sidebar clicks load content in main pane
 *   • Draggable sidebar resizer
 *   • Full-text search with ⌘/Ctrl+K shortcut
 *   • Reading time estimate per topic
 *   • On-page outline (mini-TOC) for h2/h3 headings
 *   • Topic type badges (concept/task/reference/glossentry)
 *   • Image zoom on click
 *   • Heading anchor links with click-to-copy
 *   • Breadcrumb navigation
 *   • Index page DOM restructuring + dashboard
 *   • Fixed sidebar with collapsible sections
 *   • Current page highlight + auto-scroll into view
 *   • Next / Previous page navigation bar
 *   • Progress tracking with checkboxes (localStorage)
 *   • Dark mode toggle with localStorage
 *   • Copy-to-clipboard for code blocks
 *   • Scroll progress bar
 *   • Mobile sidebar toggle with overlay
 *   • Keyboard navigation (left/right arrows)
 */

(function () {
  'use strict';

  /* ── Utility ── */
  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); };

  /* ════════════════════════════════════════════
     DARK MODE
     ════════════════════════════════════════════ */
  window.toggleDark = function () {
    document.body.classList.toggle('dark');
    var isDark = document.body.classList.contains('dark');
    localStorage.setItem('extense-dark', isDark ? '1' : '0');
    var btn = $('#themeBtn');
    if (btn) btn.innerHTML = isDark ? '&#9788; Light' : '&#9681; Dark';
  };

  function initDark() {
    if (localStorage.getItem('extense-dark') === '1') {
      document.body.classList.add('dark');
      var btn = $('#themeBtn');
      if (btn) btn.innerHTML = '&#9788; Light';
    }
  }

  /* ════════════════════════════════════════════
     SIDEBAR TOGGLE (mobile)
     ════════════════════════════════════════════ */
  window.extToggleSidebar = function () {
    var nav = $('nav.toc');
    var overlay = $('#sidebarOverlay');
    if (!nav) return;
    var isOpen = nav.classList.toggle('open');
    if (overlay) overlay.classList.toggle('open', isOpen);
  };

  /* ════════════════════════════════════════════
     COPY CODE
     ════════════════════════════════════════════ */
  window.extCopyCode = function (btn) {
    var pre = btn.closest('pre') || btn.parentElement;
    var code = pre.querySelector('code');
    var text = code ? code.textContent : pre.textContent;
    navigator.clipboard.writeText(text).then(function () {
      btn.textContent = 'Copied!'; btn.classList.add('copied');
      setTimeout(function () { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
    }).catch(function () {
      var ta = document.createElement('textarea');
      ta.value = text; ta.style.cssText = 'position:fixed;opacity:0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); btn.textContent = 'Copied!'; } catch (e) {}
      document.body.removeChild(ta);
      setTimeout(function () { btn.textContent = 'Copy'; }, 2000);
    });
  };

  function initCopyButtons() {
    $$('pre').forEach(function (pre) {
      if (pre.querySelector('.copy-btn')) return;
      var btn = document.createElement('button');
      btn.className = 'copy-btn'; btn.type = 'button';
      btn.textContent = 'Copy';
      btn.onclick = function () { extCopyCode(btn); };
      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  }

  /* ════════════════════════════════════════════
     SCROLL PROGRESS BAR
     ════════════════════════════════════════════ */
  function initProgress() {
    var fill = $('#progressFill');
    if (!fill) return;
    window.addEventListener('scroll', function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      fill.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
    });
  }

  /* ════════════════════════════════════════════
     GO TO TOP BUTTON
     ════════════════════════════════════════════ */
  function initGoTop() {
    var btn = $('#goTopBtn');
    if (!btn) {
      btn = document.createElement('button');
      btn.className = 'go-top-btn'; btn.id = 'goTopBtn';
      btn.title = 'Back to top';
      btn.setAttribute('aria-label', 'Scroll to top');
      btn.innerHTML = '\u2191';
      btn.onclick = function () { window.scrollTo({ top: 0, behavior: 'smooth' }); };
      document.body.appendChild(btn);
    }
    window.addEventListener('scroll', function () {
      btn.classList.toggle('visible', window.scrollY > 300);
    });
  }

  /* ════════════════════════════════════════════
     READING TIME ESTIMATE
     ════════════════════════════════════════════ */
  function initReadingTime() {
    var article = $('article[role="article"]') || $('article');
    if (!article || isIndexPage()) return;

    // Don't duplicate
    if (article.querySelector('.reading-time')) return;

    var text = article.textContent || '';
    var words = text.trim().split(/\s+/).length;
    var minutes = Math.max(1, Math.round(words / 220));
    var label = minutes === 1 ? '1 min read' : minutes + ' min read';

    var el = document.createElement('div');
    el.className = 'reading-time';
    el.innerHTML = '<span class="rt-icon">\u23F1</span> ' + label;

    // Insert after the first h1
    var h1 = article.querySelector('h1, .topictitle1');
    if (h1 && h1.nextSibling) {
      h1.parentNode.insertBefore(el, h1.nextSibling);
    }
  }

  /* ════════════════════════════════════════════
     TOPIC TYPE BADGE
     ════════════════════════════════════════════ */
  function initTopicTypeBadge() {
    var article = $('article[role="article"]') || $('article');
    if (!article || isIndexPage()) return;
    if (article.querySelector('.topic-type-badge')) return;

    var type = null;
    var icons = { concept: '\uD83D\uDCD6', task: '\u2611', reference: '\uD83D\uDD17', glossentry: '\uD83D\uDCDA' };
    var labels = { concept: 'Concept', task: 'Task', reference: 'Reference', glossentry: 'Glossary' };

    // Try to detect from body class or article class
    var cls = (article.className || '') + ' ' + (document.body.className || '');
    if (/\btask\b/.test(cls) || article.querySelector('.taskbody, .steps')) type = 'task';
    else if (/\bconcept\b/.test(cls) || article.querySelector('.conbody')) type = 'concept';
    else if (/\breference\b/.test(cls) || article.querySelector('.refbody')) type = 'reference';
    else if (/\bglossentry\b/.test(cls) || article.querySelector('.glossterm')) type = 'glossentry';

    if (!type) return;

    var badge = document.createElement('div');
    badge.className = 'topic-type-badge ' + type;
    badge.textContent = (icons[type] || '') + ' ' + (labels[type] || type);

    var h1 = article.querySelector('h1, .topictitle1');
    if (h1) {
      h1.parentNode.insertBefore(badge, h1);
    }
  }

  /* ════════════════════════════════════════════
     ON-PAGE OUTLINE — Right Sidebar
     ════════════════════════════════════════════ */
  function initPageOutline() {
    // Remove any existing right sidebar
    var existing = $('.right-sidebar');
    if (existing) existing.remove();
    document.body.classList.remove('has-right-sidebar');

    var article = $('article[role="article"]') || $('article');
    if (!article || isIndexPage()) return;

    var headings = $$('h2, h3, .sectiontitle, .topictitle2, .topictitle3', article);
    if (headings.length < 3) return;

    // Create right sidebar
    var sidebar = document.createElement('aside');
    sidebar.className = 'right-sidebar';
    sidebar.setAttribute('aria-label', 'On this page');

    var title = document.createElement('div');
    title.className = 'right-sidebar-title';
    title.textContent = 'On this page';
    sidebar.appendChild(title);

    var ul = document.createElement('ul');
    ul.className = 'right-sidebar-list';

    headings.forEach(function (h, i) {
      if (!h.id) h.id = 'section-' + i;

      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent.replace(/[#\uD83D\uDD17]/g, '').trim();

      var tag = h.tagName ? h.tagName.toLowerCase() : '';
      var cls = h.className || '';
      if (tag === 'h3' || /topictitle3/.test(cls)) {
        li.className = 'rso-h3';
      }

      a.addEventListener('click', function (e) {
        e.preventDefault();
        var target = document.getElementById(h.id);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          history.replaceState(null, '', '#' + h.id);
        }
      });

      li.appendChild(a);
      ul.appendChild(li);
    });

    sidebar.appendChild(ul);
    document.body.appendChild(sidebar);
    document.body.classList.add('has-right-sidebar');

    // Scroll spy — highlight current section in right sidebar
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          $$('.right-sidebar-list a', sidebar).forEach(function (a) { a.classList.remove('active'); });
          var link = sidebar.querySelector('a[href="#' + entry.target.id + '"]');
          if (link) link.classList.add('active');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });

    headings.forEach(function (h) { observer.observe(h); });
  }

  /* ════════════════════════════════════════════
     HEADING ANCHOR LINKS
     ════════════════════════════════════════════ */
  function initHeadingAnchors() {
    var article = $('article[role="article"]') || $('article');
    if (!article || isIndexPage()) return;

    $$('h2, h3, .sectiontitle, .topictitle2, .topictitle3', article).forEach(function (h, i) {
      if (h.querySelector('.heading-anchor')) return;
      if (!h.id) h.id = 'section-' + i;

      var anchor = document.createElement('a');
      anchor.className = 'heading-anchor';
      anchor.href = '#' + h.id;
      anchor.textContent = '#';
      anchor.title = 'Copy link to this section';
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        var url = location.origin + location.pathname + '#' + h.id;
        navigator.clipboard.writeText(url).catch(function () {});
        history.replaceState(null, '', '#' + h.id);
        anchor.textContent = '\u2713';
        setTimeout(function () { anchor.textContent = '#'; }, 1500);
      });
      h.appendChild(anchor);
    });
  }

  /* ════════════════════════════════════════════
     IMAGE ZOOM
     ════════════════════════════════════════════ */
  function initImageZoom() {
    var article = $('article[role="article"]') || $('article');
    if (!article) return;

    $$('.fig img, article img', article).forEach(function (img) {
      if (img.dataset.zoomInit) return;
      img.dataset.zoomInit = '1';
      img.addEventListener('click', function () {
        img.classList.toggle('zoomed');
      });
    });
  }

  /* ════════════════════════════════════════════
     BREADCRUMB NAVIGATION
     ════════════════════════════════════════════ */
  function initBreadcrumb() {
    var article = $('article[role="article"]') || $('article');
    if (!article || isIndexPage()) return;
    if (article.querySelector('.breadcrumb')) return;

    var nav = $('nav.toc');
    if (!nav) return;

    var currentFile = location.pathname.split('/').pop() || 'index.html';
    var activeLink = null;
    $$('a[href]', nav).forEach(function (a) {
      var hrefFile = a.getAttribute('href').split('/').pop().split('#')[0];
      if (hrefFile === currentFile) activeLink = a;
    });

    if (!activeLink) return;

    var crumbs = [];
    var el = activeLink.parentElement;
    while (el && el !== nav) {
      if (el.tagName === 'LI') {
        var span = el.querySelector(':scope > span');
        var link = el.querySelector(':scope > a');
        if (span) crumbs.unshift({ text: span.textContent.trim(), href: null });
        else if (link && link !== activeLink) {
          crumbs.unshift({ text: link.textContent.trim(), href: link.getAttribute('href') });
        }
      }
      el = el.parentElement;
    }

    // Add home
    crumbs.unshift({ text: 'Home', href: 'index.html' });

    if (crumbs.length < 2) return;

    var bc = document.createElement('nav');
    bc.className = 'breadcrumb';
    bc.setAttribute('aria-label', 'Breadcrumb');

    crumbs.forEach(function (crumb, i) {
      if (i > 0) {
        var sep = document.createElement('span');
        sep.className = 'sep';
        sep.textContent = '\u203A';
        bc.appendChild(sep);
      }
      if (crumb.href) {
        var a = document.createElement('a');
        a.href = crumb.href;
        a.textContent = crumb.text;
        bc.appendChild(a);
      } else {
        var s = document.createElement('span');
        s.textContent = crumb.text;
        bc.appendChild(s);
      }
    });

    // Insert at top of article
    var h1 = article.querySelector('h1, .topictitle1');
    var firstChild = article.querySelector('.topic-type-badge') || h1 || article.firstChild;
    if (firstChild) {
      firstChild.parentNode.insertBefore(bc, firstChild);
    }
  }

  /* ════════════════════════════════════════════
     FULL-TEXT SEARCH (builds index from sidebar)
     ════════════════════════════════════════════ */
  var searchIndex = null;
  var searchModal = null;

  function buildSearchIndex() {
    if (searchIndex) return;
    searchIndex = [];

    var nav = $('nav.toc');
    if (!nav) return;

    var links = $$('a[href]', nav);
    var fetched = 0;
    var total = links.length;

    links.forEach(function (a) {
      var href = a.getAttribute('data-abs') || a.getAttribute('href');
      var title = a.textContent.trim();

      // Find the part/section this belongs to
      var partLabel = '';
      var parent = a.parentElement;
      while (parent && parent !== nav) {
        if (parent.tagName === 'LI') {
          var span = parent.querySelector(':scope > span');
          if (span) { partLabel = span.textContent.trim(); break; }
        }
        parent = parent.parentElement;
      }

      // Fetch the content of each page
      fetch(href).then(function (res) {
        if (!res.ok) throw new Error();
        return res.text();
      }).then(function (html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var article = doc.querySelector('article') || doc.querySelector('main') || doc.body;
        // Strip scripts and styles
        $$('script, style', article).forEach(function (el) { el.remove(); });
        var text = article.textContent.replace(/\s+/g, ' ').trim();

        searchIndex.push({
          title: title,
          href: href,
          part: partLabel,
          text: text.substring(0, 5000) // Limit to first 5000 chars for perf
        });
      }).catch(function () {
        searchIndex.push({ title: title, href: href, part: partLabel, text: '' });
      }).finally(function () {
        fetched++;
      });
    });
  }

  function createSearchModal() {
    if (searchModal) return;

    var overlay = document.createElement('div');
    overlay.className = 'search-modal-overlay';
    overlay.id = 'searchOverlay';

    var isMac = /Mac|iPhone|iPad/.test(navigator.platform || '');
    var shortcutKey = isMac ? '\u2318K' : 'Ctrl+K';

    overlay.innerHTML =
      '<div class="search-modal">' +
        '<div class="search-header">' +
          '<span class="search-icon">\uD83D\uDD0D</span>' +
          '<input type="text" class="search-input" id="searchInput" placeholder="Search topics\u2026" autocomplete="off" />' +
          '<span class="search-kbd">Esc</span>' +
        '</div>' +
        '<div class="search-results" id="searchResults"></div>' +
        '<div class="search-footer">' +
          '<span><kbd>\u2191</kbd><kbd>\u2193</kbd> navigate</span>' +
          '<span><kbd>Enter</kbd> open</span>' +
          '<span><kbd>Esc</kbd> close</span>' +
        '</div>' +
      '</div>';

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeSearch();
    });

    document.body.appendChild(overlay);
    searchModal = overlay;

    var input = $('#searchInput');
    var results = $('#searchResults');
    var activeIdx = -1;

    input.addEventListener('input', function () {
      var query = input.value.trim().toLowerCase();
      if (query.length < 2) {
        results.innerHTML = '';
        activeIdx = -1;
        return;
      }
      doSearch(query, results);
      activeIdx = -1;
    });

    input.addEventListener('keydown', function (e) {
      var items = $$('.search-result-item', results);
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        activeIdx = Math.min(activeIdx + 1, items.length - 1);
        highlightResult(items, activeIdx);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        activeIdx = Math.max(activeIdx - 1, 0);
        highlightResult(items, activeIdx);
      } else if (e.key === 'Enter' && activeIdx >= 0 && items[activeIdx]) {
        e.preventDefault();
        items[activeIdx].click();
      }
    });
  }

  function doSearch(query, container) {
    if (!searchIndex) { container.innerHTML = '<div class="search-no-results">Building search index\u2026</div>'; return; }

    var words = query.split(/\s+/);
    var scored = [];

    searchIndex.forEach(function (entry) {
      var titleLower = entry.title.toLowerCase();
      var textLower = entry.text.toLowerCase();
      var score = 0;

      words.forEach(function (w) {
        if (titleLower.indexOf(w) >= 0) score += 10;
        var idx = textLower.indexOf(w);
        if (idx >= 0) score += 3;
      });

      if (score > 0) {
        scored.push({ entry: entry, score: score });
      }
    });

    scored.sort(function (a, b) { return b.score - a.score; });
    var top = scored.slice(0, 15);

    if (top.length === 0) {
      container.innerHTML = '<div class="search-no-results">No results for \u201C' + escHtml(query) + '\u201D</div>';
      return;
    }

    var html = '';
    top.forEach(function (item) {
      var snippet = getSnippet(item.entry.text, words, 120);
      html += '<a class="search-result-item" href="' + escAttr(item.entry.href) + '">' +
        '<div class="sr-title">' + highlightText(escHtml(item.entry.title), words) + '</div>' +
        (snippet ? '<div class="sr-snippet">' + highlightText(escHtml(snippet), words) + '</div>' : '') +
        (item.entry.part ? '<div class="sr-path">' + escHtml(item.entry.part) + '</div>' : '') +
      '</a>';
    });
    container.innerHTML = html;

    // Attach click handlers for SPA navigation
    $$('.search-result-item', container).forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        closeSearch();
        var href = a.getAttribute('href');
        spaNavigate(href, false);
      });
    });
  }

  function getSnippet(text, words, maxLen) {
    var lower = text.toLowerCase();
    var bestIdx = -1;
    words.forEach(function (w) {
      var idx = lower.indexOf(w);
      if (idx >= 0 && (bestIdx < 0 || idx < bestIdx)) bestIdx = idx;
    });
    if (bestIdx < 0) return text.substring(0, maxLen);
    var start = Math.max(0, bestIdx - 40);
    var snippet = text.substring(start, start + maxLen);
    return (start > 0 ? '\u2026' : '') + snippet + (start + maxLen < text.length ? '\u2026' : '');
  }

  function highlightText(html, words) {
    words.forEach(function (w) {
      if (w.length < 2) return;
      var re = new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      html = html.replace(re, '<mark>$1</mark>');
    });
    return html;
  }

  function highlightResult(items, idx) {
    items.forEach(function (el, i) {
      el.classList.toggle('active', i === idx);
    });
    if (items[idx]) items[idx].scrollIntoView({ block: 'nearest' });
  }

  function escHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function escAttr(s) {
    return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
  }

  window.openSearch = function () {
    createSearchModal();
    buildSearchIndex();
    var overlay = $('#searchOverlay');
    if (overlay) {
      overlay.classList.add('open');
      var input = $('#searchInput');
      if (input) { input.value = ''; input.focus(); }
      $('#searchResults').innerHTML = '';
    }
  };

  function closeSearch() {
    var overlay = $('#searchOverlay');
    if (overlay) overlay.classList.remove('open');
  }

  function initSearchShortcut() {
    document.addEventListener('keydown', function (e) {
      // Cmd/Ctrl + K to open search
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        openSearch();
      }
      // Escape to close search
      if (e.key === 'Escape') {
        closeSearch();
      }
      // "/" to open search (when not in input)
      if (e.key === '/' && !e.target.closest('input, textarea, [contenteditable]')) {
        e.preventDefault();
        openSearch();
      }
    });
  }

  /* ════════════════════════════════════════════
     INDEX PAGE: restructure DOM for sidebar layout
     ════════════════════════════════════════════ */
  function isIndexPage() {
    return !$('header[role="banner"]') && $('nav > ul.map, nav > ul.bookmap');
  }

  function initIndexPage() {
    if (!isIndexPage()) return false;

    var body = document.body;

    var header = document.createElement('header');
    header.setAttribute('role', 'banner');
    var topbar = body.querySelector('.extense-topbar');
    var progressBar = body.querySelector('.progress-bar');
    var overlay = body.querySelector('.sidebar-overlay');
    if (topbar) header.appendChild(topbar);
    if (progressBar) header.appendChild(progressBar);
    if (overlay) header.appendChild(overlay);
    body.insertBefore(header, body.firstChild);

    var nav = body.querySelector('nav');
    if (nav) {
      nav.classList.add('toc');
      nav.setAttribute('role', 'navigation');
      $$('li', nav).forEach(function (li) {
        var firstChild = li.firstChild;
        if (firstChild && firstChild.nodeType === 3 && firstChild.textContent.trim()) {
          var text = firstChild.textContent.trim();
          var span = document.createElement('span');
          span.textContent = text;
          li.replaceChild(span, firstChild);
        }
      });
    }

    var h1 = body.querySelector('h1.topictitle1');
    var footer = body.querySelector('footer.extense-footer');

    var main = document.createElement('main');
    main.setAttribute('role', 'main');
    var article = document.createElement('article');
    article.setAttribute('role', 'article');
    article.id = 'index-content';

    if (h1) article.appendChild(h1);
    article.appendChild(createIndexDashboard(nav));
    main.appendChild(article);

    if (footer) {
      body.insertBefore(main, footer);
    } else {
      body.appendChild(main);
    }

    return true;
  }

  function createIndexDashboard(nav) {
    var dash = document.createElement('div');
    dash.className = 'index-dashboard';

    var completed = getProgress();
    var allLinks = nav ? $$('a[href]', nav) : [];
    var total = allLinks.length;
    var done = 0;
    allLinks.forEach(function (a) {
      var key = normalizeHref(a.getAttribute('href'));
      if (completed[key]) done++;
    });
    var pct = total > 0 ? Math.round((done / total) * 100) : 0;

    var isMac = /Mac|iPhone|iPad/.test(navigator.platform || '');
    var shortcutKey = isMac ? '\u2318K' : 'Ctrl+K';

    dash.innerHTML =
      '<div class="dash-welcome">' +
        '<p class="dash-intro">Welcome to the <strong>Extense DITA Complete</strong> training guide. ' +
        'Use the sidebar to navigate topics, press <kbd>' + shortcutKey + '</kbd> to search, ' +
        'or click <strong>Start Learning</strong> below. ' +
        'Check off topics as you complete them to track your progress.</p>' +
      '</div>' +

      '<div class="dash-progress-card">' +
        '<h2 class="dash-card-title">Your Progress</h2>' +
        '<div class="dash-progress-bar"><div class="dash-progress-fill" id="dashProgressFill" style="width:' + pct + '%"></div></div>' +
        '<div class="dash-progress-text" id="dashProgressText">' + done + ' of ' + total + ' topics completed (' + pct + '%)</div>' +
        '<div class="dash-actions">' +
          (allLinks.length > 0 ?
            '<a href="' + allLinks[0].getAttribute('href') + '" class="dash-start-btn">\u25B6 Start Learning</a>' : '') +
          '<button class="dash-reset-btn" onclick="extResetProgress()">\u21BA Reset Progress</button>' +
        '</div>' +
      '</div>' +

      '<div class="dash-parts" id="dashParts"></div>';

    return dash;
  }

  function buildPartProgress(nav) {
    var partsEl = $('#dashParts');
    if (!partsEl || !nav) return;

    var completed = getProgress();
    var parts = $$(':scope > ul > li', nav);
    var html = '';

    parts.forEach(function (part) {
      var span = part.querySelector(':scope > span');
      var partTitle = span ? span.textContent.trim() : 'Section';
      var partLinks = $$('a[href]', part);
      var partTotal = partLinks.length;
      var partDone = 0;
      partLinks.forEach(function (a) {
        if (completed[normalizeHref(a.getAttribute('href'))]) partDone++;
      });
      var partPct = partTotal > 0 ? Math.round((partDone / partTotal) * 100) : 0;

      html += '<div class="dash-part-item">' +
        '<div class="dash-part-header">' +
          '<span class="dash-part-title">' + partTitle + '</span>' +
          '<span class="dash-part-stat">' + partDone + '/' + partTotal + '</span>' +
        '</div>' +
        '<div class="dash-part-bar"><div class="dash-part-fill" style="width:' + partPct + '%"></div></div>' +
      '</div>';
    });

    partsEl.innerHTML = html;
  }

  /* ════════════════════════════════════════════
     PROGRESS TRACKING (localStorage)
     ════════════════════════════════════════════ */
  var PROGRESS_KEY = 'extense-topic-progress';

  function getProgress() {
    try { var d = localStorage.getItem(PROGRESS_KEY); return d ? JSON.parse(d) : {}; } catch (e) { return {}; }
  }

  function saveProgress(data) {
    try { localStorage.setItem(PROGRESS_KEY, JSON.stringify(data)); } catch (e) {}
  }

  function normalizeHref(href) {
    return href.replace(/^(\.\.\/)+/, '').split('#')[0];
  }

  window.extResetProgress = function () {
    if (confirm('Reset all progress? This cannot be undone.')) {
      localStorage.removeItem(PROGRESS_KEY);
      location.reload();
    }
  };

  function initProgressTracking() {
    var nav = $('nav.toc');
    if (!nav) return;

    var completed = getProgress();
    var allLinks = $$('a[href]', nav);

    var summaryDiv = document.createElement('div');
    summaryDiv.className = 'toc-progress-summary';
    summaryDiv.id = 'tocProgressSummary';
    nav.insertBefore(summaryDiv, nav.firstChild);

    allLinks.forEach(function (a) {
      var li = a.parentElement;
      if (!li || li.querySelector('.progress-check')) return;

      var key = normalizeHref(a.getAttribute('href'));
      var cb = document.createElement('button');
      cb.type = 'button';
      cb.className = 'progress-check' + (completed[key] ? ' checked' : '');
      cb.setAttribute('aria-label', completed[key] ? 'Mark as incomplete' : 'Mark as complete');
      cb.title = completed[key] ? 'Completed - click to undo' : 'Click to mark complete';
      cb.innerHTML = completed[key] ? '&#10003;' : '';

      cb.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var data = getProgress();
        if (data[key]) {
          delete data[key];
          cb.classList.remove('checked');
          cb.innerHTML = '';
          cb.title = 'Click to mark complete';
          li.classList.remove('topic-completed');
        } else {
          data[key] = Date.now();
          cb.classList.add('checked');
          cb.innerHTML = '&#10003;';
          cb.title = 'Completed - click to undo';
          li.classList.add('topic-completed');
        }
        saveProgress(data);
        updateProgressSummary(nav);
        buildPartProgress(nav);
        updateDashboardProgress(nav);
      });

      li.insertBefore(cb, a);
      if (completed[key]) li.classList.add('topic-completed');
    });

    updateProgressSummary(nav);
    if (isIndexPage() || $('#dashParts')) buildPartProgress(nav);
  }

  function updateProgressSummary(nav) {
    var summary = $('#tocProgressSummary');
    if (!summary) return;

    var completed = getProgress();
    var allLinks = $$('a[href]', nav);
    var total = allLinks.length;
    var done = 0;
    allLinks.forEach(function (a) {
      if (completed[normalizeHref(a.getAttribute('href'))]) done++;
    });
    var pct = total > 0 ? Math.round((done / total) * 100) : 0;

    summary.innerHTML =
      '<div class="toc-progress-label">' +
        '<span>Progress</span>' +
        '<span class="toc-progress-count">' + done + '/' + total + '</span>' +
      '</div>' +
      '<div class="toc-progress-bar">' +
        '<div class="toc-progress-fill" style="width:' + pct + '%"></div>' +
      '</div>';
  }

  function updateDashboardProgress(nav) {
    var fillEl = $('#dashProgressFill');
    var textEl = $('#dashProgressText');
    if (!fillEl || !textEl) return;

    var completed = getProgress();
    var allLinks = $$('a[href]', nav);
    var total = allLinks.length;
    var done = 0;
    allLinks.forEach(function (a) {
      if (completed[normalizeHref(a.getAttribute('href'))]) done++;
    });
    var pct = total > 0 ? Math.round((done / total) * 100) : 0;
    fillEl.style.width = pct + '%';
    textEl.textContent = done + ' of ' + total + ' topics completed (' + pct + '%)';
  }

  /* ════════════════════════════════════════════
     SIDEBAR: current page, collapse, scroll
     ════════════════════════════════════════════ */
  function initSidebar() {
    var nav = $('nav.toc');
    if (!nav) return;

    var links = $$('a[href]', nav);
    if (!links.length) return;

    var loc = window.location.pathname;
    var currentFile = loc.split('/').pop() || 'index.html';
    var currentPath = loc.replace(/^.*?\/dita-topics\//, 'dita-topics/');

    var activeLink = null;
    links.forEach(function (a) {
      var href = a.getAttribute('href');
      var hrefFile = href.split('/').pop().split('#')[0];
      var hrefNorm = href.replace(/^(\.\.\/)+/, '').split('#')[0];
      if (hrefFile === currentFile || hrefNorm === currentPath) activeLink = a;
    });

    if (activeLink) {
      activeLink.parentElement.classList.add('toc-active');
      var parent = activeLink.parentElement;
      while (parent && parent !== nav) {
        if (parent.tagName === 'LI') parent.classList.remove('collapsed');
        parent = parent.parentElement;
      }
      setTimeout(function () {
        activeLink.scrollIntoView({ block: 'center', behavior: 'auto' });
      }, 100);
    }

    // Add topic count badges to Part headers
    $$(':scope > ul > li > span', nav).forEach(function (span) {
      if (span.querySelector('.toc-count-badge')) return;
      var count = $$('a[href]', span.parentElement).length;
      if (count > 0) {
        var badge = document.createElement('span');
        badge.className = 'toc-count-badge';
        badge.textContent = count;
        span.appendChild(badge);
      }
    });

    $$('li > span', nav).forEach(function (span) {
      span.addEventListener('click', function (e) {
        e.preventDefault();
        span.parentElement.classList.toggle('collapsed');
        saveSidebarState(nav);
      });
    });

    // Restore saved state, or default to all parts collapsed except active
    var restored = restoreSidebarState(nav);
    if (!restored) {
      $$(':scope > ul > li', nav).forEach(function (li) {
        if (li.querySelector('ul') && !li.querySelector('.toc-active')) {
          li.classList.add('collapsed');
        }
      });
    }
  }

  function saveSidebarState(nav) {
    var state = [];
    $$('li > span', nav).forEach(function (span, i) {
      if (span.parentElement.classList.contains('collapsed')) state.push(i);
    });
    try { sessionStorage.setItem('extense-sidebar', JSON.stringify(state)); } catch (e) {}
  }

  function restoreSidebarState(nav) {
    try {
      var saved = sessionStorage.getItem('extense-sidebar');
      if (!saved) return false;
      var state = JSON.parse(saved);
      // Clear current state, then apply saved
      $$('li > span', nav).forEach(function (span, i) {
        span.parentElement.classList.remove('collapsed');
        if (state.indexOf(i) >= 0) span.parentElement.classList.add('collapsed');
      });
      var active = nav.querySelector('.toc-active');
      if (active) {
        var p = active;
        while (p && p !== nav) {
          if (p.tagName === 'LI') p.classList.remove('collapsed');
          p = p.parentElement;
        }
      }
      return true;
    } catch (e) { return false; }
  }

  /* ════════════════════════════════════════════
     NEXT / PREVIOUS PAGE NAVIGATION
     ════════════════════════════════════════════ */
  function initPageNav() {
    var old = $('.page-nav'); if (old) old.remove();

    var nav = $('nav.toc');
    if (!nav) return;

    var allLinks = $$('a[href]', nav).filter(function (a) {
      return a.getAttribute('href').indexOf('#') !== 0;
    });
    if (allLinks.length < 2) return;

    var currentAbs = location.href.split('#')[0].split('?')[0];
    var currentIdx = -1;
    allLinks.forEach(function (a, i) {
      var absHref = a.getAttribute('data-abs') || new URL(a.getAttribute('href'), location.href).href;
      if (absHref.split('#')[0] === currentAbs) currentIdx = i;
    });

    if (currentIdx < 0) {
      var currentFile = location.pathname.split('/').pop() || 'index.html';
      allLinks.forEach(function (a, i) {
        var hrefFile = a.getAttribute('href').split('/').pop().split('#')[0];
        if (hrefFile === currentFile) currentIdx = i;
      });
    }

    if (currentIdx < 0) return;

    var prevLink = currentIdx > 0 ? allLinks[currentIdx - 1] : null;
    var nextLink = currentIdx < allLinks.length - 1 ? allLinks[currentIdx + 1] : null;
    if (!prevLink && !nextLink) return;

    var pageNav = document.createElement('div');
    pageNav.className = 'page-nav';

    if (prevLink) {
      var pa = document.createElement('a');
      pa.href = prevLink.getAttribute('href');
      pa.className = 'nav-prev';
      pa.innerHTML = '<span class="nav-label">Previous</span><span class="nav-title">' + prevLink.textContent.trim() + '</span>';
      pageNav.appendChild(pa);
    } else {
      pageNav.appendChild(document.createElement('div'));
    }

    if (nextLink) {
      var na = document.createElement('a');
      na.href = nextLink.getAttribute('href');
      na.className = 'nav-next';
      na.innerHTML = '<span class="nav-label">Next</span><span class="nav-title">' + nextLink.textContent.trim() + '</span>';
      pageNav.appendChild(na);
    }

    var main = $('main[role="main"]') || $('main');
    var article = main ? $('article', main) : null;
    var target = article || main;
    if (target) target.appendChild(pageNav);
  }

  /* ════════════════════════════════════════════
     KEYBOARD NAVIGATION
     ════════════════════════════════════════════ */
  function initKeyNav() {
    document.addEventListener('keydown', function (e) {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable) return;
      if ($('#searchOverlay.open')) return; // Don't navigate when search is open

      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
        var link = e.key === 'ArrowLeft' ? $('.page-nav .nav-prev') : $('.page-nav .nav-next');
        if (link) { e.preventDefault(); link.click(); }
      }
    });
  }

  /* ════════════════════════════════════════════
     SPA NAVIGATION
     ════════════════════════════════════════════ */
  function absolutizeLinks(container, baseUrl) {
    $$('a[href]', container).forEach(function (a) {
      var href = a.getAttribute('href');
      if (href && !href.startsWith('#') && !href.startsWith('http') &&
          !href.startsWith('javascript:') && !href.startsWith('mailto:')) {
        try {
          var abs = new URL(href, baseUrl).href;
          a.setAttribute('data-abs', abs);
          a.setAttribute('href', abs);
        } catch (e) {}
      }
    });
    $$('img[src]', container).forEach(function (img) {
      var src = img.getAttribute('src');
      if (src && !src.startsWith('http') && !src.startsWith('data:')) {
        try { img.setAttribute('src', new URL(src, baseUrl).href); } catch (e) {}
      }
    });
  }

  function spaNavigate(url, isPopState) {
    var main = $('main[role="main"]') || $('main');
    if (!main) { location.href = url; return; }

    main.classList.add('spa-loading');

    fetch(url)
      .then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.text();
      })
      .then(function (html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');

        var newArticle = doc.querySelector('article[role="article"]') || doc.querySelector('article');
        if (!newArticle) {
          var newMain = doc.querySelector('main[role="main"]') || doc.querySelector('main');
          if (newMain) {
            newArticle = document.createElement('article');
            newArticle.setAttribute('role', 'article');
            newArticle.innerHTML = newMain.innerHTML;
          }
        }
        if (!newArticle) { location.href = url; return; }

        absolutizeLinks(newArticle, url);

        main.innerHTML = '';
        main.appendChild(newArticle);
        main.classList.remove('spa-loading');

        var newTitle = doc.querySelector('title');
        if (newTitle) document.title = newTitle.textContent;

        if (!isPopState) {
          history.pushState({ spaUrl: url }, document.title, url);
        }

        spaUpdateActive(url);
        restoreSidebarWidth();
        restoreSidebarState($('nav.toc'));

        // Re-initialize content features
        initCopyButtons();
        initPageNav();
        initReadingTime();
        initTopicTypeBadge();
        initPageOutline();
        initHeadingAnchors();
        initImageZoom();
        initBreadcrumb();

        window.scrollTo(0, 0);
        var fill = $('#progressFill');
        if (fill) fill.style.width = '0%';
      })
      .catch(function (err) {
        console.warn('SPA navigation failed:', err);
        main.classList.remove('spa-loading');
        location.href = url;
      });
  }

  function spaUpdateActive(url) {
    var nav = $('nav.toc');
    if (!nav) return;

    $$('.toc-active', nav).forEach(function (el) { el.classList.remove('toc-active'); });

    var urlClean = url.split('#')[0].split('?')[0];
    var activeLink = null;
    $$('a[href]', nav).forEach(function (a) {
      var aUrl = (a.getAttribute('data-abs') || a.href || '').split('#')[0].split('?')[0];
      if (aUrl === urlClean) activeLink = a;
    });

    if (!activeLink) {
      var targetFile = urlClean.split('/').pop();
      $$('a[href]', nav).forEach(function (a) {
        var aFile = a.getAttribute('href').split('/').pop().split('#')[0];
        if (aFile === targetFile) activeLink = a;
      });
    }

    if (activeLink) {
      activeLink.parentElement.classList.add('toc-active');
      var parent = activeLink.parentElement;
      while (parent && parent !== nav) {
        if (parent.tagName === 'LI') parent.classList.remove('collapsed');
        parent = parent.parentElement;
      }
      activeLink.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }
  }

  function initSPANav() {
    var nav = $('nav.toc');
    if (!nav) return;

    absolutizeLinks(nav, location.href);
    var main = $('main[role="main"]') || $('main');
    if (main) absolutizeLinks(main, location.href);

    history.replaceState({ spaUrl: location.href }, document.title, location.href);

    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href]');
      if (!link) return;

      var href = link.getAttribute('href');
      if (!href) return;

      if (href.startsWith('#') || href.startsWith('javascript:') || href.startsWith('mailto:')) return;
      if (href.match(/^https?:\/\//) && !href.startsWith(location.origin)) return;
      var pathPart = href.split('?')[0].split('#')[0];
      if (pathPart.match(/\.(pdf|zip|png|jpg|jpeg|gif|svg|css|js)$/i)) return;
      if (e.ctrlKey || e.metaKey || e.shiftKey || e.button !== 0) return;

      var targetFile = pathPart.split('/').pop();
      if (targetFile === 'index.html') return;

      e.preventDefault();
      var absUrl = link.getAttribute('data-abs') || new URL(href, location.href).href;
      spaNavigate(absUrl, false);
    });

    window.addEventListener('popstate', function (e) {
      restoreSidebarWidth();
      if (e.state && e.state.spaUrl) {
        var targetFile = e.state.spaUrl.split('/').pop().split('#')[0];
        if (targetFile === 'index.html') { location.href = e.state.spaUrl; return; }
        spaNavigate(e.state.spaUrl, true);
      }
    });
  }

  /* ════════════════════════════════════════════
     DRAGGABLE SIDEBAR RESIZER
     ════════════════════════════════════════════ */
  var SIDEBAR_WIDTH_KEY = 'extense-sidebar-width';

  function restoreSidebarWidth() {
    try {
      var saved = localStorage.getItem(SIDEBAR_WIDTH_KEY);
      if (saved) {
        var w = parseInt(saved, 10);
        if (w >= 180 && w <= 600) {
          document.documentElement.style.setProperty('--sidebar-w', w + 'px');
        }
      }
    } catch (e) {}
  }

  function initResizer() {
    var nav = $('nav.toc');
    if (!nav) return;
    if (window.innerWidth <= 768) return;

    restoreSidebarWidth();

    var resizer = document.createElement('div');
    resizer.className = 'sidebar-resizer';
    resizer.title = 'Drag to resize sidebar';
    resizer.setAttribute('aria-label', 'Resize sidebar');
    document.body.appendChild(resizer);

    var isResizing = false, startX = 0, startW = 0;

    resizer.addEventListener('mousedown', function (e) {
      isResizing = true;
      startX = e.clientX;
      startW = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--sidebar-w'), 10) || 280;
      document.body.classList.add('resizing');
      e.preventDefault();
    });

    document.addEventListener('mousemove', function (e) {
      if (!isResizing) return;
      var newWidth = Math.max(180, Math.min(600, startW + e.clientX - startX));
      document.documentElement.style.setProperty('--sidebar-w', newWidth + 'px');
    });

    document.addEventListener('mouseup', function () {
      if (!isResizing) return;
      isResizing = false;
      document.body.classList.remove('resizing');
      localStorage.setItem(SIDEBAR_WIDTH_KEY, parseInt(getComputedStyle(document.documentElement).getPropertyValue('--sidebar-w'), 10));
    });

    resizer.addEventListener('touchstart', function (e) {
      isResizing = true;
      startX = e.touches[0].clientX;
      startW = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--sidebar-w'), 10) || 280;
      document.body.classList.add('resizing');
      e.preventDefault();
    }, { passive: false });

    document.addEventListener('touchmove', function (e) {
      if (!isResizing) return;
      var newWidth = Math.max(180, Math.min(600, startW + e.touches[0].clientX - startX));
      document.documentElement.style.setProperty('--sidebar-w', newWidth + 'px');
    }, { passive: true });

    document.addEventListener('touchend', function () {
      if (!isResizing) return;
      isResizing = false;
      document.body.classList.remove('resizing');
      localStorage.setItem(SIDEBAR_WIDTH_KEY, parseInt(getComputedStyle(document.documentElement).getPropertyValue('--sidebar-w'), 10));
    });

    window.addEventListener('resize', function () {
      resizer.style.display = window.innerWidth <= 768 ? 'none' : '';
    });
  }

  /* ════════════════════════════════════════════
     INIT
     ════════════════════════════════════════════ */

  /* ── PWA: Offline Status Indicator ──────────────────────── */
  function initOfflineDownload() {
    if (!('serviceWorker' in navigator)) return;

    const topbar = document.querySelector('.extense-topbar .topbar-actions');
    if (!topbar) return;

    const btn = document.createElement('button');
    btn.className = 'topbar-btn';
    btn.id = 'offline-btn';
    btn.title = 'Offline reading status';
    btn.style.cssText = 'font-size:.8rem;padding:4px 10px;border-radius:6px;border:1px solid var(--text-sec);color:var(--text-sec);background:transparent;cursor:default;margin-left:4px;pointer-events:none;';

    // Check if we're online or offline
    function updateStatus() {
      if (navigator.onLine) {
        btn.textContent = '● Online';
        btn.style.borderColor = 'var(--green)';
        btn.style.color = 'var(--green)';
        btn.title = 'Connected — pages are being cached for offline use';
      } else {
        btn.textContent = '● Offline';
        btn.style.borderColor = 'var(--gold)';
        btn.style.color = 'var(--gold)';
        btn.title = 'Offline — reading from cached pages';
      }
    }

    updateStatus();
    window.addEventListener('online', updateStatus);
    window.addEventListener('offline', updateStatus);
    topbar.insertBefore(btn, topbar.firstChild);
  }

  function init() {
    initDark();
    initIndexPage();
    initCopyButtons();
    initProgress();
    initGoTop();
    initResizer();
    initSidebar();
    initProgressTracking();
    initPageNav();
    initKeyNav();
    initSPANav();
    initSearchShortcut();
    initReadingTime();
    initTopicTypeBadge();
    initPageOutline();
    initHeadingAnchors();
    initImageZoom();
    initBreadcrumb();
    initOfflineDownload();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
