"""
MÓZG BOGA - AUTHENTICATION MODULE
JWT-based authentication, password hashing, and user management
"""
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from fastapi import HTTPException, status
import secrets
import os
import json

# Configuration
SECRET_KEY = os.getenv("JWT_SECRET", "your-super-secret-jwt-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ===== PYDANTIC MODELS =====
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    user_type: str = "observer"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    user_type: str
    is_active: bool
    is_verified: bool
    agent_id: Optional[str]
    total_interactions: int
    success_rate: int
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    user: UserResponse

class TokenData(BaseModel):
    email: Optional[str] = None

# ===== AUTHENTICATION FUNCTIONS =====
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Weryfikuje hasło z hashem"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Tworzy hash hasła"""
    return pwd_context.hash(password)

def generate_agent_id(username: str) -> str:
    """Generuje unikalny agent_id dla SYNERGY"""
    random_suffix = secrets.token_hex(4)
    return f"agent_{username}_{random_suffix}"

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Tworzy JWT token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> TokenData:
    """Weryfikuje JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    return token_data

def create_synergy_weights(user_type: str) -> str:
    """Tworzy domyślne wagi SYNERGY na podstawie typu użytkownika"""
    weights_map = {
        "observer": [2, 3, 5, 5, 3, 2],      # Konserwatywne
        "creator": [4, 5, 7, 7, 5, 4],       # Kreatywne
        "editor": [3, 4, 6, 6, 4, 3],        # Zbalansowane
        "admin": [5, 6, 8, 8, 6, 5]          # Agresywne
    }
    
    weights = weights_map.get(user_type, weights_map["observer"])
    return json.dumps(weights)

def validate_user_type(user_type: str) -> bool:
    """Waliduje typ użytkownika"""
    valid_types = ["observer", "creator", "editor", "admin"]
    return user_type in valid_types

# ===== USER MANAGEMENT =====
def create_user_dict(user_data: UserCreate) -> Dict[str, Any]:
    """Przygotowuje dane użytkownika do zapisu w bazie"""
    if not validate_user_type(user_data.user_type):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user type"
        )
    
    agent_id = generate_agent_id(user_data.username)
    synergy_weights = create_synergy_weights(user_data.user_type)
    
    return {
        "username": user_data.username,
        "email": user_data.email,
        "hashed_password": get_password_hash(user_data.password),
        "full_name": user_data.full_name,
        "user_type": user_data.user_type,
        "agent_id": agent_id,
        "synergy_weights": synergy_weights,
        "is_active": True,
        "is_verified": False,
        "total_interactions": 0,
        "success_rate": 0
    }

# ===== SYNERGY INTEGRATION =====
def update_user_synergy_stats(user_id: int, success_percentage: int) -> Dict[str, Any]:
    """Aktualizuje statystyki użytkownika po interakcji z SYNERGY"""
    return {
        "last_interaction": datetime.utcnow(),
        "total_interactions": "increment",  # Will be handled in the database layer
        "success_rate": success_percentage  # Moving average can be calculated later
    }

if __name__ == "__main__":
    # Test hasła
    password = "test123"
    hashed = get_password_hash(password)
    print(f"Password: {password}")
    print(f"Hashed: {hashed}")
    print(f"Verified: {verify_password(password, hashed)}")
    
    # Test tokena
    token = create_access_token(data={"sub": "test@example.com"})
    print(f"Token: {token}")
    verified = verify_token(token)
    print(f"Verified email: {verified.email}")