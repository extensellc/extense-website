$ErrorActionPreference = "Stop"
$OutDir = "out/html5"

dita -i dita/maps/guides/getting-started.ditamap -f html5 -o $OutDir `
  --propertyfile=build/html5-sidebar.properties

Write-Host "Built HTML to: $OutDir"

# Copy site JS (required by override.xsl)
New-Item -ItemType Directory -Force -Path "$OutDir\js" | Out-Null
Copy-Item -Recurse -Force "js\*" "$OutDir\js\"
