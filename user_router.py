from fastapi import APIRouter,Depends
from db_user_service import *
from model import User,get_session
from sqlmodel import Session

my_router = APIRouter(
    prefix="/user"
)

@my_router.get("/{user_id}")
def get_user_by_id(user_id:int, session:Session = Depends(get_session)):
    return get_user(user_id,session)

@my_router.post("/")
def create_new_user(user:User, session: Session= Depends(get_session)):
    return create_user(user,session)

@my_router.delete("/{user_id}")
def delete_user_by_id(user_id:int,session:Session = Depends(get_session)):
    return delete_user(user_id,session)
