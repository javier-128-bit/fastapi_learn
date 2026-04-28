from fastapi import APIRouter
from typing import Optional
from schemas.transaction_schema import TransactionCreate, Tipe
from services.transaction_service import (
    insert_transaction_service,
    get_transaction_service
)

router = APIRouter(prefix="/transaction", tags=["Transaction"])

@router.post("/")
def create(data: TransactionCreate):
    insert_transaction_service(data.dict())
    return {"message": "berhasil ditambahkan"}

@router.get("/")
def get_all(tipe: Optional[Tipe] = None):
    data = get_transaction_service(tipe)
    return {
        "message": "berhasil diambil",
        "data": data
    }