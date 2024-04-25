from typing import Optional
from fastapi import Depends, File, UploadFile
from app.shared import request_object, use_case

from app.domain.player.entity import PlayerBase, PlayerInDB, Player
from app.infra.transaction.transaction_repository import TransactionRepository


class CreatePlayerRequestObject(request_object.ValidRequestObject):
    def __init__(self, player_in: PlayerBase) -> None:
        self.player_in = player_in

    @classmethod
    def builder(cls, payload: Optional[PlayerBase] = None) -> request_object.RequestObject:
        invalid_req = request_object.InvalidRequestObject()
        if payload is None:
            invalid_req.add_error("payload", "Invalid payload")

        if invalid_req.has_errors():
            return invalid_req

        return CreatePlayerRequestObject(player_in=payload)


class CreatePlayerUseCase(use_case.UseCase):
    def __init__(self, player_repository: PlayerRepository = Depends(PlayerRepository)):
        self.player_repository = player_repository

    def process_request(self, req_object: CreatePlayerRequestObject):
        player_in: PlayerBase = req_object.player_in

        obj_in: PlayerBase = PlayerInDB(**player_in.model_dump())
        player_in_db: PlayerInDB = self.player_repository.create(player=obj_in)

        return Player(**player_in_db.model_dump())
