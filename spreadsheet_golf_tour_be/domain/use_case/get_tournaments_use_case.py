from spreadsheet_golf_tour_be.services.rapid_api_wrapper import RapidApiWrapperService
from spreadsheet_golf_tour_be.services.tournaments import TournamentsService
from spreadsheet_golf_tour_be.constants import PGA
from typing import Optional, Dict, Any


class GetTournamentsUseCase:

    def __init__(self) -> None:
        self.rapid_api_wrapper = RapidApiWrapperService()
        self.tournaments_service = TournamentsService(
            api_wrapper=self.rapid_api_wrapper,
            org_id=PGA,
        )

    def display_data(self) -> Optional[Dict[str, Any]]:
        return self.tournaments_service.fetch_tournaments()
