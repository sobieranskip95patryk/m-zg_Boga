
from __future__ import annotations
import yaml
from pathlib import Path
from gokai.core.intrinsic import IntrinsicValue
from gokai.core.skills import SkillValue
from gokai.core.decisions import DecisionValue
from gokai.core.context import ContextValue
from gokai.core.personality import PersonalityValue
from gokai.core.energy import EnergyValue
from gokai.core.time import TimeValue

class GOKAIFormula:
    def __init__(self, config_path: str | None = None):
        cfg = {}
        if config_path and Path(config_path).exists():
            cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8")) or {}

        self.W = IntrinsicValue(cfg.get("W", 7))
        self.M = SkillValue(cfg.get("M", 6))
        self.D = DecisionValue(cfg.get("D", 4))
        self.C = ContextValue(cfg.get("C", 5))
        self.A = PersonalityValue(cfg.get("A", 8))
        self.E = EnergyValue(cfg.get("E", 6))
        self.T = TimeValue(cfg.get("T", 3))

    def S(self) -> float:
        s_sum = self.W.value() + self.M.value() + self.D.value() + self.C.value() + self.A.value()
        return s_sum * self.E.value() * self.T.value()
