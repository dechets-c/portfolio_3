from datetime import datetime

from pydantic import BaseModel


class CertificationCreate(BaseModel):
    nom: str
    recu_par: str
    date_obtention: datetime
