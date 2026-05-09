---
title: "Migrations fail in Architecture, not in Migration"
summary: "Most botched DITA migrations were lost before the first batch ran. The conversion design — and the QA harness around it — is where the project succeeds or fails."
publishedAt: 2025-11-04
readingTime: "11 min read"
topic: "CCMS Migration"
draft: false
---

> Phase 4 copy directive: this post is a placeholder structural shell. Phase 4
> editorial production replaces this body with the practitioner-authored
> long-form post that meets the locked editorial bar.

## The pattern

Almost every DITA migration that goes sideways traces the failure back to the same upstream cause: the conversion design was an afterthought. Architecture decisions about the target schema were made too late, the QA harness was an afterthought to the conversion runs, and the migration team was discovering content-quality problems in production batches that should have been surfaced in pilot.

The failure feels like execution. The cause is design.

## Discovery isn't optional

[Phase 4 expansion: what Discovery in a migration context actually looks like — content audit at scale, sampling strategy, identifying the content patterns that will resist conversion, understanding the legacy authoring workflow that produced the patterns. The argument that skipping Discovery is the most common single cause of failed migrations across the industry, and the reason isn't laziness — it's that Discovery is unglamorous and doesn't ship anything visible.]

## Conversion design before conversion code

[Phase 4 expansion: the mapping spec from source patterns to target DITA constructs is the architectural artifact. Examples of source-to-target mappings that look obvious but aren't: heading-level disambiguation, footnote handling, figure references, conditional content profiling, controlled vocabulary mapping. The argument that the conversion code is small once the mapping spec is right; the cost is in the mapping spec, not the code.]

## QA harness before pilot conversion

[Phase 4 expansion: the validation strategy as part of the conversion design, not a downstream check. Schematron rules that encode the target schema's actual constraints; structural validators that catch round-trip equivalence failures; metadata completeness checks; link integrity post-conversion. The argument that the QA harness has to run in parallel with the conversion engine, not after.]

## The pilot is the architecture's final exam

[Phase 4 expansion: how a representative pilot conversion surfaces architecture decisions that need adjustment before the production run. The pilot isn't a small migration; it's a stress test for the schema design and the mapping spec. The discipline of stopping the program after pilot, fixing the architecture, and re-running pilot before authorizing production conversion.]

## Cutover as procedural, not panicked

[Phase 4 expansion: the rollback plan as a first-class engineering artifact. Parallel running protocols. The pattern of cutovers that go smoothly: every failure mode was rehearsed before go-live; every recovery procedure was tested. The pattern of cutovers that don't: the rollback plan was a paragraph, and the team discovered missing pieces under fire.]

## Closing

The migration phase carries the heaviest production load, but the work that determines whether it succeeds happens in Architecture. The 45% reuse rate we deliver isn't a function of the conversion engine; it's a function of the conversion design.
