"""DB methods for Record"""
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from ...entities.user import User, UserEmail, UserRegister, UserId, UserName, UserPassword
from ...entities.record import Record, CreateRecord
from ...entities.general import CreatedAt
from .db_models import UserModel, RecordModel


def get_records_by_user(db: Session, user_id: UserId) -> List[Record]:
	"""Get Records by user"""
	db_records = db.query(RecordModel).filter(RecordModel.user_id == user_id).all()
	records = list(map(RecordModel.to_model, db_records))

	return records


def create_record(db: Session, request: CreateRecord):
    """Create Record."""
    record = RecordModel(
		    user_id = int(request.user_id),
        created_at = str(datetime.now()),
        happiness= int(request.happiness),
        motivation= int(request.motivation),
        workout= str(request.workout),
        helped= str(request.helped),
        carories= int(request.carories),
        steps= int(request.steps),
        meditation= int(request.meditation),
        study= int(request.study),
		    work= int(request.work)
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record.to_model()

