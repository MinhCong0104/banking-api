import requests
import os
import gspread
from fastapi import APIRouter, Body, Depends, Path, Query, UploadFile, File
from typing import Annotated, Union, Dict, List

from app.shared.decorator import response_decorator
from app.config import settings
from app.infra.service.google_service import gc
from app.domain.google_sheet.entity import GoogleSheetInRetrieve, GoogleSheetInUpdate
from app.use_cases.google_sheet.update import UpdateGoogleSheetRequestObject, UpdateGoogleSheetUseCase
from app.use_cases.google_sheet.get import GetGoogleSheetRequestObject, GetGoogleSheetUseCase


router = APIRouter()
""" Dữ liệu nhận được
{
    'date': '28/03/2024',
    'name': 'Công',
    'sheet': 'Sân không cố định',
    'amount': 100.000,
}
=> Cập nhật tích đã đóng tiền, cập nhật credit của player
Ví dụ cần đóng 120k mới đủ -> Notice: thiếu 20k
Chỉ cần đóng 80k -> Thêm 20k vào quỹ
"""


fake_data = {
    'name': 'Công',
    'amount': 50000,
}


@router.get("")
@response_decorator()
def get_data(
    payload: GoogleSheetInRetrieve = Body(..., title="Update Sheet payload"),
    get_google_sheet_use_case: GetGoogleSheetUseCase = Depends(GetGoogleSheetUseCase),
):
    req_object = GetGoogleSheetRequestObject.builder(payload=payload)
    response = get_google_sheet_use_case.execute(request_object=req_object)
    return response


@router.put("")
@response_decorator()
def write_data(
    payload: GoogleSheetInUpdate = Body(..., title="Update Sheet payload"),
    update_google_sheet_use_case: UpdateGoogleSheetUseCase = Depends(UpdateGoogleSheetUseCase),
):
    req_object = UpdateGoogleSheetRequestObject.builder(payload=payload)
    response = update_google_sheet_use_case.execute(request_object=req_object)
    return requests.put("/players", json=fake_data)
