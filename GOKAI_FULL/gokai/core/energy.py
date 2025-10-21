
"""E — Energia (stan, zasoby)"""
class EnergyValue:
    def __init__(self, base: float = 6.0):
        self.base = float(base)
    def value(self) -> float:
        return self.base
