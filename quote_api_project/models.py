from pydantic import BaseModel

# Model representing a quote
class Quote(BaseModel):
    text: str
    author: str