from pydantic import BaseModel

# Model used when user searches holidays
class HolidayRequest(BaseModel):
    country_code: str
    year: int