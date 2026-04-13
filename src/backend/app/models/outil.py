from sqlalchemy import Column, Integer, String, null

from app.db import Base


class Outil(Base):
    __tablename__ = "outils"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    categorie = Column(String)
    niveau = Column(Integer)
    url_logo = Column(String, nullable=True)
