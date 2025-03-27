from models.user import User
from sqlmodel import select, Session
import hashlib


def get_user(user_id: int, session: Session):
    user = session.get(User,user_id)

    if not user:
        return "User does not found"
    return user

def create_user(user: User, session: Session):
    
    user.password_hash = hashlib.sha256(user.password_hash.encode()).hexdigest()
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
def delete_user(user_id : int,session: Session):
    user = session.get(User,user_id) 

    if not user:
        return "User not found!"             
    session.delete(user)
    session.commit()
    return "User has been deleted!"  

def login(email : str, password : str, session: Session):
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()

    if not user:
        return "email not found!"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password == user.password:
        return user