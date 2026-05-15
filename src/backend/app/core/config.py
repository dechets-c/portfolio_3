import os
import logging
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import URL

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


def build_database_url() -> URL:
    """Build database URL from environment variables."""
    if db_name and db_user:
        logger.info(
            f"Building database URL for {db_user}@{db_host}:{db_port}/{db_name}"
        )
        return URL.create(
            "postgresql+psycopg2",
            username=db_user,
            password=db_password,
            host=db_host,
            database=db_name,
            port=db_port,
        )
    else:
        # Fallback to SQLite for testing
        logger.warning(
            "Database environment variables not fully set. Using SQLite fallback."
        )
        return URL.create("sqlite", database=":memory:")


DATABASE_URL = build_database_url()
