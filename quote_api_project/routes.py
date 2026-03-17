from fastapi import APIRouter
import requests
from database import quote_cache

router = APIRouter()

API_URL = "https://zenquotes.io/api/random"


@router.get("/quote")
def get_quote():

    # Return cached quote if available
    if quote_cache["quote"]:
        return {"source": "cache", "data": quote_cache["quote"]}

    try:

        response = requests.get(API_URL, timeout=10)

        if response.status_code != 200:
            return {"error": "Failed to fetch quote"}

        data = response.json()[0]

        quote_data = {
            "text": data["q"],
            "author": data["a"]
        }

        # Save quote in cache
        quote_cache["quote"] = quote_data

        return {"source": "api", "data": quote_data}

    except requests.exceptions.RequestException as e:

        return {
            "error": "API connection failed",
            "details": str(e)
        }