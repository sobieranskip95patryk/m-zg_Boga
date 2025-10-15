import pytest
from fastapi.testclient import TestClient
from core.api.main import app

client = TestClient(app)

def test_ask_endpoint():
    response = client.post("/v1/ask", json={"context": "test context", "power_k": 1})
    assert response.status_code == 200
    assert "S_prob" in response.json()
    assert "E" in response.json()
    assert "F" in response.json()

def test_ingest_endpoint():
    response = client.post("/v1/ingest", json={"title": "Test Document", "text": "This is a test document."})
    assert response.status_code == 200
    assert "doc_id" in response.json()

def test_plan_endpoint():
    response = client.post("/v1/plan", json={"goal": "Test Goal", "context": "Test Context"})
    assert response.status_code == 200
    assert "steps" in response.json()

def test_simulate_endpoint():
    response = client.post("/v1/simulate", json={"scenario": "Test Scenario"})
    assert response.status_code == 200
    assert "simulation_report" in response.json()

def test_decisions_endpoint():
    response = client.get("/v1/decisions/1")
    assert response.status_code == 200
    assert "audit_trail" in response.json()

def test_policy_endpoint():
    response = client.post("/v1/policy/test", json={"decision": "Test Decision"})
    assert response.status_code == 200
    assert "policy_check" in response.json()

def test_metrics_endpoint():
    response = client.get("/v1/metrics")
    assert response.status_code == 200
    assert "KPI" in response.json()