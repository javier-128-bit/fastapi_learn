from fastapi import APIRouter
from schemas.auth_schema import Register,Login
from services.auth_service import (
    register_user_service,login_user_service
)

routerAuth=APIRouter(prefix="/user",tags=["User"])

@routerAuth.post("/register")
def register(data:Register):
    register_user_service(data.dict())
    return {"message": "berhasil register"}

@routerAuth.post("/login")
def login (data:Login):
    return login_user_service(data.dict())
    