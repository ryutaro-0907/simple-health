"""User Services."""
from typing import List

from sqlalchemy.orm import Session

from ..entities.user import User, UserId, UserRegister
from ..interfaces import user_db_handler

def register_user(db: Session, request: UserRegister):
    return user_db_handler.create_user(
        db=db, request=request)

def get_all_user(db:Session) -> List[User]:
	return user_db_handler.get_all_user(db)

def get_user_by_userid(db: Session, _id: UserId) -> User:
    return user_db_handler.get_user_by_id(db=db, _id=_id)








