from sqlalchemy import Column, Date, Integer, String

from app.db import Base


class Formation(Base):
    __tablename__ = "formations"

    id = Column(Integer, primary_key=True, index=True)
    nom_formation = Column(String)
    nom_ecole = Column(String)
    niveau = Column(String)
    secteur = Column(String)
    date_debut = Column(Date)
    date_fin = Column(Date, nullable=True)
