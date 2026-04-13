from enum import Enum

from pydantic import BaseModel


class _LangageNiv(str, Enum):
    A1 = "A1 - Débutant"
    A2 = "A2 - Élémentaire"
    B1 = "B1 - Intermédiaire"
    B2 = "B2 - Intermédiaire ++"
    C1 = "C1 - Avancé"
    C2 = "C2 - Maitrise"
    NATIF = "Langue maternelle"


class LangageCreate(BaseModel):
    name: str
    niveau: _LangageNiv
