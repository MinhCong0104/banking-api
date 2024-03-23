from fastapi import APIRouter
from app.interfaces.rest.api_v1.endpoints import transaction

api_router = APIRouter()
api_router.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])
