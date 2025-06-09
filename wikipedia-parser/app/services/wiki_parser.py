import httpx
from bs4 import BeautifulSoup
from app.repositories.article_repository import ArticleRepository

class WikiParserService:
    def __init__(self, article_repo: ArticleRepository):
        self.article_repo = article_repo

    async def parse_and_save(self, url, level=0, max_depth=5, parent_id=None):
        if level >= max_depth:
            return

        async with httpx.AsyncClient(follow_redirects=True) as client:
            response = await client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.find("h1").text if soup.find("h1") else "No Title"
            content = soup.find("div", {"id": "bodyContent"}).get_text(separator="\n")

        article_id = await self.article_repo.save_article_if_not_exists(url, title, content, parent_id, level)


        links = [a['href'] for a in soup.find_all("a", href=True) if a['href'].startswith("/wiki/")]
        for link in links:
            full_url = f"https://en.wikipedia.org{link}"
            await self.parse_and_save(full_url, level + 1, max_depth, article_id)
