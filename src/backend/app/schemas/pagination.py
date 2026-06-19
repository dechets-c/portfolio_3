from typing import Generic, TypeVar, List
from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response model."""

    items: List[T] = Field(..., description="List of items in this page")
    total: int = Field(..., description="Total number of items")
    page: int = Field(..., description="Current page number (1-indexed)")
    page_size: int = Field(..., description="Number of items per page")
    total_pages: int = Field(..., description="Total number of pages")

    class Config:
        json_schema_extra = {
            "example": {
                "items": [],
                "total": 100,
                "page": 1,
                "page_size": 10,
                "total_pages": 10,
            }
        }


class PaginationParams(BaseModel):
    """Pagination parameters for API queries."""

    page: int = Field(1, ge=1, description="Page number (1-indexed)")
    page_size: int = Field(10, ge=1, le=100, description="Items per page (max 100)")
