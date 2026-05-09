/*
  Content collections — Extense LLC
  Spec ref: EXTENSE_DESIGN_BRIEF.md §8 (/insights)

  Single collection: insights — long-form posts for the editorial publication
  surface. Topic taxonomy locked: DITA / S1000D / CCMS Migration / RAG-AI /
  Methodology.

  Editorial bar (locked): every post names tools and standards, takes a
  position, could be read by a working DITA architect without insulting their
  intelligence. Posts that don't pass the bar don't ship.
*/

import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const insights = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/insights" }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    publishedAt: z.coerce.date(),
    readingTime: z.string(), // e.g., "8 min read"
    topic: z.enum(["DITA", "S1000D", "CCMS Migration", "RAG/AI", "Methodology"]),
    draft: z.boolean().optional().default(false),
  }),
});

export const collections = { insights };
