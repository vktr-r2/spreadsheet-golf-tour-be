from seed_data.seeder import Seeder
from spreadsheet_golf_tour_be.models.golfers import Golfers
from datetime import datetime


class GolfersSeeder(Seeder):
    @classmethod
    def setup_seed_data(cls):
        from database import db

        if db.session.query(Golfers).first() is None:
            golfers = [
                Golfers(
                    source_id="1000",
                    f_name="Tiger",
                    l_name="Woods",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1001",
                    f_name="Rory",
                    l_name="McIlroy",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1002",
                    f_name="Scottie",
                    l_name="Scheffler",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1003",
                    f_name="Xander",
                    l_name="Schauffle",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1004",
                    f_name="Viktor",
                    l_name="Hovland",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1005",
                    f_name="Sungjae",
                    l_name="Im",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1006",
                    f_name="Sahith",
                    l_name="Thegala",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1007",
                    f_name="Hideki",
                    l_name="Matsuyama",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1008",
                    f_name="Jordan",
                    l_name="Speith",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1009",
                    f_name="Justin",
                    l_name="Thomas",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
                Golfers(
                    source_id="1010",
                    f_name="Max",
                    l_name="Homa",
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                ),
            ]
            db.session.bulk_save_objects(golfers)
