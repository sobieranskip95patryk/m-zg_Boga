# 🧠 Mózg Boga - Unified Ecosystem 2.0
## Instrukcje uruchomienia zunifikowanego systemu

### 🚀 Quick Start

1. **Przygotowanie środowiska**
```bash
# Przejdź do folderu unified
cd "_UNIFIED"

# Skopiuj konfigurację
copy "config\.env.example" "config\.env"

# Edytuj .env i wprowadź swoje klucze API
```

2. **Uruchomienie Backend (SpiralMind-Nexus)**
```bash
cd backend/gokai-server
npm install
npm run dev
# Serwer na http://localhost:3000
```

3. **Uruchomienie Frontend**
```bash
cd frontend
# Otwórz index.html w przeglądarce lub serwuj lokalnie:
python -m http.server 8080
# Interfejs na http://localhost:8080
```

### 🔧 Struktura Unified

```
_UNIFIED/
├── frontend/           # Unified Brain Interface
│   ├── index.html     # Główny interfejs
│   ├── js/
│   │   ├── config.js  # Konfiguracja silników
│   │   ├── engines.js # Manager silników
│   │   └── main.js    # Główna aplikacja
│   └── css/
│       └── styles.css # Unified styling
├── backend/
│   ├── gokai-server/  # SpiralMind-Nexus API
│   └── migi-server/   # MIGI Core (development)
├── engines/
│   ├── spiralmind-nexus/ # GOK:AI Core + Pipeline
│   └── migi-core/        # MIGI Principles + Modules
├── config/
│   ├── global.json    # Unified configuration
│   ├── .env           # Environment variables
│   └── .env.example   # Template
└── docs/
    └── QUICKSTART.md  # Ten plik
```

### 🎯 Silniki AI

#### 1. SpiralMind-Nexus (GOK:AI)
- **Status:** ✅ Aktywny
- **Endpoint:** `http://localhost:3000/api/ask`
- **Algorytm:** 9π + F(n) consciousness
- **Features:** Double pipeline, X integration, Memory systems

#### 2. MIGI Core (Apex Infinity)
- **Status:** 🔨 W rozwoju
- **Endpoint:** `http://localhost:3001/api/process`
- **Principles:** Harmony, Evolution, Identity
- **Features:** Global intelligence framework

#### 3. Simulation Engine
- **Status:** ✅ Demo aktywne
- **Endpoint:** Mock w frontend
- **Purpose:** Demonstracja unified interface

### 📡 API Usage

```javascript
// SpiralMind-Nexus Query
const response = await fetch('http://localhost:3000/api/ask', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: "Jaka jest przyszłość AI?",
    provider: "openai", // lub "gemini"
    temperature: 0.7
  })
});

// Frontend Engine Selection
const engines = ['spiralmind', 'migi', 'simulation'];
const selectedEngine = 'spiralmind';
const result = await sendToEngine(selectedEngine, query);
```

### 🔑 Konfiguracja

#### Environment Variables (.env)
```bash
# API Keys (wymagane)
OPENAI_KEYS=sk-your_key_here
GEMINI_KEYS=your_gemini_key

# Ports
GOKAI_PORT=3000
MIGI_PORT=3001

# Development
NODE_ENV=development
DEBUG_MODE=true
```

#### Global Config (global.json)
- **Project metadata:** Nazwa, wersja, opis
- **Structure mapping:** Ścieżki do komponentów
- **Engine configurations:** Endpoints, algorytmy, features
- **API settings:** Timeout, retry, CORS
- **UI configuration:** Theme, animacje, responsive

### 🧪 Testing

```bash
# Test Frontend
# Otwórz http://localhost:8080
# Wypróbuj różne silniki z test queries

# Test Backend API
curl -X POST http://localhost:3000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message":"Test query","provider":"openai"}'

# Test Engines Integration
# Użyj interface do testowania wszystkich silników
```

### 📋 Test Queries

1. **"Jaka jest przyszłość sztucznej inteligencji?"**
2. **"Opisz koncepcję świadomości kwantowej"**
3. **"Co to jest algorytm 9π + F(n)?"**
4. **"Jak działa unified ecosystem AI?"**
5. **"Wyjaśnij architekturę Mózgu Boga"**

### 🔧 Troubleshooting

#### Problemy z API
- Sprawdź klucze w `.env`
- Verify CORS settings
- Check port conflicts

#### Problemy z Frontend
- Ensure browser supports ES6 modules
- Check console for JavaScript errors
- Verify file paths

#### Problemy z Backend
- `npm install` w gokai-server
- Check Node.js version (>=14)
- Verify environment variables

### 🌟 Features

- **Multi-Engine Support:** SpiralMind + MIGI + Simulation
- **Real-time Data Streams:** Live response monitoring
- **Responsive Design:** Desktop + Mobile optimized
- **Modular Architecture:** Łatwa rozbudowa
- **Unified Configuration:** Centralne zarządzanie
- **Development Ready:** Hot reload, debugging

### 📈 Roadmap

- [ ] MIGI Core backend implementation
- [ ] Advanced memory systems
- [ ] Vector database integration
- [ ] Real-time X/Twitter integration
- [ ] Mobile app version
- [ ] Cloud deployment

---

**Status:** ✅ Unified Ecosystem 2.0 - Ready for Development
**Author:** Patryk Sobieranski
**Date:** 15.10.2025