import os
import logging
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)

load_dotenv()

# Database configuration
db_name = os.getenv("db_name")
db_host = os.getenv("db_host", "localhost")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_port = os.getenv("db_port", "5432")

# Security configuration
SECRET_KEY = os.getenv("secret_key")
if not SECRET_KEY:
    logger.warning(
        "SECRET_KEY not set in environment. Using default for development only!"
    )
    SECRET_KEY = "dev-secret-key-change-in-production"

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()

# CORS
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


def _build_sqlite_fallback() -> URL:
    sqlite_path = Path(__file__).resolve().parents[2] / "portfolio_s3.db"
    logger.warning(f"Falling back to SQLite database at {sqlite_path}")
    return URL.create("sqlite+pysqlite", database=str(sqlite_path))


def build_database_url() -> URL:
    """Build database URL from environment variables."""
    if db_name and db_user:
        postgres_url = URL.create(
            "postgresql+psycopg2",
            username=db_user,
            password=db_password,
            host=db_host,
            database=db_name,
            port=db_port,
            query={"connect_timeout": "3"},
        )

        if ENVIRONMENT != "production":
            try:
                test_engine = create_engine(postgres_url, pool_pre_ping=True)
                with test_engine.connect():
                    logger.info(
                        f"Using PostgreSQL database for {db_user}@{db_host}:{db_port}/{db_name}"
                    )
                    return postgres_url
            except SQLAlchemyError as error:
                logger.warning(f"PostgreSQL unavailable locally: {error}")
                return _build_sqlite_fallback()

        logger.info(
            f"Using PostgreSQL database for {db_user}@{db_host}:{db_port}/{db_name}"
        )
        return postgres_url
    else:
        return _build_sqlite_fallback()


DATABASE_URL = build_database_url()
