from pydantic import BaseModel

class CreatedAt(str):
    """created at."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class DeletedAt(str):
    """delted at."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)