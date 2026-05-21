from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class _CategorieComp(str, Enum):
    STAT = "Statistiques"
    DEV = "Développement"
    DATA = "Data"
    INF = "Informatique"
    SOFT = "Soft Skills"


class CompetenceCreate(BaseModel):
    name: str
    niveau: int
    categorie_comp: _CategorieComp
    date_debut_comp: datetime
