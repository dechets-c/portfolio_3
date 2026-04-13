from enum import Enum
from typing import Optional

from pydantic import BaseModel, HttpUrl


class _OutilCategory(Enum):
    DEV = "Developpement"
    DATA = "Data"
    BUR = "Bureautique"


class OutilCreate(BaseModel):
    name: str
    categorie: str
    niveau: int
    url_logo: Optional[HttpUrl] = None
