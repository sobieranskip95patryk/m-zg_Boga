from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Dict
import yaml
import random
import httpx
import os
import datetime
from dotenv import load_dotenv
# Importujemy tylko co istnieje
from gokai_core.main import load_config

# ===== AUTH SYSTEM IMPORT =====
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '6_USER_AUTH_SYSTEM', 'backend'))

# Ładowanie .env
load_dotenv()

app = FastAPI(
    title="Mózg Boga API",
    description="Zintegrowany ekosystem silników AI",
    version="1.0.0"
)

# OAuth2 scheme for JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Ustawienie CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

# ===== HEALTHCHECK (no auth required) =====
@app.get("/health")
async def health_check():
    """Sprawdzenie stanu serwera i usług"""
    services = {
        "openai": "ok" if os.getenv("OPENAI_API_KEY") else "missing_key",
        "google": "ok" if os.getenv("GOOGLE_API_KEY") else "missing_key",
        "config": "ok" if os.path.exists("gokai_core/config.yml") else "missing",
        "gokai_core": "ok"
    }
    
    return {
        "status": "ok",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0",
        "services": services
    }

@app.get("/")
async def root():
    """Główny endpoint"""
    return {
        "message": "Mózg Boga API - Świadoma AI",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.post("/api/run_task")
async def run_task(task: TaskRequest, user: dict = Depends(get_current_user)) -> Dict:
    """Uruchomienie zadania w Mózgu Boga"""
    try:
        config = load_config()
    except FileNotFoundError:
        return {"error": "Configuration file not found"}

    # Symulacja procesowania zadania
    result = f"[MÓZG BOGA] Procesowanie zadania: '{task.payload}'"
    success_pct = random.uniform(0.7, 0.95)
    strategy = random.choice(["creative", "analytical", "hybrid"])
    
    return {
        "message": result,
        "success_pct": success_pct,
        "strategy": strategy,
        "user": user["email"],
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.post("/api/migi_7g")
async def migi_7g(migi: MigiRequest, user: dict = Depends(get_current_user)) -> Dict:
    """Symulacja połączenia z MIGI 7G"""
    try:
        config = load_config()
    except FileNotFoundError:
        return {"error": "Configuration file not found"}

    # Symulacja pracy deweloperów
    mock_developers = random.randint(100, 1000)
    contribution = f"Zadanie '{migi.task}' zostało rozłożone na {mock_developers} deweloperów"
    
    return {
        "task": migi.task,
        "contribution": contribution,
        "mock_developers": mock_developers,
        "user": user["email"],
        "timestamp": datetime.datetime.now().isoformat()
    }

# ===== AUTH INTEGRATION =====
try:
    from models import User, get_db, create_tables
    from auth import UserCreate, UserLogin, UserResponse, Token, verify_token
    
    # Ensure database tables exist
    create_tables()
    
    # Add auth endpoints
    from fastapi import Form
    from sqlalchemy.orm import Session
    
    @app.post("/auth/register", response_model=UserResponse)
    async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
        """Quick registration endpoint"""
        # Check if user exists
        existing_user = db.query(User).filter(
            (User.email == user_data.email) | (User.username == user_data.username)
        ).first()
        
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")
        
        # Create user with auth.py helper
        from auth import create_user_dict
        user_dict = create_user_dict(user_data)
        db_user = User(**user_dict)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return UserResponse(
            id=db_user.id, username=db_user.username, email=db_user.email,
            full_name=db_user.full_name, user_type=db_user.user_type,
            is_active=db_user.is_active, is_verified=db_user.is_verified,
            agent_id=db_user.agent_id, total_interactions=db_user.total_interactions,
            success_rate=db_user.success_rate, created_at=db_user.created_at
        )
    
    @app.post("/auth/login", response_model=Token)
    async def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
        """Quick login endpoint"""
        from auth import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
        from datetime import timedelta
        
        user = db.query(User).filter(User.email == user_data.email).first()
        
        if not user or not verify_password(user_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        access_token = create_access_token(
            data={"sub": user.email}, 
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return Token(
            access_token=access_token, token_type="bearer",
            expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            user=UserResponse(
                id=user.id, username=user.username, email=user.email,
                full_name=user.full_name, user_type=user.user_type,
                is_active=user.is_active, is_verified=user.is_verified,
                agent_id=user.agent_id, total_interactions=user.total_interactions,
                success_rate=user.success_rate, created_at=user.created_at
            )
        )
        
except ImportError as e:
    print(f"⚠️ Auth system not available: {e}")

# ===== STARTUP =====
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Starting Mózg Boga API server on port {port}")
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )