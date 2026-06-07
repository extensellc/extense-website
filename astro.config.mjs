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
    // FAQ moved under Resources; old Company URL 301s to the new location.
    '/company/faqs': '/resources/faq',
    // Retired placeholder "insights" posts -> their dedicated guide pages.
    '/resources/ai-content-readiness': '/resources/ai-readiness',
    '/resources/dita-migration-playbook': '/resources/migration-playbook',
    '/resources/publishing-automation': '/resources/automation-guide',

    // Defensive 301s for the OLD ex-tense.co .html URLs, in case anything
    // hits them on the new domain. (Primary equity transfer is the old
    // domain's own .htaccess — see docs/reframe-2026/seo-cutover.md.)
    '/about.html': '/company',
    '/contact.html': '/contact',
    '/our-process.html': '/company/our-process',
    '/careers.html': '/company/careers',
    '/privacy-policy.html': '/privacy',
    '/terms.html': '/terms',
    '/solutions/technical-documentation-publishing.html': '/solutions/technical-docs-and-publishing',
    '/solutions/content-migration-modernization.html': '/solutions/content-migration',
    '/solutions/xml-data-interoperability.html': '/solutions/xml-data-interoperability',
    '/services/dita-engineering.html': '/services/dita-engineering',
    '/services/publishing-engineering.html': '/services/publishing-engineering',
    '/services/ccms-services.html': '/services/ccms-services',
    '/services/xml-engineering.html': '/services/xml-engineering',
    '/services/technical-writing-content-development.html': '/services/technical-writing-content-development',
    '/services/structured-content-strategy.html': '/services/structured-content-strategy',
    '/services/system-integration.html': '/services/system-integration',
    '/industries/government.html': '/industries/government-and-defense',
    '/industries/financial-services.html': '/industries/financial-services',
    '/industries/insurance.html': '/industries/insurance',
    '/industries/automotive.html': '/industries/transportation',
    '/industries/life-sciences.html': '/industries/life-sciences',
    '/resources/faqs.html': '/resources/faq',
    '/resources/ai-content-readiness-guide.html': '/resources/ai-readiness',
    '/resources/dita-migration-playbook.html': '/resources/migration-playbook',
    '/resources/publishing-automation-guide.html': '/resources/automation-guide',
    '/work': '/company/our-work-and-case-studies',
    '/work/case-studies.html': '/company/our-work-and-case-studies',
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
        if (item.url.match(/\/(solutions|services|industries|resources|company|contact)\/?$/)) {
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
