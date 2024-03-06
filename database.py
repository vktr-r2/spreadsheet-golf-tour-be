from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    from spreadsheet_golf_tour_be.models import users  # noqa
    from spreadsheet_golf_tour_be.models import golfers  # noqa
    from spreadsheet_golf_tour_be.models import tournaments  # noqa

    with app.app_context():
        db.create_all()


def seed_db(app):
    with app.app_context():
        from seed_data.users_seeder import UsersSeeder
        from seed_data.golfers_seeder import GolfersSeeder
        from seed_data.tournaments_seeder import TournamentsSeeder

        "Seeding the database..."
        UsersSeeder.seed_table()
        GolfersSeeder.seed_table()
        TournamentsSeeder.seed_table()
        print("Database seeding completed.")
