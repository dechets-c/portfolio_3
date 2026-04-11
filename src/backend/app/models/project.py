from sqlalchemy import Column, Integer, String, Date
from app.db import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    date_debut = Column(Date)
    date_fin = Column(Date, nullable=True)
    role = Column(String)
    url = Column(String, nullable=True)
