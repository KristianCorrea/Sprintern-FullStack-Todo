from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User  # Only used for type hints, avoiding runtime import. Otherwise this creates an import loop.

class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = Field(default=False)
    due_date: Optional[datetime] = None

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)  # Equivalent to `created_at` in SQL
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})  # Equivalent to `updated_at` in SQL

    user: "User" = Relationship(back_populates="tasks")