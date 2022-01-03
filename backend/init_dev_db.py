# """Init Dev DB."""
# import logging
# import os

# from api.domain.models.organization import OrganizationId, OrganizationName
# from api.domain.models.project import (ProjectDate, ProjectDescription, ProjectName, ProjectPeriod,
#                                        ProjectRequest)
# from api.infrastructure.db import project_datasource
# from api.infrastructure.db.entities import Base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# db_user = os.environ.get('DB_USER', 'user')
# db_pass = os.environ.get('DB_PASS', 'pass')

# SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@localhost:5432/app_db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


# def init() -> None:
#     """init."""
#     with SessionLocal() as db:
#         project_datasource.create_organization(
#             db=db, name=OrganizationName("株式会社○○"))

#         project_datasource.create_project(
#             db=db,
#             organization_id=OrganizationId(1),
#             request=ProjectRequest(name=ProjectName("Hacarus社地盤検査"),
#                                    description=ProjectDescription("Hacarus社社屋建設PJ"),
#                                    period=ProjectPeriod(
#                                        start_date=ProjectDate(2021, 11, 17),
#                                        end_date=ProjectDate(2021, 11, 18))))


# def main() -> None:
#     """main."""
#     logger.info("Creating initial data")
#     init()
#     logger.info("Initial data created")


# if __name__ == "__main__":
#     main()
