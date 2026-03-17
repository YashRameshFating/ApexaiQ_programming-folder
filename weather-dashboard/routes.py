from fastapi import APIRouter
from models import CityRequest
from database import weather_collection
import requests

router = APIRouter()

API_KEY = "09f948eb96879f4653ec127fb48beca0"

@router.post("/weather")
def get_weather(data: CityRequest):

    city = data.city.lower()

    cached = weather_collection.find_one({"city": city})

    # If data exists in MongoDB
    if cached:
        cached.pop("_id", None)

        return {
            "source": "cache",
            **cached
        }

    # Fetch from OpenWeatherMap API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url).json()

    # Extract weather data
    temperature = response["main"]["temp"]
    description = response["weather"][0]["description"]
    icon = response["weather"][0]["icon"]

    weather_data = {
        "city": city,
        "temperature": temperature,
        "description": description,
        "icon": icon
    }

    # Save in MongoDB
    weather_collection.insert_one(weather_data)

    return {
        "source": "api",
        **weather_data
    }