"""Transaction repository module"""
from typing import Optional, Dict, Union, List, Any
from mongoengine import QuerySet, DoesNotExist
from bson import ObjectId

from app.infra.database.models.transaction import Transaction as TransactionModel
from app.domain.transaction.entity import TransactionInDB, TransactionInCreate, TransactionInUpdate
from app.domain.shared.enum import UserRole, Type
from app.shared.utils.general import date2datetime


class TransactionRepository:
    def __init__(self):
        pass

    def create(self, transaction: TransactionInCreate) -> TransactionInDB:
        """
        Create new transaction in db
        :param transaction:
        :return:
        """
        new_transaction = TransactionModel(**transaction.model_dump())
        # and save it to db
        new_transaction.save()

        return TransactionInDB.model_validate(new_transaction)

    def get_by_id(self, id: Union[str, ObjectId]) -> Optional[TransactionModel]:
        """
        Get category in db from id
        :param id:
        :return:
        """
        qs: QuerySet = TransactionModel.objects(id=id)
        # retrieve unique result
        # https://mongoengine-odm.readthedocs.io/guide/querying.html#retrieving-unique-results
        try:
            transaction: TransactionModel = qs.get()
            return transaction
        except DoesNotExist:
            return None

    def update(self, id: ObjectId, data: Union[TransactionInUpdate, Dict[str, Any]]) -> bool:
        try:
            data = data.model_dump(exclude_none=True) if isinstance(data, TransactionInUpdate) else data
            TransactionModel.objects(id=id).update_one(**data, upsert=False)
            return True
        except Exception:
            return False

    def delete(self, id: ObjectId) -> bool:
        try:
            TransactionModel.objects(id=id).delete()
            return True
        except Exception:
            return False

    def count(self, conditions: Dict[str, Union[str, bool, ObjectId]] = {}) -> int:
        try:
            return TransactionModel._get_collection().count_documents(conditions)
        except Exception:
            return 0

    def find(self, conditions: Dict[str, Union[str, bool, ObjectId]]) -> List[Optional[TransactionModel]]:
        try:
            docs = TransactionModel._get_collection().find(conditions)
            return [TransactionModel.from_mongo(doc) for doc in docs] if docs else []
        except Exception:
            return []
