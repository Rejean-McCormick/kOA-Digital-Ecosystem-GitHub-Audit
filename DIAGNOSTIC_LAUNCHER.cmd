@echo off
setlocal
cd /d "%~dp0"
title kOA GitHub Audit - diagnostic Windows

echo =============================================================
echo   kOA GitHub Audit - mode diagnostic (console visible)
echo =============================================================
echo.
echo Chemin : %~dp0
echo.
where py >nul 2>nul
if not errorlevel 1 (
  echo Utilisation du lanceur Python py -3
  py -3 "%~dp0kOA_GitHub_Audit_Launcher.pyw"
  goto result
)
where python >nul 2>nul
if not errorlevel 1 (
  echo Utilisation de python
  python "%~dp0kOA_GitHub_Audit_Launcher.pyw"
  goto result
)
echo ERREUR : Python introuvable. Installez Python 3.11+
echo depuis python.org avec Tcl/Tk et Python Launcher.
goto result
:result
echo.
echo Consultez aussi le journal :
echo %LOCALAPPDATA%\kOA-GitHub-Audit\launcher-startup.log
echo.
pause
