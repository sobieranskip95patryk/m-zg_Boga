from fastapi import APIRouter, HTTPException
from core.metrics import get_metrics

router = APIRouter()

@router.get("/metrics")
async def read_metrics():
    try:
        metrics = get_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))