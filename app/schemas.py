from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.user

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: RoleEnum
    is_verified: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_to_id: int

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    status: TaskStatus