from typing import Optional
from fastapi import Depends
from app.shared import request_object, use_case
from app.domain.shared.enum import GoogleSheetColor
from app.domain.google_sheet.entity import GoogleSheetInUpdate
from app.infra.service.google_service import gc
from app.domain.player.entity import PlayerInDB, Player
from app.infra.player.player_repository import PlayerRepository


fake_data = {
    "date": "28/03/2024",
    "name": "Công",
    "sheet_name": "Sân không cố định",
    "amount": 100000,
}


class UpdateGoogleSheetRequestObject(request_object.ValidRequestObject):
    def __init__(self, payload: GoogleSheetInUpdate) -> None:
        self.payload = payload

    @classmethod
    def builder(cls, payload: Optional[GoogleSheetInUpdate] = None) -> request_object.RequestObject:
        invalid_req = request_object.InvalidRequestObject()
        if payload is None:
            invalid_req.add_error("payload", "Invalid payload")

        if invalid_req.has_errors():
            return invalid_req

        return UpdateGoogleSheetRequestObject(payload=payload)


class UpdateGoogleSheetUseCase(use_case.UseCase):
    def __init__(self, player_repository: PlayerRepository = Depends(PlayerRepository)):
        self.player_repository = player_repository

    def process_request(self, req_object: UpdateGoogleSheetRequestObject):

        payload: GoogleSheetInUpdate = req_object.payload
        wks = gc.open(payload.spread_name).worksheet(payload.sheet_name)
        col = wks.findall(payload.name)[0].col if wks.findall(payload.name) else False
        row = wks.findall(payload.date)[0].row if wks.findall(payload.date) else False
        if not (col and row):
            return {"Error": "Can not find date or name in google sheet"}
        res = wks.format(wks.cell(row, col).address, {"backgroundColor": GoogleSheetColor.YELLOW})
        if not res:
            return {"Error": "Update google sheet failed"}

        player: PlayerInDB = self.player_repository.get_by_name(name=payload.name)
        player.credit += payload.amount
        self.player_repository.update(id=player.id, data=dict(credit=player.credit))
        player.reload()

        return Player(**PlayerInDB.model_validate(player).model_dump())
