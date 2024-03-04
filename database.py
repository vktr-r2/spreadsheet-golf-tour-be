from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    from spreadsheet_golf_tour_be.models import users  # noqa

    with app.app_context():
        db.create_all()


def seed_db(app):
    with app.app_context():
        from seed_data.users_seeder import UsersSeeder

        "Seeding the database..."
        UsersSeeder.seed_table()
        print("Database seeding completed.")
