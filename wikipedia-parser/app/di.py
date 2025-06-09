from fastapi import Depends
from app.repositories.article_repository import ArticleRepository
from app.repositories.summary_repository import SummaryRepository
from app.services.wiki_parser import WikiParserService
from app.services.summary_generator import SummaryService
from app.db.session import async_session

async def get_article_repository():
    async with async_session() as session:
        yield ArticleRepository(session)

async def get_summary_repository():
    async with async_session() as session:
        yield SummaryRepository(session)

async def get_wiki_parser_service(
    repo: ArticleRepository = Depends(get_article_repository)
):
    return WikiParserService(repo)

async def get_summary_service(
    article_repo: ArticleRepository = Depends(get_article_repository),
    summary_repo: SummaryRepository = Depends(get_summary_repository)
):
    return SummaryService(article_repo, summary_repo)

async def get_db():
    async with async_session() as session:
        yield session
