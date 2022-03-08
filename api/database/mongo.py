from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
url = f"mongodb+srv://{username}:{password}@databcn.ot3vw.mongodb.net/test"

db = MongoClient(url).get_database("databcn")


