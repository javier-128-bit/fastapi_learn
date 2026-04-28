from fastapi import FastAPI

application=FastAPI()

@application.get("/transaction")
def get_transaction(tipe:str,amount:int):
    return f"tipe ini adalah {tipe} dan jumlahnya {amount}" 

#PATH
@application.get("/transaction/{tipe}")
def get_transaction(tipe):
    return f"Tipe ku adalah {tipe}"

