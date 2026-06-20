import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import admin, auth, public
from app.core.config import CORS_ORIGINS, LOG_LEVEL, ENVIRONMENT
from app.core.exceptions import AppException
from app.middleware import RequestIDMiddleware, LoggingMiddleware
from app.schemas.errors import ErrorResponse, ErrorDetail, HealthCheckResponse
from app.db.database import Base, engine

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Portfolio S3 Backend",
    version="0.1.0",
    description="Backend API for portfolio management system",
)

# Add middleware in correct order (innermost/last to outermost/first)
app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIDMiddleware)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS if ENVIRONMENT == "production" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception handlers
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    """Handle custom application exceptions."""
    request_id = getattr(request.state, "request_id", "unknown")
    logger.error(f"[{request_id}] {exc.error_code}: {exc.message}")

    error_detail = ErrorDetail(
        error_code=exc.error_code,
        message=exc.message,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "errors": [error_detail.model_dump()],
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    request_id = getattr(request.state, "request_id", "unknown")
    logger.error(f"[{request_id}] Unhandled exception: {str(exc)}", exc_info=True)

    error_detail = ErrorDetail(
        error_code="INTERNAL_ERROR",
        message="An unexpected error occurred"
        if ENVIRONMENT == "production"
        else str(exc),
    )

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "errors": [error_detail.model_dump()],
        },
    )



# Include routers
app.include_router(public.router)
app.include_router(admin.router)
app.include_router(auth.router)

logger.info(f"FastAPI app initialized (environment: {ENVIRONMENT})")
logger.info(f"CORS origins: {CORS_ORIGINS if ENVIRONMENT == 'production' else 'all'}")


@app.on_event("startup")
def startup_create_tables():
    """Ensure tables exist for local development and testing."""
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables ensured on startup")


@app.get("/health", response_model=HealthCheckResponse)
def health_check():
    """Health check endpoint for monitoring."""
    logger.debug("Health check requested")
    return HealthCheckResponse(status="ok", version="0.1.0")


def main():
    logger.info("Starting Portfolio S3 Backend")


if __name__ == "__main__":
    main()
