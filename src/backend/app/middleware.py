"""Application middleware."""

import logging
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


logger = logging.getLogger(__name__)


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Add unique request ID to all requests for tracing."""

    async def dispatch(self, request: Request, call_next) -> Response:
        # Generate or get request ID
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request.state.request_id = request_id

        # Log request
        logger.debug(
            f"[{request_id}] {request.method} {request.url.path} - "
            f"Client: {request.client.host if request.client else 'unknown'}"
        )

        # Process request
        response = await call_next(request)

        # Add request ID to response headers
        response.headers["X-Request-ID"] = request_id

        # Log response
        logger.debug(
            f"[{request_id}] {request.method} {request.url.path} - Status: {response.status_code}"
        )

        return response


class LoggingMiddleware(BaseHTTPMiddleware):
    """Enhanced logging for request/response."""

    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = getattr(request.state, "request_id", "unknown")

        # Process request
        response = await call_next(request)

        # Log based on status code
        if response.status_code >= 400:
            logger.warning(
                f"[{request_id}] {request.method} {request.url.path} returned {response.status_code}"
            )
        elif response.status_code >= 300:
            logger.info(
                f"[{request_id}] {request.method} {request.url.path} returned {response.status_code}"
            )

        return response
