"""Define routers for User."""
from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from ..use_cases import user_services
from ..entities.user import User, UserId, UserRegister, UserSignIn
from ..interfaces.db.database import get_db

router = APIRouter()

@router.post("/users/signup", response_model=User)
def create_user(request: UserRegister, db: Session = Depends(get_db)):
    """[summary]
    Sign up endpoint
    Args:
        request (UserRegister): [Object]
        db (Session, optional): [description]. Defaults to Depends(get_db).

    Returns:
        [type]: [Json response]
    """
    try:
        user = user_services.register_user(
            db=db, request=request)

        response = {
            'code':201,
            'id': user.id,
            'message':' user created.'
        }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)
    except:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
            'code':400,
            'message': 'internal error could not register user.'
        })

@router.post("/users/signin", response_model=User)
def user_signin(request: UserSignIn, db: Session = Depends(get_db)):
    """[summary]
    Sign in endpoint
    Args:
        request (UserRegister): [description]
        db (Session, optional): [description]. Defaults to Depends(get_db).

    Returns:
        [type]: [description]
    """
    try:
        user = user_services.user_signin(
            db=db, request=request)

        response = {
            'code':200,
            'id': user.id,
            'message':' user found.'
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=response)
    except:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
            'code':400,
            'message': 'internal error could not register user.'
        })


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



