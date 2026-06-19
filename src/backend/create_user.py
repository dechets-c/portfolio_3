#!/usr/bin/env python
import sys
import secrets
from pathlib import Path

# Ensure project root is on path
ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT))

from app.db.database import SessionLocal, engine, Base
from app.models.user import User
from app.core.security import get_password_hash


def main(email: str, password: str | None = None):
    if password is None:
        password = secrets.token_urlsafe(12)

    # Create tables if needed
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            user.hashed_password = get_password_hash(password)
            db.add(user)
            db.commit()
            print(f"Updated password for existing user: {email}")
        else:
            user = User(email=email, hashed_password=get_password_hash(password))
            db.add(user)
            db.commit()
            print(f"Created user: {email}")
        print("Password:", password)
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_user.py email [password]")
        sys.exit(2)
    email = sys.argv[1]
    pwd = sys.argv[2] if len(sys.argv) >= 3 else None
    main(email, pwd)
