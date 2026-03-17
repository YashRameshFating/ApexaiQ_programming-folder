from fastapi import APIRouter
import requests
from models import CryptoRequest
from database import price_cache

router = APIRouter()

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"


@router.post("/price")
def get_crypto_price(data: CryptoRequest):

    coin = data.coin_id.lower()

    # Check cache
    if coin in price_cache:
        return {"source": "cache", "data": price_cache[coin]}

    url = f"{BASE_URL}?ids={coin}&vs_currencies=usd"

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {"error": "API request failed"}

        price_data = response.json()

        price_cache[coin] = price_data

        return {"source": "api", "data": price_data}

    except requests.exceptions.RequestException as e:

        return {
            "error": "Failed to connect to CoinGecko API",
            "details": str(e)
        }