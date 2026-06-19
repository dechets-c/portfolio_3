import logging
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app import models

router = APIRouter(prefix="/data", tags=["public"])
logger = logging.getLogger(__name__)


# Projects
@router.get("/projects")
def list_projects(db: Session = Depends(get_db)):
    logger.debug("Fetching all projects")
    projects = db.query(models.Project).all()
    logger.debug(f"Retrieved {len(projects)} projects")
    return projects


@router.get("/project/{item_id}")
def get_project(item_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching project with id: {item_id}")
    project = db.query(models.Project).filter(models.Project.id == item_id).first()
    if not project:
        logger.warning(f"Project with id {item_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    logger.debug(f"Retrieved project: {item_id}")
    return project


# Competences
@router.get("/competences")
def list_competences(db: Session = Depends(get_db)):
    logger.debug("Fetching all competences")
    competences = db.query(models.Competence).all()
    logger.debug(f"Retrieved {len(competences)} competences")
    return competences


@router.get("/competence/{item_id}")
def get_competence(item_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching competence with id: {item_id}")
    competence = (
        db.query(models.Competence).filter(models.Competence.id == item_id).first()
    )
    if not competence:
        logger.warning(f"Competence with id {item_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    logger.debug(f"Retrieved competence: {item_id}")
    return competence


# Formations
@router.get("/formations")
def list_formations(db: Session = Depends(get_db)):
    logger.debug("Fetching all formations")
    formations = db.query(models.Formation).all()
    logger.debug(f"Retrieved {len(formations)} formations")
    return formations


@router.get("/formation/{item_id}")
def get_formation(item_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching formation with id: {item_id}")
    formation = (
        db.query(models.Formation).filter(models.Formation.id == item_id).first()
    )
    if not formation:
        logger.warning(f"Formation with id {item_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    logger.debug(f"Retrieved formation: {item_id}")
    return formation


# Outils
@router.get("/outils")
def list_outils(db: Session = Depends(get_db)):
    logger.debug("Fetching all outils")
    outils = db.query(models.Outil).all()
    logger.debug(f"Retrieved {len(outils)} outils")
    return outils


@router.get("/outil/{item_id}")
def get_outil(item_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching outil with id: {item_id}")
    outil = db.query(models.Outil).filter(models.Outil.id == item_id).first()
    if not outil:
        logger.warning(f"Outil with id {item_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    logger.debug(f"Retrieved outil: {item_id}")
    return outil


# Profiles
@router.get("/profiles")
def list_profiles(db: Session = Depends(get_db)):
    logger.debug("Fetching all profiles")
    profiles = db.query(models.Profile).all()
    logger.debug(f"Retrieved {len(profiles)} profiles")
    return profiles


@router.get("/profile/{item_id}")
def get_profile(item_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching profile with id: {item_id}")
    profile = db.query(models.Profile).filter(models.Profile.id == item_id).first()
    if not profile:
        logger.warning(f"Profile with id {item_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    logger.debug(f"Retrieved profile: {item_id}")
    return profile


# Loisirs
@router.get("/loisirs")
def list_loisirs(db: Session = Depends(get_db)):
    logger.debug("Fetching all loisirs")
    loisirs = db.query(models.Loisir).all()
    logger.debug(f"Retrieved {len(loisirs)} loisirs")
    return loisirs


@router.get("/loisir/{item_id}")
def get_loisir(item_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching loisir with id: {item_id}")
    loisir = db.query(models.Loisir).filter(models.Loisir.id == item_id).first()
    if not loisir:
        logger.warning(f"Loisir with id {item_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    logger.debug(f"Retrieved loisir: {item_id}")
    return loisir


# Langages
@router.get("/langages")
def list_langages(db: Session = Depends(get_db)):
    logger.debug("Fetching all langages")
    langages = db.query(models.Langage).all()
    logger.debug(f"Retrieved {len(langages)} langages")
    return langages


@router.get("/langage/{item_id}")
def get_langage(item_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching langage with id: {item_id}")
    langage = db.query(models.Langage).filter(models.Langage.id == item_id).first()
    if not langage:
        logger.warning(f"Langage with id {item_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    logger.debug(f"Retrieved langage: {item_id}")
    return langage
