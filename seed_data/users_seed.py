from database import db
from spreadsheet_golf_tour_be.models.users import Users
from sqlalchemy.exc import IntegrityError
from uuid import uuid4
from datetime import datetime

seed_users = [
    {
        "uuid": uuid4(),
        "email": "user1@example.com",
        "username": "user1",
        "password": "password123",
        "f_name": "John",
        "l_name": "Doe",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    },
    {
        "uuid": uuid4(),
        "email": "user2@example.com",
        "username": "user2",
        "password": "password123",
        "f_name": "Jane",
        "l_name": "Doe",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    },
]

for user_data in seed_users:
    user = Users(**user_data)
    db.session.add(user)

try:
    db.session.commit()
except IntegrityError:
    db.session.rollback()
    print("An error occurred, and the DB transaction was rolled back")
