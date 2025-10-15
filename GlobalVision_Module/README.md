# GlobalVision Module

Moduł GlobalVision to rozszerzenie projektu "Apex Infiniti" i silnika "GOK:AI". Jego celem jest wizualizacja globalnych danych, integracja z pipeline GOK:AI oraz prezentacja wyników (np. mapy, wskaźniki, statusy) w UI.

## Struktura
- `main.js` – logika wizualizacji i integracji z UI_Prototype.
- `globalvision.css` – style dla komponentów wizualnych.
- `assets/` – obrazy, mapy, przyszłe pliki danych.

## Integracja
- Moduł jest podłączony do `UI_Prototype/index.html` jako dodatkowy komponent.
- Dane z GlobalVision mogą być używane jako input do pipeline GOK:AI.
- Wyniki (np. P(S), statusy) mogą być prezentowane na mapie lub w panelu.

## Przykład użycia
1. Załaduj `main.js` w `index.html`:
   `<script src="../GlobalVision_Module/main.js"></script>`
2. Dodaj komponent mapy lub panelu do UI.
3. Przekazuj dane do pipeline GOK:AI i wyświetlaj wyniki.

## Kontakt
Patryk Sobierański Meta-Geniusz-GOK, mtaquestwebside@wp.pl
