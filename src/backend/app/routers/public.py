from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app import models

router = APIRouter(prefix="/data", tags=["public"])


# Projects
@router.get("/projects")
def list_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects


@router.get("/project/{item_id}")
def get_project(item_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == item_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return project


# Competences
@router.get("/competences")
def list_competences(db: Session = Depends(get_db)):
    competences = db.query(models.Competence).all()
    return competences


@router.get("/competence/{item_id}")
def get_competence(item_id: int, db: Session = Depends(get_db)):
    competence = db.query(models.Competence).filter(models.Competence.id == item_id).first()
    if not competence:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return competence


# Formations
@router.get("/formations")
def list_formations(db: Session = Depends(get_db)):
    formations = db.query(models.Formation).all()
    return formations


@router.get("/formation/{item_id}")
def get_formation(item_id: int, db: Session = Depends(get_db)):
    formation = db.query(models.Formation).filter(models.Formation.id == item_id).first()
    if not formation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return formation


# Outils
@router.get("/outils")
def list_outils(db: Session = Depends(get_db)):
    outils = db.query(models.Outil).all()
    return outils


@router.get("/outil/{item_id}")
def get_outil(item_id: int, db: Session = Depends(get_db)):
    outil = db.query(models.Outil).filter(models.Outil.id == item_id).first()
    if not outil:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outil


# Profiles
@router.get("/profiles")
def list_profiles(db: Session = Depends(get_db)):
    profiles = db.query(models.Profile).all()
    return profiles


@router.get("/profile/{item_id}")
def get_profile(item_id: int, db: Session = Depends(get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == item_id).first()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return profile


# Loisirs
@router.get("/loisirs")
def list_loisirs(db: Session = Depends(get_db)):
    loisirs = db.query(models.Loisir).all()
    return loisirs


@router.get("/loisir/{item_id}")
def get_loisir(item_id: int, db: Session = Depends(get_db)):
    loisir = db.query(models.Loisir).filter(models.Loisir.id == item_id).first()
    if not loisir:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return loisir


# Langages
@router.get("/langages")
def list_langages(db: Session = Depends(get_db)):
    langages = db.query(models.Langage).all()
    return langages


@router.get("/langage/{item_id}")
def get_langage(item_id: int, db: Session = Depends(get_db)):
    langage = db.query(models.Langage).filter(models.Langage.id == item_id).first()
    if not langage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return langage

