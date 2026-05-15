from app.schemas.competence import CompetenceCreate
from app.schemas.formation import FormationCreate
from app.schemas.langage import LangageCreate
from app.schemas.loisir import LoisirCreate
from app.schemas.outil import OutilCreate
from app.schemas.profile import ProfilCreate
from fastapi import APIRouter, Depends  # depends pour ce qui est dans dependencies
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import ProjectCreate
from app import models
from app.routers.auth import get_current_user
from fastapi import HTTPException, status

router = APIRouter(
    prefix="/admin", tags=["admin"], dependencies=[Depends(get_current_user)]
)

# allowed models map: lower-case -> (ModelClass, UpdateSchema)
from app.schemas.update_schemas import (
    UpdateProject,
    UpdateCompetence,
    UpdateFormation,
    UpdateOutil,
    UpdateProfil,
    UpdateLoisir,
    UpdateLangage,
)

allowed_models = {
    "project": (models.Project, UpdateProject),
    "competence": (models.Competence, UpdateCompetence),
    "formation": (models.Formation, UpdateFormation),
    "outil": (models.Outil, UpdateOutil),
    "profile": (models.Profile, UpdateProfil),
    "loisir": (models.Loisir, UpdateLoisir),
    "langage": (models.Langage, UpdateLangage),
}


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
    new_prof = models.Profile(**data.model_dump())
    db.add(new_prof)
    db.commit()
    db.refresh(new_prof)

    return {"message": "Profil inséré avec succès", "id": new_prof.id}


@router.post("/create_loisir")
def create_loisir(data: LoisirCreate, db: Session = Depends(get_db)):
    new_loisir = models.Loisir(**data.model_dump())
    db.add(new_loisir)
    db.commit()
    db.refresh(new_loisir)

    return {"message": "Loisir inséré avec succès", "id": new_loisir.id}


@router.post("/create_langage")
def create_langage(data: LangageCreate, db: Session = Depends(get_db)):
    new_lang = models.Langage(**data.model_dump())
    db.add(new_lang)
    db.commit()
    db.refresh(new_lang)

    return {"message": "Langage inséré avec succès", "id": new_lang.id}


@router.delete("/delete/{model_name}/{item_id}")
def delete_from_db(model_name: str, item_id: int, db: Session = Depends(get_db)):
    entry = allowed_models.get(model_name.lower())
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unknown model"
        )
    model = entry[0]
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    db.delete(obj)
    db.commit()
    return {"message": "Deleted", "id": item_id}


@router.put("/update/{model_name}/{item_id}")
def update_from_db(
    model_name: str, item_id: int, data: dict, db: Session = Depends(get_db)
):
    entry = allowed_models.get(model_name.lower())
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unknown model"
        )
    model = entry[0]
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    # update fields from request body
    for key, value in data.items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}


# Per-model typed updates
@router.put("/project/{item_id}")
def update_project(item_id: int, data: UpdateProject, db: Session = Depends(get_db)):
    model = models.Project
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    for key, value in data.model_dump(exclude_none=True).items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}


@router.put("/competence/{item_id}")
def update_competence(
    item_id: int, data: UpdateCompetence, db: Session = Depends(get_db)
):
    model = models.Competence
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    for key, value in data.model_dump(exclude_none=True).items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}


@router.put("/formation/{item_id}")
def update_formation(
    item_id: int, data: UpdateFormation, db: Session = Depends(get_db)
):
    model = models.Formation
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    for key, value in data.model_dump(exclude_none=True).items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}


@router.put("/outil/{item_id}")
def update_outil(item_id: int, data: UpdateOutil, db: Session = Depends(get_db)):
    model = models.Outil
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    for key, value in data.model_dump(exclude_none=True).items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}


@router.put("/profile/{item_id}")
def update_profile(item_id: int, data: UpdateProfil, db: Session = Depends(get_db)):
    model = models.Profile
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    for key, value in data.model_dump(exclude_none=True).items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}


@router.put("/loisir/{item_id}")
def update_loisir(item_id: int, data: UpdateLoisir, db: Session = Depends(get_db)):
    model = models.Loisir
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    for key, value in data.model_dump(exclude_none=True).items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}


@router.put("/langage/{item_id}")
def update_langage(item_id: int, data: UpdateLangage, db: Session = Depends(get_db)):
    model = models.Langage
    obj = db.query(model).filter(model.id == item_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    for key, value in data.model_dump(exclude_none=True).items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "Updated", "id": item_id}
