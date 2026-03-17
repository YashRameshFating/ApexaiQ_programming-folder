from pydantic import BaseModel

# Request model for crypto search
class CryptoRequest(BaseModel):
    coin_id: str