from repositories.transaction_repositories import (
    create_transaction,
    get_transactions
)
from fastapi import HTTPException
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token tidak valid"
        )

def insert_transaction_service(data,token):
    verify_token(token)
    return create_transaction(data)

def get_transaction_service(token,tipe=None,page=1, limit=10):
    verify_token(token)
    query = {}

    if tipe:
        query["tipe"] = tipe

    skip = (page - 1) * limit

    data = get_transactions(
        filter_query=query,
        skip=skip,
        limit=limit
    )


    for item in data:
        item["_id"] = str(item["_id"])

    return {
        "page": page,
        "limit": limit,
        "data": data
    }