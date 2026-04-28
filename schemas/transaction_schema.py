from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Tipe(str, Enum):
    INCOME = "INCOME"
    PURCHASE = "PURCHASE"
    INVEST = "INVEST"

class Method(str, Enum):
    BANK = "BANK"
    CASH = "CASH"
    QRIS = "QRIS"

class TransactionCreate(BaseModel):
    tipe: Tipe
    amount: int
    notes: Optional[str] = None
    method: Method

