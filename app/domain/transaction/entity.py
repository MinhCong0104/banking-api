from datetime import datetime, date as Date
from typing import Optional, List, Union, Any
from pydantic import ConfigDict
from app.domain.shared.entity import BaseEntity, IDModelMixin, DateTimeModelMixin, Pagination
from app.domain.shared.enum import Type


class TransactionBase(BaseEntity):
    # date: Union[datetime, Date]
    note: Optional[str] = None
    file: Any


class TransactionInDB(IDModelMixin, DateTimeModelMixin, TransactionBase):
    # https://docs.pydantic.dev/2.4/concepts/models/#arbitrary-class-instances
    model_config = ConfigDict(from_attributes=True)


class TransactionInCreate(BaseEntity):
    note: Optional[str] = None
    # date: str


class TransactionInUpdate(BaseEntity):
    date: Optional[Union[datetime, Date]]
    note: Optional[str] = None


class Transaction(TransactionBase):
    """
    Transaction domain entity
    """

    id: str
