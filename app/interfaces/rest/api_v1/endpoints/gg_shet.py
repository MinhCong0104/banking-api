import requests
from fastapi import APIRouter, Body, Depends, Path, Query, UploadFile, File
from typing import Annotated, Union, Dict, List
from app.shared.decorator import response_decorator
from app.config import settings
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



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

def batch_update_values(
    spreadsheet_id, range_name, value_input_option, _values
):
  """
  Creates the batch_update the user has access to.
  Load pre-authorized user credentials from the environment.
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()
  # pylint: disable=maybe-no-member
  try:
    service = build("sheets", "v4", credentials=creds)

    values = [
        [],
    ]
    data = [
        {"range": range_name, "values": values},
    ]
    body = {"valueInputOption": value_input_option, "data": data}
    result = (
        service.spreadsheets()
        .values()
        .batchUpdate(spreadsheetId=spreadsheet_id, body=body)
        .execute()
    )
    print(f"{(result.get('totalUpdatedCells'))} cells updated.")
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error


# if __name__ == "__main__":
#   # Pass: spreadsheet_id, range_name value_input_option and _values)
#   batch_update_values(
#       "1CM29gwKIzeXsAppeNwrc8lbYaVMmUclprLuLYuHog4k",
#       "A1:C2",
#       "USER_ENTERED",
#       [["F", "B"], ["C", "D"]],
#   )


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
    range: str = 'Tiền cầu sân cố định',
    name: List[str] = []
):
    url = f"{settings.GG_SHEET_URL}/{settings.GG_SHEET_ID}/values/{range}?key={settings.GG_SHEET_API_KEY}"
    data = {
        "range": f"{range}!L3:N3",
        "majorDimension": "ROWS",
        "values": [
            ["TRUE"], ["FALSE"], ["TRUE"],
        ],
    }
    response = requests.put(url, json=data)
    return response.status_code



    # batch_update_values(
    #     settings.GG_SHEET_ID,
    #     f"{range}!L3:N3",
    #     "USER_ENTERED",
    #     [["True"], ["FALSE"], ["True"]],
    # )
    # return {"Response": "OK"}
