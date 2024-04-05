import requests
import os
import gspread
from fastapi import APIRouter, Body, Depends, Path, Query, UploadFile, File
from typing import Annotated, Union, Dict, List

from app.shared.decorator import response_decorator
from app.config import settings
from app.infra.service.google_service import gc
from app.domain.google_sheet.entity import GoogleSheetInUpdateOld, GoogleSheetInRetrieve, GoogleSheetInUpdate
from app.use_cases.google_sheet.update import UpdateGoogleSheetRequestObject, UpdateGoogleSheetUseCase
from app.use_cases.google_sheet.get import GetGoogleSheetRequestObject, GetGoogleSheetUseCase


router = APIRouter()
""" Dữ liệu nhận được
{
    'name': 'Công',
    'amount': 100.000,
}
"""


# @router.get("")
# @response_decorator()
# def get_data(
#     payload: GoogleSheetInRetrieve = Body(..., title="Update Sheet payload"),
#     get_google_sheet_use_case: GetGoogleSheetUseCase = Depends(GetGoogleSheetUseCase),
# ):
#     req_object = GetGoogleSheetRequestObject.builder(payload=payload)
#     response = get_google_sheet_use_case.execute(request_object=req_object)
#     return response


@router.put("")
@response_decorator()
def update_credit(
    payload: PlayerInUpdate = Body(..., title="Update Sheet payload"),
    update_player_use_case: UpdatePlayerUseCase = Depends(UpdatePlayerUseCase),
):
    req_object = UpdatePlayerRequestObject.builder(payload=payload)
    response = update_player_use_case.execute(request_object=req_object)
    return response