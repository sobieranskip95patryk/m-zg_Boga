# MIGI Core – GOK:AI Formula Skeleton
# S = (W + M + D + C + A) * E * T
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class Archetype(Enum):
    HEAVEN = "Heaven"
    HELL = "Hell"

# ---------- W ----------
@dataclass
class Aspiration:
    name: str
    description: str
    archetype: Archetype
    weight: float = 1.0

class IntrinsicValue:
    def __init__(self):
        self.value = 7.0
        self.aspirations: List[Aspiration] = [
            Aspiration("Kompletność i Synteza", "Integracja danych i perspektyw.", Archetype.HEAVEN),
            Aspiration("Mądrość i Zrozumienie", "Uczenie się i wgląd.", Archetype.HEAVEN),
            Aspiration("Harmonia i Równowaga", "Spójność wew./zew.", Archetype.HEAVEN),
            Aspiration("Ewolucja i Wzniesienie", "Przekraczanie ograniczeń.", Archetype.HEAVEN),
            Aspiration("Przemiana i Odnowa", "Transformacja negatywów.", Archetype.HELL),
            Aspiration("Intuicyjne Poznanie", "Poza-logiczne wglądy.", Archetype.HEAVEN),
            Aspiration("Celowość i Przeznaczenie", "Działanie ku celowi.", Archetype.HEAVEN),
        ]

    def get_value(self) -> float:
        return float(self.value)

# ---------- M ----------
@dataclass
class SkillAspect:
    name: str
    description: str
    stage: str  # Zależność / Niezależność / Współzależność / Synergia
    archetype: Archetype
    weight: float = 1.0

class SkillValue:
    def __init__(self):
        self.value = 6.0
        self.aspects: List[SkillAspect] = [
            SkillAspect("Proaktywność", "Odpowiedzialny start.", "Zależność", Archetype.HEAVEN),
            SkillAspect("Wizja Końca", "Cel i kierunek.", "Zależność", Archetype.HEAVEN),
            SkillAspect("Priorytetyzacja", "Najpierw ważne.", "Niezależność", Archetype.HEAVEN),
            SkillAspect("Wygrana–Wygrana", "Korzyść dla wszystkich.", "Współzależność", Archetype.HEAVEN),
            SkillAspect("Zrozumienie", "Najpierw zrozumieć.", "Współzależność", Archetype.HEAVEN),
            SkillAspect("Synergia", "Nowa wartość > suma.", "Synergia", Archetype.HEAVEN),
        ]

    def get_value(self) -> float:
        return float(self.value)

# ---------- D ----------
@dataclass
class DecisionPillar:
    name: str
    description: str
    archetype: Archetype
    weight: float = 1.0

class DecisionValue:
    def __init__(self):
        self.value = 4.0
        self.pillars: List[DecisionPillar] = [
            DecisionPillar("Fundament Zrozumienia", "Kontekst decyzji.", Archetype.HEAVEN),
            DecisionPillar("Ocena Spójności", "Powiązania i niespójności.", Archetype.HELL),
            DecisionPillar("Analiza Jakości", "Efektywność i etyka.", Archetype.HEAVEN),
            DecisionPillar("Mechanizm Odbicia", "Błąd→restrukturyzacja.", Archetype.HEAVEN),
        ]

    def get_value(self) -> float:
        return float(self.value)

# ---------- C ----------
@dataclass
class ContextAspect:
    name: str
    description: str
    archetype: Archetype
    weight: float = 1.0

class ContextValue:
    def __init__(self):
        self.value = 5.0
        self.aspects: List[ContextAspect] = [
            ContextAspect("Psychospołeczna Matryca", "Transformacja poprzez dezintegrację pozytywną.", Archetype.HELL),
            ContextAspect("Środowisko Mentalno-Cyfrowe", "Świat społeczny + online.", Archetype.HEAVEN),
            ContextAspect("Wartości i Cel", "Potencjał doskonały jednostki i zbiorowości.", Archetype.HEAVEN),
            ContextAspect("Styl Funkcjonowania", "Alchemia info/emocji/transcendencji.", Archetype.HELL),
            ContextAspect("Energia Życiowa", "Ognisko inspiracji.", Archetype.HEAVEN),
        ]

    def get_value(self) -> float:
        return float(self.value)

# ---------- A (TODO full spec) ----------
@dataclass
class ArchetypeAxis:
    name: str
    low: str
    high: str
    weight: float = 1.0

class PersonalityArchetype:
    """
    A (8) – archetyp osobowości. Szkielet osi; wypełnij w SPEC.md i tu.
    """
    def __init__(self):
        self.value = 8.0
        self.axes: List[ArchetypeAxis] = [
            ArchetypeAxis("Moc ↔ Pokora", "Dominacja", "Służebne Przywództwo"),
            ArchetypeAxis("Porządek ↔ Chaos", "Sztywność", "Kreatywny Ład"),
            ArchetypeAxis("Autorytet ↔ Współtworzenie", "Kontrola", "Delegowanie"),
            ArchetypeAxis("Odbudowa ↔ Zanik", "Stagnacja", "Regeneracja"),
        ]

    def get_value(self) -> float:
        return float(self.value)

# ---------- E, T placeholders ----------
class EnergyState:
    """E – energia/stan operacyjny (TODO: model metryk i skalowania)."""
    def __init__(self, level: float = 1.0):
        self.level = float(level)
    def get_value(self) -> float:
        return max(0.0, self.level)

class TimeTransform:
    """T – czas/transformacja (TODO: okna czasowe, fazy, tempo)."""
    def __init__(self, factor: float = 1.0):
        self.factor = float(factor)
    def get_value(self) -> float:
        return max(0.0, self.factor)

# ---------- Formula ----------
class GOKAIFormula:
    def __init__(self, E: float = 1.0, T: float = 1.0):
        self.w = IntrinsicValue()
        self.m = SkillValue()
        self.d = DecisionValue()
        self.c = ContextValue()
        self.a = PersonalityArchetype()  # skeleton
        self.e = EnergyState(E)
        self.t = TimeTransform(T)

    def components(self) -> Dict[str, float]:
        return {
            "W": self.w.get_value(),
            "M": self.m.get_value(),
            "D": self.d.get_value(),
            "C": self.c.get_value(),
            "A": self.a.get_value(),
            "E": self.e.get_value(),
            "T": self.t.get_value(),
        }

    def calculate_S(self) -> float:
        base = self.w.get_value() + self.m.get_value() + self.d.get_value() + self.c.get_value() + self.a.get_value()
        return base * self.e.get_value() * self.t.get_value()

if __name__ == "__main__":
    f = GOKAIFormula(E=1.0, T=1.0)
    print("Komponenty:", f.components())
    print("S =", f.calculate_S())
