![Rocket Fuell Girls Logo](images/logo_prp.png)

# 🚀 Rocket Fuell Girls Platform

**Ekskluzywna platforma dla modelek poszukujących pracy w branży modelingu**

*Część ekosystemu MTAQuestWebsideX.com*

## 🌟 O Platformie

Rocket Fuell Girls to nowoczesna platforma dedykowana modelkom poszukującym pracy w różnych sektorach modelingu. Od klasycznych sesji modowych, przez kreacje artystyczne, aż po specjalistyczne sesje erotics-fantasies - nasza platforma łączy modelki z odpowiednimi zleceniodawcami.

### 🎯 Dla Kogo?

- **Początkujące modelki** - pierwsza platforma do budowania portfolio
- **Doświadczone modelki** - rozszerzanie bazy klientów
- **Modelki specjalistyczne** - niszowe projekty fotograficzne
- **Fotografowie** - wyszukiwanie odpowiednich modelek
- **Agencje** - skauting nowych talentów

## � Funkcjonalności

### 🔥 Dla Modelek
- **Portfolio Upload**: Drag & drop z podglądem miniatur
- **Profil Modelki**: Szczegółowe dane, wymiary, specjalizacje
- **Kategorie**: Moda, glamour, artystyczne, erotics-fantasies
- **Bezpieczeństwo**: Pełna kontrola nad widocznością zdjęć
- **Messaging**: Bezpieczna komunikacja ze zleceniodawcami

### 🛡️ System Moderacji
- **Panel Administratora**: Zatwierdzanie zdjęć i profili
- **Filtrowanie treści**: Automatyczne wykrywanie nieodpowiednich materiałów
- **Raportowanie**: System zgłaszania nadużyć
- **Weryfikacja**: Potwierdzanie tożsamości modelek

### 🎨 Galeria & Portfolio
- **Responsywna karuzela** z zatwierdzonymi zdjęciami
- **Filtry kategorii**: Łatwe wyszukiwanie po typie modelingu
- **Lightbox**: Pełnoekranowy podgląd zdjęć
- **Share**: Udostępnianie portfolio na social media

## 🛠️ Technologie

- **Backend**: Node.js, Express, Multer, Sharp
- **Database**: SQLite3 z pełnym schema dla modelek
- **Frontend**: Vanilla JavaScript, CSS3 z Glass Morphism
- **Security**: EXIF removal, file sanitization, input validation
- **Deploy**: Docker, Docker Compose, GitHub Actions CI/CD
- **Design**: Ultra-modern cyberpunk aesthetic

## 🚀 Ultra-Modern Design

- **Glass Morphism**: Półprzezroczyste elementy z blur effects
- **Neon Colors**: Cyberpunk palette (pink, purple, blue, green)
- **Smooth Animations**: 60fps transitions i hover effects
- **Responsive**: Mobile-first approach
- **Dark Theme**: Futurystyczny wygląd inspirowany sci-fi

## 🔧 Instalacja i Uruchomienie

### Prerequisites
- Node.js 18+
- Docker (opcjonalne)
- Git

### Lokalnie
```bash
# Sklonuj repozytorium
git clone https://github.com/sobieranskip95patryk/rocket_fuell_girls.git
cd rocket_fuell_girls

# Zainstaluj zależności
npm install

# Uruchom serwer deweloperski
npm start

# Serwer dostępny na http://localhost:3000
```

### Docker
```bash
# Zbuduj i uruchom z Docker Compose
docker-compose up --build

# Lub tylko Docker
docker build -t rocket-fuell-girls .
docker run -p 3000:3000 rocket-fuell-girls
```

## 📡 API Endpoints

### Photos
- `POST /api/upload` - Upload zdjęcia
- `GET /api/photos` - Lista zatwierdzonych zdjęć
- `GET /api/photos/pending` - Zdjęcia do moderacji
- `POST /api/photos/:id/approve` - Zatwierdź zdjęcie
- `POST /api/photos/:id/reject` - Odrzuć zdjęcie

### Models
- `POST /api/models` - Rejestracja modelki
- `GET /api/models` - Lista modelek
- `GET /api/models/:id` - Profil modelki

## 🛡️ Bezpieczeństwo

- **File Validation**: Sprawdzanie typu i rozmiaru plików
- **EXIF Removal**: Usuwanie metadanych ze zdjęć
- **Input Sanitization**: Walidacja wszystkich danych wejściowych
- **Rate Limiting**: Ochrona przed spamem
- **HTTPS**: Szyfrowane połączenia (produkcja)

## 🎯 Roadmap

- [ ] **System wiadomości** - Chat między modelkami a fotografami
- [ ] **Płatności** - Integracja z systemami płatności
- [ ] **Kalendarz** - Zarządzanie terminami sesji
- [ ] **Reviews** - System ocen i komentarzy
- [ ] **Mobile App** - Aplikacja mobilna React Native
- [ ] **AI Tagging** - Automatyczne tagowanie zdjęć

## 🤝 Contribution

1. Fork projektu
2. Utwórz feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit zmiany (`git commit -m 'Add some AmazingFeature'`)
4. Push do branch (`git push origin feature/AmazingFeature`)
5. Otwórz Pull Request

## 📄 Licencja

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Kontakt

**MTAQuestWebsideX Team**
- Website: [MTAQuestWebsideX.com](https://MTAQuestWebsideX.com)
- Email: contact@mtaquestwebsidex.com
- GitHub: [@sobieranskip95patryk](https://github.com/sobieranskip95patryk)

---

*Zbudowane z ❤️ dla społeczności modelingu*

- **Glass Morphism**: Półprzezroczyste elementy z blur effects
- **Neon Colors**: Cyberpunk palette (pink, purple, blue, green)
- **Smooth Animations**: 60fps transitions i hover effects
- **Responsive**: Mobile-first approach
- **Dark Theme**: Futurystyczny wygląd inspirowany sci-fi
