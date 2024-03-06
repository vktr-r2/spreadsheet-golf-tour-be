from database import db
from datetime import datetime
from sqlalchemy import Column, DateTime, String, BigInteger, Integer, Boolean


class Tournaments(db.Model):
    __tablename__ = "tournaments"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    source_id = Column(String(10), nullable=False)
    name = Column(String(100), nullable=False)
    year = Column(String(4), nullable=False)
    golf_course = Column(String(100), nullable=False)
    location = Column(String(255), nullable=False)
    par = Column(Integer, nullable=True)
    start_date = Column(DateTime(), nullable=False)
    end_date = Column(DateTime(), nullable=False)
    week_number = Column(String(3), nullable=False)
    time_zone = Column(String(20), nullable=True)
    major_championship = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
