from datetime import datetime, date as Date
from typing import Optional, List, Union, Any
from pydantic import ConfigDict
from app.domain.shared.entity import BaseEntity, IDModelMixin, DateTimeModelMixin, Pagination
from app.domain.shared.enum import Type


class PlayerBase(BaseEntity):
    name: str
    gender: str
    credit: float


class PlayerInDB(IDModelMixin, DateTimeModelMixin, PlayerBase):
    # https://docs.pydantic.dev/2.4/concepts/models/#arbitrary-class-instances
    model_config = ConfigDict(from_attributes=True)


class PlayerInUpdateCredit(BaseEntity):
    name: str
    amount: float


class PlayerInCreate(BaseEntity):
    spread_name: Optional[str] = 'Vì một tương lai vui khỏe 2024'
    sheet_name: str
    date: Optional[str] = None
    range: Optional[str] = None
