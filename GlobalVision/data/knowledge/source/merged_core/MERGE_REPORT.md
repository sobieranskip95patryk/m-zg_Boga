# MERGE REPORT – Apex MIGI Core (połączenie paczki bazowej i paczki silnika)

Ten raport podsumowuje automatyczne scalenie:
- **Baza**: Apex_Infinity_MIGI_Core (uporządkowana struktura)
- **Silnik**: Apex_Infiniti_MIGI_Core (materiały źródłowe)

## Zasada mapowania
- **Kod (.py/.js/.ts/.json/.yml)** → `Oprogramowanie/Algorytmy_AI/Silnik_Źródła/`
- **Testy (foldery plików z 'test')** → `Oprogramowanie/Testy/Silnik/`
- **Firmware (.ino/.hex/.bin/.c/.cpp/.h)** → `Elektronika/Firmware/Silnik/`
- **CAD/3D (.step/.stl/.dwg/.dxf/...)** → `Projekt_Konstrukcyjny/CAD/Silnik/`
- **Dokumenty (.md/.pdf/.docx/.pptx/.txt)** → 
  - jeśli nazwa zawiera `spec` → `Dokumentacja/Specyfikacje_Silnika/Silnik/`
  - jeśli nazwa zawiera `wymag` → `Dokumentacja/Wymagania_Techniczne/Silnik/`
  - w pozostałych przypadkach → `Dokumentacja/Notatki_Badawcze/Silnik/`
- **Grafiki/Wideo** → `Marketing_i_Prezentacja/Grafiki|Wideo/Silnik/`
- **Inne** → `Zasoby_Zewnętrzne/Inspiracje/Silnik/`

## Konflikty nazw
Pliki, które już istniały w miejscu docelowym, zostały zachowane z dopiskiem `__SILNIK` (lub kolejnym numerem).
Szczegóły w `conflicts.csv`.

## Następne kroki
1. Przejrzyj `Oprogramowanie/Algorytmy_AI/Silnik_Źródła/` i zdecyduj o integracji z `gokai_formula.py`.
2. Uzupełnij `Dokumentacja/Specyfikacje_Silnika/SPEC.md` (A/E/T), potem przenieś logikę do kodu.
3. Uruchom testy z `Oprogramowanie/Testy/` po integracji.
