@echo off
setlocal
chcp 65001 >nul
set "PYTHONIOENCODING=utf-8"
py -3 "%~dp0Archiver-Emission-4.py" %*
set "result=%errorlevel%"
echo.
echo Code final : %result%
pause
exit /b %result%
