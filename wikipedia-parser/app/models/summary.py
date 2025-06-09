from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import declarative_base

from app.models.article import Article

Base = declarative_base()

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey(Article.id, ondelete="CASCADE"), unique=True)
    summary = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
