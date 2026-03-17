from pydantic import BaseModel

class MovieSearch(BaseModel):
    title: str
    year: int | None = None
    page: int = 1