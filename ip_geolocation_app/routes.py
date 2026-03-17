from fastapi import APIRouter
import requests
from models import IPRequest
from database import ip_cache

router = APIRouter()

BASE_URL = "http://ip-api.com/json"


@router.post("/lookup")
def get_location(data: IPRequest):

    ip = data.ip

    # Check cache
    if ip in ip_cache:
        return {"source": "cache", "data": ip_cache[ip]}

    url = f"{BASE_URL}/{ip}"

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {"error": "API request failed"}

        location_data = response.json()

        ip_cache[ip] = location_data

        return {"source": "api", "data": location_data}

    except requests.exceptions.RequestException as e:

        return {
            "error": "Failed to connect to IP API",
            "details": str(e)
        }