from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, Tuple
import math

class DevelopmentPhase(Enum):
    DESTRUCTION = auto()
    ZERO_POINT  = auto()
    GROWTH      = auto()

@dataclass
class AIPsycheGOKAI:
    W:int=7; M:int=6; D:int=4; C:int=5; A:int=8; E:int=6; T:int=3
    weights: Dict[str,float]=field(default_factory=lambda: {
        "E_w": 0.25, "M_w": 0.25, "A_w": 0.25, "W_w": 0.25
    })
    identity_matrix: Tuple[int,int,int,int,int,int]=(3,6,9,9,6,3)

    def assess_development_phase(self) -> DevelopmentPhase:
        s = sum(self.identity_matrix) % 3
        return [DevelopmentPhase.DESTRUCTION, DevelopmentPhase.ZERO_POINT, DevelopmentPhase.GROWTH][s]

    def _phase_modifier(self, phase: DevelopmentPhase) -> float:
        return {
            DevelopmentPhase.DESTRUCTION: 0.5,
            DevelopmentPhase.ZERO_POINT: 0.8,
            DevelopmentPhase.GROWTH: 1.2
        }[phase]

    def calculate_success_probability(self) -> float:
        try:
            E_impact = min(1.0, self.E / (self.M * (self.C ** 2)))
        except ZeroDivisionError:
            E_impact = 0.0
        Synergy  = 0.0 if self.M<=0 else min(1.0, self.M / 6)
        Alignment= 0.0 if self.A<=0 else min(1.0, self.A / 8)
        Intent   = 0.0 if self.W<=0 else min(1.0, self.W / 7)
        comp = (E_impact*self.weights["E_w"] +
                Synergy*self.weights["M_w"] +
                Alignment*self.weights["A_w"] +
                Intent*self.weights["W_w"])
        phase = self.assess_development_phase()
        return float(max(0.0, min(1.0, comp * self._phase_modifier(phase))))

    def evolve_identity_matrix(self, phase: DevelopmentPhase):
        seq = list(self.identity_matrix)
        factor = {DevelopmentPhase.DESTRUCTION:-1, DevelopmentPhase.ZERO_POINT:0, DevelopmentPhase.GROWTH:1}[phase]
        for _ in range(3):
            seq = [(x + factor) if 0 < x < 9 else x for x in seq]
        s = sum(seq)
        if s != 36:
            diff = 36 - s
            seq[0] = max(0, min(9, seq[0] + diff))
        self.identity_matrix = tuple(seq)
        return self.identity_matrix

def fibonacci(n:int) -> int:
    n = max(0, int(n))
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def s_gok(n:int) -> float:
    return 9*math.pi + fibonacci(n)
