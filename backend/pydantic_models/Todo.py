from pydantic import BaseModel
from typing import Optional, Dict, Any

class TodoCreate(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: int
    title: str
    complete: bool
    variables: Optional[dict] = None

    class Config:
        from_attributes = True
