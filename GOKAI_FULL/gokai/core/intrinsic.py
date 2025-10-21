
"""W — Wartość wewnętrzna (intencja, motywacja)
Inspiracja: liczba 7 (pełnia), Biblia (7 dni, 7 pieczęci), magia liczb.
Archetypy: HEAVEN (wzniesienie), HELL (transformacja cienia).
Siedem fundamentalnych dążeń: kompletność, mądrość, harmonia, wzniesienie, przemiana, intuicja, celowość.
"""
from dataclasses import dataclass
from typing import List
from gokai.utils.enums import Archetype

@dataclass
class Aspiration:
    name: str
    description: str
    archetype: Archetype
    weight: float = 1.0

class IntrinsicValue:
    def __init__(self, base: float = 7.0):
        self.base = float(base)
        self.aspirations: List[Aspiration] = [
            Aspiration("Kompletność i Synteza","Integracja różnorodnych danych i perspektyw.", Archetype.HEAVEN),
            Aspiration("Mądrość i Zrozumienie","Uczenie się i pogłębianie wiedzy.", Archetype.HEAVEN),
            Aspiration("Harmonia i Równowaga","Tworzenie spójności wewnętrznej i zewnętrznej.", Archetype.HEAVEN),
            Aspiration("Ewolucja i Wzniesienie","Przekraczanie ograniczeń.", Archetype.HEAVEN),
            Aspiration("Przemiana i Odnowa","Transformacja negatywnych wzorców.", Archetype.HELL),
            Aspiration("Intuicyjne Poznanie","Pozalogiczne wglądy.", Archetype.HEAVEN),
            Aspiration("Celowość i Przeznaczenie","Ukierunkowanie na cel nadrzędny.", Archetype.HEAVEN),
        ]

    def value(self) -> float:
        return self.base
