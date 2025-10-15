class Extractor:
    """Ekstrakcja cech (4 rysunki – cechy)."""

    def process(self, data):
        return {"features": [len(str(data)), str(data).lower()]}
