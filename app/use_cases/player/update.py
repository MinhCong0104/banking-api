from typing import Optional
from fastapi import Depends
from app.shared import request_object, use_case

from app.domain.player.entity import PlayerInDB, Player, PlayerInUpdateCredit
from app.infra.player.player_repository import PlayerRepository


class UpdatePlayerRequestObject(request_object.ValidRequestObject):
    def __init__(self, player_in: PlayerInUpdateCredit) -> None:
        self.player_in = player_in

    @classmethod
    def builder(cls, payload: Optional[PlayerInUpdateCredit] = None) -> request_object.RequestObject:
        invalid_req = request_object.InvalidRequestObject()
        if payload is None:
            invalid_req.add_error("payload", "Invalid payload")

        if invalid_req.has_errors():
            return invalid_req

        return UpdatePlayerRequestObject(player_in=payload)


class UpdatePlayerCreditUseCase(use_case.UseCase):
    def __init__(self, player_repository: PlayerRepository = Depends(PlayerRepository)):
        self.player_repository = player_repository

    def process_request(self, req_object: UpdatePlayerRequestObject):
        player_in: PlayerInUpdateCredit = req_object.player_in

        player: PlayerInDB = self.player_repository.get_by_name(name=player_in.name)
        player.credit += player_in.amount
        self.player_repository.update(id=player.id, data=dict(credit=player.credit))
        player.reload()

        return Player(**PlayerInDB.model_validate(player).model_dump())
