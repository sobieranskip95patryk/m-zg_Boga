# MTA Platform - Unified AI Gateway

> **"Zrób clona i działamy"** - kompletna platforma w jednym repo.

## 🚀 Quick Start (Windows)

```bash
# Klonuj i uruchom
git clone https://github.com/sobieranskip95patryk/m-zg_Boga.git
cd m-zg_Boga

# Uruchom całą platformę jednym kliknięciem
start-platform.bat

# Test w przeglądarce
# Otwórz: mózgBogaindex.html
```

## 🏗️ Architektura

```
MTA Platform
├── Gateway (port 8080) ── Frontend połączenia
├── GOK:AI (port 3000) ── m-zg_Boga repo 
├── SpiralMind (port 3801) ── Python pipeline wrapper
└── MIGI (port 3802) ── Development stub
```

## 🔧 Komponenty

### 1. **Gateway** (`gateway/`)
- **Port**: 8080
- **Endpoint**: `POST /api/chat/ask`
- **Health**: `GET /api/health`
- **Credits**: `GET /api/credits/balance`

### 2. **GOK:AI** (`_UNIFIED/backend/gokai-server/`)
- **Port**: 3000 (istniejący serwer)
- **Multi-provider**: OpenAI + Gemini
- **Status**: ✅ Production ready

### 3. **SpiralMind Adapter** (`adapters/spiralmind/`)
- **Port**: 3801
- **Pipeline**: Python subprocess z `_UNIFIED/engines/spiralmind-nexus/`
- **Status**: 🔄 Integration ready

### 4. **MIGI Adapter** (`adapters/migi/`)
- **Port**: 3802
- **Type**: Development stub
- **Status**: 🚧 Waiting for apex_infinity_MIGI_Core

## 📱 Frontend

Zaktualizowany `mózgBogaindex.html`:
- ✅ Gateway integration
- ✅ Engine switching: GOK:AI → SpiralMind → MIGI → Simulation
- ✅ Health monitoring
- ✅ Responsive UI

### Environment Config

```html
<script>
  window.__CONFIG__ = { 
    GATEWAY_URL: "http://localhost:8080"
  }
</script>
```

## 🧪 API Testing

```bash
# Health check
curl http://localhost:8080/api/health

# GOK:AI test
curl -X POST http://localhost:8080/api/chat/ask \
  -H 'Content-Type: application/json' \
  -d '{"engine":"gokai","prompt":"test GOK:AI"}'

# SpiralMind test  
curl -X POST http://localhost:8080/api/chat/ask \
  -H 'Content-Type: application/json' \
  -d '{"engine":"spiralmind","prompt":"test SpiralMind"}'

# MIGI test
curl -X POST http://localhost:8080/api/chat/ask \
  -H 'Content-Type: application/json' \
  -d '{"engine":"migi","prompt":"test MIGI"}'
```

## 🔑 Environment Variables

```bash
# Gateway config
PORT=8080
GOKAI_BASE=http://localhost:3000
SPIRALMIND_BASE=http://localhost:3801  
MIGI_BASE=http://localhost:3802

# Tokens (optional)
GOKAI_TOKEN=your_token_here
SPIRALMIND_TOKEN=your_token_here
MIGI_TOKEN=your_token_here
```

## 📊 Response Format

Wszystkie silniki zwracają ustandaryzowany format:

```json
{
  "ok": true,
  "engine": "gokai",
  "text": "AI response text",
  "meta": {
    "provider": "openai",
    "model": "gpt-4o-mini", 
    "timestamp": "2025-10-15T...",
    "keyUsed": "sk-...***"
  }
}
```

## 🔄 Integration Status

| Engine | Status | Endpoint | Notes |
|--------|--------|----------|-------|
| GOK:AI | ✅ Ready | `/api/ask` | Production serwer z _UNIFIED |
| SpiralMind | 🔄 Integration | `/api/ask` | Python pipeline wrapper |
| MIGI | 🚧 Stub | `/api/process` | Waiting for real repo |
| Gateway | ✅ Ready | `/api/chat/ask` | Unified proxy |

## 🛠️ Development

### Dodawanie nowego silnika

1. Utwórz adapter w `adapters/your_engine/`
2. Dodaj endpoint do gateway w `gateway/server.js`
3. Dodaj opcję w frontend `engines` config
4. Test przez gateway API

### Database Integration

Credits/tokenization ready dla:
- SQLite/PostgreSQL backend
- User management
- Payment gateway integration
- On-chain bridge (future)

## 🎯 Roadmap

- [ ] ✅ **Gateway integration** (DONE)
- [ ] 🔄 **SpiralMind Python pipeline** (IN PROGRESS)
- [ ] 📊 **Credits/tokenization system**
- [ ] 🔗 **On-chain bridge**
- [ ] 📱 **Enhanced UI modules**
- [ ] 🌐 **Deployment automation**

---

**Autor**: Patryk Sobierański Meta-Geniusz-GOK  
**Repo**: [m-zg_Boga](https://github.com/sobieranskip95patryk/m-zg_Boga)  
**Contact**: mtaquestwebside@wp.pl