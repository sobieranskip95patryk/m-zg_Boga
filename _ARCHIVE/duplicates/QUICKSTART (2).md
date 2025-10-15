# 🚀 QUICK START - Rocket Fuell Girls

## Szybkie uruchomienie (5 minut)

### 1. Instalacja

```bash
# Klonuj/pobierz projekt
git clone https://github.com/patryksobieranskikla/projekt-strona-PRP.git
cd projekt-strona-PRP

# Zainstaluj Node.js dependencies
npm install
```

### 2. Uruchom serwer

```bash
# Uruchom aplikację
npm start

# Otwórz w przeglądarce:
# http://localhost:3000 - główna strona
# http://localhost:3000/admin - panel administratora
```

### 3. Testuj funkcjonalności

1. **Upload zdjęć**:
   - Wejdź na główną stronę
   - Przewiń do sekcji "Dołącz Do Nas" 
   - Wypełnij formularz i przeciągnij zdjęcia
   - Kliknij "Wyślij Aplikację"

2. **Moderacja**:
   - Wejdź na `/admin`
   - Zobacz przesłane zdjęcia
   - Zatwierdź lub odrzuć

3. **Galeria**:
   - Zatwierdzone zdjęcia pojawią się w sekcji "Nasze Modelki"

## 🐳 Docker (alternatywnie)

```bash
# Jedna komenda - zbuduj i uruchom
docker-compose up -d

# Sprawdź logi
docker-compose logs -f

# Zatrzymaj
docker-compose down
```

## 📁 Ważne pliki

- `server.js` - Backend API
- `index.html` - Frontend strony
- `admin.html` - Panel administratora
- `style.css` - Style CSS
- `uploads/` - Katalog na zdjęcia (tworzony automatycznie)
- `rocket_fuell.db` - Baza danych (tworzona automatycznie)

## ⚠️ Przed PRODUKCJĄ

**MUSISZ DODAĆ**:
1. Autoryzację do panelu admin
2. HTTPS/SSL
3. Weryfikację wieku (18+)
4. Regulamin i politykę prywatności
5. Backup bazy danych

## 🔗 Useful URLs

- Main site: http://localhost:3000
- Admin panel: http://localhost:3000/admin
- API health: http://localhost:3000/api/health
- Photos API: http://localhost:3000/api/photos

## 🆘 Problemy?

```bash
# Problem z Sharp?
npm rebuild sharp

# Problem z uprawnieniami?
chmod 755 uploads

# Restart serwera
npm start
```

**Gotowe! Platforma działa! 🎉**