from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.task import Task  # Only used for type hints, avoiding runtime import. Otherwise this creates an import loop.

# defines common attributes (username, email) that multiple models may share.
class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)

# Defining User (Main Table Model)
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    tasks: List["Task"] = Relationship(back_populates="user")