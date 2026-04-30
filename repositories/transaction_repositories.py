from core.config import transaction_collection

def create_transaction(data):
    return transaction_collection.insert_one(data)

def get_transactions(filter_query,skip=0,limit=10):
    return list(transaction_collection.find(filter_query).skip(skip)
        .limit(limit))

