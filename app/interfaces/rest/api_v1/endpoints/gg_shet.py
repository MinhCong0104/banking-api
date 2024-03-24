from fastapi import APIRouter, Body, Depends, Path, Query, UploadFile, File
from typing import Annotated, Union, Dict, List
from app.shared.decorator import response_decorator



router = APIRouter()


@router.get(
    "",
    # response_model=Transaction,
)
@response_decorator()
def get_data():
    return {"result": "OK"}
