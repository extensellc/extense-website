// @ts-check
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: process.env.PUBLIC_SITE_URL ?? 'https://www.extense.co',
  output: 'static',
  // /capabilities was retired (folded into Solutions + Services). 301 every
  // old capability URL to the Services index. Once the 7 service detail pages
  // exist (Services rework), these can deep-link to the matching service.
  redirects: {
    '/capabilities': '/services',
    '/capabilities/information-architecture': '/services',
    '/capabilities/content-migration': '/services',
    '/capabilities/ccms-and-publishing': '/services',
    '/capabilities/ai-ready-content': '/services',
  },
  adapter: vercel({
    webAnalytics: { enabled: false },
    imageService: false,
  }),
  integrations: [
    sitemap({
      filter: (page) =>
        // Exclude PDF route from sitemap (it's an artifact, not a page)
        !page.endsWith('/capability-statement.pdf'),
      changefreq: 'monthly',
      priority: 0.7,
      lastmod: new Date(),
      serialize(item) {
        // Boost homepage and primary landing pages
        if (item.url === 'https://www.extense.co/') {
          return { ...item, priority: 1.0 };
        }
        if (item.url.match(/\/(public-sector|private-sector|capabilities|about|insights|contact)\/?$/)) {
          return { ...item, priority: 0.9 };
        }
        return item;
      },
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
    format: 'directory',
  },
  prefetch: {
    prefetchAll: false,
    defaultStrategy: 'hover',
  },
});
