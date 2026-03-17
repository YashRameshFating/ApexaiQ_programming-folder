from fastapi import APIRouter, HTTPException
from models import CurrencyRequest
from database import history_collection
import requests

router = APIRouter()

API_KEY = "e423381d00afd75a2dda06a5"


@router.post("/convert")
def convert_currency(data: CurrencyRequest):
    """
    Convert currency using ExchangeRate API
    """

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{data.from_currency}/{data.to_currency}"

    res = requests.get(url)

    if res.status_code != 200:
        raise HTTPException(status_code=500, detail="Exchange API failed")

    response = res.json()

    if "conversion_rate" not in response:
        raise HTTPException(status_code=400, detail="Invalid currency")

    rate = response["conversion_rate"]

    result = rate * data.amount

    history_collection.insert_one({
        "from": data.from_currency,
        "to": data.to_currency,
        "amount": data.amount,
        "rate": rate,
        "result": result
    })

    return {
        "rate": rate,
        "converted_amount": result
    }


@router.get("/history")
def get_history():
    """
    Returns previous conversions
    """

    data = []

    for item in history_collection.find({}, {"_id": 0}):
        data.append(item)

    return data