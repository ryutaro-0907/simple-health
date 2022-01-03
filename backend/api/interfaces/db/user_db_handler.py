"""DB methods for User"""
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from ...entities.user import User, UserEmail, UserRegister, UserId, UserName, UserPassword
from ...entities.general import CreatedAt
from .db_models import UserModel


def get_all_user(db: Session) -> List[User]:
    db_users = db.query(UserModel).all()

    users = list(map(UserModel.to_model, db_users))
    return users


def get_user_by_id(db: Session, _id: UserId) -> User:
    user = db.query(UserModel).filter(UserModel.id == _id).first()
    return user.to_model()

def create_user(db: Session, request: UserRegister):
    """Create User."""
    user = UserModel(
        username=request.username,
        email=request.email,
        password=request.password,
        created_at=datetime.now()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.to_model()

