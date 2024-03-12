from flask_restful import Resource
from spreadsheet_golf_tour_be.domain.use_case.get_tournaments_use_case import GetTournamentsUseCase
from typing import Optional, Dict, Any


class TournamentsResource(Resource):
    def __init__(self) -> None:
        self.tournaments = GetTournamentsUseCase()

    def get(self) -> Optional[Dict[str, Any]]:
        return self.tournaments.display_data()
