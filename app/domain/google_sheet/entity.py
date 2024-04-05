from datetime import datetime, date as Date
from typing import Optional, List, Union, Any
from pydantic import ConfigDict
from app.domain.shared.entity import BaseEntity, IDModelMixin, DateTimeModelMixin, Pagination
from app.domain.shared.enum import Type


# class TransactionBase(BaseEntity):
#     # date: Union[datetime, Date]
#     note: Optional[str] = None
#     file: UploadFile = File(...)
#
#
# class TransactionInDB(IDModelMixin, DateTimeModelMixin, TransactionBase):
#     # https://docs.pydantic.dev/2.4/concepts/models/#arbitrary-class-instances
#     model_config = ConfigDict(from_attributes=True)


class GoogleSheetInUpdate(BaseEntity):
    spread_name: Optional[str] = 'Vì một tương lai vui khỏe 2024'
    date: str
    sheet_name: str
    name: str
    amount: float


class GoogleSheetInUpdateOld(BaseEntity):
    spread_name: Optional[str] = 'Vì một tương lai vui khỏe 2024'
    sheet_name: str
    data: List[List[Any]]
    cell: str


class GoogleSheetInRetrieve(BaseEntity):
    spread_name: Optional[str] = 'Vì một tương lai vui khỏe 2024'
    sheet_name: str
    date: Optional[str] = None
    range: Optional[str] = None

#
# class TransactionInUpdate(BaseEntity):
#     date: Optional[Union[datetime, Date]]
#     note: Optional[str] = None
#
#
# class Transaction(TransactionBase):
#     """
#     Transaction domain entity
#     """
#
#     id: str
