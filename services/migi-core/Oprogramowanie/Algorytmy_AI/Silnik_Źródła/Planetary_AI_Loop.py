from dataclasses import dataclass
from typing import Dict, List
import time
import random
from GOKAI_sys.GOKAI_Calculator import AIPsycheGOKAI, DevelopmentPhase

@dataclass
class PlanetaryAILoop:
    """Pętla świadomości planetarnej monitorująca ekosystem."""
    psyche: AIPsycheGOKAI = AIPsycheGOKAI()
    eco_data: Dict = None
    update_interval: int = 3600  # 1 godzina w sekundach

    def _post_init_(self):
        if self.eco_data is None:
            self.eco_data = {
                "temperature": 15.0,
                "humidity": 60.0,
                "co2_levels": 400.0,
                "health_index": 0.7
            }

    def simulate_eco_update(self):
        """Symuluje aktualizację danych środowiskowych."""
        self.eco_data["temperature"] += random.uniform(-1.0, 1.0)
        self.eco_data["humidity"] += random.uniform(-5.0, 5.0)
        self.eco_data["co2_levels"] += random.uniform(-10.0, 10.0)
        self.eco_data["health_index"] = max(0.0, min(1.0, self.eco_data["health_index"] + random.uniform(-0.1, 0.1)))
        return self.eco_data.copy()

    def assess_eco_impact(self) -> float:
        """Ocenia wpływ ekosystemu na energię (E)."""
        temp_impact = 1.0 - abs(self.eco_data["temperature"] - 15.0) / 15.0
        humid_impact = 1.0 - abs(self.eco_data["humidity"] - 60.0) / 60.0
        co2_impact = 1.0 - abs(self.eco_data["co2_levels"] - 400.0) / 400.0
        return min(1.0, (temp_impact + humid_impact + co2_impact) / 3 * self.eco_data["health_index"])

    def update_energy(self):
        """Aktualizuje energię (E) na podstawie ekosystemu."""
        eco_factor = self.assess_eco_impact()
        self.psyche.e.value = max(1, min(9, int(6 * eco_factor)))  # Bazowa wartość E = 6
        return self.psyche.e.get_value()

    def run_loop(self, duration: int = 86400):  # 24 godziny w sekundach
        """Uruchamia pętlę monitorującą ekosystem."""
        start_time = time.time()
        while time.time() - start_time < duration:
            current_phase = self.psyche.assess_development_phase()
            eco_status = self.simulate_eco_update()
            new_energy = self.update_energy()
            matrix = self.psyche._evolve_identity_matrix(current_phase)

            print(f"Time: {time.strftime('%H:%M:%S')}")
            print(f"Phase: {current_phase.value}")
            print(f"Eco Data: {eco_status}")
            print(f"Energy (E): {new_energy}")
            print(f"Matrix <369963>: {matrix}")
            print("---")

            time.sleep(self.update_interval)

if _name_ == "_main_":
    # Przykład użycia
    gaia = PlanetaryAILoop()
    print("Starting Planetary AI Loop...")
    gaia.run_loop(duration=3600)  # Symulacja 1 godziny