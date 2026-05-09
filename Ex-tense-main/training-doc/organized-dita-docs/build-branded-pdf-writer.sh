#!/bin/bash
# ============================================================
# Extense LLC — Writer-Track Branded PDF Build Script
# 
# Builds a filtered PDF for the Technical Writer persona using
# audience-writer.ditaval to exclude developer-only parts
# (VII, VIII, IX) while retaining the writer learning path
# (Parts I–VI, X, Appendices, plus DITAVAL filtering topic).
#
# Usage:
#   ./build-branded-pdf-writer.sh [output-dir]
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DITA_OT="/home/upkar/dev/DITA-OT-Extense/dita-ot/build/tmp/dist/bin/dita"
DITAMAP="$SCRIPT_DIR/extense-supermap.ditamap"
DITAVAL="$SCRIPT_DIR/ditaval/audience-writer.ditaval"
PLUGIN_DIR="$SCRIPT_DIR/plugins/com.extense.pdf.branded"
OUTPUT_DIR="${1:-/home/upkar/dev/Ex-tense/training-doc/output/pdf-writer}"

echo "╔══════════════════════════════════════════════════════╗"
echo "║  Extense LLC — Writer-Track Branded PDF Build       ║"
echo "║  Filter: audience-writer.ditaval                    ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# Step 1: Ensure plugin is installed
echo "▸ Installing PDF plugin..."
PLUGIN_DEST="$(dirname "$DITA_OT")/../plugins/com.extense.pdf.branded"
rm -rf "$PLUGIN_DEST"
cp -r "$PLUGIN_DIR" "$PLUGIN_DEST"
"$DITA_OT" --install 2>/dev/null || true
echo "  ✓ Plugin installed"

# Step 2: Clean output
echo "▸ Cleaning output directory..."
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"
echo "  ✓ Clean"

# Step 3: Build filtered PDF
echo "▸ Building writer-track PDF (filtering with $DITAVAL)..."
"$DITA_OT" \
  -i "$DITAMAP" \
  -f pdf \
  -o "$OUTPUT_DIR" \
  --filter="$DITAVAL" \
  --args.chapter.layout=MINITOC \
  --args.bookmap-order=retain \
  --args.bookmark.style=EXPANDED \
  -v \
  2>&1 | tail -20
echo "  ✓ Build complete"

# Step 3b: Rename output PDF to writer-track filename
ORIG_PDF=$(find "$OUTPUT_DIR" -name "*.pdf" -type f | head -1)
if [ -n "$ORIG_PDF" ]; then
  FINAL_PDF="$OUTPUT_DIR/extense-supermap-writer.pdf"
  mv "$ORIG_PDF" "$FINAL_PDF"
fi

# Step 4: Report
PDF_FILE=$(find "$OUTPUT_DIR" -name "*.pdf" -type f | head -1)
if [ -n "$PDF_FILE" ]; then
  PDF_SIZE=$(du -h "$PDF_FILE" | cut -f1)
  PDF_PAGES=$(python3 -c "
import subprocess
try:
    result = subprocess.run(['pdfinfo', '$PDF_FILE'], capture_output=True, text=True, timeout=5)
    for line in result.stdout.split('\n'):
        if 'Pages:' in line:
            print(line.split(':')[1].strip())
            break
except:
    print('?')
" 2>/dev/null || echo "?")
  echo ""
  echo "═══════════════════════════════════════════════════════"
  echo "  Writer PDF generated: $PDF_FILE"
  echo "  Size: $PDF_SIZE"
  echo "  Pages: $PDF_PAGES"
  echo "  Filter: audience-writer.ditaval"
  echo "  Excluded: Parts VII (DITA-OT Dev), VIII (XSLT), IX (AI Pipeline)"
  echo "═══════════════════════════════════════════════════════"
else
  echo ""
  echo "  ✗ No PDF file found in output directory!"
  echo "    Check output above for errors."
  exit 1
fi
