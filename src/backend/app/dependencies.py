# Contient les infos partagées entre les apps
# Genre les sessions de databases

from app.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
