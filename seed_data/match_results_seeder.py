from seed_data.seeder import Seeder
from spreadsheet_golf_tour_be.models.match_results import MatchResults


class MatchResultsSeeder(Seeder):
    @classmethod
    def setup_seed_data(cls):
        from database import db

        if db.session.query(MatchResults).first() is None:
            match_results = [
                MatchResults(
                    tournament_id=1,
                    user_id=1,
                    total_score=567,
                    place=1,
                    winner_picked=True,
                ),
                MatchResults(
                    tournament_id=1,
                    user_id=2,
                    total_score=567,
                    place=2,
                    winner_picked=False,
                ),
                MatchResults(
                    tournament_id=1,
                    user_id=3,
                    total_score=567,
                    place=3,
                    winner_picked=False,
                    cuts_missed=1,
                ),
                MatchResults(
                    tournament_id=1,
                    user_id=4,
                    total_score=567,
                    place=4,
                    winner_picked=False,
                    cuts_missed=2,
                ),
            ]
            db.session.bulk_save_objects(match_results)
