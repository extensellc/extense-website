---
title: "AI-readiness is a content-engineering problem"
summary: "Most regulated-industry RAG deployments fail at the content layer, not the model layer. Retrieval precision is upstream of model selection."
publishedAt: 2026-01-15
readingTime: "9 min read"
topic: "RAG/AI"
draft: false
---

> Phase 4 copy directive: this post is a placeholder structural shell. Phase 4
> editorial production replaces this body with the practitioner-authored
> long-form post that meets the locked editorial bar — names tools and
> standards, takes a position, could be read by a working DITA architect or
> retrieval engineer without insulting their intelligence.

## The frame: precision over recall in regulated workloads

In open-domain RAG, recall failures are noticeable but rarely catastrophic — a missed result is a worse user experience, not a regulatory event. In regulated industries, the asymmetry inverts: a hallucinated citation is materially worse than a missed one. The missed result gets escalated to a human; the hallucinated citation gets followed.

This single asymmetry reshapes every architectural decision in a content-engineering pipeline that supports regulated AI deployments.

## What "AI-ready content" actually means

[Phase 4 expansion: structured-content prerequisites for retrieval — chunking strategy aligned to semantic boundaries, metadata schema for filtered retrieval, provenance tracking through the pipeline, content-typing that survives ingestion. Concrete examples from DITA and S1000D where each prerequisite has a natural counterpart. Anti-patterns: chunking that severs claim from evidence, metadata that gets stripped at ingestion, content models that don't survive the round-trip.]

## The evaluation harness is the architecture

[Phase 4 expansion: argument that retrieval evaluation isn't a measurement step at the end — it's an architectural component that shapes chunking and metadata decisions. Test sets per use case, regression harnesses that catch retrieval drift after content changes, the discipline of measuring precision against representative regulated-industry queries before production deployment.]

## When the content estate fights the retrieval architecture

[Phase 4 expansion: the failure pattern when content was never engineered for retrieval — RAG over Word documents, chunking that respects file boundaries instead of semantic boundaries, metadata that exists only at the document level. The remediation pattern: content remediation as a Migration-pillar activity rather than an AI-pillar activity, because the work is content engineering, not model engineering.]

## Closing: the model selection comes after

The most successful AI deployments in regulated industries are the ones where the content was engineered for retrieval before the model was selected. The reverse — model selected, content retrofitted afterward — is the failure pattern that produces six-figure investments in models running against four-figure-quality content estates.
