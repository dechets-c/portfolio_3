from sqlalchemy import Column, Integer, String

from app.db import Base


class Loisir(Base):
    __tablename__ = "loisirs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
