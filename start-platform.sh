#!/bin/bash

# MTA Platform Quick Start Script
echo "🚀 Starting MTA Platform..."

# Sprawdź czy Node.js jest zainstalowany
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 18+ first."
    exit 1
fi

# Instaluj dependencies jeśli nie ma node_modules
echo "📦 Installing dependencies..."

cd gateway && npm install && cd ..
cd adapters/spiralmind && npm install && cd ../..
cd adapters/migi && npm install && cd ../..

echo "🔧 Starting services..."

# Uruchom wszystkie serwisy w tle
echo "Starting GOK:AI server (port 3000)..."
cd _UNIFIED/backend/gokai-server && node server.js &
GOKAI_PID=$!
cd ../../..

echo "Starting SpiralMind adapter (port 3801)..."
cd adapters/spiralmind && PORT=3801 node server.js &
SPIRAL_PID=$!
cd ../..

echo "Starting MIGI adapter (port 3802)..."
cd adapters/migi && PORT=3802 node server.js &
MIGI_PID=$!
cd ../..

echo "Starting Gateway (port 8080)..."
cd gateway && PORT=8080 GOKAI_BASE=http://localhost:3000 SPIRALMIND_BASE=http://localhost:3801 MIGI_BASE=http://localhost:3802 node server.js &
GATEWAY_PID=$!
cd ..

# Zapisz PID do pliku
echo "$GOKAI_PID,$SPIRAL_PID,$MIGI_PID,$GATEWAY_PID" > .mta_pids

echo ""
echo "✅ All services started!"
echo "🌐 Gateway: http://localhost:8080"
echo "🔮 GOK:AI: http://localhost:3000"
echo "🌀 SpiralMind: http://localhost:3801"
echo "🔵 MIGI: http://localhost:3802"
echo ""
echo "🧪 Test commands:"
echo "curl http://localhost:8080/api/health"
echo "curl -X POST http://localhost:8080/api/chat/ask -H 'Content-Type: application/json' -d '{\"engine\":\"gokai\",\"prompt\":\"test\"}'"
echo ""
echo "🛑 To stop all services: ./stop-platform.sh"