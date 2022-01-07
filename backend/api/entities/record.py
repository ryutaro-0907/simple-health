"""Define Record."""

from pydantic import BaseModel, Field

from .user import UserId
from .general import CreatedAt


class RecordId(str):
    """Record id."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)
class Happiness(str):
    """Record happiness."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class Motivation(str):
    """Record motivation."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

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

class Carories(str):
    """Record carories."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class Steps(str):
    """Record steps."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class Meditation(str):
    """Record meditation."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class Study(str):
    """Record study."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class Work(str):
    """Record work."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

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

