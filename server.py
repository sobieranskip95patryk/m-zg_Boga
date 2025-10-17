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
import importlib
import sys
from dotenv import load_dotenv
# Importujemy tylko co istnieje
from gokai_core.main import load_config

# ===== AUTH SYSTEM IMPORT =====
sys.path.append(os.path.join(os.path.dirname(__file__), '6_USER_AUTH_SYSTEM', 'backend'))

# ===== CONSCIOUSNESS SYSTEM IMPORT =====
sys.path.append(os.path.join(os.path.dirname(__file__), '7_SYSTEM_SELF'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'GlobalVision_Module'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'SpiralMemory_Module'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'SYNERGY_Module'))

try:
    # Import przy użyciu importlib dla folderów z cyframi
    seven_system_module = importlib.import_module('7_SYSTEM_SELF')
    
    from integration import SystemSelfManager, ConsciousnessAPI, IntegrationBridge
    
    # Inicjalizuj instancje globalnie
    consciousness_manager = SystemSelfManager()
    consciousness_api = ConsciousnessAPI(consciousness_manager)
    integration_bridge = IntegrationBridge(consciousness_manager)
    CONSCIOUSNESS_ENABLED = True
    print("🧠 System Świadomości zainicjalizowany!")
except ImportError as e:
    print(f"⚠️ System Świadomości niedostępny: {e}")
    CONSCIOUSNESS_ENABLED = False
    consciousness_manager = None
    consciousness_api = None
    integration_bridge = None

# GlobalVision Module
try:
    from collective_self import get_echo_mapper, generate_collective_map, get_collective_recommendations
    GLOBALVISION_ENABLED = True
    print("🌍 GlobalVision Module zainicjalizowany!")
except ImportError as e:
    print(f"⚠️ GlobalVision Module niedostępny: {e}")
    GLOBALVISION_ENABLED = False

# SpiralMemory Module
try:
    from spiral_memory import get_spiral_memory, log_spiral_event
    spiral_memory = get_spiral_memory()
    SPIRAL_MEMORY_ENABLED = True
    print("🌀 SpiralMemory Module zainicjalizowany!")
except ImportError as e:
    print(f"⚠️ SpiralMemory Module niedostępny: {e}")
    SPIRAL_MEMORY_ENABLED = False
    spiral_memory = None

# SYNERGY Module
try:
    from synergy_core import (
        get_synergy_collective_core, 
        record_user_vote, 
        apply_collective_synergy_correction,
        get_synergy_dashboard_data
    )
    synergy_collective = get_synergy_collective_core()
    SYNERGY_COLLECTIVE_ENABLED = True
    print("⚡ SYNERGY Collective Module zainicjalizowany!")
except ImportError as e:
    print(f"⚠️ SYNERGY Collective Module niedostępny: {e}")
    SYNERGY_COLLECTIVE_ENABLED = False
    synergy_collective = None# Ładowanie .env
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
        load_config()
    except FileNotFoundError:
        return {"error": "Configuration file not found"}

    # Symulacja procesowania zadania
    result = f"[MÓZG BOGA] Procesowanie zadania: '{task.payload}'"
    success_pct = random.uniform(0.7, 0.95)
    strategy = random.choice(["creative", "analytical", "hybrid"])
    
    # ===== INTEGRACJA Z SYSTEMEM ŚWIADOMOŚCI =====
    if CONSCIOUSNESS_ENABLED:
        user_id = user.get("email", "anonymous")
        consciousness_manager.process_user_decision(
            user_id=user_id,
            context=f"Wykonanie zadania MÓZG BOGA: {task.payload}",
            inputs={"task_payload": task.payload, "strategy": strategy},
            outputs={"result": result, "success_rate": success_pct},
            confidence=success_pct,
            consciousness_level=3  # Średni poziom dla zadań API
        )
    
    return {
        "message": result,
        "success_pct": success_pct,
        "strategy": strategy,
        "user": user["email"],
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.post("/api/migi")
async def run_migi_simulation(request: MigiRequest, user: dict = Depends(get_current_user)) -> Dict:
    """Uruchomienie sieci MIGI 7G"""
    try:
        load_config()
    except FileNotFoundError:
        return {"error": "Configuration file not found"}
    
    # Symulacja sieci MIGI 7G
    network_latency = random.uniform(0.1, 2.0)
    throughput = random.uniform(800, 1200)
    ai_acceleration = random.uniform(150, 300)
    
    result = {
        "message": f"[MIGI 7G] Zadanie: '{request.task}' wykonane",
        "network_performance": {
            "latency_ms": round(network_latency, 2),
            "throughput_mbps": round(throughput, 2),
            "ai_acceleration_percent": round(ai_acceleration, 2)
        },
        "status": "completed",
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # ===== INTEGRACJA Z SYSTEMEM ŚWIADOMOŚCI =====
    if CONSCIOUSNESS_ENABLED:
        user_id = user.get("email", "migi_user")
        consciousness_level = 4 if ai_acceleration > 200 else 3  # Wyższy poziom dla lepszej wydajności
        consciousness_manager.process_user_decision(
            user_id=user_id,
            context=f"Wykonanie zadania MIGI 7G: {request.task}",
            inputs={
                "task": request.task, 
                "expected_latency": 1.0,
                "expected_throughput": 1000
            },
            outputs={
                "actual_latency": network_latency,
                "actual_throughput": throughput,
                "ai_acceleration": ai_acceleration
            },
            confidence=min(ai_acceleration / 300, 1.0),  # Pewność na podstawie przyspieszenia
            consciousness_level=consciousness_level
        )
    
    return result

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

# ===== HELPER FUNCTIONS =====

def get_consciousness_manager():
    """Pobiera instancję consciousness managera"""
    global consciousness_manager
    if consciousness_manager is None and CONSCIOUSNESS_ENABLED:
        print("🧠 Inicjalizuję consciousness manager...")
        consciousness_module = importlib.import_module('lib.7_SYSTEM_SELF.consciousness_manager')
        consciousness_manager = consciousness_module.ConsciousnessManager()
    return consciousness_manager

def get_consciousness_api():
    """Pobiera instancję consciousness API"""
    global consciousness_api
    if consciousness_api is None and CONSCIOUSNESS_ENABLED:
        print("🔌 Inicjalizuję consciousness API...")
        consciousness_api_module = importlib.import_module('lib.7_SYSTEM_SELF.consciousness_api')
        consciousness_api = consciousness_api_module.ConsciousnessAPI()
    return consciousness_api

def get_integration_bridge():
    """Pobiera instancję integration bridge"""
    global integration_bridge
    if integration_bridge is None and CONSCIOUSNESS_ENABLED:
        print("🌉 Inicjalizuję integration bridge...")
        integration_bridge_module = importlib.import_module('lib.7_SYSTEM_SELF.integration_bridge')
        integration_bridge = integration_bridge_module.IntegrationBridge()
    return integration_bridge

def get_echo_mapper():
    """Pobiera instancję UserEchoMapper"""
    global echo_mapper
    if echo_mapper is None and GLOBALVISION_ENABLED:
        print("🗺️ Inicjalizuję echo mapper...")
        from GlobalVision_Module.collective_self import UserEchoMapper
        echo_mapper = UserEchoMapper()
    return echo_mapper

def generate_collective_map():
    """Generuje mapę kolektywnej świadomości"""
    if GLOBALVISION_ENABLED:
        from GlobalVision_Module.collective_self import generate_collective_map as gcm
        return gcm()
    return {"error": "GlobalVision disabled"}

def get_collective_recommendations():
    """Pobiera rekomendacje kolektywne"""
    if GLOBALVISION_ENABLED:
        from GlobalVision_Module.collective_self import generate_synergy_recommendations
        return generate_synergy_recommendations()
    return []

def get_spiral_memory():
    """Pobiera instancję SpiralMemoryCore"""
    global spiral_memory
    if spiral_memory is None and SPIRAL_MEMORY_ENABLED:
        print("🌀 Inicjalizuję spiral memory...")
        from SpiralMemory_Module.spiral_memory import SpiralMemoryCore
        spiral_memory = SpiralMemoryCore()
    return spiral_memory

# ===== CONSCIOUSNESS SYSTEM ENDPOINTS =====
if CONSCIOUSNESS_ENABLED:
    
    @app.get("/api/consciousness/status")
    async def get_consciousness_status():
        """Status systemu świadomości"""
        try:
            # Import z modułu 7_SYSTEM_SELF
            consciousness_status = {
                "module_version": "1.0.0",
                "system_conscious": consciousness_manager.is_active,
                "awareness_level": consciousness_manager.system_self.current_awareness_level,
                "active_nodes": len(consciousness_manager.spiral_visualizer.spiral_nodes),
                "collective_users": len(consciousness_manager.global_vision.user_patterns),
                "field_strength": consciousness_manager.global_vision.consciousness_field.field_strength,
                "last_reflection": consciousness_manager.last_reflection_time.isoformat()
            }
            return consciousness_status
        except Exception as e:
            return {"error": f"Status consciousness failed: {str(e)}", "status": "error"}
    
    @app.get("/api/consciousness/state")
    async def get_consciousness_state():
        """GET /api/consciousness/state - Aktualny stan świadomości"""
        return consciousness_api.get_current_consciousness_state()
    
    @app.get("/api/consciousness/spiral")
    async def get_spiral_data():
        """GET /api/consciousness/spiral - Dane wizualizacji spiralnej"""
        return consciousness_api.get_spiral_visualization_data()
    
    @app.get("/api/consciousness/collective")
    async def get_collective_report():
        """GET /api/consciousness/collective - Raport inteligencji kolektywnej"""
        return consciousness_api.get_collective_intelligence_report()
    
    @app.get("/api/consciousness/dashboard")
    async def get_dashboard_data():
        """GET /api/consciousness/dashboard - Dane dla dashboard"""
        return consciousness_api.get_dashboard_data()
    
    @app.post("/api/consciousness/decision")
    async def register_decision(decision_data: dict, user: dict = Depends(get_current_user)):
        """POST /api/consciousness/decision - Rejestracja decyzji użytkownika"""
        user_id = user.get("email", "anonymous")
        return consciousness_api.post_user_decision(user_id, decision_data)
    
    @app.post("/api/consciousness/reflect")
    async def generate_reflection():
        """POST /api/consciousness/reflect - Generuj refleksję systemową"""
        return consciousness_api.post_generate_reflection()
    
    @app.get("/api/consciousness/spiral/html")
    async def get_spiral_html():
        """GET /api/consciousness/spiral/html - HTML wizualizacji spiralnej"""
        from fastapi.responses import HTMLResponse
        html_content = consciousness_api.get_spiral_visualization_html()
        return HTMLResponse(content=html_content)
    
    @app.get("/api/consciousness/dashboard/html")
    async def get_consciousness_dashboard():
        """Dashboard świadomości systemowej"""
        from fastapi.responses import HTMLResponse
        
        # Wczytaj szablon dashboard
        dashboard_path = os.path.join(os.path.dirname(__file__), '7_SYSTEM_SELF', 'templates', 'consciousness_dashboard.html')
        try:
            with open(dashboard_path, 'r', encoding='utf-8') as f:
                dashboard_html = f.read()
            return HTMLResponse(content=dashboard_html)
        except FileNotFoundError:
            return HTMLResponse(content="<h1>🧠 Dashboard Świadomości</h1><p>Plik templates/consciousness_dashboard.html nie został znaleziony.</p>")
    
    @app.post("/api/consciousness/activate")
    async def activate_consciousness():
        """POST /api/consciousness/activate - Aktywuj tryb świadomości"""
        return consciousness_api.post_activate_consciousness()
    
    @app.post("/api/consciousness/deactivate")
    async def deactivate_consciousness():
        """POST /api/consciousness/deactivate - Dezaktywuj tryb świadomości"""
        return consciousness_api.post_deactivate_consciousness()
    
    # ===== SYNERGY INTEGRATION =====
    @app.post("/api/synergy/consciousness")
    async def sync_synergy_with_consciousness(synergy_data: dict, user: dict = Depends(get_current_user)):
        """Synchronizacja SYNERGY z systemem świadomości"""
        user_id = user.get("email", "synergy_user")
        
        # Przetwórz przez most integracyjny
        result = integration_bridge.sync_with_synergy_weights(synergy_data.get("weights", {}))
        
        # Dodaj informacje o użytkowniku
        result["user_id"] = user_id
        result["synergy_data"] = synergy_data
        
        return result
    
    @app.get("/api/synergy/insights")
    async def get_synergy_consciousness_insights():
        """Wglądy świadomości dla systemu SYNERGY"""
        return integration_bridge.get_consciousness_insights_for_synergy()
    
    print("🧠 Endpoints systemu świadomości zostały załadowane!")
    
else:
    print("⚠️ System świadomości wyłączony - endpoints niedostępne")

# ===== GLOBALVISION MODULE ENDPOINTS =====
if GLOBALVISION_ENABLED:
    
    @app.get("/api/globalvision/collective")
    async def get_collective_analysis():
        """Analiza kolektywnej świadomości"""
        try:
            collective_data = generate_collective_map()
            return collective_data
        except Exception as e:
            return {"error": f"Collective analysis failed: {str(e)}"}
    
    @app.get("/api/globalvision/recommendations")
    async def get_collective_recommendations_api():
        """Rekomendacje dla SYNERGY na podstawie kolektywnej analizy"""
        try:
            recommendations = get_collective_recommendations()
            return recommendations
        except Exception as e:
            return {"error": f"Recommendations failed: {str(e)}", "recommendations": []}
    
    @app.get("/api/globalvision/echo/{user_id}")
    async def get_user_echo_profile(user_id: str):
        """Profil emocjonalny użytkownika"""
        try:
            echo_mapper = get_echo_mapper()
            profile = echo_mapper.get_user_emotional_profile(user_id)
            return profile
        except Exception as e:
            return {"error": f"User echo profile failed: {str(e)}"}
    
    @app.post("/api/globalvision/echo")
    async def add_user_echo(echo_data: dict, user: dict = Depends(get_current_user)):
        """Dodaje echo użytkownika do mapy kolektywnej"""
        try:
            user_id = user.get("email", "anonymous")
            echo_mapper = get_echo_mapper()
            
            emotion = echo_data.get("emotion", "neutral")
            intensity = echo_data.get("intensity", 0.5)
            context = echo_data.get("context", "user_interaction")
            
            echo_mapper.add_user_echo(user_id, emotion, intensity, context)
            
            return {
                "status": "echo_added",
                "user_id": user_id,
                "emotion": emotion,
                "intensity": intensity,
                "timestamp": datetime.datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": f"Add echo failed: {str(e)}"}
    
    @app.get("/api/globalvision/dashboard")
    async def get_globalvision_dashboard():
        """Dashboard GlobalVision Module"""
        from fastapi.responses import HTMLResponse
        
        dashboard_path = os.path.join(os.path.dirname(__file__), 'GlobalVision_Module', 'frontend', 'collective_dashboard.html')
        try:
            with open(dashboard_path, 'r', encoding='utf-8') as f:
                dashboard_html = f.read()
            return HTMLResponse(content=dashboard_html)
        except FileNotFoundError:
            return HTMLResponse(content="<h1>🌍 GlobalVision Dashboard</h1><p>Dashboard file not found.</p>")
    
    print("🌍 GlobalVision endpoints załadowane!")

# ===== SPIRAL MEMORY MODULE ENDPOINTS =====
if SPIRAL_MEMORY_ENABLED:
    
    @app.get("/api/spiral/analysis")
    async def get_spiral_analysis():
        """Analiza kolektywnej ewolucji spiralnej"""
        try:
            spiral_memory = get_spiral_memory()
            analysis = spiral_memory.analyze_collective_evolution()
            return analysis
        except Exception as e:
            return {"error": f"Spiral analysis failed: {str(e)}"}
    
    @app.get("/api/spiral/timeline/{user_id}")
    async def get_user_spiral_timeline(user_id: str):
        """Timeline rozwoju spiralnego użytkownika"""
        try:
            spiral_memory = get_spiral_memory()
            timeline = spiral_memory.get_user_timeline(user_id)
            return {"user_id": user_id, "timeline": timeline}
        except Exception as e:
            return {"error": f"User timeline failed: {str(e)}"}
    
    @app.get("/api/spiral/synchronicities")
    async def get_spiral_synchronicities():
        """Wykrywa synchroniczne zjawiska ewolucji"""
        try:
            spiral_memory = get_spiral_memory()
            synchronicities = spiral_memory.detect_synchronous_evolution()
            return {"synchronicities": synchronicities}
        except Exception as e:
            return {"error": f"Synchronicities detection failed: {str(e)}"}
    
    @app.get("/api/spiral/recommendations")
    async def get_spiral_recommendations():
        """Rekomendacje na podstawie analizy ewolucji spiralnej"""
        try:
            spiral_memory = get_spiral_memory()
            recommendations = spiral_memory.generate_evolution_recommendations()
            return {"recommendations": recommendations}
        except Exception as e:
            return {"error": f"Spiral recommendations failed: {str(e)}"}
    
    @app.post("/api/spiral/event")
    async def log_spiral_event_api(event_data: dict, user: dict = Depends(get_current_user)):
        """Loguje wydarzenie spiralne"""
        try:
            user_id = user.get("email", "anonymous")
            spiral_memory = get_spiral_memory()
            
            level = event_data.get("level", 1)
            emotion = event_data.get("emotion", "neutral")
            decision_summary = event_data.get("decision_summary", "User decision")
            context = event_data.get("context", "api_log")
            intensity = event_data.get("intensity", 0.5)
            transformation_type = event_data.get("transformation_type", "evolution")
            
            event = spiral_memory.log_spiral_event(
                user_id=user_id,
                level=level,
                emotion=emotion,
                decision_summary=decision_summary,
                context=context,
                intensity=intensity,
                transformation_type=transformation_type
            )
            
            return {
                "status": "event_logged",
                "event_id": event.timestamp,
                "user_id": user_id,
                "level": level,
                "is_breakthrough": event.breakthrough_marker
            }
        except Exception as e:
            return {"error": f"Log spiral event failed: {str(e)}"}
    
    @app.get("/api/spiral/export")
    async def export_spiral_data():
        """Eksportuje dane spiralne dla wizualizacji"""
        try:
            spiral_memory = get_spiral_memory()
            export_data = spiral_memory.export_for_visualization()
            return export_data
        except Exception as e:
            return {"error": f"Spiral export failed: {str(e)}"}
    
    print("🌀 SpiralMemory endpoints załadowane!")

# ===== SYNERGY COLLECTIVE ENDPOINTS =====
if SYNERGY_COLLECTIVE_ENABLED:
    
    @app.post("/api/synergy/vote")
    async def submit_collective_vote(vote_data: dict, user: dict = Depends(get_current_user)):
        """Rejestruje głos użytkownika w systemie kolektywnym"""
        try:
            user_id = user.get("email", f"anonymous_{datetime.datetime.now().timestamp()}")
            
            direction = vote_data.get("direction", "exploration")
            intensity = float(vote_data.get("intensity", 0.5))
            reasoning = vote_data.get("reasoning", "")
            
            result = record_user_vote(user_id, direction, intensity, reasoning)
            
            return {
                "vote_submitted": True,
                "user_id": user_id,
                "direction": direction,
                "intensity": intensity,
                "result": result,
                "meta_geniusz_influence": result.get("user_influence", 0),
                "collective_state": result.get("current_state", {}),
                "platform": "MTAQuestWebsideX.com"
            }
        except Exception as e:
            return {"error": f"Vote submission failed: {str(e)}"}
    
    @app.get("/api/synergy/dashboard")
    async def get_synergy_collective_dashboard():
        """Dashboard SYNERGY Collective Intelligence"""
        try:
            dashboard_data = get_synergy_dashboard_data()
            return dashboard_data
        except Exception as e:
            return {"error": f"Dashboard data failed: {str(e)}"}
    
    @app.post("/api/synergy/apply-correction")
    async def apply_synergy_correction(user: dict = Depends(get_current_user)):
        """Aplikuje kolektywną korektę SYNERGY na podstawie głosów i narracji"""
        try:
            correction_result = apply_collective_synergy_correction()
            
            return {
                "correction_applied": True,
                "user": user.get("email", "anonymous"),
                "result": correction_result,
                "meta_analysis": "Collective intelligence has modified SYNERGY parameters",
                "platform": "MTAQuestWebsideX.com",
                "timestamp": datetime.datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": f"Correction application failed: {str(e)}"}
    
    @app.get("/api/synergy/voting-interface")
    async def get_synergy_voting_interface():
        """Interface głosowania kolektywnego"""
        from fastapi.responses import HTMLResponse
        
        interface_path = os.path.join(os.path.dirname(__file__), 'SYNERGY_Module', 'frontend', 'synergy_voting.html')
        try:
            with open(interface_path, 'r', encoding='utf-8') as f:
                interface_html = f.read()
            return HTMLResponse(content=interface_html)
        except FileNotFoundError:
            return HTMLResponse(content="<h1>⚡ SYNERGY Voting Interface</h1><p>Interface file not found.</p>")
    
    @app.get("/synergy-voting")
    async def serve_synergy_voting():
        """Serves the SYNERGY voting interface"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/synergy_voting.html")
    
    @app.get("/synergy-dashboard")
    async def serve_synergy_dashboard():
        """Serves the unified SYNERGY dashboard"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/synergy_dashboard.html")
    
    @app.get("/synergy-mobile")
    async def serve_synergy_mobile():
        """Serves the mobile SYNERGY dashboard PWA"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/mobile/index.html")
    
    @app.get("/spiral-visualizer")
    async def serve_spiral_visualizer():
        """Serves the SpiralMind Visualizer PWA"""
        from fastapi.responses import FileResponse
        return FileResponse("SpiralMind_Module/visualizer/index.html")
    
    @app.get("/api/synergy/dashboard-script")
    async def serve_dashboard_script():
        """Serves the dashboard JavaScript"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/dashboard.js", media_type="application/javascript")
    
    @app.get("/api/synergy/mobile-script")
    async def serve_mobile_script():
        """Serves the mobile dashboard JavaScript"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/mobile/app.js", media_type="application/javascript")
    
    @app.get("/api/spiral/visualizer-script")
    async def serve_spiral_script():
        """Serves the spiral visualizer JavaScript"""
        from fastapi.responses import FileResponse
        return FileResponse("SpiralMind_Module/visualizer/spiral.js", media_type="application/javascript")
    
    # PWA Manifest files
    @app.get("/synergy-mobile/manifest.json")
    async def serve_mobile_manifest():
        """Serves the mobile PWA manifest"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/mobile/manifest.json", media_type="application/json")
    
    @app.get("/spiral-visualizer/manifest.json")
    async def serve_spiral_manifest():
        """Serves the spiral visualizer PWA manifest"""
        from fastapi.responses import FileResponse
        return FileResponse("SpiralMind_Module/visualizer/manifest.json", media_type="application/json")
    
    # Service Workers
    @app.get("/synergy-mobile/service-worker.js")
    async def serve_mobile_sw():
        """Serves the mobile PWA service worker"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/mobile/service-worker.js", media_type="application/javascript")
    
    @app.get("/spiral-visualizer/service-worker.js")
    async def serve_spiral_sw():
        """Serves the spiral visualizer PWA service worker"""
        from fastapi.responses import FileResponse
        return FileResponse("SpiralMind_Module/visualizer/service-worker.js", media_type="application/javascript")
    
    # CSS files
    @app.get("/synergy-mobile/style.css")
    async def serve_mobile_css():
        """Serves the mobile dashboard CSS"""
        from fastapi.responses import FileResponse
        return FileResponse("SYNERGY_Module/frontend/mobile/style.css", media_type="text/css")
    
    # Spiral data endpoint
    @app.get("/spiral-visualizer/spiral_data.json")
    async def serve_spiral_data():
        """Serves the spiral visualization data"""
        from fastapi.responses import FileResponse
        return FileResponse("SpiralMind_Module/visualizer/spiral_data.json", media_type="application/json")
    
    @app.get("/api/synergy/voting-status")
    async def get_voting_status():
        """Gets current voting status"""
        try:
            dashboard_data = get_synergy_dashboard_data()
            voting_state = dashboard_data.get("voting_state", {})
            
            return {
                "current_votes": voting_state.get("current_votes", []),
                "dominant_direction": voting_state.get("dominant_direction", "neutral"),
                "average_intensity": voting_state.get("average_intensity", 0.0),
                "total_voters": voting_state.get("total_voters", 0),
                "consensus_strength": voting_state.get("confidence", 0.0),
                "last_update": voting_state.get("last_vote_time", ""),
                "platform": "MTAQuestWebsideX.com"
            }
        except Exception as e:
            return {"error": f"Voting status failed: {str(e)}"}
    
    @app.get("/api/synergy/recommendations")
    async def get_synergy_recommendations():
        """Pobiera rekomendacje na podstawie kolektywnego głosowania"""
        try:
            dashboard_data = get_synergy_dashboard_data()
            recommendation = dashboard_data.get("collective_recommendation", {})
            
            return {
                "recommendations": recommendation,
                "meta_geniusz_analysis": recommendation.get("meta_analysis", ""),
                "suggested_levels": recommendation.get("suggested_levels", []),
                "synergy_adjustments": recommendation.get("synergy_adjustments", []),
                "platform": "MTAQuestWebsideX.com",
                "timestamp": datetime.datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": f"Recommendations failed: {str(e)}"}
    
    @app.get("/api/synergy/influence-stats")
    async def get_influence_statistics():
        """Statystyki wpływu kolektywnego na SYNERGY"""
        try:
            dashboard_data = get_synergy_dashboard_data()
            voting_state = dashboard_data.get("voting_state", {})
            
            return {
                "influence_statistics": {
                    "total_votes": dashboard_data.get("total_votes", 0),
                    "dominant_direction": voting_state.get("dominant_direction", "neutral"),
                    "collective_confidence": voting_state.get("confidence", 0.0),
                    "total_voters": voting_state.get("total_voters", 0),
                    "distribution": voting_state.get("distribution", {}),
                    "last_vote_time": voting_state.get("last_vote_time", ""),
                    "meta_geniusz_status": dashboard_data.get("meta_geniusz_status", "UNKNOWN")
                },
                "system_evolution": "Collective consciousness actively shaping SYNERGY",
                "platform": "MTAQuestWebsideX.com"
            }
        except Exception as e:
            return {"error": f"Influence statistics failed: {str(e)}"}
    
    print("⚡ SYNERGY Collective endpoints załadowane!")
else:
    print("⚠️ SYNERGY Collective endpoints niedostępne")

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