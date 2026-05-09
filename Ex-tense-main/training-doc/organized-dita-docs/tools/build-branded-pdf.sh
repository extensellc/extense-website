#!/bin/bash
# ============================================================
# Extense LLC — Branded PDF Build Script
# 
# Builds the DITA Training Guide as a branded PDF using the
# com.extense.pdf.branded plugin with DITA-OT's PDF2 + FOP.
#
# Usage:
#   ./build-branded-pdf.sh [output-dir]
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DITA_OT="/home/upkar/dev/DITA-OT-Extense/dita-ot/build/tmp/dist/bin/dita"
DITAMAP="$SCRIPT_DIR/dita-training-guide.ditamap"
PLUGIN_DIR="$SCRIPT_DIR/plugins/com.extense.pdf.branded"
OUTPUT_DIR="${1:-/home/upkar/dev/Ex-tense/training-doc/output/pdf-branded}"

echo "╔══════════════════════════════════════════════════════╗"
echo "║  Extense LLC — Branded PDF Build                    ║"
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

# Step 3: Build PDF
echo "▸ Building branded PDF (this may take a minute)..."
"$DITA_OT" \
  -i "$DITAMAP" \
  -f pdf \
  -o "$OUTPUT_DIR" \
  --args.chapter.layout=MINITOC \
  --args.bookmap-order=retain \
  --args.bookmark.style=EXPANDED \
  -v \
  2>&1 | tail -20
echo "  ✓ Build complete"

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
  echo "  PDF generated: $PDF_FILE"
  echo "  Size: $PDF_SIZE"
  echo "  Pages: $PDF_PAGES"
  echo "═══════════════════════════════════════════════════════"
else
  echo ""
  echo "  ✗ No PDF file found in output directory!"
  echo "    Check output above for errors."
  exit 1
fi
