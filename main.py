from fastapi import FastAPI
from routers.transaction_router import router

application = FastAPI()
application.include_router(router)