from sqlalchemy.exc import IntegrityError


class Seeder:
    @classmethod
    def seed_table(cls):

        from database import db

        try:
            cls.setup_seed_data()
            db.session.commit()
            print(f"{cls.__name__} ran successfully")
        except IntegrityError:
            db.session.rollback()
            print(f"An error occurred with {cls.__name__}, transaction was rolled back")

    @classmethod
    def setup_seed_data(cls):
        raise NotImplementedError("The setup_seed_data method must be implemented by subclasses.")
