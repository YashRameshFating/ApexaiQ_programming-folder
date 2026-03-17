from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb+srv://YashFating:Yash%40123@completecoding0.2ectl0t.mongodb.net/hospital?retryWrites=true&w=majority&appName=CompleteCoding")

# Database name
db = client["hospital"]

# Collection to store articles
news_collection = db["articles"]