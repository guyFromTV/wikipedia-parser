from fastapi import FastAPI
from app.api import parser, summary
from app.models.article import Base as ArticleBase
from app.models.summary import Base as SummaryBase
from app.db.session import engine

app = FastAPI()

app.include_router(parser.router)
app.include_router(summary.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(ArticleBase.metadata.create_all)
        await conn.run_sync(SummaryBase.metadata.create_all)
