$ExportFileName = "putty-save.reg"
try {
    New-Item -Path "$env:USERPROFILE\puttysave" -ItemType Directory -Force | Out-Null
} catch {
    Write-Host "Directory already exists"
}

$ExportPath = "$env:USERPROFILE\puttysave"
$ExportRegKey = "HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions"

if (Test-Path "$ExportPath\$ExportFileName") {
    Remove-Item "$ExportPath\$ExportFileName"
}

reg export $ExportRegKey "$ExportPath\$ExportFileName"

Write-Host "Putty sessions exported to $ExportPath\$ExportFileName"