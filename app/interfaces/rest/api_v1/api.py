from fastapi import APIRouter
from app.interfaces.rest.api_v1.endpoints import transaction, gg_shet

api_router = APIRouter()
api_router.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])
api_router.include_router(gg_shet.router, prefix="/sheet", tags=["Sheet"])
