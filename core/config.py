import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("CLIENT_MONGO")

client = pymongo.MongoClient(MONGO_URL)
db = client["learning_fastapi"]
transaction_collection = db["transaction"]