from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import Optional

application = FastAPI()

data_transaction = []

class Tipe(str, Enum):
    INCOME = "INCOME"
    PURCHASE = "PURCHASE"
    INVEST = "INVEST"

class Method(str, Enum):
    BANK = "BANK"
    CASH = "CASH"
    QRIS = "QRIS"

class InputType(BaseModel):
    tipe: Tipe
    amount: int
    notes: Optional[str] = None
    method: Method

# Query Parameter
@application.get("/transaction")
def get_transaction(tipe: str, amount: int):
    return {
        "tipe": tipe,
        "amount": amount
    }

# Path Parameter
@application.get("/transaction/{tipe}")
def get_tipe(tipe: str):
    return {
        "tipe": tipe
    }

# POST
@application.post("/transaction")
def insert_transaction(data: InputType):
    data_transaction.append(data.dict())
    return {
        "message": "berhasil ditambahkan",
        "data": data
    }