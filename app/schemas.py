from pydantic import BaseModel
from typing import Optional


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True