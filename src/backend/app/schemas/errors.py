"""Error response schemas."""

from pydantic import BaseModel, Field
from typing import Any, Optional


class ErrorDetail(BaseModel):
    """Standard error detail response."""

    error_code: str = Field(..., description="Machine-readable error code")
    message: str = Field(..., description="Human-readable error message")
    details: Optional[Any] = Field(None, description="Additional error details")

    class Config:
        json_schema_extra = {
            "example": {
                "error_code": "VALIDATION_ERROR",
                "message": "Email is invalid",
                "details": None,
            }
        }


class ErrorResponse(BaseModel):
    """Standard error response body."""

    status: str = Field("error", description="Always 'error' for error responses")
    errors: list[ErrorDetail] = Field(..., description="List of errors")


class HealthCheckResponse(BaseModel):
    """Health check response."""

    status: str = Field("ok", description="Health status")
    version: Optional[str] = Field(None, description="API version")

    class Config:
        json_schema_extra = {"example": {"status": "ok", "version": "0.1.0"}}
