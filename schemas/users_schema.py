
# returns a dictionary. Schema that handles a single user
def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "given_name": user["given_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "password": user["password"]
    }

# Schema that handles multiple users


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]
