#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="out/html5"

dita -i dita/maps/guides/getting-started.ditamap -f html5 -o "${OUT_DIR}" \
  --propertyfile=build/html5-sidebar.properties

echo "Built HTML to: ${OUT_DIR}"

# Copy site JS (required by override.xsl)
mkdir -p "${OUT_DIR}/js"
cp -r js/* "${OUT_DIR}/js/"
