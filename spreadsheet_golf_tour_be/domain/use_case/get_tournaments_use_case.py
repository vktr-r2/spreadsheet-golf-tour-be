from spreadsheet_golf_tour_be.services.rapid_api_wrapper import RapidApiWrapperService
from spreadsheet_golf_tour_be.services.tournaments import TournamentsService
from spreadsheet_golf_tour_be.constants import PGA


class GetTournamentsUseCase:

    def __init__(self):
        self.rapid_api_wrapper = RapidApiWrapperService()
        self.tournaments_service = TournamentsService(
            api_wrapper=self.rapid_api_wrapper,
            org_id=PGA,
        )

    def display_data(self):
        return self.tournaments_service.fetch_tournaments()
