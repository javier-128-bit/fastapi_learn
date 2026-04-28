from repositories.transaction_repositories import (
    create_transaction,
    get_transactions
)

def insert_transaction_service(data):
    return create_transaction(data)

def get_transaction_service(tipe=None):
    query = {}

    if tipe:
        query["tipe"] = tipe

    data = get_transactions(query)

    for item in data:
        item["_id"] = str(item["_id"])

    return data