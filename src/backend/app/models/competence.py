from sqlalchemy import Column, Integer, String, Date

from app.db import Base


class Competence(Base):
    __tablename__ = "competences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    categorie_comp = Column(String)
    date_debut_comp = Column(Date)
