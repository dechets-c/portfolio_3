from fastapi import APIRouter, Depends  # depends pour ce qui est dans dependencies

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/insert")
def insert_to_db():
    pass


@router.post("/delete")
def delete_from_db():
    pass


@router.post("/update")
def update_from_db():
    pass
