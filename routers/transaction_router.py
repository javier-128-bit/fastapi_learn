from fastapi import APIRouter,Header, HTTPException,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from schemas.transaction_schema import TransactionCreate, Tipe
from services.transaction_service import (
    insert_transaction_service,
    get_transaction_service,
  
)

routerTransaction = APIRouter(prefix="/transaction", tags=["Transaction"])

security = HTTPBearer()


@routerTransaction.post("/")
def create(data: TransactionCreate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    insert_transaction_service(data.dict(),token)
    return {"message": "berhasil ditambahkan"}

@routerTransaction.get("/")
def get_all(
    tipe: Optional[Tipe] = None,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    data = get_transaction_service(token, tipe)

    return {
        "message": "berhasil diambil",
        "data": data
    }
