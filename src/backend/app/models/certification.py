from sqlalchemy import Column, Integer, String, Date

from app.db import Base


class Certification(Base):
    __tablename__ = "certifications"

    id_certification = Column(Integer, index=True, primary_key=True)
    nom = Column(String)
    recu_par = Column(String)
    date_obtention = Column(Date)
