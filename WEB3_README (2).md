# 🚀 Hip-Hop Universe - Inteligentne Kontrakty i Demo Web3

**Gotowy do produkcji szkielet z tokenem DRT + NFT Świadomości + frontendem Next.js**

## ⚡ Szybki Start

### 1. Instalacja Zależności
```bash
# Zainstaluj wszystkie zależności workspace
npm run install:all

# Lub zainstaluj indywidualnie
npm install
cd packages/contracts && npm install
cd ../../apps/web && npm install
```

### 2. Wdrożenie Inteligentnych Kontraktów (Mumbai Testnet)
```bash
cd packages/contracts

# Skopiuj szablon środowiska
cp .env.example .env
# Edytuj .env z twoim kluczem prywatnym i kluczami API

# Wdróż na testnet Mumbai
npm run deploy:mumbai

# Testuj kontrakty
npm run test:contracts
```

### 3. Konfiguracja Frontendu
```bash
cd apps/web

# Skopiuj szablon środowiska
cp .env.example .env.local
# Dodaj adresy kontraktów z wdrożenia

# Uruchom serwer deweloperski
npm run dev
```

### 4. Dostęp do Demo
- **Lokalnie**: http://localhost:3000
- **Produkcja**: https://sobieranskip95patryk.github.io/hip_hop_universe/

---

## 📁 Struktura Projektu

```
hip_hop_universe/
├── apps/
│   └── web/                 # Frontend demo Next.js
│       ├── src/
│       │   ├── app/         # Strony routera aplikacji
│       │   ├── components/  # Komponenty React
│       │   ├── lib/         # ABI kontraktów i narzędzia
│       │   └── styles/      # Style globalne
│       └── package.json
├── packages/
│   └── contracts/           # Inteligentne kontrakty Hardhat
│       ├── contracts/       # Pliki Solidity
│       │   ├── DRTToken.sol
│       │   └── ConsciousnessNFT.sol
│       ├── scripts/         # Skrypty wdrożenia
│       ├── deployments/     # Rekordy wdrożeń
│       └── package.json
├── integration/             # Oryginalny mostek świadomości
└── README.md               # Ten plik
```

---

## 💰 Funkcje Tokenu DRT

### Podstawowa Funkcjonalność
- **Standard ERC20** z możliwością spalania
- **Opłaty Transakcyjne**: 2% (0,5% spalanie, 1% skarbiec, 0,5% nagrody)
- **Nagrody Świadomości**: Możliwość mintowania przez wyrocznie
- **Zarządzanie Skarbcem**: Automatyczne podziały przychodów
- **Zwolnienia z Opłat**: Dla kontraktów platformy

### Zaawansowane Funkcje
- **Mechanizm Deflacyjny**: Spalanie tokenów przy transakcjach
- **Integracja ze Świadomością**: Nagrody za autentyczne wkłady kulturowe
- **Skarbiec Multi-podpis**: Bezpieczne zarządzanie funduszami
- **Możliwość Zatrzymania**: Funkcja awaryjnego zatrzymania

---

## 🧠 Funkcje NFT Świadomości

### Typy NFT
- **Stany Podstawowe**: Podstawowe reprezentacje świadomości
- **Zrzuty Ewolucji**: Śledzenie postępów
- **Fuzje Współpracy**: Kreacje wielu artystów
- **Momenty Kulturowe**: Znaczące wydarzenia kulturowe
- **Przepływ Artystyczny**: Zrzuty procesu twórczego
- **Rezonans Społeczny**: Świadomość społeczna

### Zaawansowane Funkcje
- **Łańcuchy Ewolucji**: Relacje rodzic-dziecko między tokenami
- **Ocena Kompatybilności**: Algorytm dopasowywania świadomości
- **System Rzadkości**: Dynamiczna rzadkość oparta na atrybutach
- **Egzekwowanie Tantiem**: Automatyczne tantiemy dla twórców (EIP-2981)
- **Tokeny Współpracy**: NFT z wieloma właścicielami

---

## 🌐 Funkcje Demo Frontendu

### Integracja Web3
- **Połączenie Portfela**: MetaMask, WalletConnect, Rainbow
- **Wsparcie Multi-chain**: Polygon i testnet Mumbai
- **Saldo w Czasie Rzeczywistym**: Tokeny DRT i MATIC
- **Interakcja z Kontraktami**: Operacje odczytu/zapisu

### Komponenty UI
- **Design Glassmorphism**: Nowoczesne efekty wizualne
- **Responsywny Layout**: Podejście mobile-first
- **Ciemny Motyw**: Estetyka hip-hop
- **System Animacji**: Integracja Framer Motion

---

## 🔧 Polecenia Deweloperskie

### Inteligentne Kontrakty
```bash
cd packages/contracts

# Kompiluj kontrakty
npm run compile

# Wdróż na testnet Mumbai
npm run deploy:mumbai

# Wdróż na mainnet Polygon
npm run deploy:polygon

# Uruchom testy
npm run test

# Weryfikuj na Polygonscan
npm run verify:mumbai
```

### Frontend
```bash
cd apps/web

# Serwer deweloperski
npm run dev

# Build produkcyjny
npm run build

# Sprawdzanie typów
npm run type-check

# Linting
npm run lint
```

### Monorepo
```bash
# Zbuduj wszystkie pakiety
npm run build

# Wyczyść wszystkie node_modules
npm run clean

# Zainstaluj wszystkie zależności
npm run install:all
```

---

## 🔑 Zmienne Środowiskowe

### Inteligentne Kontrakty (`.env`)
```bash
PRIVATE_KEY=twoj_klucz_prywatny_bez_0x
MUMBAI_RPC_URL=https://rpc-mumbai.maticvigil.com
POLYGON_RPC_URL=https://polygon-rpc.com
POLYGONSCAN_API_KEY=twoj_klucz_api_polygonscan
TREASURY_ADDRESS_MUMBAI=0x...
TREASURY_ADDRESS_POLYGON=0x...
```

### Frontend (`.env.local`)
```bash
NEXT_PUBLIC_DRT_TOKEN_ADDRESS=0x...
NEXT_PUBLIC_CONSCIOUSNESS_NFT_ADDRESS=0x...
NEXT_PUBLIC_NETWORK=mumbai
NEXT_PUBLIC_CHAIN_ID=80001
NEXT_PUBLIC_RPC_URL=https://rpc-mumbai.maticvigil.com
NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID=twoj_id_walletconnect
```

---

## 🚀 Przewodnik Wdrożenia

### 1. Wdrożenie Inteligentnych Kontraktów
```bash
# 1. Skonfiguruj środowisko
cd packages/contracts
cp .env.example .env
# Edytuj .env z twoimi danymi uwierzytelniającymi

# 2. Wdróż na testnet
npm run deploy:mumbai

# 3. Zanotuj adresy kontraktów z wyjścia
# 4. Weryfikuj na Polygonscan (opcjonalnie)
npm run verify:mumbai
```

### 2. Wdrożenie Frontendu
```bash
# 1. Skonfiguruj środowisko
cd apps/web
cp .env.example .env.local
# Dodaj adresy kontraktów z kroku 1

# 2. Zbuduj dla produkcji
npm run build

# 3. Wdróż na Vercel/Netlify/GitHub Pages
```

### 3. Wdrożenie GitHub Pages
```bash
# Z katalogu głównego repozytorium
git add .
git commit -m "Dodaj inteligentne kontrakty Web3 i demo Next.js"
git push origin main

# Włącz GitHub Pages w ustawieniach repozytorium
# Ustaw źródło na gałąź main
```

---

## 📊 Informacje o Kontraktach

### Token DRT
- **Nazwa**: Drift Token
- **Symbol**: DRT
- **Miejsca Dziesiętne**: 18
- **Całkowita Podaż**: 1,000,000 DRT (początkowa)
- **Maksymalna Podaż**: 10,000,000 DRT

### NFT Świadomości
- **Nazwa**: ConsciousnessNFT
- **Symbol**: CNSC
- **Standard**: ERC721 + ERC721Enumerable + ERC721URIStorage
- **Tantiemy**: 2,5% domyślnie

---

## 🔗 Linki i Zasoby

### Demo Na Żywo
- **GitHub Pages**: https://sobieranskip95patryk.github.io/hip_hop_universe/
- **Repozytorium**: https://github.com/sobieranskip95patryk/hip_hop_universe

### Dokumentacja
- **Przewodnik Integracji**: [INTEGRATION_COMPLETE.md](INTEGRATION_COMPLETE.md)
- **Architektura**: [INTEGRATION_ARCHITECTURE.md](INTEGRATION_ARCHITECTURE.md)
- **Przegląd Ekosystemu**: [ECOSYSTEM_MANIFEST.md](ECOSYSTEM_MANIFEST.md)

### Blockchain
- **Polygon**: https://polygon.technology/
- **Testnet Mumbai**: https://mumbai.polygonscan.com/
- **Kran**: https://faucet.polygon.technology/

---

## 🎯 Następne Kroki

### Natychmiastowe (Tydzień 1)
- [ ] Wdróż kontrakty na testnet Mumbai
- [ ] Skonfiguruj frontend z adresami kontraktów
- [ ] Testuj połączenie portfela i podstawową funkcjonalność
- [ ] Dodaj przechowywanie metadanych IPFS dla NFT

### Krótkoterminowe (Miesiąc 1)
- [ ] Wdróż na mainnet Polygon
- [ ] Dodaj płynność tokenu DRT (DEX)
- [ ] Wdróż system wyroczni świadomości
- [ ] Stwórz interfejs marketplace NFT

### Średnioterminowe (Kwartał 1)
- [ ] Rozwój aplikacji mobilnej
- [ ] Zaawansowane funkcje świadomości
- [ ] Zarządzanie społecznościowe (DAO)
- [ ] Program wdrażania artystów

---

## 🤝 Współpraca

1. Zrób fork repozytorium
2. Stwórz gałąź funkcji: `git checkout -b feature/awesome-feature`
3. Commituj zmiany: `git commit -m 'Dodaj awesome feature'`
4. Push do gałęzi: `git push origin feature/awesome-feature`
5. Wyślij pull request

---

## 📄 Licencja

Licencja MIT - zobacz plik [LICENSE](LICENSE) dla szczegółów.

---

**🎵 Stworzone z ❤️ przez zespół Hip-Hop Universe**

*"Gdzie każdy inteligentny kontrakt to zwrotka, każda transakcja to beat, a każdy użytkownik to współtwórca globalnej świadomości kultury hip-hop."*

---

### ⭐ **Oznacz to repozytorium gwiazdką** jeśli wierzysz w przyszłość integracji kulturowo-Web3!

**🚀 Wdrażaj. Twórz. Ewoluuj. Transcenduj. 🚀**