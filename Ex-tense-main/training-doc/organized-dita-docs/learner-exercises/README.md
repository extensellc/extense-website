# Learner Exercises

Hands-on DITA exercises organized by learning phase. Each exercise is a self-contained DITA task topic with step-by-step instructions, expected output, and self-check criteria.

## Structure

| File | Phase | Persona | Description |
|------|-------|---------|-------------|
| `phase1-setup-verification.dita` | 1: Foundation | Both | Install DITA-OT, verify environment, run first build |
| `phase2-first-topics.dita` | 2: Authoring | Both | Write concept, task, and reference topics from scratch |
| `phase2-maps-and-reuse.dita` | 2: Authoring | Both | Create maps, use conref/keyref, build a reusable library |
| `phase3-publishing-builds.dita` | 3W: Publishing | Writer | Build HTML5/PDF, apply DITAVAL filters, multi-variant output |
| `phase3-architecture-exploration.dita` | 3E: Architecture | Engineer | Trace preprocessing pipeline, inspect temp files, map extension points |
| `phase4-plugin-development.dita` | 4: Developer | Engineer (optional Writer) | Create an HTML5 plugin with XSLT overrides and CSS branding |
| `phase5-capstone-project.dita` | 5: Capstone | Both | End-to-end project combining authoring, reuse, publishing, and customization |
| `exercises.ditamap` | — | — | Map collecting all exercises for building |

## Prerequisites

- DITA-OT 4.x installed (Phase 1 exercise walks through this)
- Java 17+
- A text/XML editor (VS Code recommended)

## How to Build

```bash
cd learner-exercises
dita -i exercises.ditamap -f html5 -o out/exercises
```

## Persona Key

- **[W]** = Technical Writer track
- **[E]** = Software Engineer track
- **[Both]** = Required for everyone
