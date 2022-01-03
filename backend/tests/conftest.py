"""conftest."""
import pytest
from api.domain.models.organization import OrganizationId, OrganizationName
from api.domain.models.project import (ProjectDate, ProjectDescription, ProjectName, ProjectPeriod,
                                       ProjectRequest)
from api.infrastructure.db import entities, project_datasource
from api.infrastructure.db.database import get_db
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
    entities.Base.metadata.create_all(engine)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield session_local

    # Drop the test database
    drop_database(test_sqlalchemy_database_url)


def temp_db(f):
    """Temp db."""
    def func(test_session_local, *args, **kwargs):
        # テスト用のDBに接続するためのsessionmaker instanse
        #  (SessionLocal) をfixtureから受け取る

        def override_get_db():
            try:
                db = test_session_local()
                yield db
            finally:
                db.close()

        init_test_db(test_session_local)

        # fixtureから受け取るSessionLocalを使うようにget_dbを強制的に変更
        app.dependency_overrides[get_db] = override_get_db

        # Run tests
        f(*args, **kwargs)
        # get_dbを元に戻す
        app.dependency_overrides[get_db] = get_db

    return func


def init_test_db(test_session_local):
    """Initialize DB."""
    with test_session_local() as db:
        project_datasource.create_organization(
            db=db, name=OrganizationName("株式会社○○"))

        project_datasource.create_project(
            db=db,
            organization_id=OrganizationId(1),
            request=ProjectRequest(name=ProjectName("Hacarus社地盤検査"),
                                   description=ProjectDescription("Hacarus社社屋建設PJ"),
                                   period=ProjectPeriod(
                                       start_date=ProjectDate(2021, 11, 17),
                                       end_date=ProjectDate(2021, 11, 18))))
