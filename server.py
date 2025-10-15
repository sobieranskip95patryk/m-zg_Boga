from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2AuthorizationCodeBearer
from pydantic import BaseModel
from typing import Dict
import yaml
import random
import httpx
from gokai_core.main import Synergy, run_cycle, simulate_migi_7g_connection

app = FastAPI()

# Ustawienie CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth 2.0 z Google
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/auth",
    tokenUrl="https://oauth2.googleapis.com/token",
    scopes={"openid": "OpenID", "email": "Email"}
)

class TaskRequest(BaseModel):
    payload: str

class MigiRequest(BaseModel):
    task: str

async def get_current_user(token: str = Depends(oauth2_scheme)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {token}"}
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/api/run_task")
async def run_task(task: TaskRequest, user: dict = Depends(get_current_user)) -> Dict:
    try:
        with open("gokai_core/config.yml", 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        return {"error": "Configuration file not found"}

    shared_state = {'level': 0, 'n': 1, 'last_success_pct': 0.0, 'history': [], 'weights': config['core_params']['matrix_weights']}
    synergy = Synergy(shared_state, config)

    strategy = synergy.orchestrate({'payload': task.payload})
    result, success_pct = run_cycle(task.payload, config, shared_state['weights'])
    
    return {
        "message": result,
        "success_pct": success_pct,
        "strategy": strategy['mode'],
        "user": user["email"]
    }

@app.post("/api/migi_7g")
async def migi_7g(migi: MigiRequest, user: dict = Depends(get_current_user)) -> Dict:
    try:
        with open("gokai_core/config.yml", 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        return {"error": "Configuration file not found"}

    contribution = simulate_migi_7g_connection(config, migi.task)
    return {
        "task": migi.task,
        "contribution": contribution,
        "mock_developers": random.randint(100, config['migi_7g']['max_contributors']),
        "user": user["email"]
    }