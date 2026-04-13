from pydantic import BaseModel


class LoisirCreate(BaseModel):
    name: str
    description: str
