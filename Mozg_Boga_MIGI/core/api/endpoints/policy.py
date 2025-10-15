from fastapi import APIRouter, HTTPException
from core.kernel.AGI_Kernel import AGI_Kernel

router = APIRouter()
kernel = AGI_Kernel()

@router.post("/v1/policy/test")
async def test_policy_compliance(policy_data: dict):
    try:
        compliance_result = kernel.evaluate_policy(policy_data)
        return {"compliance": compliance_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))