"""Define routers for Record."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..use_cases import record_services
from ..entities.user import UserId
from ..entities.record import Record, RecordId, CreateRecord
from ..interfaces.db.database import get_db

router = APIRouter()

@router.post("/records", response_model=Record)
def create_record(request: CreateRecord, db: Session = Depends(get_db)):
    return record_services.create_record(
        db=db, request=request)


@router.get("/records/{user_id}", response_model=List[Record])
def get_records_by_user(user_id: UserId, db: Session = Depends(get_db)):
    records: List[Record] = \
        record_services.get_all_record_by_user(db=db, user_id=user_id)
    if records is None:
        raise HTTPException(status_code=404, detail="Records not found")

    return records




