from pydantic import BaseModel
from typing import Optional


class School(BaseModel):
    id: Optional[int] = None
    name: str
    location: str


class SchoolUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
