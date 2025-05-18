# -------------------------------------------
# Simple Node.js & npm Setup Script
# For Windows via PowerShell
# -------------------------------------------

# 1. Basic version detection function
function Get-CommandVersion {
    param (
        [string]$Command,
        [string]$VersionArg = "-v"
    )
    
    try {
        $output = & $Command $VersionArg 2>$null
        return $output
    }
    catch {
        return $null
    }
}

# 2. Check if Node.js is installed
Write-Host "Checking for Node.js..." -ForegroundColor Cyan
$nodeVersion = Get-CommandVersion "node"

if ($nodeVersion) {
    Write-Host "Node.js is installed: $nodeVersion" -ForegroundColor Green
}
else {
    Write-Host "Node.js is not installed" -ForegroundColor Yellow
    
    # 3. Prompt to install Node.js
    Write-Host "Would you like to install Node.js? (Y/N)" -ForegroundColor Yellow
    $response = Read-Host
    
    if ($response -eq "Y" -or $response -eq "y") {
        Write-Host "Installing Node.js..." -ForegroundColor Cyan
        
        # 4. Download and install Node.js
        $installerPath = "$env:TEMP\node-installer.msi"
        $downloadUrl = "https://nodejs.org/dist/latest-v18.x/node-v18.18.0-x64.msi"
        
        Write-Host "Downloading Node.js installer..." -ForegroundColor Cyan
        Invoke-WebRequest -Uri $downloadUrl -OutFile $installerPath -UseBasicParsing
        
        Write-Host "Running installer (this may take a minute)..." -ForegroundColor Cyan
        Start-Process "msiexec.exe" -ArgumentList "/i `"$installerPath`" /quiet /norestart" -Wait
        
        Write-Host "Cleaning up..." -ForegroundColor Cyan
        Remove-Item $installerPath -Force
        
        # 5. Verify installation
        Write-Host "Verifying installation..." -ForegroundColor Cyan
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
        $nodeVersion = Get-CommandVersion "node"
        
        if ($nodeVersion) {
            Write-Host "Node.js installed successfully: $nodeVersion" -ForegroundColor Green
        }
        else {
            Write-Host "Node.js installation may have failed. Please restart PowerShell and try again." -ForegroundColor Red
        }
    }
}

# 6. Check if npm is installed
Write-Host "`nChecking for npm..." -ForegroundColor Cyan
$npmVersion = Get-CommandVersion "npm"

if ($npmVersion) {
    Write-Host "npm is installed: $npmVersion" -ForegroundColor Green
}
else {
    Write-Host "npm is not installed. It should be included with Node.js." -ForegroundColor Yellow
}

# 7. Basic summary
Write-Host "`nSetup check complete." -ForegroundColor Cyan