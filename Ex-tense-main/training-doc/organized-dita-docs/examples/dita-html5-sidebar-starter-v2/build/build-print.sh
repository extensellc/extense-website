#!/usr/bin/env bash
set -euo pipefail
OUT_DIR="out/html5-print"
dita -i dita/maps/guides/getting-started.ditamap -f html5 -o "${OUT_DIR}" \
  --propertyfile=build/html5-sidebar-print.properties
mkdir -p "${OUT_DIR}/js"
cp -r js/* "${OUT_DIR}/js/"
echo "Built PRINT variant to: ${OUT_DIR}"
