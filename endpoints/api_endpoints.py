from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from kernel.agi_kernel import AGIKernel
from agents.reasoner import Reasoner
from agents.planner import Planner
from core.knowledge.rag import RAG
from fastapi.security import APIKeyHeader

app = FastAPI(title="MIGI Core API")

api_key_header = APIKeyHeader(name="X-API-KEY")

class Auth:
    def __init__(self):
        self.api_key = "your_api_key"  # Z .env

def get_auth(api_key: str = Depends(api_key_header)):
    auth = Auth()
    if api_key != auth.api_key:
        raise HTTPException(401, "Invalid API Key")
    return auth

class InputData(BaseModel):
    text: str
    phase_score: float = 0.5
    phase: str = "Punkt 0"

class Decision(BaseModel):
    s_prob: float
    reasoning: str
    plan: list
    k: str

kernel = AGIKernel()
kernel.load_model()
reasoner = Reasoner()
planner = Planner()
rag = RAG()

@app.post("/v1/ask", response_model=Decision)
def ask(data: InputData, auth: Auth = Depends(get_auth)):
    s_prob = kernel.calculate_s(data.dict())
    reasoning = reasoner.reason(data.dict())["reasoning"]
    plan = planner.plan(data.dict())["plan"]
    k = rag.query(data.text)
    return Decision(s_prob=s_prob, reasoning=reasoning, plan=plan, k=k)

@app.post("/v1/ingest")
def ingest(data: InputData, auth: Auth = Depends(get_auth)):
    rag.ingest(data.text)
    return {"status": "ingested"}

@app.post("/v1/plan")
def plan(data: InputData, auth: Auth = Depends(get_auth)):
    return planner.plan(data.dict())

@app.post("/v1/simulate")
def simulate(data: InputData, auth: Auth = Depends(get_auth)):
    return {"simulation": f"Raport dla fazy {data.phase}"}

@app.get("/v1/decisions/{id}")
def get_decision(id: int, auth: Auth = Depends(get_auth)):
    return {"decision": f"Audit trail for decision {id}"}

@app.post("/v1/policy/test")
def test_policy(data: InputData, auth: Auth = Depends(get_auth)):
    return {"passed": True}

@app.get("/v1/metrics")
def metrics(auth: Auth = Depends(get_auth)):
    return {"metrics": {"latency": 0.1, "s_prob_avg": 75.5}}
