# XML Fundamentals Training Guide

**From XML Basics to Your First DITA Project**

A structured training manual covering XML, DTD, XSD, and introductory DITA — designed as a prerequisite for the Extense DITA Training Guide.

## Who Is This For?

- Technical writers new to XML
- Content strategists learning structured content
- Developers working with XML-based systems
- Anyone preparing to learn DITA

**No prior XML experience required.**

## Structure

The training is organized into 4 progressive parts plus hands-on exercises:

| Part | Title | Chapters | Difficulty |
|------|-------|----------|------------|
| 1 | XML Fundamentals | Ch 1-4 + Reference | Beginner |
| 2 | Document Type Definitions (DTD) | Ch 5-7 + Reference | Beginner |
| 3 | XML Schema Definition (XSD) | Ch 8-10 + Reference | Intermediate |
| 4 | Introduction to DITA | Ch 11-13 + Reference | Intermediate |
| — | Learner Exercises | Exercises 1-4 | Progressive |

## File Organization

```
xml-fundamentals-training/
├── xml-fundamentals-supermap.ditamap   # Master bookmap
├── topics/
│   ├── frontmatter/preface.dita
│   ├── part01-xml/                     # 4 concept topics + 1 reference
│   ├── part02-dtd/                     # 3 concept topics + 1 reference
│   ├── part03-xsd/                     # 3 concept topics + 1 reference
│   └── part04-dita-intro/              # 3 concept topics + 1 reference
├── submaps/
│   ├── part01-xml-fundamentals.ditamap
│   ├── part02-dtd-validation.ditamap
│   ├── part03-xsd-schemas.ditamap
│   └── part04-dita-introduction.ditamap
└── learner-exercises/
    ├── exercises.ditamap
    ├── exercise01-xml-basics.dita
    ├── exercise02-dtd-validation.dita
    ├── exercise03-xsd-schema.dita
    └── exercise04-first-dita-project.dita
```

## Building

### Prerequisites

- [DITA Open Toolkit](https://www.dita-ot.org) 4.x or later
- Java 17+

### Build HTML5

```bash
dita --input=xml-fundamentals-supermap.ditamap \
     --format=html5 \
     --output=out/html5
```

### Build PDF

```bash
dita --input=xml-fundamentals-supermap.ditamap \
     --format=pdf \
     --output=out/pdf
```

## Learning Path

1. Read chapters in order (Part 1 → 2 → 3 → 4)
2. Complete the corresponding exercise after each part
3. Use the quick-reference topics as cheat sheets while working
4. After completing this guide, continue with the **Extense DITA Training Guide** for advanced topics

## Estimated Time

| Activity | Time |
|----------|------|
| Part 1: XML Fundamentals (reading) | 2-3 hours |
| Exercise 1: XML Basics | 45-60 min |
| Part 2: DTD (reading) | 2-3 hours |
| Exercise 2: DTD Validation | 60-90 min |
| Part 3: XSD (reading) | 3-4 hours |
| Exercise 3: XSD Schemas | 60-90 min |
| Part 4: DITA Intro (reading) | 2-3 hours |
| Exercise 4: First DITA Project | 90-120 min |
| **Total** | **~16-22 hours** |

## Author

Extense LLC — Intelligent Content Services

## License

Copyright © 2026 Extense LLC. All rights reserved.
