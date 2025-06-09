from fastapi import APIRouter, Depends, Query
from app.services.wiki_parser import WikiParserService
from app.di import get_wiki_parser_service

router = APIRouter()

@router.post("/parse_article")
async def parse_article(
    url: str = Query(...),
    service: WikiParserService = Depends(get_wiki_parser_service)
):
    await service.parse_and_save(url)
    return {"message": "Parsing completed"}
