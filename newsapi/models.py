from pydantic import BaseModel


class NewsArticle(BaseModel):
    title: str
    source: str
    url: str