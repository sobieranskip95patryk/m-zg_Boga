from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class PlanRequest(BaseModel):
    goal: str
    context: Dict[str, str]

class PlanResponse(BaseModel):
    steps: List[str]
    estimates: List[str]
    confidence: float

@router.post("/v1/plan", response_model=PlanResponse)
async def plan(request: PlanRequest):
    # Here you would implement the logic to create a plan based on the goal and context
    # For now, we will return a mock response
    if not request.goal:
        raise HTTPException(status_code=400, detail="Goal must be provided")

    # Mock implementation of planning logic
    steps = ["Step 1: Analyze context", "Step 2: Define objectives", "Step 3: Create action plan"]
    estimates = ["1 day", "2 days", "3 days"]
    confidence = 0.85  # Example confidence level

    return PlanResponse(steps=steps, estimates=estimates, confidence=confidence)