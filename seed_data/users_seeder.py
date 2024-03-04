from seed_data.seeder import Seeder
from spreadsheet_golf_tour_be.models.users import Users
from uuid import uuid4
from datetime import datetime


class UsersSeeder(Seeder):
    @classmethod
    def setup_seed_data(cls):
        from database import db

        users = [
            Users(
                uuid=uuid4(),
                email="user1@example.com",
                username="user1",
                password="pw123",
                f_name="John",
                l_name="Daily",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            ),
            Users(
                uuid=uuid4(),
                email="user2@example.com",
                username="user2",
                password="pw123",
                f_name="Jane",
                l_name="Park",
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            ),
        ]
        db.session.bulk_save_objects(users)
