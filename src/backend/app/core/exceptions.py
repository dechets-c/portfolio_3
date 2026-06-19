"""Custom exception classes for the application."""

from fastapi import status


class AppException(Exception):
    """Base exception for application errors."""

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: str = "BAD_REQUEST",
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(self.message)


class ValidationException(AppException):
    """Raised when input validation fails."""

    def __init__(self, message: str, error_code: str = "VALIDATION_ERROR"):
        super().__init__(message, status.HTTP_422_UNPROCESSABLE_ENTITY, error_code)


class NotAuthenticatedException(AppException):
    """Raised when user is not authenticated."""

    def __init__(
        self, message: str = "Not authenticated", error_code: str = "NOT_AUTHENTICATED"
    ):
        super().__init__(message, status.HTTP_401_UNAUTHORIZED, error_code)


class NotAuthorizedException(AppException):
    """Raised when user doesn't have permission."""

    def __init__(
        self, message: str = "Not authorized", error_code: str = "NOT_AUTHORIZED"
    ):
        super().__init__(message, status.HTTP_403_FORBIDDEN, error_code)


class ResourceNotFoundException(AppException):
    """Raised when a resource is not found."""

    def __init__(self, resource: str = "Resource", error_code: str = "NOT_FOUND"):
        message = f"{resource} not found"
        super().__init__(message, status.HTTP_404_NOT_FOUND, error_code)


class ConflictException(AppException):
    """Raised when there's a conflict (e.g., duplicate entry)."""

    def __init__(self, message: str, error_code: str = "CONFLICT"):
        super().__init__(message, status.HTTP_409_CONFLICT, error_code)


class InternalServerException(AppException):
    """Raised for internal server errors."""

    def __init__(
        self, message: str = "Internal server error", error_code: str = "INTERNAL_ERROR"
    ):
        super().__init__(message, status.HTTP_500_INTERNAL_SERVER_ERROR, error_code)
