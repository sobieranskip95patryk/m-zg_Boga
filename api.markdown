# Dokumentacja API Mózgu Boga

## Przegląd
Ten dokument opisuje kluczowe funkcje i klasy dostępne w systemie Mózg Boga.

## Moduł `gokai_core.main`
### Klasa: `Synergy`
- **Metoda: `orchestrate(current_event: Dict[str, Any]) -> Dict[str, Any]`**
  - Opis: Decyduje o strategii przetwarzania zadania na podstawie entropii i słów kluczowych.
  - Parametry:
    - `current_event`: Słownik z kluczem `payload` (ciąg znaków zadania).
  - Zwraca: Słownik z kluczami `pipelines`, `mode` i `alpha`.

### Funkcja: `simulate_migi_7g_connection(config: Dict, task: str) -> float`
- Opis: Symuluje odpowiedź sieci MIGI 7G.
- Parametry:
  - `config`: Konfiguracja systemu.
  - `task`: Ciąg znaków zadania.
- Zwraca: Wartość od 0.5 do 0.95 (symulowany współczynnik sukcesu).

## Moduł `gokai_core.utils.weights`
### Funkcja: `rebalance_weights(weights: List[int], success_pct: float, risk_tolerance: float) -> List[int]`
- Opis: Rebalansuje wAGI matrycy `<347743>` na podstawie sukcesu zadania.
- Parametry:
  - `weights`: Lista wag (np. [3, 4, 7, 7, 4, 3]).
  - `success_pct`: Procent sukcesu zadania.
  - `risk_tolerance`: Tolerancja ryzyka z `config.yml`.
- Zwraca: Nowa lista wag.

## Moduł `gokai_core.models.entropy_model`
### Klasa: `EntropyModel`
- **Metoda: `predict(data: str) -> float`**
  - Opis: Oblicza entropię zadania (obecnie heurystyka, w przyszłości model ML).
  - Parametry:
    - `data`: Ciąg znaków zadania.
  - Zwraca: Wartość entropii.

## Przykład użycia
```python
from gokai_core.main import Synergy, run_cycle
config = {...}  # Wczytaj config.yml
shared_state = {'level': 0, 'weights': config['core_params']['matrix_weights'], ...}
synergy = Synergy(shared_state, config)
event = {'payload': 'Zaprojektuj robota.'}
strategy = synergy.orchestrate(event)
result, success = run_cycle(event['payload'], config, shared_state['weights'])
```