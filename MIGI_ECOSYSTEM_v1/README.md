# MIGI_ECOSYSTEM_v1

Monorepo MVP dla ekosystemu **GOK:AI / MIGI / Apex Infiniti**.

## Skład
- **backend/** FastAPI (Python) — rdzeń S(GOK:AI), wyliczanie P(S), REST API.
- **frontend/** proste UI (HTML/JS) z oknem % sukcesu + wywołanie API.
- **core/** logika TypeScript: `CoreSelph`, intuicja, sygnatura.
- **system/** `SelphOS`, `ConsciousKernel`.
- **avatar/** `PinkManAgent`, `AvatarInterface`.
- **agents/** przykładowe agenty MIGI (CORE, NOVA).
- **mp_packets/** próbki MP z checksumami SHA-256.
- **infra/** szkice deploymentu (docker-compose, K8s manifesty szkic).
- **docs/** architektura, KPI, manifest.
- **scripts/** narzędzia dev.

## Uruchomienie
### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate || .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (statyczny)
Otwórz `frontend/public/index.html` w przeglądarce. Zmień `BACKEND_URL` jeśli port inny niż 8000.

## API
- `POST /api/ps` — oblicza P(S) na podstawie wejścia i paramów matrycy `<369963>` oraz sygnatury `9π` i Fibonacciego.

## Licencja
MIT (szkic). 
