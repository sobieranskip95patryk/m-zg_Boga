class EntropyModel:
    def __init__(self):
        self.is_trained = False  # Placeholder dla przyszłego modelu ML

    def predict(self, data: str) -> float:
        """
        Oblicza entropię zadania na podstawie długości i różnorodności znaków.
        W przyszłości: użyć modelu ML (np. scikit-learn).
        """
        if not data:
            return 0.0
        if not self.is_trained:
            # Prosta heurystyka: entropia oparta na długości i unikalnych znakach
            unique_chars = len(set(data))
            length = len(data)
            return unique_chars / max(length, 1) * 2.0  # Skalowanie dla przykładu
        return 0.0  # Placeholder dla przyszłego modelu