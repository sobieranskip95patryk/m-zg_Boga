# 🚀 Instrukcje Git Push dla Rocket Fuell Girls

## Przygotowanie do pushu na GitHub

### 1. Otwórz terminal w katalogu projektu
```bash
cd C:\Users\patry\Desktop\strona_PRP
```

### 2. Inicjuj repo Git (jeśli nie jest już zainicjowane)
```bash
git init
```

### 3. Dodaj remote repository
```bash
git remote add origin https://github.com/sobieranskip95patryk/rocket_fuell_girls.git
```

### 4. Dodaj wszystkie pliki do staging
```bash
git add .
```

### 5. Sprawdź co zostanie zacommitowane
```bash
git status
```

### 6. Commit z opisem
```bash
git commit -m "Initial commit: Rocket Fuell Girls platform

- Full-stack platform for models to upload photos
- Node.js backend with Express, Multer, Sharp
- SQLite database for metadata
- Admin panel for moderation
- Responsive frontend with drag&drop upload
- Docker configuration for easy deployment
- Complete documentation and quick start guide"
```

### 7. Push na GitHub
```bash
git branch -M main
git push -u origin main
```

## Alternatywnie - jeśli masz już repo Git:

### Zmień remote na nowe repozytorium
```bash
git remote set-url origin https://github.com/sobieranskip95patryk/rocket_fuell_girls.git
```

### Push do nowego repo
```bash
git push -u origin main
```

## Po pushu - sprawdź GitHub

1. Otwórz: https://github.com/sobieranskip95patryk/rocket_fuell_girls
2. Sprawdź czy wszystkie pliki są na miejscu
3. Sprawdź czy README.md wyświetla się poprawnie
4. Możesz stworzyć release tag

## Tworzenie pierwszego release

```bash
git tag -a v1.0.0 -m "Rocket Fuell Girls v1.0.0 - Initial MVP release"
git push origin v1.0.0
```

## Struktura plików w repo

Po pushu powinieneś zobaczyć:
```
rocket_fuell_girls/
├── .gitignore              # Ignorowane pliki
├── README.md               # Dokumentacja główna
├── QUICKSTART.md           # Szybki start
├── package.json            # Node.js dependencies
├── server.js               # Backend API
├── index.html              # Frontend
├── admin.html              # Panel admin
├── style.css               # Styles
├── schema.sql              # Database schema
├── Dockerfile              # Docker config
├── docker-compose.yml      # Docker orchestration
├── .dockerignore           # Docker ignore
└── uploads/                # Upload directory
    └── .gitkeep            # Keep directory in git
```

## Troubleshooting

### Problem: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/sobieranskip95patryk/rocket_fuell_girls.git
```

### Problem: "failed to push"
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### Problem: "permission denied"
Sprawdź czy masz dostęp do repo lub użyj Personal Access Token zamiast hasła.

## Po pushu - następne kroki

1. **Skonfiguruj GitHub Pages** (jeśli chcesz frontend hosting)
2. **Dodaj Secrets** dla CI/CD (jeśli planujesz automatyczny deployment)
3. **Stwórz Issues** dla kolejnych funkcjonalności
4. **Dodaj Contributors** jeśli pracujesz w zespole

**Ready to push! 🚀**