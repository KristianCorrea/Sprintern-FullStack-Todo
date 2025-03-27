from fastapi import APIRouter,Depends
from services.task_service import *
from models.task import Task
from config.database import get_session
from sqlmodel import Session

task_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Endpoint to get all tasks
@task_router.get("/")
def get_all(session: Session = Depends(get_session)):
    # Use the get_session dependency to inject a database session
    # Then call get_all_tasks service function with that session
    return get_all_tasks(session)


# Endpoint to create a new task
@task_router.post("/")
def create(task: Task, session: Session = Depends(get_session)):
    # Use the Task model for request body validation
    # Inject database session and call create_task service function
    return create_task(task, session)

# Endpoint to get a specific task by ID
@task_router.get("/{task_id}")
def get(task_id: int, session: Session = Depends(get_session)):
    # Get task_id from path parameter
    # Inject database session and call get_task service function
    return get_task(task_id, session)

# Endpoint to update a task by ID
@task_router.put("/{task_id}")
def update(task_id: int, updated: Task, session: Session = Depends(get_session)):
    # Get task_id from path parameter
    # Get updated task data from request body
    # Inject database session and call update_task service function
    return update_task(task_id, updated, session)


# Endpoint to delete a task by ID
@task_router.delete("/{task_id}")
def delete(task_id: int, session: Session = Depends(get_session)):
    # Get task_id from path parameter
    # Inject database session and call delete_task service function
    return delete_task(task_id, session)

