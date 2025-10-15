
"""T — Czas (etap, cykl, moment)"""
class TimeValue:
    def __init__(self, base: float = 3.0):
        self.base = float(base)
    def value(self) -> float:
        return self.base
