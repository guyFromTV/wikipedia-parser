from app.models.article import Article
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

class ArticleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_article_by_url(self, url: str):
        result = await self.session.execute(
            select(Article).where(Article.url == url)
        )
        return result.scalar_one_or_none()

    async def save_article_if_not_exists(
        self, url: str, title: str, content: str, parent_id: int, level: int
    ):
        existing_article = await self.get_article_by_url(url)
        if existing_article:
            return existing_article.id

        article = Article(
            url=url,
            title=title,
            content=content,
            parent_id=parent_id,
            level=level
        )
        self.session.add(article)

        try:
            await self.session.commit()
            await self.session.refresh(article)
            return article.id
        except IntegrityError:
            await self.session.rollback()
            # Если другая транзакция успела вставить такую же статью, то берём её
            existing_article = await self.get_article_by_url(url)
            return existing_article.id if existing_article else None
