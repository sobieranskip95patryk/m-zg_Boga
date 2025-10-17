"""
MÓZG BOGA - USER AUTH ENDPOINTS
FastAPI endpoints for user registration, login, and management
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import sys
import os

# Add the auth system to path
sys.path.append(os.path.join(os.path.dirname(__file__), '6_USER_AUTH_SYSTEM', 'backend'))

from models import User, UserSession, SynergyLog, get_db, create_tables
from auth import (
    UserCreate, UserLogin, UserResponse, Token, 
    create_user_dict, create_access_token, verify_password, verify_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from datetime import timedelta, datetime

# Ensure tables exist
create_tables()

# Router for auth endpoints
auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

# ===== REGISTRATION =====
@auth_router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """Rejestracja nowego użytkownika"""
    
    # Check if user already exists
    existing_user = db.query(User).filter(
        (User.email == user_data.email) | (User.username == user_data.username)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists"
        )
    
    # Create user
    user_dict = create_user_dict(user_data)
    db_user = User(**user_dict)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return UserResponse(
        id=db_user.id,
        username=db_user.username,
        email=db_user.email,
        full_name=db_user.full_name,
        user_type=db_user.user_type,
        is_active=db_user.is_active,
        is_verified=db_user.is_verified,
        agent_id=db_user.agent_id,
        total_interactions=db_user.total_interactions,
        success_rate=db_user.success_rate,
        created_at=db_user.created_at
    )

# ===== LOGIN =====
@auth_router.post("/login", response_model=Token)
async def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    """Logowanie użytkownika"""
    
    # Find user
    user = db.query(User).filter(User.email == user_data.email).first()
    
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    # Update last login
    user.last_login = datetime.utcnow()
    db.commit()
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        user=UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            user_type=user.user_type,
            is_active=user.is_active,
            is_verified=user.is_verified,
            agent_id=user.agent_id,
            total_interactions=user.total_interactions,
            success_rate=user.success_rate,
            created_at=user.created_at
        )
    )

# ===== PROFILE =====
@auth_router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user)):
    """Pobiera profil aktualnego użytkownika"""
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
        full_name=current_user.full_name,
        user_type=current_user.user_type,
        is_active=current_user.is_active,
        is_verified=current_user.is_verified,
        agent_id=current_user.agent_id,
        total_interactions=current_user.total_interactions,
        success_rate=current_user.success_rate,
        created_at=current_user.created_at
    )

# ===== SYNERGY LOGS =====
@auth_router.get("/synergy-history")
async def get_synergy_history(
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    """Historia interakcji użytkownika z SYNERGY"""
    logs = db.query(SynergyLog).filter(
        SynergyLog.user_id == current_user.id
    ).order_by(SynergyLog.created_at.desc()).limit(50).all()
    
    return {
        "user_id": current_user.id,
        "agent_id": current_user.agent_id,
        "total_interactions": current_user.total_interactions,
        "success_rate": current_user.success_rate,
        "recent_logs": [
            {
                "id": log.id,
                "task_payload": log.task_payload,
                "strategy_used": log.strategy_used,
                "success_percentage": log.success_percentage,
                "execution_time": log.execution_time,
                "created_at": log.created_at
            }
            for log in logs
        ]
    }

# ===== HELPER FUNCTIONS =====
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Dependency do pobierania aktualnego użytkownika z tokena"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        token_data = verify_token(token)
        if token_data.email is None:
            raise credentials_exception
    except:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    
    return user