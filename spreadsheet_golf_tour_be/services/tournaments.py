from typing import Optional, Dict, Any
from spreadsheet_golf_tour_be.services.rapid_api_wrapper import RapidApiWrapperService


class TournamentsService:

    def __init__(self, api_wrapper: RapidApiWrapperService, org_id: str) -> None:
        self.api_wrapper = api_wrapper
        self.org_id = org_id

    def fetch_tournaments(self) -> Optional[Dict[str, Any]]:
        try:
            tournaments = self.api_wrapper.call_schedule_endpoint(self.org_id)
            return tournaments
        except Exception as e:
            raise e
