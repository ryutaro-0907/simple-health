"""Define routers of Project."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..application.service import project_service
from ..domain.models.inspection import InspectionArea
from ..domain.models.organization import OrganizationId
from ..domain.models.project import Project, ProjectId, ProjectRequest, ProjectWithInspections
from ..infrastructure.db.database import get_db

router = APIRouter()


@router.post("/projects", response_model=Project)
def create_project(request: ProjectRequest, db: Session = Depends(get_db)):
    """プロジェクト作成."""
    # FIXME: ログイン中のユーザーの組織IDを取得
    organization_id = OrganizationId(1)
    return project_service.register(
        db=db, organization_id=organization_id, request=request)


@router.get("/projects/inspections", response_model=List[ProjectWithInspections])
def read_projects_with_inspections(db: Session = Depends(get_db)):
    """プロジェクト一覧(探査情報付き)取得."""
    # FIXME: ログイン中のユーザーの組織IDを取得
    organization_id = OrganizationId(1)
    projects: List[ProjectWithInspections] = \
        project_service.get_projects_with_inspections(
            db=db,
            organization_id=OrganizationId(organization_id))
    if projects is None:
        raise HTTPException(status_code=404, detail="Projects not found")

    return projects


@router.get("/projects/{_id}", response_model=Project)
def read_project(_id: int, db: Session = Depends(get_db)):
    """プロジェクト取得."""
    db_project = project_service.get_project(db=db, _id=ProjectId(value=_id))
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.get("/projects/{project_id}/inspections", response_model=ProjectWithInspections)
def read_project_with_inspection(project_id: int, db: Session = Depends(get_db)):
    """プロジェクト(探査情報付き)取得."""
    db_project = project_service.get_project_with_inspection(db=db, _id=ProjectId(value=project_id))
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.get("/projects/{project_id}/latest-area", response_model=InspectionArea)
def read_latest_area(project_id: int, db: Session = Depends(get_db)):
    """最新の探査エリアを取得."""
    db_project = project_service.get_latest_area(db=db, _id=ProjectId(value=project_id))
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project
