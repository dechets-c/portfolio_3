from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class _NiveauFormation(str, Enum):
    BAC = "Bac"
    BUT = "Bac +3"
    INGE = "Bac +5"
    LICENCE = "Bac +3"
    MASTER = "Bac +5"


class _Secteur(str, Enum):
    INFO = "Informatique"
    DATA = "Data"


class FormationCreate(BaseModel):
    nom_formation: str
    nom_ecole: str
    niveau: _NiveauFormation
    secteur: _Secteur
    date_debut: datetime
    date_fin: Optional[datetime] = None
