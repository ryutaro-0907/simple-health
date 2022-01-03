"""entities."""
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from ...entities.user import User, UserEmail, UserName, UserPassword, UserId
from ...entities.record import (Record, RecordId, Happiness, Motivation, Workout, Helped, Carories, Steps, Meditation, Study, Work)
from ...entities.general import CreatedAt


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
                    email=UserEmail(self.email), password=UserPassword(self.password),
                    created_at=CreatedAt(self.created_at))


class RecordModel(Base):
    """Record Model."""

    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())

    happiness = Column(Integer, nullable=False)
    motivation = Column(Integer, nullable=False)
    workout = Column(String, nullable=False)
    helped = Column(String, nullable=False)
    carories = Column(Integer, nullable=False)
    steps = Column(Integer, nullable=False)
    meditation = Column(Integer, nullable=False)
    study = Column(Integer, nullable=False)
    work = Column(Integer, nullable=False)

    def to_model(self) -> Record:
        """To Model."""
        return Record(id=RecordId(self.id), user_id=UserId(self.user_id),
            created_at=CreatedAt(self.created_at), happiness=Happiness(self.happiness), motivation=Motivation(self.motivation),
            workout=Workout(self.workout), helped=Helped(self.helped),carories=Carories(self.carories), steps=Steps(self.steps),
            meditation=Meditation(self.meditation), study=Study(self.study), work=Work(self.work))
