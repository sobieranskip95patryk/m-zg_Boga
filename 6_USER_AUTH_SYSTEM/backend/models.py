"""
MÓZG BOGA - USER DATABASE MODELS
SQLAlchemy models for user authentication and management
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from pathlib import Path

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mozg_boga_users.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    """Model użytkownika w systemie Mózg Boga"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    user_type = Column(String(50), default="observer")  # observer, creator, editor, admin
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    
    # SYNERGY Integration
    agent_id = Column(String(100), unique=True, index=True)  # Unikalny ID dla SYNERGY
    synergy_weights = Column(Text)  # JSON string z personalnymi wagami
    total_interactions = Column(Integer, default=0)
    success_rate = Column(Integer, default=0)  # Procent sukcesu w SYNERGY

class UserSession(Base):
    """Model sesji użytkownika"""
    __tablename__ = "user_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    session_token = Column(String(255), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    ip_address = Column(String(45))
    user_agent = Column(Text)

class SynergyLog(Base):
    """Log działań SYNERGY dla użytkowników"""
    __tablename__ = "synergy_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    session_id = Column(Integer, index=True)
    task_payload = Column(Text)
    strategy_used = Column(String(50))  # creative, analytical, hybrid
    success_percentage = Column(Integer)
    execution_time = Column(Integer)  # milliseconds
    weights_used = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
    
def create_tables():
    """Tworzy wszystkie tabele w bazie danych"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")

def get_db():
    """Dependency injection dla sesji bazy danych"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    # Uruchamianie tylko do testów
    create_tables()
    print(f"Database URL: {DATABASE_URL}")
    print(f"Tables created: {', '.join(Base.metadata.tables.keys())}")