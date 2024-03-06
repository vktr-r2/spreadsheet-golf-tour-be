from database import db
from datetime import datetime
from sqlalchemy import Column, DateTime, String, BigInteger


class Golfers(db.Model):
    __tablename__ = "golfers"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    source_id = Column(String(10), nullable=False)
    f_name = Column(String(16), nullable=False)
    l_name = Column(String(16), nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
