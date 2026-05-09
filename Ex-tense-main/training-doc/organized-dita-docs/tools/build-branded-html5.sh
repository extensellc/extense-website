#!/bin/bash
# ============================================================
# Extense LLC — Branded HTML5 Build Script
# 
# Builds the DITA Training Guide with the com.extense.html5.branded
# plugin and copies static assets (JS/CSS) to output.
#
# Usage:
#   ./build-branded-html5.sh [output-dir]
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DITA_OT="/home/upkar/dev/DITA-OT-Extense/dita-ot/build/tmp/dist/bin/dita"
DITAMAP="$SCRIPT_DIR/dita-training-guide.ditamap"
PLUGIN_DIR="$SCRIPT_DIR/plugins/com.extense.html5.branded"
PROPERTIES="$SCRIPT_DIR/build-branded-html5.properties"
OUTPUT_DIR="${1:-/home/upkar/dev/Ex-tense/training-doc/output/html5-branded}"

echo "╔══════════════════════════════════════════════════════╗"
echo "║  Extense LLC — Branded HTML5 Build                  ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# Step 1: Ensure plugin is installed
echo "▸ Installing plugin..."
rm -rf "$(dirname "$DITA_OT")/../plugins/com.extense.html5.branded"
cp -r "$PLUGIN_DIR" "$(dirname "$DITA_OT")/../plugins/"
"$DITA_OT" --install 2>/dev/null || true
echo "  ✓ Plugin installed"

# Step 2: Clean output
echo "▸ Cleaning output directory..."
rm -rf "$OUTPUT_DIR"
echo "  ✓ Clean"

# Step 3: Build
echo "▸ Building HTML5 output..."
"$DITA_OT" \
  -i "$DITAMAP" \
  -f html5 \
  -o "$OUTPUT_DIR" \
  --propertyfile="$PROPERTIES" \
  2>&1 | grep -E "^(Error|Warning|Topic Video)" || true
echo "  ✓ Build complete"

# Step 4: Copy static assets
echo "▸ Copying static assets..."
mkdir -p "$OUTPUT_DIR/js" "$OUTPUT_DIR/css"
cp "$PLUGIN_DIR/js/site.js" "$OUTPUT_DIR/js/"
cp "$PLUGIN_DIR/css/brand.css" "$OUTPUT_DIR/css/"
echo "  ✓ Assets copied"

# Step 5: Report
HTML_COUNT=$(find "$OUTPUT_DIR" -name "*.html" | wc -l)
echo ""
echo "═══════════════════════════════════════════════════════"
echo "  Build complete: $HTML_COUNT HTML files"
echo "  Output: $OUTPUT_DIR"
echo "  Open:   $OUTPUT_DIR/index.html"
echo "═══════════════════════════════════════════════════════"
