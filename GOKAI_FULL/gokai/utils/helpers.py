
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

def clamp(v: float, a: float = 0.0, b: float = 9.0) -> float:
    return max(a, min(b, float(v)))

def wavg(values: Iterable[float], weights: Iterable[float]) -> float:
    vals = list(values); wgts = list(weights)
    s = sum(wgts) or 1.0
    return sum(v*w for v, w in zip(vals, wgts)) / s

@dataclass
class ComponentScore:
    name: str
    value: float
    note: str = ""
