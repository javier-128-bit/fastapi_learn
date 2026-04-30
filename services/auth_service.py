import bcrypt
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from repositories.auth_repositories import (
    register_user,find_user_by_username
)

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
EXPIRE_MINUTES = int(os.getenv("EXPIRE_MINUTES"))
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)

    payload.update({
        "exp": expire
    })

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

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
    
    access_token = create_access_token({
        "sub": user["username"]
    })

    return {
        "message": "login berhasil",
        "user": user["username"],
        "access_token": access_token,
        "token_type": "bearer"
    }