# 🧠 AnonymousAgent 2.0

Systemowy agent ochrony, tropiciel i czyściciel ekosystemu MetaGeniuszPL / MTAQuestWebsideX.

## Moduły
- **GeoScanner**: Odczyt lokalizacji IP
- **IntentAnalyzer**: Analiza intencji i wykrywanie manipulacji
- **ThreatMap**: Wizualizacja zagrożeń
- **PurgeEngine**: Usuwanie kont o niskim zaufaniu
- **ReportInterface**: Raportowanie i alerty

## Integracja
- Możliwość podpięcia do systemu jaźni jako SecuritySelph
- Dashboard do monitorowania: React + Leaflet.js (darmowe narzędzia)
- Backend: Node.js, MongoDB Atlas, ipapi.com

## Przykład użycia
```ts
import { GeoScanner } from "./geo/GeoScanner";
import { IntentAnalyzer } from "./core/IntentAnalyzer";
import { ThreatMap } from "./geo/ThreatMap";
import { PurgeEngine } from "./purge/PurgeEngine";
import { ReportInterface } from "./report/ReportInterface";

const geo = new GeoScanner();
const intent = new IntentAnalyzer();
const threatMap = new ThreatMap();
const purge = new PurgeEngine();
const report = new ReportInterface();

const testProfile = {
  id: "user123",
  ip: "8.8.8.8",
  trustScore: 0.2,
  activity: 0,
  lastMessage: "Send me bitcoin, urgent!"
};

analyzeProfile(testProfile);
```

## Specyfikacja "Na Bogato i Za Darmo"
- Wszystkie narzędzia mają darmowe wersje
- Możesz hostować backend na Heroku/Render/Railway (free tier)
- Integracja z Microsoft: Copilot, Azure Functions, Power Automate, OneNote, Teams — wszystko w darmowych planach na start

---

## 1. Uruchomienie lokalne (Node.js/Express)

### Instalacja
```
npm install
npm install axios
```

### Start serwera
```
node index.js
```

## 2. Integracja z Microsoft Azure
- Utwórz konto na Azure Portal (darmowy tier)
- Skonfiguruj Azure Functions do automatycznego czyszczenia kont
- Użyj Azure Table Storage do logowania raportów
- Możesz hostować backend na Azure App Service (darmowy tier)

## 3. Integracja z Microsoft Copilot
- PinkManAgent może działać jako Copilot Avatar (Web/Edge)
- Użyj Copilot Studio do generowania interfejsu i automatyzacji
- Integracja z Power Automate do synchronizacji alertów i raportów

## 4. Integracja z xAI (Grok)
- Zarejestruj się na console.x.ai i pobierz klucz API (free tier)
- Użyj Grok API do analizy intencji i stylu wypowiedzi
- Przykład:
```js
// Node.js
const axios = require('axios');
const res = await axios.post('https://api.x.ai/grok', { prompt: 'Analyze intent: ...' }, { headers: { 'Authorization': 'Bearer <API_KEY>' } });
```

## 5. Podpięcie do MongoDB Atlas/Supabase
- Utwórz darmową bazę na MongoDB Atlas lub Supabase
- Skonfiguruj połączenie w backendzie:
```js
// Node.js
const { MongoClient } = require('mongodb');
const client = new MongoClient('<MONGODB_URI>');
await client.connect();
```

## 6. Dashboard z mapą zagrożeń (Leaflet.js)
- Dodaj Leaflet.js do projektu React/TSX:
```
npm install leaflet react-leaflet
```
- Przykład komponentu:
```tsx
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
<MapContainer center={[52, 21]} zoom={5} style={{ height: '400px', width: '100%' }}>
  <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
  {threats.map((t, i) => <Marker key={i} position={[t.lat, t.lon]}><Popup>{t.profileId}</Popup></Marker>)}
</MapContainer>
```

## 7. Przykłady integracji z innymi repozytoriami
- PinkManAgent (pinkplayevo-jaźń) może wywoływać metody AnonymousAgent przez API
- NetworkSelph (only_together) może synchronizować listę kont z PurgeEngine
- FinanceModule (drift_money) może raportować podejrzane transakcje do ThreatMap

## 8. Uruchomienie w chmurze (Heroku/Render/Railway)
- Załóż konto, podłącz repozytorium, wybierz Node.js
- Skonfiguruj zmienne środowiskowe (API keys, MongoDB URI)
- Deploy i monitoruj logi

---

System gotowy do rozbudowy, testów i integracji z ekosystemem Microsoft/xAI!
