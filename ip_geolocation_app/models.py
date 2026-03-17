from pydantic import BaseModel

# Request model
class IPRequest(BaseModel):
    ip: str