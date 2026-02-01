# VAULT HEALTH CHECK SCRIPT
# Run this to generate a To-Do list of fixes.
# It DOES NOT modify your files.

$vaultPath = Get-Location
$reportFile = "$vaultPath/VAULT_HEALTH_REPORT.md"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"

# Start the Report
"---" | Out-File $reportFile
"title: Vault Health Report" | Out-File $reportFile -Append
"date: $timestamp" | Out-File $reportFile -Append
"tags: [admin, report]" | Out-File $reportFile -Append
"---" | Out-File $reportFile -Append
"" | Out-File $reportFile -Append
"# 🏥 Vault Health Report ($timestamp)" | Out-File $reportFile -Append
"> [!info] Instructions" | Out-File $reportFile -Append
"> Use this list to manually fix file names and frontmatter. Check off items as you go." | Out-File $reportFile -Append
"" | Out-File $reportFile -Append

# 1. CHECK NAMING CONVENTIONS (Title Case)
"## 1. Naming Consistency (NPCs & Locations)" | Out-File $reportFile -Append
$foldersToCheck = @("Campaigns\Campaign 1\NPCs", "Campaigns\Campaign 1\World\Grimmora\Locations")

foreach ($folder in $foldersToCheck) {
    $fullPath = Join-Path $vaultPath $folder
    if (Test-Path $fullPath) {
        Get-ChildItem -Path $fullPath -Recurse -Filter "*.md" | ForEach-Object {
            # Check if filename starts with lowercase letter
            if ($_.Name -match '^[a-z]') {
                "- [ ] **Rename**: `"$($_.Name)`" should be Title Case (Found in: `$($_.Directory.Name)`)" | Out-File $reportFile -Append
            }
        }
    }
}

# 2. CHECK FRONTMATTER SCHEMA
"" | Out-File $reportFile -Append
"## 2. Missing Metadata (Frontmatter)" | Out-File $reportFile -Append

# Get ALL markdown files in Campaigns
Get-ChildItem -Path "$vaultPath/Campaigns" -Recurse -Filter "*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -TotalCount 15 -Raw
    
    # Check for basic Frontmatter existence
    if ($content -notmatch "^---") {
        "- [ ] **Missing FM**: `"$($_.Name)`" has no YAML frontmatter." | Out-File $reportFile -Append
        return # Skip further checks for this file
    }

    # NPC Checks
    if ($_.Directory.Name -eq "NPCs" -or $content -match "type:\s*npc") {
        if ($content -notmatch "status:") {
            "- [ ] **NPC Data**: `"$($_.Name)`" is missing `status` field." | Out-File $reportFile -Append
        }
        if ($content -match "type:\s*cnp") { # Catch the specific typo you mentioned
            "- [ ] **Typo**: `"$($_.Name)`" has type `cnp` instead of `npc`." | Out-File $reportFile -Append
        }
    }

    # Location Checks
    if ($_.FullName -match "Locations" -or $content -match "type:\s*location") {
        if ($content -notmatch "region:") {
            "- [ ] **Location Data**: `"$($_.Name)`" is missing `region` field." | Out-File $reportFile -Append
        }
    }
}

# 3. CHECK FOR CLUTTER
"" | Out-File $reportFile -Append
"## 3. Clutter & Conflicts" | Out-File $reportFile -Append
Get-ChildItem -Path "$vaultPath" -Recurse -Filter "*Copy*" | ForEach-Object {
    "- [ ] **Delete/Merge**: `"$($_.Name)`" appears to be a duplicate." | Out-File $reportFile -Append
}
Get-ChildItem -Path "$vaultPath" -Recurse -Filter "Untitled*" | ForEach-Object {
    "- [ ] **Rename/Delete**: `"$($_.Name)`" is unnamed." | Out-File $reportFile -Append
}

Write-Host "Health Check Complete. Open VAULT_HEALTH_REPORT.md in Obsidian." -ForegroundColor Green