from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool

    class Config:
        from_attributes = True
class UserCreate(BaseModel):
    username: str
    password: str