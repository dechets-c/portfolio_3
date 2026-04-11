from fastapi import APIRouter, Depends  # depends pour ce qui est dans dependencies
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import ProjectCreate
from app import models

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/create_project")
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(**data.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {"message": "Projet inséré avec succès", "id": new_project.id}


@router.post("/delete")
def delete_from_db():
    pass


@router.post("/update")
def update_from_db():
    pass
