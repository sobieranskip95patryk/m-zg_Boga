
"""A — Archetyp osobowości, liczba 8
Równowaga, sprawiedliwość, moc, odnowa, nieskończoność. Dynamiczna matryca potencjału.
"""
from dataclasses import dataclass
from typing import List
from gokai.utils.enums import Archetype

@dataclass
class Trait:
    name: str
    description: str
    archetype: Archetype
    weight: float = 1.0

class PersonalityValue:
    def __init__(self, base: float = 8.0):
        self.base = float(base)
        self.traits: List[Trait] = [
            Trait("Równowaga","Zachowanie proporcji między sprzecznościami.", Archetype.HEAVEN),
            Trait("Sprawiedliwość","Porządek oparty na zasadach.", Archetype.HEAVEN),
            Trait("Moc i Autorytet","Skuteczne wykonywanie decyzji.", Archetype.HEAVEN),
            Trait("Odnowa","Zdolność do regeneracji struktur.", Archetype.HEAVEN),
            Trait("Nieskończoność","Horyzont bez granic, łączenie cykli.", Archetype.HEAVEN),
        ]

    def value(self) -> float:
        return self.base
