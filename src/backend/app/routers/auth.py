import logging
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import User
from app.schemas.auth import Token, UserCreate, UserOut
from app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    decode_access_token,
)
from app.core.exceptions import (
    ConflictException,
    NotAuthenticatedException,
    ResourceNotFoundException,
)
from fastapi.security import OAuth2PasswordBearer

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Registration attempt for email: {user.email}")
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        logger.warning(f"Registration failed: Email {user.email} already registered")
        raise ConflictException(
            f"Email {user.email} is already registered",
            error_code="EMAIL_ALREADY_REGISTERED",
        )
    db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"User registered successfully: {user.email}")
    return db_user


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    logger.info(f"Login attempt for email: {form_data.username}")
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        logger.warning(f"Login failed for email: {form_data.username}")
        raise NotAuthenticatedException(
            "Incorrect email or password", error_code="INVALID_CREDENTIALS"
        )
    access_token = create_access_token({"sub": user.email})
    logger.info(f"Login successful for email: {form_data.username}")
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    try:
        payload = decode_access_token(token)
        email = payload.get("sub")
        if email is None:
            logger.warning("Invalid token: no email in payload")
            raise NotAuthenticatedException("Invalid token", error_code="INVALID_TOKEN")
        user = db.query(User).filter(User.email == email).first()
        if not user:
            logger.warning(f"User not found for email: {email}")
            raise ResourceNotFoundException("User")
        logger.debug(f"User authenticated: {email}")
        return user
    except Exception as e:
        logger.error(f"Authentication error: {str(e)}")
        if isinstance(e, (NotAuthenticatedException, ResourceNotFoundException)):
            raise
        raise NotAuthenticatedException(
            "Invalid authentication credentials", error_code="AUTH_ERROR"
        )
