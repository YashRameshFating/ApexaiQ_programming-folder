from pymongo import MongoClient

# connect to local MongoDB
client = MongoClient("mongodb+srv://YashFating:Yash%40123@completecoding0.2ectl0t.mongodb.net/hospital?retryWrites=true&w=majority&appName=CompleteCoding")

# create database
db = client["hospital"]

# create collection
history_collection = db["conversion_history"]