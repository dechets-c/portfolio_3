from datetime import datetime

from pydantic import BaseModel, EmailStr, HttpUrl
from pydantic_extra_types.phone_numbers import PhoneNumber


class ProfilCreate(BaseModel):
    prenom: str
    nom: str
    email: EmailStr
    telephone: PhoneNumber
    adresse: str
    dn: datetime
    linkedin: HttpUrl
    github: HttpUrl
    photo: HttpUrl
    bio: str
