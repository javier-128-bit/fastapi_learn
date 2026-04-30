from fastapi import APIRouter,Header,Depends,Query
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
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    data = get_transaction_service(token, tipe,page=page,
        limit=limit)

    return {
        "message": "berhasil diambil",
        "data": data
    }
