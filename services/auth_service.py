import bcrypt

from repositories.auth_repositories import (
    register_user,find_user_by_username
)

def register_user_service(data):
   hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt()).decode()
   data["password"]=hashed
   return register_user(data)


def login_user_service(data):
    
    user = find_user_by_username(data["username"])

    if not user:
        return {"message": "user tidak ditemukan"}

    is_valid = bcrypt.checkpw(
        data["password"].encode(),
        user["password"].encode()
    )

    if not is_valid:
        return {"message": "password salah"}

    return {
        "message": "login berhasil",
        "user": user["username"]
    }