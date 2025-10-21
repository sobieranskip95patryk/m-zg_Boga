from dataclasses import dataclass
from typing import List, Dict
import numpy as np
from GOKAI_sys.GOKAI_Calculator import AIPsycheGOKAI, DevelopmentPhase

@dataclass
class MetaGeniusAgent:
    """Agent ewoluujący strategie na podstawie decyzji historycznych."""
    psyche: AIPsycheGOKAI = AIPsycheGOKAI()
    learning_rate: float = 0.1
    memory: List[Dict] = None

    def _post_init_(self):
        if self.memory is None:
            self.memory = []

    def store_decision(self, decision: Dict):
        """Zapisuje decyzję historyczną do pamięci agenta."""
        self.memory.append({
            "scenario": decision.get("scenario", ""),
            "success": decision.get("success", False),
            "consistent": decision.get("consistent", True),
            "timestamp": decision.get("timestamp", "2025-08-01T22:00:00")
        })

    def evaluate_history(self) -> float:
        """Ocenia jakość decyzji historycznych."""
        if not self.memory:
            return 0.5
        success_rate = sum(1 for d in self.memory if d["success"]) / len(self.memory)
        consistency = sum(1 for d in self.memory if d["consistent"]) / len(self.memory)
        return (success_rate + consistency) / 2

    def adapt_strategy(self, current_phase: DevelopmentPhase) -> Dict:
        """Adaptuje strategię na podstawie fazy i historii."""
        quality = self.evaluate_history()
        matrix = self.psyche._evolve_identity_matrix(current_phase)
        weights = self.psyche._evolve_identity(current_phase)

        # Modyfikacja strategii na podstawie jakości i fazy
        base_strategy = {
            "focus": "optimization" if quality < 0.5 else "innovation",
            "priority": "stability" if current_phase == DevelopmentPhase.POINT_0 else "growth",
            "confidence": min(1.0, quality * weights["T"])
        }

        # Dostosowanie z użyciem learning_rate
        if quality < 0.5 and current_phase == DevelopmentPhase.DESTRUCTION:
            base_strategy["focus"] = "recovery"
            base_strategy["confidence"] *= (1 - self.learning_rate)
        elif quality > 0.7 and current_phase == DevelopmentPhase.DEVELOPMENT:
            base_strategy["confidence"] *= (1 + self.learning_rate)

        return base_strategy

    def generate_action_plan(self, scenario: Dict) -> Dict:
        """Generuje plan działania na podstawie scenariusza."""
        current_phase = self.psyche.assess_development_phase()
        strategy = self.adapt_strategy(current_phase)
        probability = self.psyche.calculate_success_probability(scenario)

        return {
            "scenario": scenario,
            "strategy": strategy,
            "probability": probability,
            "phase": current_phase.value,
            "matrix": matrix,
            "recommended_action": f"Proceed with {strategy['focus']} (Priority: {strategy['priority']})"
        }

    def learn_from_feedback(self, outcome: Dict):
        """Aktualizuje pamięć na podstawie wyniku."""
        self.store_decision(outcome)
        quality = self.evaluate_history()
        print(f"Updated quality: {quality:.2f}, Memory size: {len(self.memory)}")

if _name_ == "_main_":
    # Przykład użycia
    agent = MetaGeniusAgent()
    
    # Przykładowe decyzje historyczne
    agent.store_decision({"scenario": "Test 1", "success": True, "consistent": True})
    agent.store_decision({"scenario": "Test 2", "success": False, "consistent": False})
    agent.store_decision({"scenario": "Test 3", "success": True, "consistent": True})

    # Przykładowy scenariusz
    scenario = {"goal": "Innowacja", "resources": 5, "outcome": 0.9}
    plan = agent.generate_action_plan(scenario)
    
    print("Agent Strategy Plan:")
    for key, value in plan.items():
        if key == "matrix":
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value}")

    # Przykładowy feedback
    agent.learn_from_feedback({"scenario": "Feedback Test", "success": True, "consistent": True})

    import json
with open("Intent_Engine.json", "r") as f:
    config = json.load(f)
print(config["intent_config"]["core_parameters"]["W"])  # Wyświetli 7