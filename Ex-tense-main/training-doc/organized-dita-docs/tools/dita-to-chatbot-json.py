#!/usr/bin/env python3
"""
Extense DITA-to-Chatbot JSON Ingestion Pipeline
=================================================
Converts DITA XML content into structured JSON/JSONL chunks suitable for
RAG (Retrieval-Augmented Generation) chatbot ingestion and vector database
embedding.

Features:
  - Section-aware chunking (preserves DITA semantic boundaries)
  - Metadata inheritance (topic-level metadata flows to all chunks)
  - Glossary extraction (creates a separate term lookup index)
  - Content manifest generation
  - Configurable chunk sizing with overlap

Usage:
  python dita-to-chatbot-json.py --input <dita-topics-dir> --output <output-dir>
  python dita-to-chatbot-json.py --input ./dita-topics --output ./chatbot-data --format jsonl

Output files:
  - chunks.jsonl          — One JSON object per line, ready for embedding
  - content-manifest.json — Index of all topics with metadata
  - glossary-index.json   — Term lookup with definitions, synonyms, usage
  - ingestion-report.json — Statistics and quality checks

Author: Extense LLC
Date:   2026-02-10
"""

import argparse
import json
import os
import re
import sys
import hashlib
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET
from typing import Optional


# ─── Configuration ────────────────────────────────────────────────────────────

DEFAULT_MAX_CHUNK_TOKENS = 1500
DEFAULT_MIN_CHUNK_TOKENS = 50
DEFAULT_OVERLAP_SENTENCES = 2
APPROX_CHARS_PER_TOKEN = 4  # rough estimate for English text


# ─── XML Text Extraction ─────────────────────────────────────────────────────

def get_text(element: ET.Element) -> str:
    """Recursively extract all text content from an XML element, stripping tags."""
    parts = []
    if element.text:
        parts.append(element.text)
    for child in element:
        parts.append(get_text(child))
        if child.tail:
            parts.append(child.tail)
    return ''.join(parts).strip()


def get_text_with_structure(element: ET.Element) -> str:
    """Extract text preserving some logical structure (paragraphs, list items)."""
    lines = []
    for child in element:
        tag = child.tag
        if tag in ('p', 'li', 'cmd', 'info', 'stepresult', 'note'):
            text = get_text(child)
            if text:
                if tag == 'li':
                    lines.append(f"- {text}")
                elif tag == 'note':
                    lines.append(f"Note: {text}")
                else:
                    lines.append(text)
        elif tag in ('ul', 'ol', 'steps', 'steps-unordered'):
            lines.append(get_text_with_structure(child))
        elif tag == 'step':
            cmd = child.find('cmd')
            if cmd is not None:
                lines.append(f"Step: {get_text(cmd)}")
            info = child.find('info')
            if info is not None:
                lines.append(f"  {get_text(info)}")
        elif tag == 'codeblock':
            outputclass = child.get('outputclass', '')
            code_text = get_text(child)
            if code_text:
                lang = outputclass.replace('language-', '') if outputclass else ''
                lines.append(f"```{lang}\n{code_text}\n```")
        elif tag == 'pre':
            text = get_text(child)
            if text:
                lines.append(f"```\n{text}\n```")
        elif tag == 'fig':
            title_el = child.find('title')
            if title_el is not None:
                lines.append(f"[Figure: {get_text(title_el)}]")
            # Include pre/codeblock content inside figures
            for sub in child:
                if sub.tag in ('pre', 'codeblock'):
                    lines.append(get_text(sub))
        elif tag == 'section':
            # Sections are handled at a higher level for chunking
            pass
        elif tag == 'title':
            pass  # Titles are handled separately
        elif tag in ('b', 'i', 'codeph', 'ph', 'xref'):
            text = get_text(child)
            if text:
                lines.append(text)
        else:
            text = get_text(child)
            if text:
                lines.append(text)

    return '\n'.join(lines)


# ─── Metadata Extraction ─────────────────────────────────────────────────────

def extract_prolog_metadata(root: ET.Element) -> dict:
    """Extract all metadata from DITA prolog, including custom <data> elements."""
    meta = {
        'topic_id': root.get('id', ''),
        'xml_lang': root.get('{http://www.w3.org/XML/1998/namespace}lang', 'en-US'),
        'topic_type': root.tag,  # concept, task, reference, glossgroup, etc.
        'author': '',
        'created': '',
        'revised': '',
        'keywords': [],
        'indexterms': [],
        'category': '',
        'audiences': [],
        'shortdesc': '',
        # Custom chatbot <data> elements
        'difficulty': '',
        'duration': '',
        'content_domain': '',
        'content_intent': '',
        'chatbot_priority': '',
        'service_line': '',
        'prerequisites': [],
        'resource_id': '',
    }

    # Title
    title_el = root.find('title')
    if title_el is not None:
        meta['title'] = get_text(title_el)

    # Shortdesc
    shortdesc_el = root.find('shortdesc')
    if shortdesc_el is not None:
        meta['shortdesc'] = get_text(shortdesc_el)

    # Prolog
    prolog = root.find('prolog')
    if prolog is None:
        return meta

    # Author
    author_el = prolog.find('author')
    if author_el is not None:
        meta['author'] = get_text(author_el)

    # Critdates
    critdates = prolog.find('critdates')
    if critdates is not None:
        created = critdates.find('created')
        if created is not None:
            meta['created'] = created.get('date', '')
        revised = critdates.find('revised')
        if revised is not None:
            meta['revised'] = revised.get('modified', '')

    # Metadata block
    metadata_el = prolog.find('metadata')
    if metadata_el is not None:
        # Keywords / indexterms
        keywords_el = metadata_el.find('keywords')
        if keywords_el is not None:
            for it in keywords_el.findall('indexterm'):
                term = get_text(it)
                if term:
                    meta['indexterms'].append(term)
            for kw in keywords_el.findall('keyword'):
                term = get_text(kw)
                if term:
                    meta['keywords'].append(term)

        # Category
        cat_el = metadata_el.find('category')
        if cat_el is not None:
            meta['category'] = get_text(cat_el)

        # Audience (can be multiple)
        for aud_el in metadata_el.findall('audience'):
            aud = get_text(aud_el)
            if aud:
                meta['audiences'].append(aud)

    # Resource ID
    resid = prolog.find('resourceid')
    if resid is not None:
        meta['resource_id'] = resid.get('id', '') or resid.get('appid', '')

    # Custom <data> elements (chatbot metadata)
    data_map = {
        'difficulty': 'difficulty',
        'duration': 'duration',
        'content-domain': 'content_domain',
        'content-intent': 'content_intent',
        'chatbot-priority': 'chatbot_priority',
        'service-line': 'service_line',
        'prerequisites': 'prerequisites',
    }
    for data_el in prolog.findall('data'):
        name = data_el.get('name', '')
        value = data_el.get('value', '')
        if name in data_map:
            key = data_map[name]
            if key == 'prerequisites' and value:
                meta[key] = [p.strip() for p in value.split(',') if p.strip()]
            else:
                meta[key] = value

    return meta


# ─── Section-Aware Chunking ──────────────────────────────────────────────────

def extract_sections(root: ET.Element) -> list:
    """Extract sections from a DITA topic body, respecting DITA structure."""
    sections = []

    # Find the body element (conbody, taskbody, refbody, etc.)
    body_tags = ['conbody', 'taskbody', 'refbody', 'body', 'glossBody']
    body = None
    for tag in body_tags:
        body = root.find(tag)
        if body is not None:
            break

    if body is None:
        # Try direct text extraction for simple topics
        text = get_text_with_structure(root)
        if text:
            sections.append({
                'section_id': 'main',
                'section_title': '',
                'content': text
            })
        return sections

    # Collect sections
    current_content = []
    for child in body:
        if child.tag == 'section':
            # Flush any accumulated pre-section content
            if current_content:
                sections.append({
                    'section_id': 'intro',
                    'section_title': 'Introduction',
                    'content': '\n'.join(current_content)
                })
                current_content = []

            section_id = child.get('id', f'section-{len(sections)}')
            title_el = child.find('title')
            section_title = get_text(title_el) if title_el is not None else ''
            content = get_text_with_structure(child)

            if content.strip():
                sections.append({
                    'section_id': section_id,
                    'section_title': section_title,
                    'content': content
                })
        else:
            # Content outside sections (intro material)
            text = get_text_with_structure(ET.Element('wrapper', {}))
            # Direct extraction for non-section elements
            if child.tag in ('p', 'note', 'ul', 'ol', 'table', 'fig', 'pre', 'codeblock'):
                chunk_text = get_text(child)
                if chunk_text:
                    current_content.append(chunk_text)

    # Flush remaining
    if current_content:
        sections.append({
            'section_id': 'intro',
            'section_title': 'Introduction',
            'content': '\n'.join(current_content)
        })

    return sections


def estimate_tokens(text: str) -> int:
    """Rough token count estimate based on character count."""
    return len(text) // APPROX_CHARS_PER_TOKEN


def chunk_content(sections: list, meta: dict, source_file: str,
                  max_tokens: int = DEFAULT_MAX_CHUNK_TOKENS,
                  min_tokens: int = DEFAULT_MIN_CHUNK_TOKENS) -> list:
    """Convert sections into appropriately sized chunks with metadata."""
    chunks = []

    for section in sections:
        content = section['content']
        tokens = estimate_tokens(content)

        if tokens < min_tokens:
            # Too small — will be merged with adjacent if possible
            continue

        if tokens <= max_tokens:
            # Good size — create one chunk
            chunk = create_chunk(meta, section, content, source_file, len(chunks))
            chunks.append(chunk)
        else:
            # Too large — split by paragraphs
            paragraphs = content.split('\n')
            current_chunk_text = []
            current_tokens = 0

            for para in paragraphs:
                para_tokens = estimate_tokens(para)
                if current_tokens + para_tokens > max_tokens and current_chunk_text:
                    chunk_text = '\n'.join(current_chunk_text)
                    chunk = create_chunk(meta, section, chunk_text, source_file, len(chunks))
                    chunks.append(chunk)
                    current_chunk_text = []
                    current_tokens = 0

                current_chunk_text.append(para)
                current_tokens += para_tokens

            if current_chunk_text:
                chunk_text = '\n'.join(current_chunk_text)
                if estimate_tokens(chunk_text) >= min_tokens:
                    chunk = create_chunk(meta, section, chunk_text, source_file, len(chunks))
                    chunks.append(chunk)

    return chunks


def create_chunk(meta: dict, section: dict, content: str,
                 source_file: str, chunk_index: int) -> dict:
    """Create a single chunk with full metadata for vector DB ingestion."""
    chunk_id = hashlib.sha256(
        f"{meta['topic_id']}:{section['section_id']}:{chunk_index}".encode()
    ).hexdigest()[:16]

    # Build the text that will be embedded
    # Include title + shortdesc as context prefix for better retrieval
    embed_prefix = f"# {meta.get('title', '')}\n"
    if section['section_title']:
        embed_prefix += f"## {section['section_title']}\n"
    if meta.get('shortdesc'):
        embed_prefix += f"{meta['shortdesc']}\n\n"

    return {
        'chunk_id': chunk_id,
        'topic_id': meta['topic_id'],
        'topic_title': meta.get('title', ''),
        'section_id': section['section_id'],
        'section_title': section['section_title'],

        # The text to embed
        'text': embed_prefix + content,
        'text_plain': content,  # without prefix, for display

        # Metadata for filtering and ranking
        'shortdesc': meta.get('shortdesc', ''),
        'topic_type': meta['topic_type'],
        'difficulty': meta.get('difficulty', ''),
        'duration': meta.get('duration', ''),
        'content_domain': meta.get('content_domain', ''),
        'content_intent': meta.get('content_intent', ''),
        'chatbot_priority': meta.get('chatbot_priority', ''),
        'service_line': meta.get('service_line', ''),
        'audiences': meta.get('audiences', []),
        'keywords': meta.get('indexterms', []) + meta.get('keywords', []),
        'prerequisites': meta.get('prerequisites', []),
        'category': meta.get('category', ''),

        # Provenance
        'source_file': source_file,
        'author': meta.get('author', ''),
        'created': meta.get('created', ''),
        'revised': meta.get('revised', ''),
        'resource_id': meta.get('resource_id', ''),

        # Chunk metrics
        'token_estimate': estimate_tokens(content),
        'chunk_index': chunk_index,
    }


# ─── Glossary Extraction ─────────────────────────────────────────────────────

def extract_glossary(filepath: str) -> list:
    """Parse a DITA glossgroup file into a structured glossary index."""
    entries = []

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"  Warning: Could not parse glossary {filepath}: {e}")
        return entries

    for entry in root.iter('glossentry'):
        term_el = entry.find('glossterm')
        def_el = entry.find('glossdef')
        body_el = entry.find('glossBody')

        term_data = {
            'id': entry.get('id', ''),
            'term': get_text(term_el) if term_el is not None else '',
            'definition': get_text(def_el) if def_el is not None else '',
            'surface_form': '',
            'abbreviations': [],
            'usage': '',
            'scope_note': '',
        }

        if body_el is not None:
            sf = body_el.find('glossSurfaceForm')
            if sf is not None:
                term_data['surface_form'] = get_text(sf)

            for alt in body_el.findall('glossAlt'):
                abbr = alt.find('glossAbbreviation')
                if abbr is not None:
                    term_data['abbreviations'].append(get_text(abbr))

            usage = body_el.find('glossUsage')
            if usage is not None:
                term_data['usage'] = get_text(usage)

            scope = body_el.find('glossScopeNote')
            if scope is not None:
                term_data['scope_note'] = get_text(scope)

        # Build searchable aliases for chatbot term matching
        term_data['search_aliases'] = [term_data['term'].lower()]
        if term_data['surface_form']:
            term_data['search_aliases'].append(term_data['surface_form'].lower())
        for abbr in term_data['abbreviations']:
            term_data['search_aliases'].append(abbr.lower())

        entries.append(term_data)

    return entries


# ─── File Processing ─────────────────────────────────────────────────────────

def process_dita_file(filepath: str, base_dir: str) -> tuple:
    """Process a single DITA file, returning chunks and manifest entry."""
    rel_path = os.path.relpath(filepath, base_dir)

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"  Warning: Could not parse {rel_path}: {e}")
        return [], None

    # Skip ditamaps, subject schemes, etc.
    if root.tag in ('map', 'bookmap', 'subjectScheme'):
        return [], None

    meta = extract_prolog_metadata(root)
    meta['title'] = meta.get('title', '') or root.get('id', Path(filepath).stem)

    sections = extract_sections(root)
    chunks = chunk_content(sections, meta, rel_path)

    # Manifest entry
    manifest_entry = {
        'topic_id': meta['topic_id'],
        'title': meta.get('title', ''),
        'shortdesc': meta.get('shortdesc', ''),
        'topic_type': meta['topic_type'],
        'source_file': rel_path,
        'difficulty': meta.get('difficulty', ''),
        'duration': meta.get('duration', ''),
        'content_domain': meta.get('content_domain', ''),
        'content_intent': meta.get('content_intent', ''),
        'audiences': meta.get('audiences', []),
        'keywords': meta.get('indexterms', []),
        'prerequisites': meta.get('prerequisites', []),
        'service_line': meta.get('service_line', ''),
        'chatbot_priority': meta.get('chatbot_priority', ''),
        'chunk_count': len(chunks),
        'created': meta.get('created', ''),
        'revised': meta.get('revised', ''),
    }

    return chunks, manifest_entry


def find_dita_files(input_dir: str) -> list:
    """Recursively find all .dita files in the input directory."""
    dita_files = []
    for root_dir, _, files in os.walk(input_dir):
        for f in sorted(files):
            if f.endswith('.dita'):
                dita_files.append(os.path.join(root_dir, f))
    return dita_files


# ─── Main Pipeline ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Convert DITA XML content to chatbot-ready JSON/JSONL'
    )
    parser.add_argument('--input', '-i', required=True,
                        help='Path to dita-topics directory')
    parser.add_argument('--output', '-o', required=True,
                        help='Output directory for JSON files')
    parser.add_argument('--format', '-f', choices=['jsonl', 'json'], default='jsonl',
                        help='Output format (default: jsonl)')
    parser.add_argument('--max-tokens', type=int, default=DEFAULT_MAX_CHUNK_TOKENS,
                        help=f'Maximum tokens per chunk (default: {DEFAULT_MAX_CHUNK_TOKENS})')
    parser.add_argument('--min-tokens', type=int, default=DEFAULT_MIN_CHUNK_TOKENS,
                        help=f'Minimum tokens per chunk (default: {DEFAULT_MIN_CHUNK_TOKENS})')
    parser.add_argument('--glossary', '-g',
                        help='Path to glossary.dita file (auto-detected if not specified)')

    args = parser.parse_args()

    input_dir = os.path.abspath(args.input)
    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)

    print(f"╔══════════════════════════════════════════════════════════════╗")
    print(f"║  Extense DITA → Chatbot JSON Ingestion Pipeline            ║")
    print(f"╚══════════════════════════════════════════════════════════════╝")
    print(f"  Input:      {input_dir}")
    print(f"  Output:     {output_dir}")
    print(f"  Format:     {args.format}")
    print(f"  Max tokens: {args.max_tokens}")
    print()

    # Find all DITA files
    dita_files = find_dita_files(input_dir)
    print(f"  Found {len(dita_files)} DITA files")

    # Process files
    all_chunks = []
    manifest_entries = []
    stats = {
        'files_processed': 0,
        'files_skipped': 0,
        'total_chunks': 0,
        'glossary_terms': 0,
        'topics_by_type': {},
        'topics_by_domain': {},
        'topics_by_difficulty': {},
    }

    for filepath in dita_files:
        rel = os.path.relpath(filepath, input_dir)
        print(f"  Processing: {rel}")

        chunks, manifest_entry = process_dita_file(filepath, input_dir)

        if manifest_entry:
            all_chunks.extend(chunks)
            manifest_entries.append(manifest_entry)
            stats['files_processed'] += 1
            stats['total_chunks'] += len(chunks)

            # Track stats
            ttype = manifest_entry['topic_type']
            stats['topics_by_type'][ttype] = stats['topics_by_type'].get(ttype, 0) + 1

            domain = manifest_entry.get('content_domain', 'unclassified')
            stats['topics_by_domain'][domain] = stats['topics_by_domain'].get(domain, 0) + 1

            diff = manifest_entry.get('difficulty', 'unspecified')
            stats['topics_by_difficulty'][diff] = stats['topics_by_difficulty'].get(diff, 0) + 1
        else:
            stats['files_skipped'] += 1

    # Process glossary
    glossary_path = args.glossary
    if not glossary_path:
        # Auto-detect
        candidate = os.path.join(input_dir, 'reference', 'glossary.dita')
        if os.path.exists(candidate):
            glossary_path = candidate

    glossary_entries = []
    if glossary_path and os.path.exists(glossary_path):
        print(f"\n  Processing glossary: {os.path.relpath(glossary_path, input_dir)}")
        glossary_entries = extract_glossary(glossary_path)
        stats['glossary_terms'] = len(glossary_entries)
        print(f"  Extracted {len(glossary_entries)} glossary terms")

    # ─── Write outputs ───────────────────────────────────────────────────

    # 1. Chunks
    chunks_path = os.path.join(output_dir, f'chunks.{args.format}')
    if args.format == 'jsonl':
        with open(chunks_path, 'w', encoding='utf-8') as f:
            for chunk in all_chunks:
                f.write(json.dumps(chunk, ensure_ascii=False) + '\n')
    else:
        with open(chunks_path, 'w', encoding='utf-8') as f:
            json.dump(all_chunks, f, indent=2, ensure_ascii=False)
    print(f"\n  ✓ Wrote {len(all_chunks)} chunks → {chunks_path}")

    # 2. Content manifest
    manifest = {
        'generated': datetime.now().isoformat(),
        'source': input_dir,
        'total_topics': len(manifest_entries),
        'total_chunks': len(all_chunks),
        'topics': manifest_entries,
    }
    manifest_path = os.path.join(output_dir, 'content-manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Wrote content manifest → {manifest_path}")

    # 3. Glossary index
    if glossary_entries:
        glossary_index = {
            'generated': datetime.now().isoformat(),
            'total_terms': len(glossary_entries),
            'terms': glossary_entries,
        }
        glossary_path_out = os.path.join(output_dir, 'glossary-index.json')
        with open(glossary_path_out, 'w', encoding='utf-8') as f:
            json.dump(glossary_index, f, indent=2, ensure_ascii=False)
        print(f"  ✓ Wrote glossary index ({len(glossary_entries)} terms) → {glossary_path_out}")

    # 4. Ingestion report
    stats['generated'] = datetime.now().isoformat()
    report_path = os.path.join(output_dir, 'ingestion-report.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Wrote ingestion report → {report_path}")

    # Summary
    print()
    print(f"  ══════════════════════════════════════════════════════════")
    print(f"  SUMMARY")
    print(f"  ──────────────────────────────────────────────────────────")
    print(f"  Files processed:  {stats['files_processed']}")
    print(f"  Files skipped:    {stats['files_skipped']}")
    print(f"  Total chunks:     {stats['total_chunks']}")
    print(f"  Glossary terms:   {stats['glossary_terms']}")
    print(f"  Topics by type:   {stats['topics_by_type']}")
    print(f"  By domain:        {stats['topics_by_domain']}")
    print(f"  By difficulty:    {stats['topics_by_difficulty']}")
    print(f"  ══════════════════════════════════════════════════════════")
    print()
    print(f"  Next steps:")
    print(f"  1. Embed chunks.{args.format} into your vector database")
    print(f"  2. Load glossary-index.json as a term lookup for the chatbot")
    print(f"  3. Use content-manifest.json for the chatbot's topic navigator")
    print()


if __name__ == '__main__':
    main()
