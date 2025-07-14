from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_verified = Column(Boolean, default=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.user)
    receive_emails = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="assigned_to")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    assigned_to_id = Column(Integer, ForeignKey("users.id"))

    assigned_to = relationship("User", back_populates="tasks")
