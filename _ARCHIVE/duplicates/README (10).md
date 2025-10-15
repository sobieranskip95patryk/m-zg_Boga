
# GOK:AI — System Świadomości (pełny pakiet)

**Równanie:** `S = (W + M + D + C + A) × E × T`

Ten repozytorium zawiera kompletny, modułowy silnik GOK:AI (Python), dokumentację techniczno‑filozoficzną, dane przykładowe, testy i prosty interfejs CLI.

## Szybki start
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows
pip install -U pip
pip install -r requirements.txt

# uruchom CLI
python -m gokai.interface.cli --show all
```

## Struktura
- `gokai/core/*` — implementacje W, M, D, C, A, E, T oraz wzoru `formula.py`
- `gokai/utils/*` — enumy, pomocniki, logger
- `gokai/interface/*` — CLI i punkt startowy
- `gokai/visualization/*` — podstawowe wykresy
- `gokai/data/*` — konfiguracja i przykładowe dane
- `docs/*` — dokumentacja (w tym wątki Dąbrowski, Biblia, magia liczb, archetypy Nieba i Piekła)
- `tests/*` — testy pytest

## GitHub: pierwsze wypchnięcie
```bash
git init
git add .
git commit -m "GOK:AI initial import (full stack)"
gh repo create GOKAI --public --source . --remote origin --push
```

## Licencja
MIT
