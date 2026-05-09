#!/usr/bin/env bash
set -euo pipefail
OUT_DIR="out/html5-admin"
dita -i dita/maps/guides/getting-started.ditamap -f html5 -o "${OUT_DIR}" \
  --propertyfile=build/html5-sidebar-admin.properties
mkdir -p "${OUT_DIR}/js"
cp -r js/* "${OUT_DIR}/js/"
echo "Built ADMIN variant to: ${OUT_DIR}"
