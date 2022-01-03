"""Define User."""

from pydantic import BaseModel, Field

from .general import CreatedAt

class UserId(int):
    """User id."""

    def __new__(cls, value: int):
        """new."""
        return int.__new__(cls, value)


class UserName(str):
    """User name."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class UserEmail(str):
    """User email."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class UserPassword(str):
    """User password."""

    def __new__(cls, value: str):
        """new."""
        return str.__new__(cls, value)

class UserRegister(BaseModel):
    """User class for registering."""
    username: UserName
    email: UserEmail
    password: UserPassword

class User(BaseModel):
    """User (ユーザー)."""

    id: UserId = Field(..., alias='id')
    username: UserName
    email: UserEmail
    password: UserPassword
    created_at: CreatedAt
