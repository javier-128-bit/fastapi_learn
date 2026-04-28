from core.config import user_collection

def register_user(data):
    return user_collection.insert_one(data)

def find_user_by_username(username):
    return user_collection.find_one({"username": username})