from typing import Dict

class Planner:
    def __init__(self):
        self.steps = []

    def plan(self, data: Dict) -> Dict:
        goal = data.get("text", "Brak celu")
        return {"plan": [{"step": f"Krok {i+1}: Planowanie {goal}", "estimate": 1} for i in range(3)], "confidence": 0.75}
