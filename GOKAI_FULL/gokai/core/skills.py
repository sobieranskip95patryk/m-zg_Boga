
"""M — Umiejętności i nawyki (liczba 6)
Synergia (Nawyk 6): kulminacja zależności, niezależności i współzależności.
"""
from dataclasses import dataclass
from typing import List
from gokai.utils.enums import Archetype, Stage

@dataclass
class SkillAspect:
    name: str
    description: str
    archetype: Archetype
    stage: Stage
    weight: float = 1.0

class SkillValue:
    def __init__(self, base: float = 6.0):
        self.base = float(base)
        self.aspects: List[SkillAspect] = [
            SkillAspect("Proaktywność","Odpowiedzialność za wybory.", Archetype.HEAVEN, Stage.DEPENDENCE),
            SkillAspect("Wizja Końca","Jasny rezultat działań.", Archetype.HEAVEN, Stage.DEPENDENCE),
            SkillAspect("Priorytetyzacja","Najpierw to, co najważniejsze.", Archetype.HEAVEN, Stage.INDEPENDENCE),
            SkillAspect("Wygrana‑Wygrana","Korzyści dla wszystkich.", Archetype.HEAVEN, Stage.INTERDEPENDENCE),
            SkillAspect("Zrozumienie","Najpierw zrozum, potem mów.", Archetype.HEAVEN, Stage.INTERDEPENDENCE),
            SkillAspect("Synergia","Całość > suma części.", Archetype.HEAVEN, Stage.SYNERGY),
        ]

    def value(self) -> float:
        return self.base
