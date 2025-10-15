from typing import Dict

class Reasoner:
    def __init__(self):
        self.knowledge = {}

    def reason(self, data: Dict) -> Dict:
        text = data.get("text", "")
        return {"reasoning": f"Analiza tekstu: {text}", "confidence": 0.8}
