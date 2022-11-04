from fastapi import APIRouter
from config.database import collection_name
from models.users_model import User
from schemas.users_schema import users_serializer
from bson import ObjectId

# create a basic API Route object
user_api_router = APIRouter()

# Functionality


@user_api_router.get("/")
# returning all users from the database collection in a dictionary
async def get_users():
    # Serialize before sending to frontend
    users = users_serializer(collection_name.find())
    return {"status": "ok", "data": users}


@user_api_router.get("/{id}")
# gets a user from the collection by id
async def get_user(id: str):
    # Serialize before sending to frontend
    user = users_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": user}


@user_api_router.post("/")
# inserts a new user into the database and returns the user that was inserted
# data will be taken from the frontend
async def create_user(user: User):
    # get data from database
    _id = collection_name.insert_one(dict(user))
    # Serialize before sending to frontend
    user = users_serializer(collection_name.find({"_id": _id.inserted_id}))

    return {"status": "ok", "data": user}


@user_api_router.put("/{id}")
# updates the information for an existing user in the database
async def update_user(id: str, user: User):
    # converts data from the frontend into a dictionary
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    # gets user with updated information.
    # Serialize before sending to frontend
    user = users_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": user}


@user_api_router.delete("/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete(
        {"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
