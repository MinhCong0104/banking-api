from fastapi import APIRouter, Body, Depends, Path, Query, UploadFile, File
from typing import Annotated, Union, Dict, List
from app.domain.transaction.entity import Transaction, TransactionInCreate, TransactionInDB, TransactionInUpdate
from app.shared.decorator import response_decorator
from app.domain.shared.enum import UserRole, Type
from app.use_cases.transaction.create import CreateTransactionRequestObject, CreateTransactionUseCase


router = APIRouter()


# @router.get(
#     "/{transaction_id}",
#     dependencies=[Depends(get_current_active_user)],  # auth route
#     response_model=Transaction,
# )
# @response_decorator()
# def get_transaction(
#     transaction_id: str = Path(..., title="Transaction id"),
#     get_transaction_use_case: GetTransactionUseCase = Depends(GetTransactionUseCase),
# ):
#     req_object = GetTransactionRequestObject.builder(transaction_id=transaction_id)
#     response = get_transaction_use_case.execute(request_object=req_object)
#     return response


@router.post(
    "",
    response_model=Transaction,
)
@response_decorator()
def create_transaction(
    payload: TransactionInCreate = Body(..., title="TransactionInCreate payload"),
    # files: UploadFile = File(...),
    create_transaction_use_case: CreateTransactionUseCase = Depends(CreateTransactionUseCase),
):
    req_object = CreateTransactionRequestObject.builder(payload=payload)
    response = create_transaction_use_case.execute(request_object=req_object)
    return response


# @router.post(
#     "/upload",
#     response_model=Transaction,
# )
# @response_decorator()
# def create_transaction(
#     payload: TransactionInCreate = Body(..., title="TransactionInCreate payload"),
#     create_transaction_use_case: CreateTransactionUseCase = Depends(CreateTransactionUseCase),
# ):
#     req_object = CreateTransactionRequestObject.builder(payload=payload)
#     response = create_transaction_use_case.execute(request_object=req_object)
#     return response