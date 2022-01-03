"""Define Record."""

from pydantic import BaseModel, Field

from .user import UserId
from .general import CreatedAt


class RecordId(int):
    """Record id."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)
class Happiness(int):
    """Record happiness."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)

class Motivation(int):
    """Record motivation."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)

class Workout(str):
    """Record workout."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class Helped(str):
    """Record helped."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class Carories(int):
    """Record carories."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)

class Steps(int):
    """Record steps."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)

class Meditation(int):
    """Record meditation."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)

class Study(int):
    """Record study."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)

class Work(int):
    """Record work."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)

class CreateRecord(BaseModel):
    """Record class for post."""
    user_id: UserId

    created_at: CreatedAt

    happiness: Happiness
    motivation: Motivation
    workout: Workout
    helped: Helped
    carories: Carories
    steps: Steps
    meditation: Meditation
    study: Study
    work: Work

class Record(BaseModel):
    """Record"""
    record_id: RecordId = Field(..., alias='id')
    user_id: UserId

    created_at: CreatedAt

    happiness: Happiness
    motivation: Motivation
    workout: Workout
    helped: Helped
    carories: Carories
    steps: Steps
    meditation: Meditation
    study: Study
    work: Work

