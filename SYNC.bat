@echo off
ECHO ======================================================
ECHO  Starting Quartz Sync...
ECHO  This will build your site and publish changes.
ECHO  (Please wait for the process to complete)
ECHO ======================================================

REM npx quartz sync handles: Pulling remote changes, committing local changes, building the site, and pushing to GitHub.
ECHO.
ECHO --- Running npx quartz sync...
npx quartz sync

REM 2. Completion Message
ECHO.
ECHO ======================================================
ECHO  ✅ Quartz Sync Complete! Your changes are now live.
ECHO ======================================================

PAUSE
