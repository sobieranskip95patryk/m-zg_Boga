# AI Furby 1.25D: San Andreas Edition - Game Package

Kompletny system gier 1.25D z integracją tokenów FURBX i interfejsem webowym.

## 🎮 Opis Gry

**AI Furby 1.25D: San Andreas Edition** to innowacyjna gra tekstowa z pseudo-grafiką ASCII, łącząca nostalgiczny styl retro z nowoczesnymi mechanikami tokenizacji. Gra oferuje immersyjne doświadczenie w stylu Grand Theft Auto: San Andreas, ale w unikalnym formacie 1.25D z artystyczną grafiką ASCII.

## ✨ Główne Funkcje

### 🎯 Gameplay Features
- **Pseudo-3D Navigation**: Nawigacja po 5 różnych lokacjach z detalistyczną grafiką ASCII
- **System Pojazdów**: 8 różnych pojazdów do kupienia za tokeny FURBX
- **Dynamiczne Encounters**: Interakcje z 10 różnymi NPC z rozbudowanymi osobowościami
- **Progress System**: System poziomów, doświadczenia i reputacji
- **Heat Mechanics**: Dynamiczny system "ciepłoty" wpływający na gameplay

### 🪙 FURBX Token Integration
- **Utility Token**: Rzeczywiste wydawanie tokenów FURBX w grze
- **Premium Experiences**: Ekskluzywne doświadczenia za tokeny
- **Vehicle Purchases**: Kupowanie pojazdów za tokeny FURBX
- **Economic Ecosystem**: Pełna integracja z systemem ekonomicznym

### 🌐 Multi-Platform Support
- **Console Mode**: Gra w terminalu z pełną funkcjonalnością
- **Web Interface**: Responsywny interfejs HTML5 dla przeglądarek
- **PWA Ready**: Progressive Web App z obsługą offline
- **Mobile Optimized**: Optymalizacja dla urządzeń mobilnych

## 📂 Struktura Pakietu

```
FurbyGame125D/
├── __init__.py                 # Główny launcher i package manager
├── furby_san_andreas.py        # Silnik gry 1.25D z mechanikami
├── furby_web_interface.py      # Generator interfejsu webowego HTML5
├── furby_server.py             # Flask server z REST API endpoints
└── README.md                   # Dokumentacja (ten plik)
```

## 🚀 Instalacja i Uruchomienie

### Wymagania Systemowe
- Python 3.8+
- Flask (do trybu webowego)
- System operacyjny: Windows/Linux/macOS

### Instalacja Zależności
```bash
pip install flask
```

### Uruchomienie Gry

#### 🎮 Tryb Console (Terminal)
```bash
python __init__.py --mode console --player "YourPlayerName"
```

#### 🌐 Tryb Web (Przeglądarka)
```bash
python __init__.py --mode web --host 0.0.0.0 --port 5000
```
Następnie otwórz przeglądarkę i przejdź do `http://localhost:5000`

#### 🧪 Tryb Test
```bash
python __init__.py --mode test
```

### Szybkie Uruchomienie

#### Bezpośrednio z Python
```python
from FurbyGame125D import launch_console_game, launch_web_server

# Console mode
launch_console_game("player_name")

# Web server mode
launch_web_server(host='127.0.0.1', port=5000)
```

## 🎯 Mechaniki Gry

### 📍 Lokacje
1. **🏖️ Santa Monica Beach** - Spokojne miejsce do rozpoczęcia przygody
2. **🌆 Downtown Los Santos** - Centrum biznesowe z wysokimi stawkami
3. **🎰 Las Venturas Casino** - Luksusowe kasyno z wysokim ryzykiem
4. **🏭 Industrial District** - Niebezpieczna dzielnica przemysłowa
5. **🏔️ Mount Chiliad Peak** - Ekskluzywny szczyt dla elit

### 🚗 System Pojazdów
- **Starter Car**: Bezpłatny pojazd startowy
- **Street Racer**: Szybki samochód sportowy (5.0 FBX)
- **Luxury Sedan**: Elegancka limuzyna (8.5 FBX)
- **Muscle Car**: Potężny muscle car (12.0 FBX)
- **Exotic Supercar**: Eksotyczny supersamochód (20.0 FBX)
- **Custom Lowrider**: Customowy lowrider (15.0 FBX)
- **Military Humvee**: Wojskowy pojazd (25.0 FBX)
- **Yacht on Wheels**: Najbardziej luksusowy pojazd (50.0 FBX)

### 👥 System NPC
10 różnych postaci z unikalnymi osobowościami:
- **Beach Babe Sofia**: Swobodna surferka z Santa Monica
- **Business Lady Victoria**: Wpływowa bizneswoman z Downtown
- **Casino Dancer Scarlett**: Zawodowa tancerka z Las Venturas
- **Street Racer Maya**: Niebezpieczna zawodniczka ulicznych wyścigów
- **Mountain Hiker Emma**: Outdoorowa przygoda na Mount Chiliad
- I 5 więcej unikalnych postaci...

### 🎮 Akcje w Encounters
- **😘 Sweet Talk**: Użyj uroku i gładkich słów
- **💰 Flash Cash**: Pokaż swoje bogactwo
- **🔥 Physical Seduction**: Użyj fizycznego magnetyzmu
- **🚗 Rev Engine**: Pochwal się swoim pojazdem
- **🎲 Risky Gamble**: Podejmij duże ryzyko
- **🪙 Use FBX Tokens**: Wydaj tokeny na premium doświadczenie
- **💨 Drive Away**: Opuść encounter

## 🌐 Web Interface Features

### 📱 Responsive Design
- Mobile-first approach
- Touch-friendly controls
- Adaptive layout dla różnych rozdzielczości
- PWA capabilities z offline support

### 🎨 UI Components
- **Interactive Dashboard**: Real-time player statistics
- **Progress Bars**: Wizualne wskaźniki energii, heat, reputacji
- **ASCII Art Display**: Renderowanie grafiki ASCII w przeglądarce
- **Modal Dialogs**: Encounters i results w eleganckich modalach
- **Tab Navigation**: Zorganizowane sekcje funkcjonalności

### 🔧 REST API Endpoints

#### Player & Game State
- `GET /api/game/status` - Pobierz status gry
- `POST /api/game/save` - Zapisz stan gry
- `POST /api/game/load` - Wczytaj stan gry
- `POST /api/game/reset` - Resetuj dane zapisane

#### Gameplay Actions
- `POST /api/game/encounter` - Generuj nowy encounter
- `POST /api/game/encounter/action` - Wykonaj akcję w encounter
- `GET /api/game/explore` - Eksploruj obecną lokację
- `POST /api/game/rest` - Odpocznij i odzyskaj energię

#### Travel & Vehicles
- `POST /api/game/travel` - Podróżuj między lokacjami
- `POST /api/game/vehicle/purchase` - Kup pojazd za tokeny FURBX

#### Settings
- `POST /api/game/settings` - Zaktualizuj ustawienia gry

## 💾 System Zapisów

### Automatyczne Zapisywanie
- Autosave po każdej istotnej akcji
- Backup system z timestamp
- Perzystentne dane między sesjami

### Format Zapisu
```json
{
    "player": {
        "name": "player_name",
        "level": 5,
        "experience": 450,
        "energy": 85,
        "heat": 30,
        "reputation": 120,
        "cash_usd": 5000,
        "fbx_tokens": 25.50,
        "current_vehicle": "luxury_sedan"
    },
    "game": {
        "position": 2,
        "game_time": 12.5,
        "difficulty": "normal"
    }
}
```

## 🏆 System Osiągnięć

### Kategorie Achievements
- **First Steps**: Podstawowe osiągnięcia dla nowych graczy
- **Social Master**: Osiągnięcia związane z encounters
- **Speed Demon**: Osiągnięcia związane z pojazdami
- **High Roller**: Osiągnięcia związane z wydawaniem tokenów
- **Explorer**: Osiągnięcia związane z eksploracją lokacji

## 🔧 Konfiguracja i Ustawienia

### Dostępne Ustawienia
- **Animations**: Włączanie/wyłączanie animacji
- **Sound Effects**: Efekty dźwiękowe (przygotowane na przyszłość)
- **Difficulty**: Poziom trudności (easy/normal/hard/insane)
- **Auto-save**: Automatyczne zapisywanie

### Environment Variables
```bash
FURBY_DEBUG=true                    # Włącz tryb debug
FURBY_DEFAULT_HOST=0.0.0.0         # Domyślny host dla web server
FURBY_DEFAULT_PORT=5000            # Domyślny port dla web server
FURBY_SAVE_DIRECTORY=./saves       # Katalog zapisów
```

## 🔗 Integracja z Ekosystemem

### FURBX Token System
Gra jest w pełni zintegrowana z systemem tokenów FURBX:
- Rzeczywiste wydawanie tokenów w grze
- Premium experiences za tokeny
- Integracja z wallet manager
- Połączenie z marketplace

### MTAQuestWebsideX Platform
- Seamless integration z główną platformą
- Single sign-on z kontem użytkownika
- Synchronized progress across devices
- Cloud save integration

## 🛠️ Development & Debugging

### Debug Mode
```bash
python __init__.py --mode console --debug
python __init__.py --mode web --debug --host 0.0.0.0 --port 5000
```

### Logging
Wszystkie komponenty używają zunifikowanego systemu logowania:
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Game action performed")
```

### Testing
```bash
# Uruchom wszystkie testy
python __init__.py --mode test

# Test specific component
python -m pytest furby_san_andreas.py
python -m pytest furby_web_interface.py
python -m pytest furby_server.py
```

## 📊 Performance & Scalability

### Optymalizacje
- Efficient ASCII art rendering
- Cached game state management
- Minimal memory footprint
- Fast JSON serialization

### Scalability Features
- Stateless server design
- Horizontal scaling ready
- Database integration prepared
- Load balancer friendly

## 🔮 Roadmap & Future Features

### Krótkoterminowe (Q1 2024)
- [ ] Mobile PWA dla urządzeń mobilnych
- [ ] Enhanced sound system
- [ ] Multiplayer encounters
- [ ] Advanced achievement system

### Długoterminowe (Q2-Q3 2024)
- [ ] Real-time multiplayer
- [ ] Blockchain integration
- [ ] NFT vehicle customization
- [ ] AI-powered dynamic storylines

## 🤝 Contributing

### Development Guidelines
1. Follow PEP 8 style guidelines
2. Add comprehensive docstrings
3. Include unit tests for new features
4. Update this README for major changes

### Bug Reports
- Use GitHub Issues dla bug reports
- Include detailed reproduction steps
- Provide system information
- Attach relevant log files

## 📄 License

This project is part of the Meta-Geniusz-mózg_Boga ecosystem.
All rights reserved © 2024 MTAQuestWebsideX.com

## 🎉 Credits

### Development Team
- **Lead Developer**: Meta-Geniusz-mózg_Boga AI System
- **Game Design**: AI Furby Platform Team
- **Token Integration**: FURBX Economics Team
- **Web Platform**: MTAQuestWebsideX.com Team

### Special Thanks
- Community feedback and testing
- FURBX token holders
- Beta testers and early adopters

---

**🎮 Ready to experience the future of 1.25D gaming? Launch AI Furby San Andreas Edition today!**

**🌐 Visit**: MTAQuestWebsideX.com  
**🪙 Learn more about FURBX**: [Token Documentation]  
**📱 Follow us**: @MTAQuestWebsideX  

*"Where ASCII art meets blockchain innovation"* ✨