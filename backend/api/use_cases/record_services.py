"""Records Services."""
from typing import List

from sqlalchemy.orm import Session

from ..entities.user import UserId
from ..entities.record import CreateRecord, Record, CreatedAt
from ..interfaces.db import record_db_handler

def create_record(db: Session, request: CreateRecord):
    return record_db_handler.create_record(
        db=db, request=request)

def get_all_record_by_user(db:Session, user_id:UserId) -> List[Record]:
	return record_db_handler.get_records_by_user(db=db, user_id=user_id)









