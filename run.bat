@echo off
title ShowYourWork: Evidence-First Application Validation
cd /d "%~dp0"

echo =====================================================================
echo  ShowYourWork: Evidence-First Application Validation
echo =====================================================================
echo.
echo Launching application in default browser: http://localhost:8080
start "" "http://localhost:8080"
echo.
echo Starting backend server on port 8080...

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python server.py
) else (
    "C:\Users\acer\AppData\Local\Python\pythoncore-3.14-64\python.exe" server.py
)

pause
