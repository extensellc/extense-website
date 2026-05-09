/**
 * Extense DITA Training Guide — Service Worker v2
 * Full offline support for iPad / iPhone / any PWA browser.
 *
 * Strategy:
 *   - Install: pre-cache EVERY page + all assets (fonts, CSS, JS, icons)
 *   - Fetch:   cache-first with stale-while-revalidate (instant offline nav)
 *   - Activate: purge old cache versions
 */

const CACHE_VERSION = 'extense-dita-v2';

const ALL_ASSETS = [
  './',
  './index.html',
  './css/brand.css',
  './css/fonts.css',
  './js/site.js',
  './commonltr.css',
  './commonrtl.css',
  './manifest.json',
  './icon.svg',
  './icons/icon-192.png',
  './icons/apple-touch-icon.png',
  './fonts/inter-latin.woff2',
  './fonts/jetbrains-mono-400.ttf',
  './fonts/jetbrains-mono-700.ttf',
  './topics/appendices/appendix-metadata-reference.html',
  './topics/appendices/architecture-diagram.html',
  './topics/appendices/glossary.html',
  './topics/appendices/markdown-to-dita-improvement-comparison.html',
  './topics/appendices/plugin-reference.html',
  './topics/frontmatter/preface.html',
  './topics/part01-why/ch01-what-is-intelligent-content.html',
  './topics/part01-why/ch02-problem-with-unstructured-content.html',
  './topics/part01-why/ch03-ai-readiness-maturity-model.html',
  './topics/part01-why/ch04-markdown-limitations.html',
  './topics/part02-prepare/dita-intro-guide.html',
  './topics/part02-prepare/dita-overview.html',
  './topics/part02-prepare/installing-dita-ot.html',
  './topics/part02-prepare/quick-start.html',
  './topics/part02-prepare/setting-up-authoring-tools.html',
  './topics/part03-author/ch05-dita-information-typing.html',
  './topics/part03-author/dita-authoring.html',
  './topics/part03-author/dita-reuse-variants.html',
  './topics/part03-author/writing-first-dita-project.html',
  './topics/part04-architect/ch08-topic-based-architecture.html',
  './topics/part04-architect/ch09-taxonomy-controlled-vocabulary.html',
  './topics/part05-enrich/ai-ready-authoring-guide.html',
  './topics/part05-enrich/ch06-migration-step-by-step.html',
  './topics/part05-enrich/ch07-before-after-examples.html',
  './topics/part05-enrich/ch10-metadata-enrichment.html',
  './topics/part05-enrich/schema-org-mapping.html',
  './topics/part06-publish/cicd-publishing-pipelines.html',
  './topics/part06-publish/dita-project-files.html',
  './topics/part06-publish/dita-publishing.html',
  './topics/part06-publish/multi-channel-output-formats.html',
  './topics/part06-publish/output-customization-without-plugins.html',
  './topics/part06-publish/troubleshooting-dita-builds.html',
  './topics/part07-develop/adding-pipeline-steps.html',
  './topics/part07-develop/custom-docker-images.html',
  './topics/part07-develop/debugging-playbook.html',
  './topics/part07-develop/developing-from-source.html',
  './topics/part07-develop/dita-ot-developer-handbook.html',
  './topics/part07-develop/docker-basics.html',
  './topics/part07-develop/docker-compose-preview.html',
  './topics/part07-develop/extension-points-fundamentals.html',
  './topics/part07-develop/github-actions-cicd.html',
  './topics/part07-develop/key-references.html',
  './topics/part07-develop/map-first-preprocessing.html',
  './topics/part07-develop/ot-mental-model.html',
  './topics/part07-develop/plugin-template.html',
  './topics/part07-develop/preprocessing-deep-dive.html',
  './topics/part07-develop/repo-layout-and-variants.html',
  './topics/part07-develop/robust-xslt-patterns.html',
  './topics/part07-develop/safe-customization-xslt-import.html',
  './topics/part08-customize/create-html5-plugin.html',
  './topics/part08-customize/debugging-workflow.html',
  './topics/part08-customize/dita-ot-technical-reference.html',
  './topics/part08-customize/ditaval-filtering-variants.html',
  './topics/part08-customize/exercises-and-labs.html',
  './topics/part08-customize/extended-element-overrides.html',
  './topics/part08-customize/first-override-xslt.html',
  './topics/part08-customize/html5-transform-architecture.html',
  './topics/part08-customize/passing-parameters.html',
  './topics/part08-customize/production-hardening.html',
  './topics/part08-customize/production-patterns.html',
  './topics/part08-customize/quick-checklists.html',
  './topics/part08-customize/safe-customization-strategies.html',
  './topics/part08-customize/sidebar-toc-chunking-baseline.html',
  './topics/part08-customize/sidebar-toc-customization.html',
  './topics/part08-customize/starter-repo-guide.html',
  './topics/part08-customize/toc-grouping.html',
  './topics/part08-customize/xslt-customization-tutorial.html',
  './topics/part08-customize/xslt-prerequisites.html',
  './topics/part08-customize/xslt-troubleshooting.html',
  './topics/part09-integrate/ch11-rag-pipeline-architecture.html',
  './topics/part09-integrate/ch12-chunking-and-embedding.html',
  './topics/part09-integrate/ch13-retrieval-and-generation.html',
  './topics/part10-measure/ch14-benefits-and-roi.html',
  './topics/part10-measure/ch15-utilizing-intelligent-features.html',
  './topics/part10-measure/ch16-impact-on-final-product.html'
];

// Install: pre-cache EVERYTHING for full offline reading
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_VERSION).then(function(cache) {
      return Promise.allSettled(
        ALL_ASSETS.map(function(url) {
          return cache.add(url).catch(function(err) {
            console.warn('[SW] Failed to cache:', url, err.message);
          });
        })
      ).then(function(results) {
        var ok = results.filter(function(r) { return r.status === 'fulfilled'; }).length;
        console.log('[SW] Pre-cached ' + ok + '/' + ALL_ASSETS.length + ' assets');
      });
    })
  );
  self.skipWaiting();
});

// Activate: purge old caches
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(
        keys.filter(function(k) { return k !== CACHE_VERSION; })
            .map(function(k) { return caches.delete(k); })
      );
    }).then(function() { return self.clients.claim(); })
  );
});

// Fetch: cache-first with stale-while-revalidate
self.addEventListener('fetch', function(event) {
  var url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== location.origin) return;

  event.respondWith(
    caches.match(event.request).then(function(cached) {
      if (cached) {
        // Background refresh for next visit
        event.waitUntil(
          fetch(event.request).then(function(fresh) {
            if (fresh.ok) {
              caches.open(CACHE_VERSION).then(function(c) { c.put(event.request, fresh); });
            }
          }).catch(function() {})
        );
        return cached;
      }
      // Not cached — try network
      return fetch(event.request).then(function(response) {
        if (response.ok) {
          var clone = response.clone();
          caches.open(CACHE_VERSION).then(function(c) { c.put(event.request, clone); });
        }
        return response;
      }).catch(function() {
        // Offline fallback
        if (event.request.headers.get('accept') && event.request.headers.get('accept').indexOf('text/html') !== -1) {
          return caches.match('./index.html');
        }
        return new Response('Offline', { status: 503, statusText: 'Offline' });
      });
    })
  );
});

// Message handler
self.addEventListener('message', function(event) {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  if (event.data && event.data.type === 'GET_CACHE_STATUS') {
    caches.open(CACHE_VERSION).then(function(cache) {
      cache.keys().then(function(keys) {
        if (event.source) {
          event.source.postMessage({
            type: 'CACHE_STATUS',
            cachedCount: keys.length,
            totalCount: ALL_ASSETS.length,
            version: CACHE_VERSION
          });
        }
      });
    });
  }
});
