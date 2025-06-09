from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    url = Column(Text, unique=True, nullable=False)
    title = Column(Text)
    content = Column(Text)
    parent_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"))
    level = Column(Integer, nullable=False)

    parent = relationship("Article", remote_side=[id], backref="children")
