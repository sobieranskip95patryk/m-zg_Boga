from fastapi import FastAPI
from core.api.endpoints import ask, ingest, plan, simulate, decisions, policy, metrics

app = FastAPI()

# Include the API endpoints
app.include_router(ask.router, prefix="/v1/ask", tags=["ask"])
app.include_router(ingest.router, prefix="/v1/ingest", tags=["ingest"])
app.include_router(plan.router, prefix="/v1/plan", tags=["plan"])
app.include_router(simulate.router, prefix="/v1/simulate", tags=["simulate"])
app.include_router(decisions.router, prefix="/v1/decisions", tags=["decisions"])
app.include_router(policy.router, prefix="/v1/policy", tags=["policy"])
app.include_router(metrics.router, prefix="/v1/metrics", tags=["metrics"])

@app.get("/")
async def root():
    return {"message": "Welcome to the GOK:AI API!"}