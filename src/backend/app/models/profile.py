from sqlalchemy import Column, Date, Text, String, Integer

from app.db import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    prenom = Column(String)
    nom = Column(String)
    email = Column(String)
    telephone = Column(String)
    adresse = Column(String)
    dn = Column(Date)
    linkedin = Column(String)
    github = Column(String)
    photo = Column(String)
    bio = Column(Text)
