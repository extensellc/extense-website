#!/usr/bin/env python3
"""
Enrich DITA sub-topics with full AI-ready prolog metadata.
Reads each file, determines topic type, and replaces the lean prolog
with the full prolog pattern matching the top-level topics.
"""
import os, re, sys

# ── Metadata assignments per file ──────────────────────────────────────────
# (filename, difficulty, duration, content-domain, content-intent, chatbot-priority,
#  service-line, prerequisites, category, audiences[])

DEVHANDBOOK = {
    "ot-mental-model.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "architecture",
        "content-intent": "explain",
        "chatbot-priority": "high",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-publishing",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "preprocessing-deep-dive.dita": {
        "difficulty": "advanced",
        "duration": "PT25M",
        "content-domain": "architecture",
        "content-intent": "explain",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-ot-developer-handbook",
        "category": "taxonomy:devops",
        "audience": ["developer"],
    },
    "map-first-preprocessing.dita": {
        "difficulty": "advanced",
        "duration": "PT15M",
        "content-domain": "architecture",
        "content-intent": "explain",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "preprocessing-deep-dive",
        "category": "taxonomy:devops",
        "audience": ["developer"],
    },
    "extension-points-fundamentals.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "customization",
        "content-intent": "explain",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "dita-publishing",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "safe-customization-xslt-import.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "customization",
        "content-intent": "best-practice",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "extension-points-fundamentals",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "robust-xslt-patterns.dita": {
        "difficulty": "advanced",
        "duration": "PT15M",
        "content-domain": "xslt",
        "content-intent": "reference",
        "chatbot-priority": "medium",
        "service-line": "xml-engineering",
        "prerequisites": "safe-customization-xslt-import",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "adding-pipeline-steps.dita": {
        "difficulty": "advanced",
        "duration": "PT15M",
        "content-domain": "customization",
        "content-intent": "reference",
        "chatbot-priority": "medium",
        "service-line": "xml-engineering",
        "prerequisites": "extension-points-fundamentals",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "plugin-template.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "customization",
        "content-intent": "reference",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "extension-points-fundamentals",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "developing-from-source.dita": {
        "difficulty": "expert",
        "duration": "PT30M",
        "content-domain": "devops",
        "content-intent": "how-to",
        "chatbot-priority": "low",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-ot-developer-handbook",
        "category": "taxonomy:devops",
        "audience": ["developer"],
    },
    "docker-basics.dita": {
        "difficulty": "intermediate",
        "duration": "PT20M",
        "content-domain": "devops",
        "content-intent": "explain",
        "chatbot-priority": "high",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-publishing",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "custom-docker-images.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "devops",
        "content-intent": "how-to",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "docker-basics",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "docker-compose-preview.dita": {
        "difficulty": "advanced",
        "duration": "PT15M",
        "content-domain": "devops",
        "content-intent": "how-to",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "docker-basics",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "github-actions-cicd.dita": {
        "difficulty": "advanced",
        "duration": "PT30M",
        "content-domain": "devops",
        "content-intent": "reference",
        "chatbot-priority": "high",
        "service-line": "publishing-engineering",
        "prerequisites": "docker-basics",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "debugging-playbook.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "devops",
        "content-intent": "troubleshoot",
        "chatbot-priority": "high",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-ot-developer-handbook",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "repo-layout-and-variants.dita": {
        "difficulty": "intermediate",
        "duration": "PT15M",
        "content-domain": "devops",
        "content-intent": "reference",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-publishing",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "key-references.dita": {
        "difficulty": "advanced",
        "duration": "PT10M",
        "content-domain": "architecture",
        "content-intent": "reference",
        "chatbot-priority": "low",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-ot-developer-handbook",
        "category": "taxonomy:devops",
        "audience": ["developer"],
    },
}

XSLT_TOPICS = {
    "xslt-prerequisites.dita": {
        "difficulty": "intermediate",
        "duration": "PT15M",
        "content-domain": "xslt",
        "content-intent": "explain",
        "chatbot-priority": "medium",
        "service-line": "xml-engineering",
        "prerequisites": "dita-publishing",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "html5-transform-architecture.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "xslt",
        "content-intent": "explain",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "xslt-prerequisites",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "sidebar-toc-chunking-baseline.dita": {
        "difficulty": "intermediate",
        "duration": "PT15M",
        "content-domain": "publishing",
        "content-intent": "explain",
        "chatbot-priority": "high",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-publishing",
        "category": "taxonomy:publishing",
        "audience": ["developer", "build-engineer"],
    },
    "create-html5-plugin.dita": {
        "difficulty": "advanced",
        "duration": "PT25M",
        "content-domain": "customization",
        "content-intent": "how-to",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "html5-transform-architecture",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "first-override-xslt.dita": {
        "difficulty": "intermediate",
        "duration": "PT20M",
        "content-domain": "xslt",
        "content-intent": "how-to",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "create-html5-plugin",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "safe-customization-strategies.dita": {
        "difficulty": "intermediate",
        "duration": "PT15M",
        "content-domain": "customization",
        "content-intent": "best-practice",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "xslt-prerequisites",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "sidebar-toc-customization.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "xslt",
        "content-intent": "how-to",
        "chatbot-priority": "medium",
        "service-line": "xml-engineering",
        "prerequisites": "sidebar-toc-chunking-baseline",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "extended-element-overrides.dita": {
        "difficulty": "advanced",
        "duration": "PT25M",
        "content-domain": "xslt",
        "content-intent": "reference",
        "chatbot-priority": "medium",
        "service-line": "xml-engineering",
        "prerequisites": "first-override-xslt",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "ditaval-filtering-variants.dita": {
        "difficulty": "intermediate",
        "duration": "PT20M",
        "content-domain": "content-reuse",
        "content-intent": "explain",
        "chatbot-priority": "high",
        "service-line": "dita-engineering",
        "prerequisites": "dita-reuse-variants",
        "category": "taxonomy:content-reuse",
        "audience": ["developer", "technical-writer"],
    },
    "passing-parameters.dita": {
        "difficulty": "intermediate",
        "duration": "PT10M",
        "content-domain": "publishing",
        "content-intent": "reference",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "dita-publishing",
        "category": "taxonomy:publishing",
        "audience": ["developer", "build-engineer"],
    },
    "toc-grouping.dita": {
        "difficulty": "intermediate",
        "duration": "PT10M",
        "content-domain": "publishing",
        "content-intent": "explain",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "sidebar-toc-chunking-baseline",
        "category": "taxonomy:publishing",
        "audience": ["developer", "technical-writer"],
    },
    "debugging-workflow.dita": {
        "difficulty": "advanced",
        "duration": "PT20M",
        "content-domain": "xslt",
        "content-intent": "troubleshoot",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "first-override-xslt",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "production-hardening.dita": {
        "difficulty": "advanced",
        "duration": "PT15M",
        "content-domain": "devops",
        "content-intent": "best-practice",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "create-html5-plugin",
        "category": "taxonomy:devops",
        "audience": ["developer", "build-engineer"],
    },
    "production-patterns.dita": {
        "difficulty": "advanced",
        "duration": "PT25M",
        "content-domain": "xslt",
        "content-intent": "reference",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "first-override-xslt",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "starter-repo-guide.dita": {
        "difficulty": "intermediate",
        "duration": "PT15M",
        "content-domain": "publishing",
        "content-intent": "how-to",
        "chatbot-priority": "medium",
        "service-line": "publishing-engineering",
        "prerequisites": "create-html5-plugin",
        "category": "taxonomy:publishing",
        "audience": ["developer"],
    },
    "exercises-and-labs.dita": {
        "difficulty": "advanced",
        "duration": "PT120M",
        "content-domain": "xslt",
        "content-intent": "tutorial",
        "chatbot-priority": "medium",
        "service-line": "training",
        "prerequisites": "first-override-xslt,create-html5-plugin",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
    "quick-checklists.dita": {
        "difficulty": "intermediate",
        "duration": "PT10M",
        "content-domain": "customization",
        "content-intent": "reference",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "xslt-customization-tutorial",
        "category": "taxonomy:customization",
        "audience": ["developer", "build-engineer"],
    },
    "xslt-troubleshooting.dita": {
        "difficulty": "advanced",
        "duration": "PT15M",
        "content-domain": "xslt",
        "content-intent": "troubleshoot",
        "chatbot-priority": "high",
        "service-line": "xml-engineering",
        "prerequisites": "first-override-xslt",
        "category": "taxonomy:customization",
        "audience": ["developer"],
    },
}

def build_new_prolog(topic_id, meta, existing_indexterms_xml):
    """Build the full AI-ready prolog XML block."""
    audience_lines = "\n".join(
        f'      <audience>{a}</audience>' for a in meta["audience"]
    )
    return f"""  <prolog>
    <author>Extense LLC</author>
    <critdates>
      <created date="2026-02-10"/>
    </critdates>
    <metadata>
      <keywords>
        {existing_indexterms_xml}
      </keywords>
      <category>{meta["category"]}</category>
{audience_lines}
    </metadata>
    <resourceid appid="extense-training" appname="chatbot" id="{topic_id}"/>
    <data name="difficulty" value="{meta["difficulty"]}"/>
    <data name="duration" value="{meta["duration"]}"/>
    <data name="content-domain" value="{meta["content-domain"]}"/>
    <data name="content-intent" value="{meta["content-intent"]}"/>
    <data name="chatbot-priority" value="{meta["chatbot-priority"]}"/>
    <data name="service-line" value="{meta["service-line"]}"/>
    <data name="prerequisites" value="{meta["prerequisites"]}"/>
  </prolog>"""


def process_file(filepath, meta):
    """Process a single DITA file: add xml:lang and replace prolog."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract topic id
    id_match = re.search(r'<(?:concept|task|reference)\s+id="([^"]+)"', content)
    if not id_match:
        print(f"  SKIP (no topic id found): {filepath}")
        return False
    topic_id = id_match.group(1)
    topic_type = re.search(r'<(concept|task|reference)\s+id=', content).group(1)

    # 1) Add xml:lang="en-US" to root element if missing
    if 'xml:lang=' not in content:
        # Add xml:lang after the id attribute
        content = re.sub(
            rf'(<{topic_type}\s+id="{re.escape(topic_id)}")',
            rf'\1 xml:lang="en-US"',
            content,
            count=1
        )

    # 2) Extract existing indexterms
    indexterms = re.findall(r'<indexterm>[^<]+</indexterm>', content)
    indexterms_xml = "".join(indexterms)

    # 3) Replace the entire prolog block
    new_prolog = build_new_prolog(topic_id, meta, indexterms_xml)
    content = re.sub(
        r'  <prolog>.*?</prolog>',
        new_prolog,
        content,
        flags=re.DOTALL,
        count=1
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ {os.path.basename(filepath)} ({topic_type}, {meta['difficulty']}, {meta['content-intent']})")
    return True


def main():
    base = "/home/upkar/dev/Ex-tense/training-doc/organized-dita-docs/dita-topics"

    devhandbook_dir = os.path.join(base, "developer-guides", "devhandbook-topics")
    xslt_dir = os.path.join(base, "plugins-and-customization", "xslt-topics")

    total = 0
    success = 0

    print("═" * 60)
    print("Enriching devhandbook-topics/ (16 files)")
    print("═" * 60)
    for filename, meta in DEVHANDBOOK.items():
        total += 1
        filepath = os.path.join(devhandbook_dir, filename)
        if not os.path.exists(filepath):
            print(f"  MISSING: {filepath}")
            continue
        if process_file(filepath, meta):
            success += 1

    print()
    print("═" * 60)
    print("Enriching xslt-topics/ (18 files)")
    print("═" * 60)
    for filename, meta in XSLT_TOPICS.items():
        total += 1
        filepath = os.path.join(xslt_dir, filename)
        if not os.path.exists(filepath):
            print(f"  MISSING: {filepath}")
            continue
        if process_file(filepath, meta):
            success += 1

    print()
    print(f"Done: {success}/{total} files enriched.")


if __name__ == "__main__":
    main()
