from database import db
from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, ForeignKey, Integer


class Scores(db.Model):
    __tablename__ = "scores"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    match_picks_id = Column(ForeignKey("match_picks.id"), nullable=False, index=True)
    score = Column(Integer, nullable=True)
    round = Column(Integer, nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
