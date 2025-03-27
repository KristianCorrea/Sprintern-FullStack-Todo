from fastapi import APIRouter,Depends
from services.user_service import *
from models.user import User
from config.database import get_session
from sqlmodel import Session

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@user_router.get("/{user_id}")
def get_user_by_id(user_id:int, session:Session = Depends(get_session)):
    return get_user(user_id,session)

@user_router.post("/")
def create_new_user(user:User, session: Session= Depends(get_session)):
    return create_user(user,session)

@user_router.delete("/{user_id}")
def delete_user_by_id(user_id:int,session:Session = Depends(get_session)):
    return delete_user(user_id,session)
