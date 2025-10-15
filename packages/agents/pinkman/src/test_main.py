import pytest
import httpx
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_process_query():
    # Mock token (zakładamy, że auth działa)
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIn0.-k6nP5bX8V1Qz7Z3Y1z3Q4z5W6X7Y8Z9A0B1C2D3E4F"
    response = client.post("/process", json={"query": "test"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "PinkMan processed query" in response.json()["result"]

@pytest.mark.asyncio
async def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
