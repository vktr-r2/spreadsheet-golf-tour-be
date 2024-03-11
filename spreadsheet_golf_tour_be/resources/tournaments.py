from flask_restful import Resource
from spreadsheet_golf_tour_be.domain.use_case.get_tournaments_use_case import GetTournamentsUseCase


class TournamentsResource(Resource):
    def __init__(self):
        self.tournaments = GetTournamentsUseCase()

    def get(self):
        return self.tournaments.display_data()
