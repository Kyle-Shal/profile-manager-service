from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv()
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASS")


# connecting to the MongoDB server using password
# TODO: change password location to a secret file

client = MongoClient(
    f"mongodb+srv://profile-manager:{MONGO_DB_PASSWORD}@cluster0.4yzae95.mongodb.net/?retryWrites=true&w=majority")

db = client.users_app

# Creating a collection of users
collection_name = db["users_app"]
