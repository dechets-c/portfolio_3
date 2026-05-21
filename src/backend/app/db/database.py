from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL

sqlite_mode = DATABASE_URL.get_backend_name() == "sqlite"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if sqlite_mode else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
