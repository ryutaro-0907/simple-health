"""entities."""
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from ..entities.user import UserId, UserName, UserEmail, UserPassword, User
from ..entities.general import CreatedAt

# from ..entities.record import

Base = declarative_base()


class UserModel(Base):
    """User Model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    created_at = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())

    def to_model(self) -> User:
        """To Model."""
        return User(id=UserId(self.id), username=UserName(self.username),
                    email=UserEmail(self.username), password=UserPassword(self.password),
                    created_at=CreatedAt(self.created_at))
