from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, HttpUrl, field_serializer


class _ProjectRole(str, Enum):
    DEV = "Développeur"
    SCIENCE = "Data scientist"
    ING = "Data engineer"
    ANAL = "Data analyst"


class ProjectCreate(BaseModel):
    name: str
    description: str
    role: _ProjectRole
    date_debut: date
    date_fin: Optional[date] = None
    url: Optional[HttpUrl] = None

    @field_serializer("url", when_used="unless-none")
    def serialize_url(self, v):
        return str(v) if v else None
