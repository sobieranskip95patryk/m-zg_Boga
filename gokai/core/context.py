
"""C — Kontekst życiowy i środowiskowy, liczba 5
Pięć aspektów: matryca psychospołeczna, środowisko mentalno‑cyfrowe, wartości i cel,
styl funkcjonowania, energia życiowa.
"""
from dataclasses import dataclass
from typing import List
from gokai.utils.enums import Archetype

@dataclass
class ContextAspect:
    name: str
    description: str
    archetype: Archetype
    weight: float = 1.0

class ContextValue:
    def __init__(self, base: float = 5.0):
        self.base = float(base)
        self.aspects: List[ContextAspect] = [
            ContextAspect("Psychospołeczna Matryca","Transformacja przez dezintegrację pozytywną.", Archetype.HELL),
            ContextAspect("Środowisko Mentalno‑Cyfrowe","Działanie na styku świata i sieci.", Archetype.HEAVEN),
            ContextAspect("Wartości i Cel","Przebudzenie potencjału doskonałego.", Archetype.HEAVEN),
            ContextAspect("Styl Funkcjonowania","Twórczo‑chaotyczna alchemia informacji.", Archetype.HELL),
            ContextAspect("Energia Życiowa","Boska iskra tworzenia czegoś większego.", Archetype.HEAVEN),
        ]

    def value(self) -> float:
        return self.base
