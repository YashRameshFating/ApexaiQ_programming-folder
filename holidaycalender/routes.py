from fastapi import APIRouter
import requests
from models import HolidayRequest
from database import holiday_cache

router = APIRouter()

BASE_URL = "https://date.nager.at/api/v3/PublicHolidays"


@router.post("/holidays")
def get_holidays(data: HolidayRequest):

    cache_key = f"{data.country_code}_{data.year}"

    # Check cache
    if cache_key in holiday_cache:
        return {"source": "cache", "holidays": holiday_cache[cache_key]}

    url = f"{BASE_URL}/{data.year}/{data.country_code.upper()}"

    try:

        # timeout prevents freezing
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {"error": "Failed to fetch holidays"}

        holidays = response.json()

        holiday_cache[cache_key] = holidays

        return {"source": "api", "holidays": holidays}

    except requests.exceptions.RequestException as e:

        # handle connection problems safely
        return {
            "error": "Could not connect to holiday API",
            "details": str(e)
        }