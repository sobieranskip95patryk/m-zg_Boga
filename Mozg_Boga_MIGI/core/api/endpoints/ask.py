from fastapi import APIRouter, HTTPException
from core.kernel.AGI_Kernel import AGI_Kernel

router = APIRouter()
agi_kernel = AGI_Kernel()

@router.post("/v1/ask")
async def ask_question(context: str, power_k: float):
    try:
        decision = agi_kernel.decide(context, power_k)
        return decision
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))