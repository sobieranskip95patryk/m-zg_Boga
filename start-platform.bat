@echo off
echo 🚀 Starting MTA Platform...

REM Sprawdź czy Node.js jest zainstalowany
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Node.js not found. Please install Node.js 18+ first.
    exit /b 1
)

echo 📦 Installing dependencies...

cd gateway && npm install && cd ..
cd adapters\spiralmind && npm install && cd ..\..
cd adapters\migi && npm install && cd ..\..

echo 🔧 Starting services...

echo Starting GOK:AI server (port 3000)...
start /B cmd /C "cd _UNIFIED\backend\gokai-server && node server.js"

echo Starting SpiralMind adapter (port 3801)...
start /B cmd /C "cd adapters\spiralmind && set PORT=3801 && node server.js"

echo Starting MIGI adapter (port 3802)...
start /B cmd /C "cd adapters\migi && set PORT=3802 && node server.js"

echo Starting Gateway (port 8080)...
start /B cmd /C "cd gateway && set PORT=8080 && set GOKAI_BASE=http://localhost:3000 && set SPIRALMIND_BASE=http://localhost:3801 && set MIGI_BASE=http://localhost:3802 && node server.js"

timeout /t 3

echo.
echo ✅ All services started!
echo 🌐 Gateway: http://localhost:8080
echo 🔮 GOK:AI: http://localhost:3000
echo 🌀 SpiralMind: http://localhost:3801
echo 🔵 MIGI: http://localhost:3802
echo.
echo 🧪 Test commands:
echo curl http://localhost:8080/api/health
echo curl -X POST http://localhost:8080/api/chat/ask -H "Content-Type: application/json" -d "{\"engine\":\"gokai\",\"prompt\":\"test\"}"
echo.
echo 🛑 To stop: Use Task Manager to end node.exe processes