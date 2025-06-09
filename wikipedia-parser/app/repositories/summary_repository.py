from app.models.summary import Summary
from sqlalchemy.ext.asyncio import AsyncSession

class SummaryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save_summary(self, article_id, summary_text):
        summary = Summary(article_id=article_id, summary=summary_text)
        self.session.add(summary)
        await self.session.commit()
        await self.session.refresh(summary)
        return summary
