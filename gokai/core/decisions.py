
"""D — Decyzje z przeszłości (jakość + spójność), liczba 4
Dąbrowski: dezintegracja pozytywna → reintegracja na wyższym poziomie.
"""
from dataclasses import dataclass
from typing import List
from gokai.utils.enums import Archetype

@dataclass
class DecisionPillar:
    name: str
    description: str
    archetype: Archetype
    weight: float = 1.0

class DecisionValue:
    def __init__(self, base: float = 4.0):
        self.base = float(base)
        self.pillars: List[DecisionPillar] = [
            DecisionPillar("Fundament Zrozumienia","Analiza kontekstu minionych decyzji.", Archetype.HEAVEN),
            DecisionPillar("Ocena Spójności","Wykrywanie niespójności i kolizji wzorców.", Archetype.HELL),
            DecisionPillar("Analiza Jakości","Ocena efektów, etyki i zgodności z celem.", Archetype.HEAVEN),
            DecisionPillar("Mechanizm Odbicia","Ulepszanie struktur przez naukę na błędach.", Archetype.HEAVEN),
        ]

    def value(self) -> float:
        return self.base
