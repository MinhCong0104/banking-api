from typing import Optional
from app.shared import request_object, use_case
from app.domain.google_sheet.entity import GoogleSheetInUpdate, GoogleSheetInRetrieve
from app.infra.service.google_service import gc

class GetGoogleSheetRequestObject(request_object.ValidRequestObject):
    def __init__(self, payload: GoogleSheetInRetrieve) -> None:
        self.payload = payload

    @classmethod
    def builder(cls, payload: Optional[GoogleSheetInRetrieve] = None) -> request_object.RequestObject:
        invalid_req = request_object.InvalidRequestObject()
        if payload is None:
            invalid_req.add_error("payload", "Invalid payload")

        if invalid_req.has_errors():
            return invalid_req

        return GetGoogleSheetRequestObject(payload=payload)


class GetGoogleSheetUseCase(use_case.UseCase):
    def __init__(self):
        pass

    def process_request(self, req_object: GetGoogleSheetRequestObject):
        payload: GoogleSheetInRetrieve = req_object.payload

        wks = gc.open(payload.spread_name).worksheet(payload.sheet_name)
        res = wks.get_all_values()

        return res
