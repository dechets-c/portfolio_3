from sqlalchemy import Column, Integer, String, Date

from app.db import Base


class Competence(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    orga_distribution = Column(String)
    date_obtentions = Column(Date)
