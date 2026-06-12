from typing import Optional
from datetime import datetime, date

from pydantic import BaseModel, HttpUrl, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from app.schemas.langage import _LangageNiv
from app.schemas.formation import _NiveauFormation, _Secteur
from app.schemas.competence import _CategorieComp
from app.schemas.project import _ProjectRole
from app.schemas.experience import _TypeContrat


class UpdateProject(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    role: Optional[_ProjectRole] = None
    date_debut: Optional[date] = None
    date_fin: Optional[date] = None
    url: Optional[HttpUrl] = None


class UpdateCompetence(BaseModel):
    name: Optional[str] = None
    niveau: Optional[int] = None
    categorie_comp: Optional[_CategorieComp] = None
    date_debut_comp: Optional[datetime] = None


class UpdateFormation(BaseModel):
    nom_formation: Optional[str] = None
    nom_ecole: Optional[str] = None
    niveau: Optional[_NiveauFormation] = None
    secteur: Optional[_Secteur] = None
    date_debut: Optional[datetime] = None
    date_fin: Optional[datetime] = None


class UpdateOutil(BaseModel):
    name: Optional[str] = None
    categorie: Optional[str] = None
    niveau: Optional[int] = None
    url_logo: Optional[HttpUrl] = None


class UpdateProfil(BaseModel):
    prenom: Optional[str] = None
    nom: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: Optional[PhoneNumber] = None
    adresse: Optional[str] = None
    dn: Optional[datetime] = None
    linkedin: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None
    photo: Optional[HttpUrl] = None
    bio: Optional[str] = None


class UpdateLoisir(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class UpdateLangage(BaseModel):
    name: Optional[str] = None
    niveau: Optional[_LangageNiv] = None


class UpdateExperience(BaseModel):
    entreprise: Optional[str] = None
    poste: Optional[str] = None
    description_mission: Optional[str] = None
    type_contrat: Optional[_TypeContrat] = None
    date_debut: Optional[datetime] = None
    date_fin: Optional[datetime] = None


class UpdateCertification(BaseModel):
    nom: Optional[str] = None
    recu_par: Optional[str] = None
    date_obtention: Optional[datetime] = None
