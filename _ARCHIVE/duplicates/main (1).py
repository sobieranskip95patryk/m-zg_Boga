from typing import Dict, List, Any
import logging
import random
import math
import yaml
import time
from gokai_core.utils.weights import rebalance_weights
from gokai_core.models.entropy_model import EntropyModel

# Ustawienie logowania
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- Moduł SYNERGY ---
class Synergy:
    def __init__(self, shared_state: Dict[str, Any], config: Dict):
        self.shared_state = shared_state
        self.config = config['synergy_config']
        self.entropy_model = EntropyModel()

    def orchestrate(self, current_event: Dict[str, Any]) -> Dict[str, Any]:
        payload = current_event.get('payload', '')
        entropy = self.entropy_model.predict(payload)
        is_creative = any(word in payload.lower() for word in self.config['creative_keywords'])

        logging.info(f"SYNERGY: Analizuję zadanie - entropia: {entropy:.2f}, kreatywne: {is_creative}")

        if is_creative:
            return {'pipelines': ['GOK:AI'], 'mode': 'CREATIVE_EXPLORATION', 'alpha': self.config['base_alpha']}
        elif entropy > self.config['entropy_threshold']:
            return {'pipelines': ['GOK:AI', 'LOGIKA:AI'], 'mode': 'BALANCED_BLEND'}
        else:
            return {'pipelines': ['GOK:AI'], 'mode': 'STANDARD'}

# --- Symulacja MIGI 7G ---
def simulate_migi_7g_connection(config: Dict, task: str) -> float:
    """Symuluje odpowiedź sieci 90 milionów deweloperów."""
    logging.info(f"MIGI 7G: Symuluję połączenie dla zadania: {task[:50]}...")
    dev_pool_size = config['migi_7g']['dev_pool_size']
    connection_active = config['migi_7g']['active_connection']
    max_contributors = config['migi_7g']['max_contributors']
    if not connection_active:
        logging.warning("MIGI 7G: Połączenie nieaktywne. Zwracam losowy wynik.")
        return random.uniform(0.5, 0.95)
    # Symulacja odpowiedzi sieci
    contributor_factor = min(len(task) / max_contributors, 1.0)
    return min(0.95, 0.7 + contributor_factor * 0.25)

# --- Główny pipeline spiralny ---
def run_cycle(event_payload: str, config: Dict, weights: List[int]) -> tuple[str, float]:
    logging.info(f"GOK:AI: Rozpoczynam cykl dla zadania: '{event_payload[:50]}...' z wagami {weights}")
    time.sleep(config['migi_7g']['response_delay'])
    migi_contribution = simulate_migi_7g_connection(config, event_payload)
    success_pct = 80 + random.uniform(5, 15) * migi_contribution
    if success_pct > 95:
        return f"Finalny wynik: Zadanie zakończone z sukcesem {success_pct:.2f}%.", success_pct
    else:
        return f"Finalny wynik: Wymagana dalsza optymalizacja. Sukces {success_pct:.2f}%.", success_pct

# --- Główna funkcja ---
def main():
    try:
        with open("gokai_core/config.yml", 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logging.error("Plik config.yml nie znaleziony. Upewnij się, że struktura katalogów jest poprawna.")
        return

    shared_state = {'level': 0, 'n': 1, 'last_success_pct': 0.0, 'history': [], 'weights': config['core_params']['matrix_weights']}
    synergy = Synergy(shared_state, config)

    # Trenowanie modelu entropii (przykładowe dane)
    texts = [
        "Zaprojektuj robota, który maluje obrazy.",
        "Analiza danych finansowych.",
        "Zbuduj plan na podbój Marsa.",
        "Proste zadanie testowe."
    ]
    entropy_labels = [2.5, 1.8, 2.8, 1.0]  # Przykładowe etykiety
    synergy.entropy_model.train(texts, entropy_labels)

    events = [
        {'payload': 'Zaprojektuj robota, który maluje obrazy.'},
        {'payload': 'Analiza danych finansowych.'},
        {'payload': 'Zbuduj plan na podbój Marsa.'}
    ]

    logging.info("Rozpoczynam Mózg Boga...")
    for event in events:
        logging.info("-" * 50)
        logging.info(f"Nowe zadanie: {event['payload'][:50]}...")

        # SYNERGY decyduje o strategii
        strategy = synergy.orchestrate(event)

        # Wykonanie zadania
        if 'GOK:AI' in strategy['pipelines']:
            result, success_pct = run_cycle(event['payload'], config, shared_state['weights'])
            shared_state['last_success_pct'] = success_pct
            logging.info(f"Ocena precyzji: {success_pct:.2f}%")

            # Rebalansowanie wag
            shared_state['weights'] = rebalance_weights(
                shared_state['weights'],
                success_pct,
                config['core_params']['risk_tolerance']
            )

        shared_state['level'] += 1
        shared_state['history'].append({'event': event['payload'], 'success': success_pct})

    logging.info("-" * 50)
    logging.info("Mózg Boga zakończył cykl zadań. Gotowy na nowe wyzwania.")

if __name__ == '__main__':
    main()