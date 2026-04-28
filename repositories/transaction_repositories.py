from core.config import transaction_collection

def create_transaction(data):
    return transaction_collection.insert_one(data)

def get_transactions(filter_query):
    return list(transaction_collection.find(filter_query))

