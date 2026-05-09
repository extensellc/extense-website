$ErrorActionPreference = "Stop"
$OutDir = "out/html5-web"
dita -i dita/maps/guides/getting-started.ditamap -f html5 -o $OutDir `
  --propertyfile=build/html5-sidebar-web.properties
New-Item -ItemType Directory -Force -Path "$OutDir\js" | Out-Null
Copy-Item -Recurse -Force "js\*" "$OutDir\js\"
Write-Host "Built WEB variant to: $OutDir"
