$ErrorActionPreference = "Stop"
$OutDir = "out/html5-novice"
dita -i dita/maps/guides/getting-started.ditamap -f html5 -o $OutDir `
  --propertyfile=build/html5-sidebar-novice.properties
New-Item -ItemType Directory -Force -Path "$OutDir\js" | Out-Null
Copy-Item -Recurse -Force "js\*" "$OutDir\js\"
Write-Host "Built NOVICE variant to: $OutDir"
