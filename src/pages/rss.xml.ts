/*
  RSS feed for /insights — at /rss.xml.

  Spec ref: EXTENSE_DESIGN_BRIEF.md §8 (/insights — RSS link)

  RSS is the canonical subscription mechanism for the technical audience.
*/

import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const posts = await getCollection("insights", ({ data }) => !data.draft);
  const sortedPosts = posts.sort(
    (a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime()
  );

  return rss({
    title: "Extense LLC — Resources",
    description:
      "Field notes, technical writing, and methodology dispatches from the Extense practice. DITA, S1000D, CCMS migration, RAG retrieval engineering, methodology.",
    site: context.site ?? "https://www.extense.co",
    items: sortedPosts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.publishedAt,
      description: post.data.summary,
      link: `/resources/${post.id}/`,
      categories: [post.data.topic],
    })),
    customData: `<language>en-us</language>`,
  });
}
