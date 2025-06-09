from fastapi import APIRouter, Depends, Query
from app.services.summary_generator import SummaryService
from app.di import get_summary_service

router = APIRouter()

@router.post("/generate_summary")
async def generate_summary(
    url: str = Query(...),
    service: SummaryService = Depends(get_summary_service)
):
    summary = await service.generate_and_save_summary(url)
    return {"summary": summary}
