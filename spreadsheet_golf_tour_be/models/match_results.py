from database import db
from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, ForeignKey, Integer, Boolean


class MatchResults(db.Model):
    __tablename__ = "match_results"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tournament_id = Column(ForeignKey("tournaments.id"), nullable=False, index=True)
    user_id = Column(ForeignKey("users.id"), nullable=False, index=True)
    total_score = Column(Integer, nullable=False)
    place = Column(Integer, nullable=False)
    winner_picked = Column(Boolean, nullable=False, default=False)
    cuts_missed = Column(Integer, nullable=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
