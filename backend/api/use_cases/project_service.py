"""Project Services."""
from typing import List

from sqlalchemy.orm import Session


from ...domain.models.project import Project, ProjectId, ProjectRequest, ProjectWithInspections
from ...infrastructure.db import project_datasource


def register(db: Session, organization_id: OrganizationId, request: ProjectRequest):
    """プロジェクト登録."""
    return project_datasource.create_project(
        db=db, organization_id=organization_id, request=request)


def get_projects_with_inspections(db: Session, organization_id: OrganizationId) \
        -> List[ProjectWithInspections]:
    """プロジェクト一覧取得."""
    return project_datasource.all_projects_with_inspections(db=db, organization_id=organization_id)


def get_project(db: Session, _id: ProjectId) -> Project:
    """プロジェクト情報取得."""
    return project_datasource.get_project(db=db, _id=_id)


def get_project_with_inspection(db: Session, _id: ProjectId) -> ProjectWithInspections:
    """プロジェクト情報(探査情報付き)取得."""
    return project_datasource.get_project_with_inspections(db=db, _id=_id)

