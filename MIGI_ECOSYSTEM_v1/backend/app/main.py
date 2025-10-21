from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import ps

app = FastAPI(title="GOK:AI / MIGI Core", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

app.include_router(ps.router, prefix="/api")

@app.get("/")
def root():
    return {"name": "GOK:AI Core", "status": "ok"}
