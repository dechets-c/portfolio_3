from typing import Optional
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class _TypeContrat(str, Enum):
    ALT = "Alternance"
    CDI = "CDI"
    CDD = "CDD"
    STG = "Stage"


class ExperienceCreate(BaseModel):
    entreprise: str
    poste: str
    description_mission: str
    type_contrat: _TypeContrat
    date_debut: datetime
    date_fin: Optional[datetime] = None
