from database import db
from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, ForeignKey, Boolean, Integer


class MatchPicks(db.Model):
    __tablename__ = "match_picks"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("users.id"), nullable=False, index=True)
    tournament_id = Column(ForeignKey("tournaments.id"), nullable=False, index=True)
    golfer_id = Column(ForeignKey("golfers.id"), nullable=False, index=True)
    priority = Column(Integer, nullable=False)
    drafted = Column(Boolean, nullable=True, default=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
