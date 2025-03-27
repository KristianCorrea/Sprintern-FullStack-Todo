# Import FastAPI and Depends from fastapi
# FastAPI is the main framework class, Depends is used for dependency injection
from fastapi import FastAPI, Depends
# Import CORSMiddleware for handling Cross-Origin Resource Sharing
from fastapi.middleware.cors import CORSMiddleware

from config.database import create_db_and_tables

from routes.user_router import user_router
from routes.task_router import task_router


# Create a FastAPI application instance
app = FastAPI()
app.include_router(user_router)
app.include_router(task_router)

# Startup event handler - executes when the application starts
@app.on_event("startup")
def on_startup():
    # Create database tables if they don't exist
    create_db_and_tables()

# Root endpoint that returns a simple message
@app.get("/")
def root():
    return "Hello World"