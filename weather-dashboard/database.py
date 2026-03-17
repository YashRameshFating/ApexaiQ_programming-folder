from pymongo import MongoClient

# MongoDB Atlas connection string
MONGO_URL = "mongodb+srv://YashFating:Yash%40123@completecoding0.2ectl0t.mongodb.net/hospital?retryWrites=true&w=majority&appName=CompleteCoding"

# Connect to database
client = MongoClient(MONGO_URL)

# Select database
db = client["hospital"]

# Collection for caching weather data
weather_collection = db["weather_cache"]