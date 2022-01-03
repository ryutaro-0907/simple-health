"""conftest."""
from sqlalchemy.sql.functions import user
import pytest

from api.entities.user import User, UserEmail, UserRegister, UserId, UserName, UserPassword
from api.entities.record import (Record, RecordId, CreateRecord, Happiness, Motivation, Workout, Helped, Carories, Steps, Meditation, Study, Work)
from api.entities.general import CreatedAt

from api.interfaces.db import db_models, record_db_handler, user_db_handler
from api.interfaces.db.database import get_db

from api.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database


@pytest.fixture(scope='function', name='test_session_local')
def fixture_test_session_local():
    """Test Session."""
    # settings of test database
    test_sqlalchemy_database_url = "sqlite:///./test_temp.db"
    engine = create_engine(test_sqlalchemy_database_url, connect_args={"check_same_thread": False})

    assert not database_exists(test_sqlalchemy_database_url),\
        "Test database already exists. Aborting tests."

    # Create test database and tables
    db_models.Base.metadata.create_all(engine)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield session_local

    # Drop the test database
    drop_database(test_sqlalchemy_database_url)


def temp_db(f):
    """Temp db."""
    def func(test_session_local, *args, **kwargs):
        def override_get_db():
            try:
                db = test_session_local()
                yield db
            finally:
                db.close()

        init_test_db(test_session_local)

        app.dependency_overrides[get_db] = override_get_db

        # Run tests
        f(*args, **kwargs)

        app.dependency_overrides[get_db] = get_db

    return func


def init_test_db(test_session_local):
    """Initialize DB."""
    with test_session_local() as db:
        user_db_handler.create_user(
            db=db, request=UserRegister(
            username=UserName('test_user'),
            email=UserEmail('test@gmail.com'),
            password=UserPassword('testpassword'),
            created_at=CreatedAt('2022-01-01')
        ))

        record_db_handler.create_record(
            db=db,
            request=CreateRecord(
                user_id=UserId(0),
                created_at=CreatedAt('2022-01-01'), happiness=Happiness(5), motivation=Motivation(5),
                workout=Workout('yes'), helped=Helped('yes'), carories=Carories(3000), steps=Steps(10000),
                meditation=Meditation(120), study=Study(5), work=Work(5)
            ))
