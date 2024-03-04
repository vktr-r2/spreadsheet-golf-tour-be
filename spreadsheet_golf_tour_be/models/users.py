from database import db
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy_utils import UUIDType
import uuid


class Users(db.Model):
    __tablename__ = "users"

    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    email = Column(String(40), collation="utf8mb4_unicode_ci", nullable=False)
    username = Column(String(16), collation="utf8mb4_unicode_ci", nullable=False)
    password = Column(String(255), collation="utf8mb4_unicode_ci", nullable=False)
    f_name = Column(String(16), collation="utf8mb4_unicode_ci", nullable=False)
    l_name = Column(String(16), collation="utf8mb4_unicode_ci", nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = Column(
        DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
