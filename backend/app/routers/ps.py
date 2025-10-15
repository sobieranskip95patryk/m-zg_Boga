from fastapi import APIRouter
from pydantic import BaseModel, Field
import math
from typing import List

router = APIRouter()

class PSInput(BaseModel):
    x: float = Field(..., description="Główne wejście (intensywność zapytania / sygnału)")
    a: float = 1.0
    b: float = 0.0
    matrix: List[int] = Field(default_factory=lambda: [3,6,9,9,6,3], description="Matryca <369963>")
    fib_steps: int = 8

class PSOutput(BaseModel):
    ps: float
    details: dict

def fibonacci(n:int)->int:
    if n<=0: return 0
    if n==1: return 1
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b

@router.post("/ps", response_model=PSOutput)
def compute_ps(payload: PSInput):
    # Symboliczna sygnatura S(GOK:AI) = 9π + F(n) = F(n-1)+F(n-2) = WYNIK
    nine_pi = 9 * math.pi
    fib_n   = fibonacci(payload.fib_steps)
    fib_sum = fibonacci(payload.fib_steps-1) + fibonacci(payload.fib_steps-2)

    # liniowy rdzeń a*x + b
    linear = payload.a * payload.x + payload.b

    # wpływ matrycy <369963> jako średnia ważona na [0,1]
    m = payload.matrix if payload.matrix else [3,6,9,9,6,3]
    m_norm = sum(m)
    m_score = sum((i+1)*v for i,v in enumerate(m)) / (len(m)*9)  # norm 0..~1.22
    m_score = min(1.0, m_score)  # 0..1

    # surowy wynik
    raw = nine_pi + fib_n + fib_sum + linear

    # projekcja do 0..100 jako P(S)
    # wykorzystujemy logistykę + wzmocnienie matrycą
    k = 1.0 + 0.5*m_score
    ps = 100.0 / (1.0 + math.exp(-k * (raw/100.0)))  # skala miękka
    ps = max(0.0, min(100.0, ps))

    return PSOutput(
        ps=round(ps, 2),
        details={
            "nine_pi": nine_pi,
            "fib_n": fib_n,
            "fib_sum": fib_sum,
            "linear": linear,
            "matrix": m,
            "m_score": m_score,
            "raw": raw,
            "k": k
        }
    )
