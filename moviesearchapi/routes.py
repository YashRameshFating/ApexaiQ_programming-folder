from fastapi import APIRouter
import requests
from models import MovieSearch
from database import search_collection

router = APIRouter()

API_KEY = "d05c4501"

@router.post("/movies")
def search_movies(data: MovieSearch):

    title = data.title
    page = data.page
    year = data.year

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={title}&page={page}"

    if year:
        url += f"&y={year}"

    response = requests.get(url).json()

    if response.get("Response") == "False":
        return {"error": response.get("Error")}

    movies = response.get("Search", [])

    search_collection.insert_one({
        "title": title,
        "year": year,
        "page": page
    })

    return {
        "total_results": response.get("totalResults"),
        "movies": movies
    }