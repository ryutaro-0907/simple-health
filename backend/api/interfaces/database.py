"""database."""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db_models import Base

db_user = os.environ.get('DB_USER', 'user')
db_pass = os.environ.get('DB_PASS', 'pass')
sql_type = os.environ.get('DB_type', 'type')

# SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@host.docker.internal:5432/app_db"

SQLITE_PATH = 'sqlite://///Users/ryutaro/Desktop/code/work/Health-care-app/backend/api/healthcare.db'

engine = create_engine(
    SQLITE_PATH
)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Get DB Session."""
    with SessionLocal() as db:
        yield db
