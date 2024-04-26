"""Player repository module"""
from typing import Optional, Dict, Union, List, Any
from mongoengine import QuerySet, DoesNotExist
from bson import ObjectId

from app.infra.database.models.player import Player as PlayerModel
from app.domain.player.entity import PlayerInDB, PlayerBase, PlayerInUpdateCredit
from app.domain.shared.enum import UserRole, Type
from app.shared.utils.general import date2datetime


class PlayerRepository:
    def __init__(self):
        pass

    def create(self, player: PlayerBase) -> PlayerInDB:
        """
        Create new player in db
        :param player:
        :return:
        """
        new_player = PlayerModel(**player.model_dump())
        # and save it to db
        new_player.save()

        return PlayerInDB.model_validate(new_player)

    def get_by_id(self, id: Union[str, ObjectId]) -> Optional[PlayerModel]:
        """
        Get category in db from id
        :param id:
        :return:
        """
        qs: QuerySet = PlayerModel.objects(id=id)
        # retrieve unique result
        # https://mongoengine-odm.readthedocs.io/guide/querying.html#retrieving-unique-results
        try:
            player: PlayerModel = qs.get()
            return player
        except DoesNotExist:
            return None

    def get_by_name(self, name: Union[str]) -> Optional[PlayerModel]:
        """
        Get category in db from id
        :param name:
        :return:
        """
        qs: QuerySet = PlayerModel.objects(name=name)
        # retrieve unique result
        # https://mongoengine-odm.readthedocs.io/guide/querying.html#retrieving-unique-results
        try:
            player: PlayerModel = qs.get()
            return player
        except DoesNotExist:
            return None

    # def update(self, id: ObjectId, data: Union[TransactionInUpdate, Dict[str, Any]]) -> bool:
    #     try:
    #         data = data.model_dump(exclude_none=True) if isinstance(data, TransactionInUpdate) else data
    #         PlayerModel.objects(id=id).update_one(**data, upsert=False)
    #         return True
    #     except Exception:
    #         return False

    def delete(self, id: ObjectId) -> bool:
        try:
            PlayerModel.objects(id=id).delete()
            return True
        except Exception:
            return False

    def count(self, conditions: Dict[str, Union[str, bool, ObjectId]] = {}) -> int:
        try:
            return PlayerModel._get_collection().count_documents(conditions)
        except Exception:
            return 0

    def find(self, conditions: Dict[str, Union[str, bool, ObjectId]]) -> List[Optional[PlayerModel]]:
        try:
            docs = PlayerModel._get_collection().find(conditions)
            return [PlayerModel.from_mongo(doc) for doc in docs] if docs else []
        except Exception:
            return []
