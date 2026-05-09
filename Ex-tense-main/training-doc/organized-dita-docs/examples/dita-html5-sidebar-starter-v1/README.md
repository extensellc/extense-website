# DITA HTML5 Sidebar Starter — v1 (Minimal)

A minimal DITA project that demonstrates the basics of DITA authoring and HTML5 publishing. This is the **simplified version** — use this to learn the fundamentals before moving to the [v2 starter](../dita-html5-sidebar-starter-v2/) which adds DITAVAL filtering, conref reuse, audience profiling, and a custom XSLT plugin.

## What's included

```
dita-html5-sidebar-starter-v1/
  README.md              ← this file
  build.sh               ← one-command build script
  dita/
    maps/
      getting-started.ditamap   ← root map with key definitions
    topics/
      concepts/
        what-is-acme.dita       ← concept topic
      tasks/
        install.dita            ← task topic (step-by-step)
      reference/
        cli-reference.dita      ← reference topic (command table)
```

## Prerequisites

- DITA-OT 4.x installed and on your PATH
- Java 17+

## Build

```bash
# From this directory:
./build.sh

# Or manually:
dita -i dita/maps/getting-started.ditamap -f html5 -o out/html5 --nav-toc=full
```

## What you'll learn

1. **Three topic types** — concept, task, reference
2. **Maps with key definitions** — product name as a key, resolved everywhere
3. **HTML5 output with sidebar TOC** — `--nav-toc=full`
4. **Build from command line** — the standard DITA-OT workflow

## Next steps

After completing this project, move to the **v2 starter** which adds:
- DITAVAL conditional filtering (platform/audience variants)
- Conref reuse from a shared snippets library
- Custom XSLT plugin with override templates
- Properties files for repeatable builds
- Multiple build variants (web, print, admin, novice)
