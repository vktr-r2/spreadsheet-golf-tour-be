from database import db
from datetime import datetime
from sqlalchemy import Column, DateTime, String, BigInteger
from sqlalchemy_utils import UUIDType
import uuid


class Users(db.Model):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(UUIDType(binary=False), default=uuid.uuid4)
    email = Column(String(40), nullable=False)
    username = Column(String(16), nullable=False)
    password = Column(String(255), nullable=False)
    f_name = Column(String(16), nullable=False)
    l_name = Column(String(16), nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
