from fastapi import APIRouter
import requests
from models import NewsArticle
from database import news_collection

router = APIRouter()

# Replace with your NewsAPI key
NEWS_API_KEY = "ee2bf3c2df0d4ae1a917a6ad82efd25a"


@router.get("/news")
def fetch_top_news():
    """
    Fetch top headlines from NewsAPI
    """

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

    response = requests.get(url).json()

    articles = []

    # Extract useful fields
    for item in response.get("articles", [])[:5]:
        article = {
            "title": item["title"],
            "source": item["source"]["name"],
            "url": item["url"]
        }

        articles.append(article)

        # Save to MongoDB if not already present
        if news_collection.find_one({"url": article["url"]}) is None:
            news_collection.insert_one(article)

    return {"articles": articles}


@router.get("/saved")
def get_saved_articles():
    """
    Return articles stored in MongoDB
    """

    articles = list(news_collection.find({}, {"_id": 0}))
    return {"saved_news": articles}