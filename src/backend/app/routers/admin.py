from fastapi import APIRouter, Depends  # depends pour ce qui est dans dependencies
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import (
    ProjectCreate,
    CertificationCreate,
    CompetenceCreate,
    ProfilCreate,
    OutilCreate,
    FormationCreate,
    LoisirCreate,
    LangageCreate,
)
from app import models


router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/create_project")
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(**data.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {"message": "Projet inséré avec succès", "id": new_project.id}


@router.post("/create_competence")
def create_competence(data: CompetenceCreate, db: Session = Depends(get_db)):
    new_comp = models.Competence(**data.model_dump())
    db.add(new_comp)
    db.commit()
    db.refresh(new_comp)

    return {"message": "Compétence insérée avec succès", "id": new_comp.id}


@router.post("/create_formation")
def create_formation(data: FormationCreate, db: Session = Depends(get_db)):
    new_form = models.Formation(**data.model_dump())
    db.add(new_form)
    db.commit()
    db.refresh(new_form)

    return {"message": "Formation insérée avec succès", "id": new_form.id}


@router.post("/create_outil")
def create_outil(data: OutilCreate, db: Session = Depends(get_db)):
    new_outil = models.Outil(**data.model_dump())
    db.add(new_outil)
    db.commit()
    db.refresh(new_outil)

    return {"message": "Outil inséré avec succès", "id": new_outil.id}


@router.post("/create_profile")
def create_profile(data: ProfilCreate, db: Session = Depends(get_db)):
    new_prof = models.Outil(**data.model_dump())
    db.add(new_prof)
    db.commit()
    db.refresh(new_prof)

    return {"message": "Profil inséré avec succès", "id": new_prof.id}


@router.post("/create_loisir")
def create_loisir(data: LoisirCreate, db: Session = Depends(get_db)):
    new_loisir = models.Outil(**data.model_dump())
    db.add(new_loisir)
    db.commit()
    db.refresh(new_loisir)

    return {"message": "Loisir inséré avec succès", "id": new_loisir.id}


@router.post("/create_certification")
def create_certif(data: CertificationCreate, db: Session = Depends(get_db)):
    new_certif = models.Certification(**data.model_dump())
    db.add(new_certif)
    db.commit()
    db.refresh(new_certif)

    return {"message": "Certification inséré avec succès", "id": new_certif.id}


@router.post("/create_langage")
def create_langage(data: LangageCreate, db: Session = Depends(get_db)):
    new_lang = models.Outil(**data.model_dump())
    db.add(new_lang)
    db.commit()
    db.refresh(new_lang)

    return {"message": "Langage inséré avec succès", "id": new_lang.id}


@router.post("/delete")
def delete_from_db():
    pass


@router.post("/update")
def update_from_db():
    pass
