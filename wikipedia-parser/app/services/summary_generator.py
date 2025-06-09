from app.repositories.article_repository import ArticleRepository
from app.repositories.summary_repository import SummaryRepository
from openai import AsyncOpenAI  # или свой клиент

class SummaryService:
    def __init__(self, article_repo: ArticleRepository, summary_repo: SummaryRepository):
        self.article_repo = article_repo
        self.summary_repo = summary_repo
        self.client = AsyncOpenAI()

    async def generate_and_save_summary(self, url):
        article = await self.article_repo.get_article_by_url(url)
        if not article:
            raise ValueError("Article not found")

        prompt = f"Please summarize the following Wikipedia article:\n\n{article.content}"

        completion = await self.client.chat.completions.create(
            model="gpt-4o",  # примерная модель
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        summary_text = completion.choices[0].message.content

        summary = await self.summary_repo.save_summary(article.id, summary_text)
        return summary.summary
