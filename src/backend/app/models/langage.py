from sqlalchemy import Column, Integer, String

from app.db import Base


class Langage(Base):
    __tablename__ = "langages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    niveau = Column(String)
