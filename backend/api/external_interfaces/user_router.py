"""Define routers for User."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..use_cases import user_services
from ..entities.user import User, UserId, UserRegister
from ..interfaces.database import get_db

router = APIRouter()

@router.post("/users", response_model=User)
def create_user(request: UserRegister, db: Session = Depends(get_db)):
    return user_services.register_user(
        db=db, request=request)


@router.get("/users", response_model=List[User])
def get_all_users(db: Session = Depends(get_db)):
    users: List[User] = \
        user_services.get_all_user(db=db)
    if users is None:
        raise HTTPException(status_code=404, detail="Users not found")

    return users


@router.get("/user/{_id}", response_model=User)
def get_user_by_userid(_id: int, db: Session = Depends(get_db)):
    user = user_services.get_user_by_user_id(db=db, _id=UserId(value=_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user



