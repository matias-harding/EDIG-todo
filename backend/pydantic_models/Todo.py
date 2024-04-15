from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: int
    title: str
    complete: bool

    class Config:
        from_attributes = True
