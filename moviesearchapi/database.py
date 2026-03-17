from pymongo import MongoClient

MONGO_URL = "mongodb+srv://YashFating:Yash%40123@completecoding0.2ectl0t.mongodb.net/hospital?retryWrites=true&w=majority&appName=CompleteCoding"

client = MongoClient(MONGO_URL)

db = client["hospital"]

search_collection = db["search_history"]