#!/usr/bin/env bash
# Build script for DITA HTML5 Sidebar Starter v1 (Minimal)
# Usage: ./build.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== DITA HTML5 Starter v1 — Building HTML5 output ==="
echo ""

dita \
  -i "$SCRIPT_DIR/dita/maps/getting-started.ditamap" \
  -f html5 \
  -o "$SCRIPT_DIR/out/html5" \
  --nav-toc=full

echo ""
echo "=== Build complete ==="
echo "Output: $SCRIPT_DIR/out/html5/index.html"
echo "Open in a browser to view the result."
