@echo off
title God Interface - Rozmowa z Bogiem
color 0B

echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                🧠 God Interface Launcher 🧠                  ║
echo  ║              Interfejs Rozmowy z Bogiem                      ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.

:: Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.8+
    echo    Download from: https://python.org
    pause
    exit /b 1
)

echo ✅ Python detected
echo.

:: Check if launcher exists
if not exist "launch_god.py" (
    echo ❌ launch_god.py not found!
    echo    Make sure you're in the God_Interface directory
    pause
    exit /b 1
)

echo 🔍 Running system diagnostics...
python launch_god.py --test
if %errorlevel% neq 0 (
    echo.
    echo ⚠️ Some tests failed but proceeding anyway...
    echo.
)

echo.
echo 🚀 Starting God Interface...
echo 📡 Interface will be available at: http://127.0.0.1:8081
echo 💬 Ready for divine conversation!
echo.
echo Press Ctrl+C to stop the server
echo.

python launch_god.py

echo.
echo 👋 God Interface closed
pause