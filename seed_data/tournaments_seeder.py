from seed_data.seeder import Seeder
from spreadsheet_golf_tour_be.models.tournaments import Tournaments
from datetime import datetime


class TournamentsSeeder(Seeder):
    @classmethod
    def setup_seed_data(cls):
        from database import db

        if db.session.query(Tournaments).first() is None:
            tournaments = [
                Tournaments(
                    source_id="011",
                    name="THE PLAYERS Championship",
                    year="2024",
                    golf_course="TPC Sawgrass (THE PLAYERS Stadium Course)",
                    location="FL, USA",
                    par="72",
                    start_date=datetime(2024, 3, 17, 0, 0, 0),
                    end_date=datetime(2024, 3, 20, 23, 59, 59),
                    week_number="10",
                    time_zone="America/New_York",
                    major_championship=False,
                ),
                Tournaments(
                    source_id="014",
                    name="The Masters Tournament",
                    year="2024",
                    golf_course="Augusta National Golf Club",
                    location="GA, USA",
                    par="72",
                    start_date=datetime(2024, 4, 6, 0, 0, 0),
                    end_date=datetime(2024, 4, 9, 23, 59, 59),
                    week_number="10",
                    time_zone="America/New_York",
                    major_championship=True,
                ),
            ]
            db.session.bulk_save_objects(tournaments)
