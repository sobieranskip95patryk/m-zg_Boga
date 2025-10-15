from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()
security = HTTPBearer()

class QueryRequest(BaseModel):
    query: str

# Mock xAI/Grok integracja (zastąp prawdziwym clientem)
async def mock_grok(query: str) -> Dict[str, Any]:
    return {"response": f"PinkMan AI response: {query}", "timestamp": "2025-10-10T16:00:00"}

# JWT weryfikacja
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        decoded = jwt.decode(token, os.getenv("JWT_SECRET", "supersecret"), algorithms=["HS256"])
        if decoded.get("role") not in ["admin", "agent"]:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return decoded
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/process")
async def process_query(request: QueryRequest, user: Dict = Depends(verify_token)):
    try:
        # Mock AI pipeline (np. PyTorch-based w metageniuszpl)
        grok_result = await mock_grok(request.query)
        return {
            "result": "PinkMan processed query",
            "grok": grok_result,
            "user": user["username"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3003)
