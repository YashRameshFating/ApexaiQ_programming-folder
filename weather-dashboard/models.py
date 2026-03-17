from pydantic import BaseModel

# Request model for city search
class CityRequest(BaseModel):
    city: str

# Response model
class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str