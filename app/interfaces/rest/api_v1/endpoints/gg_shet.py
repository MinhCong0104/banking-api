import requests
import os
from fastapi import APIRouter, Body, Depends, Path, Query, UploadFile, File
from typing import Annotated, Union, Dict, List
from app.shared.decorator import response_decorator
from app.config import settings

import gspread


router = APIRouter()
""" Dữ liệu nhận được
{
    'address': 'BMC',
    'date': '28/03/2024',
    'name': ['Công', 'Phương', 'Phú'],
    'amount': 100.000,
}

Ví dụ cần đóng 120k mới đủ -> Notice: thiếu 20k
Chỉ cần đóng 80k -> Thêm 20k vào quỹ
"""

def write_value(spread_name, sheet_name):
    gc = gspread.service_account()

    # Open a sheet from a spreadsheet in one go
    wks = gc.open(spread_name).sheet1

    # Update a range of cells using the top left corner address
    wks.update([[1, 2], [3, 4]], "A1")

    # Or update a single cell
    wks.update_acell("B42", "it's down there somewhere, let me take another look.")


@router.get("")
@response_decorator()
def get_data(
    range: str = 'Tiền cầu sân cố định',
    date: str = None
):
    url = f"{settings.GG_SHEET_URL}/{settings.GG_SHEET_ID}/values/{range}?key={settings.GG_SHEET_API_KEY}"
    response = requests.get(url)
    for data in response.json()['values']:
        if data[2] == date:
            return data
    return {"Response": f"Not found data in {range} with date {date}"}


@router.put("")
@response_decorator()
def write_data(
    spread_name: str = 'Tiền cầu sân cố định',
    sheet_name: str = 'DashBoard'
):
    gc = gspread.service_account("app/infra/service/annular-form-362316-44f3fc4ff288.json")
    wks = gc.open(spread_name).worksheet(sheet_name)
    wks.update([["Tháng", "Tổng số thành viên"]], "E1")
    return {"Response": "OK"}
