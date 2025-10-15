import numpy as np
from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class EntropyModel:
    def __init__(self, model_name: str = "distilbert-base-uncased"):
        self.model = pipeline("feature-extraction", model=model_name)
        self.is_trained = True

    def predict(self, data: str) -> float:
        """
        Oblicza entropię zadania na podstawie analizy semantycznej z BERT.
        """
        if not data:
            return 0.0
        try:
            # Ekstrakcja cech z BERT
            features = self.model(data)[0]
            # Prosta heurystyka: średnia wariancja cech jako miara entropii
            variance = np.var([np.mean(feature) for feature in features])
            entropy = variance * 10.0  # Skalowanie dla przykładu
            logging.info(f"Entropia BERT dla '{data[:50]}...': {entropy:.2f}")
            return entropy
        except Exception as e:
            logging.error(f"Błąd w modelu BERT: {e}")
            # Fallback: prosta heurystyka
            unique_chars = len(set(data))
            length = len(data)
            return unique_chars / max(length, 1) * 2.0