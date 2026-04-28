from fastapi import FastAPI
from routers.transaction_router import routerTransaction
from routers.auth_router import routerAuth

application = FastAPI()
application.include_router(routerTransaction)
application.include_router(routerAuth)