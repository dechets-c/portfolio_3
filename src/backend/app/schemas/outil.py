from enum import Enum
from typing import Optional

from pydantic import BaseModel, HttpUrl, field_serializer


class _OutilCategory(str, Enum):
    DEV = "Developpement"
    DATA = "Data"
    BUR = "Bureautique"


class OutilCreate(BaseModel):
    name: str
    categorie: str
    niveau: int
    url_logo: Optional[HttpUrl] = None

    @field_serializer("url_logo", when_used="unless-none")
    def serialize_url_logo(self, v):
        return str(v) if v else None
