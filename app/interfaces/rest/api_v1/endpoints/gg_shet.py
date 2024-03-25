import requests
from fastapi import APIRouter, Body, Depends, Path, Query, UploadFile, File
from typing import Annotated, Union, Dict, List
from app.shared.decorator import response_decorator
from app.config import settings


router = APIRouter()


@router.get(
    "",
    # response_model=Transaction,
)
@response_decorator()
def get_data(range = 'Tiền cầu sân cố định'):

    url = f"{settings.GG_SHEET_URL}/{settings.GG_SHEET_ID}/values/{range}?key={settings.GG_SHEET_API_KEY}"
    response = requests.get(url)
    return response.json()
