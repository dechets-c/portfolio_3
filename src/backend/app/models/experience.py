from sqlalchemy import Column, Integer, String, Date

from app.db import Base


class Experience(Base):
    __tablename__ = "experiences"

    id_experience = Column(Integer, primary_key=True, index=True)
    entreprise = Column(String)
    description_mission = Column(String)
    type_contrat = Column(String)
    date_debut = Column(Date)
    date_fin = Column(Date, nullable=True)
