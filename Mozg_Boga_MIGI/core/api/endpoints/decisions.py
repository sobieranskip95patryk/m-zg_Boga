from fastapi import APIRouter, HTTPException
from core.kernel.AGI_Kernel import AGI_Kernel

router = APIRouter()
agi_kernel = AGI_Kernel()

@router.get("/decisions/{id}")
async def get_decision_audit(id: str):
    """
    Retrieve the audit trail for a specific decision by its ID.
    """
    decision_audit = agi_kernel.get_decision_audit(id)
    if decision_audit is None:
        raise HTTPException(status_code=404, detail="Decision not found")
    return decision_audit

@router.get("/decisions/")
async def list_decisions():
    """
    List all decisions made by the AGI system.
    """
    decisions = agi_kernel.list_decisions()
    return decisions